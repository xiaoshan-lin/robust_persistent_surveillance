import os, sys
import numpy as np
from numpy import remainder as rem
from math import floor, ceil, inf
from numpy import zeros, ones
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from concorde.tsp import TSPSolver
from itertools import product
sys.path.append('./PathPlanning/Search_based_Planning/Search_2D')
import env
from christofides import tsp
project_dir = os.path.abspath(__file__ + "/../../../resource/")
import json
import elkai
import datetime

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
        self.beta_plus=prm['beta_plus']
        self.beta_minus=prm['beta_minus']
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
        self.dt = datetime.datetime.today()

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
                    s = solver.solve(verbose=False)
                    sol=s.tour.tolist()

            elif self.solver == "christofides":
                length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
                self.uav_time += timing[-1]-timing[0]
            elif self.solver == "lkh":
                if points.shape[1]<4:
                    sol = list(range(points.shape[1]))
                else:
                    sol = elkai.solve_float_matrix(dist_matrix, runs=10)

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
            distance=sum(a)+2*self.h

            if distance>max_dist:
                max_dist=distance

            start=start+num[i]

        return max_dist,solution,coord

    def maximum_partition(self):
        deta=self.footprint*self.robust
        max_distance = self.v_max*self.e/self.beta_minus-2*deta
        area = max_distance*self.r
        a = int(ceil(np.sqrt(area)))
        num = max(self.m, self.n)
        last = []

        if a>min(self.m, self.n):
            a = min(self.m, self.n)
        b = a

        for i in range(num):

            [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
            t_v=max_dist*self.footprint/self.v_max
            
            if t_v>self.e/self.beta_minus-2*deta/self.v_max:
                a = a - 1
                b = b - 1
                if last == True:
                    break
                else:
                    last = False

            else:
                if last == False or a>=min(self.m, self.n):
                    break

                else:
                    last = True
                    a = a + 1
                    b = b + 1
        [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
        t_v=max_dist*self.footprint/self.v_max

        obj_new, max_dist, solution = self.calculate_age(a,b)
        self.a_best=a
        self.b_best=b
        self.solution_best=solution
        self.age=obj_new
        return [a,b,solution,obj_new]

    def plot_uav_path(self, ax, coord_list, position, data, length_list):
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
        num_partition=position.shape[1]
        color=[(174/255,199/255,232/255),(1,187/255,120/255),(152/255,223/255,138/255),(1,152/255,150/255)]
        for j in range(num_partition):
            line_list = []
            for i in range(self.r):
                x = length_list[data[j]][0]
                y = length_list[data[j]][1]

                coord = coord_list[data[j]][i]
                if coord.size == 0:
                    continue
                coord = np.concatenate((np.array([[x/2],[y/2]]),coord),1)
                start_x=coord[0,:]+position[0,j]
                start_y=coord[1,:]+position[1,j]
                end_x=np.concatenate((coord[0,1:],coord[0,0].reshape(1,)))+position[0,j]
                end_y=np.concatenate((coord[1,1:],coord[1,0].reshape(1,)))+position[1,j]

                line = ax.plot(np.array([start_x,end_x]),np.array([start_y,end_y]),c=color[i],label='Line '+str(i))
                line_list.append(line)

        return line_list

    def plot_ugv_path(self,path):
        """
        This function plots the path for UGV
        *args:
            - path: path for UGV
        *return:
            None
        """
        if len(path) != 0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-r', linewidth=2)

    def plot_path(self, coord_list, position, data, length_list, points):
        """
        This function plots the path for UGV and UAVs
        *args:
            None
        *return:
            None
        """
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.tick_params(
            axis='both',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            left=False,
            labelbottom=True)
        ax.axis('off')
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.axis('equal')
        ax.set_position([0, 0, 1, 1])

        ax.plot([x[0] for x in self.Env.obs], [x[1] for x in self.Env.obs], "sk")
        ax.plot([x + 0.5 for x in range(self.m) for _ in range(self.n)],
                [y + 0.5 for _ in range(self.m) for y in range(self.n)],
                'o', color='grey', markersize=2.5)
        rect = Rectangle((0, 0), self.m, self.n, linewidth=1, ec='k', facecolor='none')
        ax.add_patch(rect)

        for i in range(points.shape[1]):
            x = length_list[data[i]][0]
            y = length_list[data[i]][1]
            rect = Rectangle((points[0, i]-0.5 * x, points[1, i]-0.5 * y),
                             x, y, linewidth=1, ec='k', facecolor='none')
            ax.add_patch(rect)

        self.plot_uav_path(ax, coord_list, position, data, length_list)

        fig.savefig('partition.png', dpi=1000, bbox_inches='tight', pad_inches=0)
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

    def calculate_age(self,a,b,data=None):
        max_dist_1 = 0
        max_dist_2 = 0
        max_dist_3 = 0
        m = self.m
        n = self.n

        y_num=floor(self.m/a)
        x_num=floor(self.n/b)
        if y_num!=m/a:
            a_1 = self.m - y_num*a
            [max_dist_1,solution_1,coo_1]=self.sub_partition(a_1,b,self.r)

        if x_num!=n/b:
            b_1 = self.n - x_num*b
            [max_dist_2,solution_2,coo_2]=self.sub_partition(a,b_1,self.r)

        if y_num!=m/a and x_num!=n/b:
            a_2 = self.m - y_num*a
            b_2 = self.n - x_num*b
            [max_dist_3,solution_3,coo_3]=self.sub_partition(a_2,b_2,self.r)

        t_v1 = max_dist_1*self.footprint/self.v_max
        t_v2 = max_dist_2*self.footprint/self.v_max
        t_v3 = max_dist_3*self.footprint/self.v_max

        [max_dist,solution,coo]=self.sub_partition(a,b,self.r)
        deta=self.footprint*self.robust

        t_v=max_dist*self.footprint/self.v_max

        if t_v>self.e/self.beta_minus-2*deta/self.v_max:
            return inf, 0, []

        points=self.global_path(self.m,self.n,a,b)
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
                s = solver.solve(verbose=False)
                sol=s.tour.tolist()
        elif self.solver == "christofides":
            length, sol, G, MSTree, odd_vertexes, minimum_weight_matching, timing = tsp(dist_matrix)
        elif self.solver == "lkh":
            if points.shape[1]<4:
                sol = list(range(points.shape[1]))
            else:
                sol = elkai.solve_float_matrix(dist_matrix, runs=10)
        time_global=self.footprint*np.sqrt(np.square(points[0,sol]-points[0,sol[1:]+[sol[0]]])+\
        np.square(points[1,sol]-points[1,sol[1:]+[sol[0]]]))/self.u_max

        tv_array = np.tile(t_v,time_global.shape[0])

        if y_num!=m/a:
           for i in range(0,int(x_num*(y_num+1)),int(y_num+1)):
               tv_array[i]=t_v1

        if x_num!=n/b:
            total = int((x_num+1)*ceil(self.m/a))
            for i in range(total-1,total-1-y_num,-1):
               tv_array[i]=t_v2

        if y_num!=m/a and x_num!=n/b:
            tv_array[total-1-y_num]=t_v3

        tv_plus = tv_array*self.beta_minus/self.beta_plus

        t_u=sum(np.maximum(time_global,tv_plus))

        obj_1 = sum(tv_array)+t_u

        return obj_1, max_dist, solution


def test():
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
        'beta_plus':1,\
        'beta_minus':1,\
        'e':100,\
        'a_best':0,\
        'b_best':0,\
        'robust':0,\
        'solver':"concorde",\
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
        _, _, coord = ps.sub_partition(ps.a_best, ps.b_best, ps.r)
        for c in range(len(coord)):
            with open(project_dir+'/waypoint_{}_{}.txt'.format(0,c), 'w', newline='') as out:
                for p in range(coord[c].shape[1]):
                    out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],
                                                ps.footprint*coord[c][1][p], ps.h))
        points = ps.global_path(ps.m, ps.n, ps.a_best, ps.b_best)
        data = {i: 0 for i in range(points.shape[1])}

    else:
        new_x = None
        new_y = None
        _, _, coord = ps.sub_partition(ps.a_best,ps.b_best,ps.r)
        length_list.append((ps.b_best,ps.a_best))
        coord_list.append(coord)
        for c in range(len(coord)):
            with open(project_dir+'/waypoint_{}_{}.txt'.format(0,c), 'w', newline='') as out:
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
            with open(project_dir+'/waypoint_{}_{}.txt'.format(1,c), 'w', newline='') as out:
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
            with open(project_dir+'/waypoint_{}_{}.txt'.format(2,c), 'w', newline='') as out:
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
            with open(project_dir+'/waypoint_{}_{}.txt'.format(3,c), 'w', newline='') as out:

                if coord[c].size != 0:
                    for p in range(coord[c].shape[1]):
                        out.write('{} {} {} 0\n'.format(ps.footprint*coord[c][0][p],\
                                            ps.footprint*coord[c][1][p], ps.h))

        points=ps.global_path(ps.m,ps.n,ps.a_best,ps.b_best)

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
            s = solver.solve(verbose=False)
            sol=s.tour.tolist()
    elif ps.solver == "christofides":
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

	
    print(project_dir)
    with open(project_dir+'/data.json', 'w') as f:
        json.dump(data, f)

    np.savez(project_dir+'/ugvwaypoint.npz',pos=ps.footprint*points,
             delta=position*ps.footprint,robust=ps.robust)

    ps.plot_path(coord_list, position, data, length_list, points)


if __name__ == '__main__':
    test()


