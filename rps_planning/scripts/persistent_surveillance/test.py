import os, sys, time
import numpy as np
from numpy import remainder as rem
from math import floor, ceil, inf
from numpy import zeros, ones
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from concorde.tsp import TSPSolver
import math
from itertools import product
import random
import csv
sys.path.append('./PathPlanning/Search_based_Planning/Search_2D')
import env
from Astar import AStar
from christofides import tsp
project_dir = os.path.abspath(__file__ + "/../../../resource")
import json

class PS:  

    def __init__(self,prm):
        """
        This function initializes class PS    
        *args:
            - prm parameters of the problem 
                # obs          obstacles
                # r            number of UAVs
                # m            dimension of the environment in y axis 
                # n            dimension of the environment in x axis 
                # h            height of the UAVs
                # v_max        maximum velocity of the UAVs
                # u_max        maximum velocity of the UAVs
                # footprint    sensor footprint 
                # beta         charging and depletion rate    
                # e            maximum energy
                # a_best       best partition size in y axis 
                # b_best       best partition size in x axis 
                # robust       robustness size
        *return:
            None
        """
        self.obs=prm['obs']
        self.r=prm['r']
        self.m=prm['m']
        self.n=prm['n']
        self.h=prm['h']
        self.v_max=prm['v_max']
        self.u_max=prm['u_max']
        self.footprint=prm['footprint']
        self.beta=prm['beta']
        self.e=prm['e']
        self.a_best=prm['a_best'] 
        self.b_best=prm['b_best']
        self.robust=prm['robust']
        self.solution_best=[]
        self.age=0
        self.centers=None
        self.ugv_path=[]
        self.reach_target = False
        self.record = []
        self.solver = prm['solver']
        self.planner = prm['planner']
        self.debug_ag = False
        self.uav_time = 0
        self.ugv_time = 0
        self.ugv_time_decomposition = np.array([0,0,0,0,0,0])
        self.count = 0
        
        Env=env.Env(self.m, self.n)      
        for o in self.obs:
             for i in product(np.arange(o[2]+0.5,o[3],0.5),np.arange(o[1]+0.5,o[0],0.5)):              
                Env.obs.add(i)
        self.Env=Env

    def global_path(self,m,n,a,b):
        """
        This function calculate the coordinates of the center of the sub-partitions

        *args:
            - m   length of the enviroment in y axis, int
            - n   length of the environment in x axis, int
            - a   length of the partition in y axis, int
            - b   length of the partition in x axis, int
        *return:
            centers of sub-partitions
        """

        y_num=floor(m/a)
        x_num=floor(n/b)  
        x=zeros((1,ceil(n/b)))
        y=zeros((1,ceil(m/a))) 
        y[0,0:y_num]=np.arange(a/2,a*(2*y_num+1)/2,a)
        x[0,0:x_num]=np.arange(b/2,b*(2*x_num+1)/2,b)
    
        if y_num!=m/a:    
            y[0,y_num]=m-a/2
            y_num=y_num+1

        if x_num!=n/b:
            x[0,x_num]=n-b/2
            x_num=x_num+1
    
        x_coordinate=np.repeat(x,y_num)
        y_coordinate=np.tile(np.flip(y),(1,x_num))    
        position=np.concatenate((x_coordinate.reshape(1,x_coordinate.shape[0]),y_coordinate),0)

        return position

    def global_path_2(self,m,n,a,b):
        """
        This function calculate the coordinates of the center of the sub-partitions

        *args:
            - m   length of the enviroment in y axis, int
            - n   length of the environment in x axis, int
            - a   length of the partition in y axis, int
            - b   length of the partition in x axis, int
        *return:
            centers of sub-partitions
        """
        y_num=floor(m/a)
        x_num=floor(n/b)  
        x=zeros((1,ceil(n/b)))
        y=zeros((1,ceil(m/a))) 
        y[0,0:y_num]=np.arange(a/2,a*(2*y_num+1)/2,a)
        x[0,0:x_num]=np.arange(b/2,b*(2*x_num+1)/2,b)
    
        if y_num!=m/a:    
            y[0,y_num]=y_num*a + (m-y_num*a)/2
            y_num=y_num+1

        if x_num!=n/b:
            x[0,x_num]=x_num*b + (n-x_num*b)/2
            x_num=x_num+1
             
        x_coordinate=np.repeat(x,y_num)
        y_coordinate=np.tile(np.flip(y),(1,x_num))    
        position=np.concatenate((x_coordinate.reshape(1,x_coordinate.shape[0]),y_coordinate),0)

        return position

    def sub_partition(self,a,b,r,dispmt=None):
        """
        This function plots the path for UAVs
        *args:
            - a       length of the partition in y axis, int
            - b       length of the partition in x axis, int
            - r       number of UAVs
            -dispmt   displacement of UAVs' release point from the center of sub-partition                         
        *return:
            - max_dist   maximum travel distance among the UAVs 
            - solution   TSP tours for all the UAVs
        """
        
        if dispmt==None:
            center_x=b/2
            center_y=a/2
        else:
            center_x=b/2+dispmt[0]
            center_y=a/2+dispmt[1]
        
        coord = []
        if a==1 and b!=1:           
            idx=zeros((2,b))
            idx[0,:]=np.arange(1/2,(2*b+1)/2,1)
            idx[1,:]=np.repeat(1/2,b)
            if rem(b,2)==1:
                coord.append(np.flip(idx[:,0:int((b+1)/2)],1))
                coord.append(idx[:,int((b-1)/2):])                
            else:
                center = np.array([[b/2],[1/2]])
                coord.append(np.concatenate((center,np.flip(idx[:,0:int(b/2)],1)),1))
                coord.append(np.concatenate((center,np.flip(idx[:,int(b/2):],1)),1))
            for i in range(r-2):
                coord.append(np.array([]))
            max_dist = b-1
            solution = []
            return max_dist,solution,coord 

        elif b==1 and a!=1:           
            idx=zeros((2,a))
            idx[0,:]=np.repeat(1/2,a)
            idx[1,:]=np.arange(1/2,(2*a+1)/2,1)
            if rem(a,2)==1:
                coord.append(np.flip(idx[:,0:int((a+1)/2)],1))
                coord.append(idx[:,int((a-1)/2):])
            else:
                center = np.array([[1/2],[a/2]])
                coord.append(np.concatenate((center,np.flip(idx[:,0:int(a/2)],1)),1))
                coord.append(np.concatenate((center,np.flip(idx[:,int(a/2):],1)),1))
            for i in range(r-2):
                coord.append(np.array([]))
            max_dist = a-1
            solution = []
            return max_dist,solution,coord   

        elif a==1 and b==1:
            for i in range(r):
                coord.append(np.array([]))
            max_dist = 0
            solution = []
            return max_dist,solution,coord 
        
        idx=zeros((4,a*b))
        idx[0,:]=np.array(list(range(1,a*b+1)))
        idx[1,:]=np.repeat(np.arange(1/2,(2*b+1)/2,1),a)
        idx[2,:]=np.tile(np.flip(np.arange(1/2,(2*a+1)/2,1)),(1,b))
        delta=idx[1:3,:]-np.array([[center_x],[center_y]])
        zero_index=np.where(delta[0,:]==0)[0]
        delta[0,zero_index]=1
        idx[3,:]=np.divide(delta[1,:],delta[0,:])
        idx[3,zero_index]=inf

        left=a*b
        is_nan=np.where(idx[2,zero_index]==0)[0]
        if is_nan.size!=0:
            idx=np.delete(idx,is_nan,1)
            left=a*b-1

        #first Quadrant
        index=np.logical_and(idx[1,:]>=center_x,idx[2,:]>=center_y)
        first=idx[:,index]
        first= first[0:3,first[3,:].argsort()]

        #second Quadrant
        index=np.logical_and(idx[1,:]<center_x,idx[2,:]>=center_y)
        second=idx[:,index]
        second=second[0:3,second[3,:].argsort()]

        #Third Quadrant
        index=np.logical_and(idx[1,:]<=center_x,idx[2,:]<center_y)
        third=idx[:,index]
        third=third[0:3,third[3,:].argsort()]

        #Fourth Quadrant
        index=np.logical_and(idx[1,:]>center_x,idx[2,:]<center_y)
        fourth=idx[:,index]
        fourth=fourth[0:3,fourth[3,:].argsort()]

        new_idx=np.concatenate((first,second,third,fourth),1)
        new_idx=np.concatenate((new_idx,zeros((1,new_idx.shape[1]))))
        num=[]
        robot=r

        for i in range(r):
            num.append(int(ceil(left/robot)))
            left=left-num[i]
            robot=robot-1

        solution=[]
        coord = []
        start=0
        center = np.array([[0],[center_x],[center_y]])
        max_dist=0
        for i in range(r):
            points=np.concatenate((center,new_idx[0:3,start:start+num[i]]),1)
            points_num = points.shape[1]
            dist_matrix=np.zeros((points_num,points_num))
            for pt in range(points_num):
                points_distance = points[1:3,:]-points[1:3,pt].reshape(2,1)
                dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]
            
            if self.solver == "concorde":
                if points.shape[1]<4:
                    sol = list(range(points.shape[1]))  
                else:               
                    solver = TSPSolver.from_data(2*points[1,:],2*points[2,:],"EUC_2D")
                    s = solver.solve(verbose=True)                                     
                    sol=s.tour.tolist()
            elif self.solver == "christofides":
                points_c = [[points[1,i],points[2,i]] for i in range(points.shape[1])]
                #length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(points_c)
                length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
                self.uav_time += timing[-1]-timing[0]
         
            real_trip=points[0,sol].astype(int)
            real_coord = sol[1:]   
 
            # keep uav away from each other    
            if sol[1]>sol[-1]:
                real_coord.reverse()    
            real_coord = points[1:3,real_coord]
            coord.append(real_coord)
 
            a=[np.linalg.norm(points[1:3,sol[i]]-points[1:3,\
                    sol[rem(i+1,len(sol))]]) for i in range(len(sol))]
            solution.append(real_trip)
            where_zero=np.where(real_trip==0)[0]          
            distance=sum(a)+2*self.h                        
                
            if distance>max_dist:
                max_dist=distance
            start=start+num[i]          

        return max_dist,solution,coord

    def opt_partition(self):
        """
        This function calculates the optimal partition sizes
        *args:
            None
        *return:
            - a_best           best partition size in y axis 
            - b_best           best partition size in x axis 
            - solution_best    best TSP tours for UAVs with the best partition size 
            - obj              optimal objective values of the partition size
        """
        obj = inf    
        for i in range(5):
            for j in range(5):       
                m=self.m+i
                n=self.n+j                              
                result = self.opt_mn(m,n)
                if result[3] < obj:
                    obj = result[3]
                    best_result = result
                    self.a_best=result[0]
                    self.b_best=result[1]
        self.a_best=best_result[0]
        self.b_best=best_result[1]
        self.solution_best=best_result[2]
        self.age=best_result[3]

        return best_result
        
    def opt_mn(self,m,n):
        r=self.r
        v_max=self.v_max
        u_max=self.u_max
        footprint=self.footprint
        beta=self.beta
        obj=inf
        a_best=0
        b_best=0
        e=self.e
        deta=footprint*self.robust
        solution_best = []

        m_list = []
        n_list = []
        for i in range(2,m+1):
            if rem(m,i)==0:
                m_list.append(i)

        for i in range(2,n+1):
            if rem(n,i)==0:
                n_list.append(i)

        option_mn = [(i,j) for i in m_list for j in n_list]
        product_mn = [i[0]*i[1] for i in option_mn]
        sorted_idx = np.argsort(product_mn).tolist()
        list_mn = [option_mn[i] for i in sorted_idx]
        list_mn.reverse()      
        max_distance = v_max*e/beta-2*deta

        obj=inf
        a_best=0
        b_best=0
        solution_best=[]

        for j in list_mn:         
            a = j[0]
            b = j[1]  
            if a_best != 0 and b_best != 0 and a*b<a_best*b_best:
                return [a_best,b_best,solution_best,obj]   
            
            if a*b/r>max_distance:
                continue
            if j in self.record:
                continue
            else:
                self.record.append(j)
            
            [max_dist,solution,coo]=self.sub_partition(a,b,r)
            t_v=max_dist*footprint/v_max 
 
            if t_v>e/beta-2*deta/v_max:
                continue            
            self.count += 1        
            points=self.global_path(m,n,a,b)             
            points_num = points.shape[1]
            
            dist_matrix=np.zeros((points_num,points_num))
            for pt in range(points_num):
                points_distance = points[0:2,:]-points[0:2,pt].reshape(2,1)
                dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]

            if self.solver == "concorde":   
                if points.shape[1]<4:
                    sol = list(range(points.shape[1]))  
                else:               
                    solver = TSPSolver.from_data(points[0,:],points[1,:],"EUC_2D")
                    s = solver.solve(verbose=True)                                     
                    sol=s.tour.tolist()
            elif self.solver == "christofides":
                points_c = [[points[0,i],points[1,i]] for i in range(points.shape[1])]
                #length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(points_c)
                length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
                self.ugv_time += timing[-1]-timing[0]
                time_decomposition = np.array([timing[i+1]-timing[i] for i in range(len(timing)-1)])
                self.ugv_time_decomposition = self.ugv_time_decomposition + time_decomposition 

            time_global=footprint*np.sqrt(np.square(points[0,sol]-points[0,sol[1:]+[sol[0]]])+\
            np.square(points[1,sol]-points[1,sol[1:]+[sol[0]]]))/u_max       
            t_u=sum(np.maximum(time_global,np.tile(t_v,(time_global.shape[0],))))
            obj_new=time_global.shape[0]*t_v+t_u

            if obj_new<obj:
                obj=obj_new
                a_best=a
                b_best=b
                solution_best=solution
                self.a_best=a_best
                self.b_best=b_best
                self.solution_best=solution_best
                self.age=obj
        return [a_best,b_best,solution_best,inf]

    def opt_partition_exhaustive(self):
        """
        This function calculates the optimal partition sizes
        *args:
            None
        *return:
            - a_best           best partition size in y axis 
            - b_best           best partition size in x axis 
            - solution_best    best TSP tours for UAVs with the best partition size 
            - obj              optimal objective values of the partition size
        """
        r=self.r
        m=self.m
        n=self.n
        v_max=self.v_max
        u_max=self.u_max
        footprint=self.footprint
        beta=self.beta
        obj=inf
        a_best=0
        b_best=0
        e=self.e
        i=0
        deta=footprint*self.robust
        max_distance = v_max*e/beta-2*deta

        for a in range(2,self.m+1):
            for b in range(2,self.n+1):
                if a*b/r>max_distance:
                    continue
                
                [max_dist,solution,coo]=self.sub_partition(a,b,r)
                t_v=max_dist*footprint/v_max     
     
                if t_v>e/beta-2*deta/v_max:                   
                    break
                            
                points=self.global_path(m,n,a,b) 
                points_num = points.shape[1]
                dist_matrix=np.zeros((points_num,points_num))
                for pt in range(points_num):
                    points_distance = points[0:2,:]-points[0:2,pt].reshape(2,1)
                    dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]

                if self.solver == "concorde":   
                    if points.shape[1]<4:
                        sol = list(range(points.shape[1]))  
                    else:               
                        solver = TSPSolver.from_data(points[0,:],points[1,:],"EUC_2D")
                        s = solver.solve(verbose=True)                                     
                        sol=s.tour.tolist()
                elif self.solver == "christofides":
                    points_c = [[points[0,i],points[1,i]] for i in range(points.shape[1])]
                    length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
                    self.ugv_time += timing[-1]-timing[0]
                    time_decomposition = np.array([timing[i+1]-timing[i] \
                            for i in range(len(timing)-1)])
                    self.ugv_time_decomposition = self.ugv_time_decomposition + time_decomposition 

                time_global=footprint*np.sqrt(np.square(points[0,sol]-points[0,sol[1:]+[sol[0]]])+\
                np.square(points[1,sol]-points[1,sol[1:]+[sol[0]]]))/u_max       
                t_u=sum(np.maximum(time_global,np.tile(t_v,(time_global.shape[0],))))
                obj_new=time_global.shape[0]*t_v+t_u

                if obj_new<obj:
                    obj=obj_new
                    a_best=a
                    b_best=b
                    solution_best=solution

        self.a_best=a_best
        self.b_best=b_best
        self.solution_best=solution_best
        self.age=obj

        return [a_best,b_best,solution_best,obj]

    def maximum_partition(self):
        deta=self.footprint*self.robust
        max_distance = self.v_max*self.e/self.beta-2*deta
        area = max_distance*self.r
        a = int(ceil(np.sqrt(area)))
        too_small = True
        num = max(self.m, self.n)
        last = []

        if a>min(self.m, self.n):
            a = min(self.m, self.n)
        b = a
       
        for i in range(num):        
            [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
            t_v=max_dist*self.footprint/self.v_max                  
            if t_v>self.e/self.beta-2*deta/self.v_max:                   
                too_small = False 
                a = a - 1
                b = b - 1
                if last == True:
                    break
                else:
                    last = False                  
            else:
                too_small = True
                if last == False or a>=min(self.m, self.n):
                    break
                else:
                    last = True
                    a = a + 1
                    b = b + 1
        [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
        t_v=max_dist*self.footprint/self.v_max  
        obj_new, max_dist, solution = self.calculate_age_2(a,b)
        self.a_best=a
        self.b_best=b
        self.solution_best=solution
        self.age=obj_new
        return [a,b,solution,obj_new]

    def random_obstacles(self, density):
        """
        This function generates random obstacles
        *args:
            - density  obstacle_area/environment_area
                       0<density<1
        *return:
            None      
        """
        #different sizes of obstacles
        if not (density > 0 and density < 1): 
                raise AssertionError('Obstacle density should be greater than 0 and less than 1')
        shape=[(c,d) for c in range(1,self.robust) for d in range(1,self.robust)]
        shape=[i for i in shape if i[0]**2+i[1]**2<=self.robust**2]
        unit_area=[i[0]*i[1] for i in shape]

        obs_area=floor(self.m*self.n*density)
        obs_num=floor(obs_area/sum(unit_area))

        reorder=sorted(range(len(unit_area)), key=lambda d: unit_area[d], reverse=True)
        unit_area=[unit_area[i] for i in reorder]
        shape=[shape[i] for i in reorder]

        idx=0
        obs_dict=dict()
        for i in shape:
            for j in range(obs_num):
                for chance in range(0,20):
                    x=random.randrange(0,self.n-i[0])
                    y=random.randrange(0,self.m-i[1])
  
                    center=list(product(np.arange(x+0.5,x+i[0],1),np.arange(y+0.5,y+i[1],1)))
                    is_overlapped=[c in self.Env.obs for c in center]
                    if any(is_overlapped):
                        continue
                    neighbor=list(product(np.arange(x+0.5,x+i[0],1),[y-0.5,y+i[1]+0.5]))+\
                             list(product([x-0.5,x+i[0]+0.5],np.arange(y+0.5,y+i[1],1)))
                    is_adjacent=[n in self.Env.obs for n in neighbor]
                    if any(is_adjacent):
                        continue
                    else:
                        for c in center:
                            self.Env.obs.add(c)
                        edge=list(product(range(x,x+i[0]+1,1),[y,y+i[1]]))+\
                             list(product([x,x+i[0]],range(y+1,y+i[1],1)))
                        obs_dict[idx]={'center':center, 'edge':edge, 'xy':(x,y), 'shape':i}
                        idx=idx+1
                        break

        ax=plt.gca()
        for i in obs_dict:
            rec=Rectangle(obs_dict[i]['xy'],obs_dict[i]['shape'][0],obs_dict[i]['shape'][1],color='k')
            ax.add_patch(rec)
        plt.xlim(0,self.n)
        plt.ylim(0,self.m)
        plt.axis('equal')
        plt.show()
        self.obs_dict=obs_dict 
   

    def plot_uav_path(self,solution,position,a,b):
        """
        This function plots the path for UAVs
        *args:
            - solution   TSP tours for UAVs
            - position   centers of sub-partitions
            - a          length of the partition in y axis, int
            - b          length of the partition in x axis, int
        *return:
            None      
        """
        num_rep=position.shape[1]
        idx=zeros((3,a*b+1))
        idx[0,1:]=list(range(1,a*b+1))
        idx[1,1:]=np.repeat(np.arange(1/2,(2*b+1)/2,1),a)
        idx[2,1:]=np.tile(np.flip(np.arange(1/2,(2*a+1)/2,1)),(1,b))
        idx[:,0]=np.array([[0],[b/2],[a/2]]).reshape(3,)
        r=len(solution)
        color=['r','k','b','g','m','c']
        
        for i in range(r):
            sol=solution[i]
            row=sol.shape[0]
            start_x=idx[1,sol[:]]
            start_y=idx[2,sol[:]]
            end_x=np.concatenate((idx[1,sol[1:]],idx[1,sol[0]].reshape(1,)))
            end_y=np.concatenate((idx[2,sol[1:]],idx[2,sol[0]].reshape(1,)))

            start_x=np.tile(start_x,(1,num_rep))
            start_y=np.tile(start_y,(1,num_rep))
            end_x=np.tile(end_x,(1,num_rep))
            end_y=np.tile(end_y,(1,num_rep))
            start_x=start_x+np.repeat(position[0,:],row)
            end_x=end_x+np.repeat(position[0,:],row)
            start_y=start_y+np.repeat(position[1,:],row)
            end_y=end_y+np.repeat(position[1,:],row)

            plt.plot(np.concatenate((start_x,end_x),0),np.concatenate((start_y,end_y),0),color[i])

    def plot_uav_path_2(self,coord_list,position,data,length_list):
        """
        This function plots the path for UAVs
        *args:
            - solution   TSP tours for UAVs
            - position   centers of sub-partitions
            - a          length of the partition in y axis, int
            - b          length of the partition in x axis, int
        *return:
            None      
        """
        num_rep=position.shape[1]
        color=[(174/255,199/255,232/255),(1,187/255,120/255),(152/255,223/255,138/255),(1,152/255,150/255)]      
        
        for j in range(num_rep):
            line_list = []
            for i in range(self.r):
                x = length_list[data[j]][0]
                y = length_list[data[j]][1]
                coord = coord_list[data[j]][i]
                if coord.size == 0:
                    continue
                coord =  np.concatenate((np.array([[x/2],[y/2]]),coord),1) 
                start_x=coord[0,:]+position[0,j]            
                start_y=coord[1,:]+position[1,j]   
                end_x=np.concatenate((coord[0,1:],coord[0,0].reshape(1,)))+position[0,j]   
                end_y=np.concatenate((coord[1,1:],coord[1,0].reshape(1,)))+position[1,j]   

                line = plt.plot(np.array([start_x,end_x]),np.array([start_y,end_y]),c=color[i],label='Line '+str(i))
                line_list.append(line)
        return line_list               

    def plot_ugv_path(self,path):
        """
        This function plots the path for UGV
        *args:
            - path  path for UGV
        *return:
            None      
        """
        if len(path) != 0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-r', linewidth=2)

    def plot_path(self):
        """
        This function plots the path for UGV and UAVs
        *args:
            None    
        *return:
            None      
        """
        points=self.global_path(self.m,self.n,self.a_best,self.b_best)
        position=points-points[:,0].reshape(2,1)+np.array([[0],[self.m-self.a_best]])

        if len(self.solution_best)==0:
            [max_dist,solution,coo]=self.sub_partition(self.a_best,self.b_best,self.r)
            self.solution_best=solution
        self.plot_uav_path(self.solution_best,position,self.a_best,self.b_best)

        for p in self.ugv_path:
            self.plot_ugv_path(p)

        plt.plot([x[0] for x in self.Env.obs],[x[1] for x in self.Env.obs], "sk")
        ax = plt.gca()
        cmap = self.get_cmap(points.shape[1])
        for i in range(points.shape[1]):
            rect = Rectangle((points[0,i]-0.5*self.b_best,points[1,i]-0.5*self.a_best),\
                    self.b_best,self.a_best,linewidth=1,ec=cmap(i),facecolor='none')
            ax.add_patch(rect)
        plt.show()

    def plot_path_2(self, coord_list,position,data,length_list, points):
        """
        This function plots the path for UGV and UAVs
        *args:
            None    
        *return:
            None      
        """
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
       
        line_list = self.plot_uav_path_2(coord_list,position,data,length_list)
        plt.plot([x[0] for x in self.Env.obs],[x[1] for x in self.Env.obs], "sk")

        cmap = self.get_cmap(points.shape[1])
        for i in range(points.shape[1]):
            x = length_list[data[i]][0]
            y = length_list[data[i]][1]
            rect = Rectangle((points[0,i]-0.5*x,points[1,i]-0.5*y),\
                    x,y,linewidth=1,ec='k',facecolor='none')
            ax.add_patch(rect)

        plt.tick_params(
            axis='both',       # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            labelbottom=True)

        plt.axis('off')
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        plt.axis('equal')
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,hspace = 0, wspace = 0)
        plt.savefig('partition.png', dpi=1000, bbox_inches='tight',pad_inches = 0)
        plt.show()
        
    def get_cmap(self,n, name='hsv'):
        """
        This function returns a function that maps each index in 0, 1, ..., n-1 to a distinct RGB color
        The keyword argument name must be a standard mpl colormap name.
        *args:
            - n      number of colors needed
            - name   None or standard mpl colormap name
        *return:
            None      
        """
        return plt.cm.get_cmap(name, n)

    def calculate_age(self,a,b):

        [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
        deta=self.footprint*self.robust
        t_v=max_dist*self.footprint/self.v_max
        if t_v>self.e/self.beta-2*deta/self.v_max:                   
             return inf, 0, []

        points=self.global_path(self.m,self.n,a,b)
        points_num = points.shape[1]
        dist_matrix=np.zeros((points_num,points_num))
        for pt in range(points_num):
            points_distance = points[0:2,:]-points[0:2,pt].reshape(2,1)
            dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]
        
        start_time = time.time()
        if self.solver == "concorde":
            if points.shape[1]<4:
                    sol = list(range(points.shape[1]))  
            else:               
                solver = TSPSolver.from_data(points[0,:],points[1,:],"EUC_2D")
                s = solver.solve(verbose=True)                                     
                sol=s.tour.tolist()
        elif self.solver == "christofides":
            points_c = [[points[0,i],points[1,i]] for i in range(points.shape[1])]
            #length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(points_c)
            length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
        time_global=self.footprint*np.sqrt(np.square(points[0,sol]-points[0,sol[1:]+[sol[0]]])+\
        np.square(points[1,sol]-points[1,sol[1:]+[sol[0]]]))/self.u_max
        t_u=sum(np.maximum(time_global,np.tile(t_v,(time_global.shape[0],))))

        obj_new=time_global.shape[0]*t_v+t_u
        return obj_new, max_dist, solution

    def calculate_age_2(self,a,b,data=None):
        max_dist_1 = 0
        max_dist_2 = 0
        max_dist_3 = 0
        num_1 = 0
        num_2 = 0
        num_3 = 0
        m = self.m
        n = self.n

        y_num=floor(self.m/a)
        x_num=floor(self.n/b)
        if y_num!=m/a:
            a_1 = self.m - y_num*a
            [max_dist_1,solution_1,coo_1]=self.sub_partition(a_1,b,self.r)
            num_1 = x_num

        if x_num!=n/b:
            b_1 = self.n - x_num*b
            [max_dist_2,solution_2,coo_2]=self.sub_partition(a,b_1,self.r)
            num_2 = y_num

        if y_num!=m/a and x_num!=n/b:
            a_2 = self.m - y_num*a
            b_2 = self.n - x_num*b
            [max_dist_3,solution_3,coo_3]=self.sub_partition(a_2,b_2,self.r)
            num_3 = 1

        t_v1 = max_dist_1*self.footprint/self.v_max
        t_v2 = max_dist_2*self.footprint/self.v_max
        t_v3 = max_dist_3*self.footprint/self.v_max
        
        [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
        deta=self.footprint*self.robust
       
        t_v=max_dist*self.footprint/self.v_max
      
        if t_v>self.e/self.beta-2*deta/self.v_max:                   
            return inf, 0, []

        points=self.global_path_2(self.m,self.n,a,b)
        points_num = points.shape[1]
        dist_matrix=np.zeros((points_num,points_num))
        for pt in range(points_num):
            points_distance = points[0:2,:]-points[0:2,pt].reshape(2,1)
            dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]
    
        start_time = time.time()
        if self.solver == "concorde":
            if points.shape[1]<4:
                    sol = list(range(points.shape[1]))  
            else:               
                solver = TSPSolver.from_data(points[0,:],points[1,:],"EUC_2D")
                s = solver.solve(verbose=True)                                     
                sol=s.tour.tolist()
        elif self.solver == "christofides":
            points_c = [[points[0,i],points[1,i]] for i in range(points.shape[1])]
            #length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(points_c)
            length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
        time_global=self.footprint*np.sqrt(np.square(points[0,sol]-points[0,sol[1:]+[sol[0]]])+\
        np.square(points[1,sol]-points[1,sol[1:]+[sol[0]]]))/self.u_max
        tv_array = np.tile(t_v,time_global.shape[0])
        #print(tv_array)
        
        if y_num!=m/a:
           for i in range(0,int(x_num*(y_num+1)),int(y_num+1)):
               tv_array[i]=t_v1

        if x_num!=n/b: 
            total = int((x_num+1)*ceil(self.m/a))
            for i in range(total-1,total-1-y_num,-1):
               tv_array[i]=t_v2
       
        if y_num!=m/a and x_num!=n/b: 
            tv_array[total-1-y_num]=t_v3
                          
        t_u=sum(np.maximum(time_global,tv_array))            
        obj_new=time_global.shape[0]*t_v+t_u-t_v*(num_1+num_2+num_3)+t_v1*num_1+t_v2*num_2+t_v3*num_3

        return obj_new, max_dist, solution

    def opt_partition_minimal_overlap(self):
        a_mini, b_mini = self.minimal_overlap()
        a_range = 5
        b_range = 5
        obj = inf
        for i in range(a_range):
            for j in range(b_range):
                if a_mini+i > self.m or b_mini+j>self.n:
                    continue
                
                obj_new, max_dist, sol = self.calculate_age(a_mini+i,b_mini+j)
                if obj_new < obj:
                    obj = obj_new
                    a_best = a_mini+i
                    b_best = b_mini+j
                    solution_best = sol

        self.a_best=a_best
        self.b_best=b_best
        self.solution_best=solution_best
        self.age=obj

        return [a_best,b_best,solution_best,obj]      
   
    def minimal_overlap(self):
        start = time.time()
        r=self.r
        m=self.m
        n=self.n
        v_max=self.v_max
        u_max=self.u_max
        footprint=self.footprint
        beta=self.beta
        obj=inf
        a_best=0
        b_best=0
        e=self.e
        i=0
        deta=footprint*self.robust
        add = 0
        max_distance = v_max*e/beta-2*deta
        for add in range(0, max(self.m, self.n)+1):
            record = []
            plus = [(i,j) for i in range(add+1) for j in range(add+1) if i+j==add]
            obj = inf
            option_MN = [(self.m+k[0],self.n+k[1]) for k in plus]
            product_MN = [i[0]*i[1] for i in option_MN]
            sorted_idx = np.argsort(product_MN).tolist()
            list_MN = [option_MN[i] for i in sorted_idx]
            
            for k in list_MN:
                m_list = []
                n_list = []
                m = k[0]
                n = k[1]                            
                for i in range(2,m+1):
                    if rem(m,i)==0:
                        m_list.append(i)
                for i in range(2,n+1):
                    if rem(n,i)==0:
                         n_list.append(i)               
                option_mn = [(i,j) for i in m_list for j in n_list]
                product_mn = [i[0]*i[1] for i in option_mn]
                sorted_idx = np.argsort(product_mn).tolist()
                list_mn = [option_mn[i] for i in sorted_idx]
                list_mn.reverse()
                
                for j in list_mn:         
                    a = j[0]
                    b = j[1]
                    if a*b/r>max_distance:
                        continue
                    if j in record:                     
                        continue
                    else:
                        record.append(j)
                    
                    time_1 = time.time()
                    [max_dist,solution,coo]=self.sub_partition(a,b,r)                    
                    t_v=max_dist*footprint/v_max 
           
                    if t_v>e/beta-2*deta/v_max:
                        continue
                    else:
                        return a,b                        

def debugging():

    
    mn_list = [(13,16),(17,23),(26,31),(43,53),(67,47),(101,97)]

    prm={
    'obs':{},\
    'r':4,\
    'm':32,\
    'n':17,\
    'h':4,\
    'v_max':0.5,\
    'u_max':0.3,\
    'footprint':1,\
    'beta':1,\
    'e':100,\
    'a_best':0,\
    'b_best':0,\
    'robust':0,\
    'solver':"christofides",\
    'planner':"max"
    }

    ps=PS(prm)
 
    ugv_time = []
    uav_time = []
    compute_time = []
    decomposition_time = np.zeros((len(mn_list),6))
    heuristic_ab = np.zeros((2,len(mn_list)))
    mini_ab = np.zeros((2,len(mn_list)))
    max_ab = np.zeros((2,len(mn_list)))
    heuristic_obj = []
    mini_obj = []
    max_obj = []
    max_time = []
    max_obj_1 = []
    max_time_1 = []
    exhaustive_obj = []
    exhaustive_time = []
    exhaustive_obj_1 = []
    exhaustive_time_1 = []
    heuristic_time = []
    mini_time = []

    colour=[(174/255,199/255,232/255),(1,187/255,120/255),(152/255,223/255,138/255),(1,152/255,150/255)]

    for idx,i in enumerate(mn_list):
        print("--------------------------------------")
        print(i)       
        ps.m = i[0]
        ps.n = i[1]

        ps.solver = "christofides"
        start = time.time()       
        solution_max=ps.maximum_partition()
        print("maximum:")
        print(time.time()-start)
        max_time.append(time.time()-start)
        #print([solution_max[0],solution_max[1],solution_max[3]]) 
        max_obj.append(solution_max[3])
        max_ab[0][idx]=solution_max[0]
        max_ab[1][idx]=solution_max[1]
        time.sleep(0.1)

        ps.solver = "christofides"
        start = time.time()
        solution_exhaustive=ps.opt_partition_exhaustive()
        print("exhaustive:")        
        print(time.time()-start)
        exhaustive_time.append(time.time()-start)
        #print([solution_exhaustive[0],solution_exhaustive[1],solution_exhaustive[3]])
        exhaustive_obj.append(solution_exhaustive[3])
        time.sleep(1)

        ugv_time.append(ps.ugv_time)
        uav_time.append(ps.uav_time)
        decomposition_time[idx,:]=ps.ugv_time_decomposition
        #print(ps.count)
        ps.count = 0
        ps.uav_time = 0
        ps.ugv_time = 0
        ps.record = []
        ps.ugv_time_decomposition = np.array([0,0,0,0,0,0])
    
              
    labels = ['{}'.format(i) for i in mn_list]
    
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    
    fig, ax = plt.subplots(2)
    rects1 = ax[0].bar(x - width/2, ugv_time, width, label='ugv')
    rects2 = ax[0].bar(x + width/2, uav_time, width, label='uav')

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax[0].set_ylabel('time')
    ax[0].set_title('UGV and UAV computation time')
    ax[0].set_xticks(x)
    ax[0].set_xticklabels(labels)
    ax[0].legend()

    #ax.bar_label(rects1, padding=3)
    #ax.bar_label(rects2, padding=3)

    x = np.arange(0,len(labels)*2,2)  # the label locations
    width = 0.2  # the width of the bars

    rects1 = ax[1].bar(x - 5*width/2, decomposition_time[:,0].tolist(), width, label='G')
    rects2 = ax[1].bar(x - 3*width/2, decomposition_time[:,1].tolist(), width, label='MST')
    rects3 = ax[1].bar(x - width/2, decomposition_time[:,2].tolist(), width, label='ODD')
    rects4 = ax[1].bar(x + width/2, decomposition_time[:,3].tolist(), width, label='MAT')
    rects5 = ax[1].bar(x + 3*width/2, decomposition_time[:,4].tolist(), width, label='EUL')
    rects6 = ax[1].bar(x + 5*width/2, decomposition_time[:,5].tolist(), width, label='TSP')
    
    ax[1].set_ylabel('time')
    ax[1].set_title('UGV time decomposition')
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(labels)
    ax[1].legend()
  
    fig.tight_layout()

    fig1, ax1 = plt.subplots(2)
 
    x = np.arange(len(labels))

    #ax1[0].plot(x,heuristic_obj,label='heuristic')
    ax1[0].plot(x,max_obj,'-x',label='max partition - christofides',color=colour[3])
    #ax1[0].plot(x,max_obj_1,'-o',label='max partition - concorde',color=colour[1])
    #ax1[0].plot(x,mini_obj,label='minimal overlap')
    ax1[0].plot(x,exhaustive_obj,'-s',label='exhaustive - christofides',color=colour[0])
    #ax1[0].plot(x,exhaustive_obj_1,'-o',label='exhaustive - concorde',color=colour[0])
    print(max_obj)
    print(exhaustive_obj)

    ax1[0].set_ylabel('age \s')
    ax1[0].set_xlabel('dimension of the environment \m')
    ax1[0].set_xticks(x)
    ax1[0].set_xticklabels(labels)
    ax1[0].legend()

    #ax1[1].plot(x,heuristic_time,label='heuristic')
    ax1[1].plot(x,max_time,'-x',label='max partition - christofides',color=colour[3])
    #ax1[1].plot(x,max_time_1,'-o',label='max partition - concorde',color=colour[1])
    #ax1[1].plot(x,mini_time,label='minimal overlap')
    ax1[1].plot(x,exhaustive_time,'-s',label='exhaustive - christofides',color=colour[0])
    #ax1[1].plot(x,exhaustive_time_1,'-o',label='exhaustive - concorde',color=colour[0])

    ax1[1].set_ylabel('computation time \s')
    ax1[1].set_xlabel('dimension of the environment \m')
    ax1[1].set_xticks(x)
    ax1[1].set_xticklabels(labels)
    ax1[1].legend()
    
    fig1.tight_layout()
    plt.savefig('algo.png', dpi=1200)
    plt.show()


def test():
    #obs={(12,6,6,16),(32,20,28,39)}
    #obs={(12,6,6,16)} 
    #obs={(16,12,6,10),(26,20,14,18),(14,11,38,41)}
    obs={} 
    
    prm={
        'obs':obs,\
        'r':4,\
        'm':25,\
        'n':25,\
        'h':4,\
        'v_max':0.4,\
        'u_max':0.2,\
        'footprint':1,\
        'beta':1,\
        'e':100,\
        'a_best':0,\
        'b_best':0,\
        'robust':4,\
        'solver':"christofides",\
        'planner':"max"
        }

    ps=PS(prm)
    if ps.planner == "max":
        solution_max=ps.maximum_partition()

    coord_list = []
    length_list = []
 
    for f in os.listdir(project_dir):
        os.remove(os.path.join(project_dir, f))
    
    if ps.planner != "max":
        [m,s,coord]=ps.sub_partition(ps.a_best,ps.b_best,ps.r)     
        for c in range(len(coord)):
            with open(os.path.join(project_dir,'waypoint_{}_{}.txt'.format(0,c)), 'w', newline='') as out:
                for p in range(coord[c].shape[1]):
                    out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                                ps.footprint*coord[c][1][p], ps.h))
        points=ps.global_path(ps.m,ps.n,ps.a_best,ps.b_best)
        data = {i:0 for i in range(points.shape[1])} 

    else:
        new_x = None
        new_y = None
        [m,s,coord]=ps.sub_partition(ps.a_best,ps.b_best,ps.r)
        length_list.append((ps.b_best,ps.a_best))
        coord_list.append(coord)
        for c in range(len(coord)):
            with open(os.path.join(project_dir,'waypoint_{}_{}.txt'.format(0,c)), 'w', newline='') as out:
                for p in range(coord[c].shape[1]):
                    out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                                ps.footprint*coord[c][1][p], ps.h))
        if floor(ps.m/ps.a_best) != ps.m/ps.a_best:           
            new_a = ps.m - floor(ps.m/ps.a_best)*ps.a_best
            new_y = ps.m - 0.5*new_a
            [m,s,coord]=ps.sub_partition(new_a,ps.b_best,ps.r)
            coord_list.append(coord)
            length_list.append((ps.b_best,new_a))          
        else:
            coord = [np.array([]) for z in range(ps.r)]
            coord_list.append(coord)
            length_list.append(())

        for c in range(len(coord)):
            with open(os.path.join(project_dir,'waypoint_{}_{}.txt'.format(0,c)), 'w', newline='') as out:
                if coord[c].size != 0:
                    for p in range(coord[c].shape[1]):
                        out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                            ps.footprint*coord[c][1][p], ps.h))

        if floor(ps.n/ps.b_best) != ps.n/ps.b_best:
            new_b = ps.n - floor(ps.n/ps.b_best)*ps.b_best
            new_x = ps.n - 0.5*new_b
            [m,s,coord]=ps.sub_partition(ps.a_best,new_b,ps.r)
            coord_list.append(coord)
            length_list.append((new_b,ps.a_best))

        else:
            coord = [np.array([]) for z in range(ps.r)]
            coord_list.append(coord)
            length_list.append(())

        for c in range(len(coord)):
            with open(os.path.join(project_dir,'waypoint_{}_{}.txt'.format(0,c)), 'w', newline='') as out:
                if coord[c].size != 0:
                    for p in range(coord[c].shape[1]):
                        out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                            ps.footprint*coord[c][1][p], ps.h))
        if floor(ps.n/ps.b_best) != ps.n/ps.b_best and floor(ps.m/ps.a_best) != ps.m/ps.a_best:
            [m,s,coord]=ps.sub_partition(new_a,new_b,ps.r)
            coord_list.append(coord)
            length_list.append((new_b,new_a))
        else:
            coord = [np.array([]) for z in range(ps.r)]
            coord_list.append(coord)
            length_list.append(())
        for c in range(len(coord)):          
            with open(os.path.join(project_dir,'waypoint_{}_{}.txt'.format(0,c)), 'w', newline='') as out:
                if coord[c].size != 0:
                    for p in range(coord[c].shape[1]):
                        out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                            ps.footprint*coord[c][1][p], ps.h))
            
        points=ps.global_path_2(ps.m,ps.n,ps.a_best,ps.b_best)      
        
    points_num = points.shape[1]
    dist_matrix=np.zeros((points_num,points_num))
    for pt in range(points_num):
        points_distance = points[0:2,:]-points[0:2,pt].reshape(2,1)
        dist_matrix[pt,:] = np.sqrt(points_distance[0,:]**2+points_distance[1,:]**2)[:]
   
    if ps.solver == "concorde":
         if points.shape[1]<4:
            sol = list(range(points.shape[1]))  
         else:               
            solver = TSPSolver.from_data(points[0,:],points[1,:],"EUC_2D")
            s = solver.solve(verbose=True)                                     
            sol=s.tour.tolist()
    elif ps.solver == "christofides":
        points_c = [[points[0,i],points[1,i]] for i in range(points.shape[1])]
        #length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(points_c)
        length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
    
    points=points[:,sol]
    points = np.concatenate((points[:,4:],points[:,0:4]),1)
    position = np.zeros((2,points.shape[1]))

    if new_x == None and new_y == None:
        data = {i:0 for i in range(points.shape[1])}  
    else:
        data = {} 
        for i in range(points.shape[1]):
            if points[0][i] == new_x:
                if points[1][i] == new_y:
                    data[i]=3
                    position[0][i] = points[0][i] - new_b/2
                    position[1][i] = points[1][i] - new_a/2
                else:
                    data[i]=2
                    position[0][i] = points[0][i] - new_b/2
                    position[1][i] = points[1][i] - ps.a_best/2
            else:
                if points[1][i] == new_y:
                    data[i]=1
                    position[0][i] = points[0][i] - ps.b_best/2
                    position[1][i] = points[1][i] - new_a/2
                else:
                    data[i]=0
                    position[0][i] = points[0][i] - ps.b_best/2
                    position[1][i] = points[1][i] - ps.a_best/2
    
    with open(os.path.join(project_dir,'data.json'), 'w') as f:
        json.dump(data, f)    

    np.savez(os.path.join(project_dir,'ugvwaypoint.npz'),pos=ps.footprint*points,\
            delta=position*ps.footprint,robust=ps.robust)

    ps.plot_path_2(coord_list, position,data,length_list, points)
    
    age = ps.calculate_age_2(ps.a_best,ps.b_best,data)
    print("age: {}".format(age[0]))
    print("optimal partition: [{},{}]".format(ps.a_best,ps.b_best))

if __name__=='__main__':
    test() 
    #debugging()

