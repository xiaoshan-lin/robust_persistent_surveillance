from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sqrt,inf
import time
from numpy import remainder as rem
import random


#---------End of imports


class mysim(): 
    def __init__(self):
        self.rounds = 5
        self.num_ugv = 3
        self.speed = 2
        self.euclidean_flag = False
        self.use_random_points = False
        self.equal_wait_time = False
        self.sim_init = True
        self.even_init = False
        self.coordinate_flag = False
        self.num_obs = 2
        self.sim_period = 1.9

        self.input_coordinates = "(1, 2), ( 1, 4),(1, 9 ),(3,9),(7,9),(7,5),(7,2) "
        self.input_distance = "1,2,1,1,1,2,1"
        self.input_wait_time = "1,2,1,2,1,2,1"

        self.first_arrive = [True]*self.num_ugv
        self.last_time = 0.0
        self.coordinate_time = [0.0 for i in range(self.num_ugv)]        

        self.data_from_text()
        

    def data_from_text(self):
                
        self.coordinates = self.coord_from_text(self.input_coordinates)
        self.wait_time = self.wait_time_from_text(self.input_wait_time)

        if not self.euclidean_flag:
            distance = self.distance_from_text(self.input_distance)
            
        else:
            distance = []
            for i in range(len(self.coordinates)):
                next = i + 1
                if next == len(self.coordinates):
                    next = 0
                x = self.coordinates[i][0]-self.coordinates[next][0]
                y = self.coordinates[i][1]-self.coordinates[next][1]
                distance.append(sqrt(x**2+y**2))
       
        self.time = [i/self.speed for i in distance]
        self.age = sum(self.time)+sum(self.wait_time)
        self.init_wait_time = [i*self.age/self.num_ugv for i in range(self.num_ugv)]
        self.init_flag = [True]*len(self.coordinates)
        self.time_point = [0]
        for i in range(len(self.time)):
            self.time_point.append(self.time_point[-1]+self.wait_time[i])
            self.time_point.append(self.time_point[-1]+self.time[i])
        del self.time_point[-1]
        print("desired age:")
        print(self.age)
        

    def coord_from_text(self,text):
        c_list = []
        for idx,i in enumerate(text):
           if i=='(':
               for j in range(idx+1,len(text)):
                   if text[j]==',':
                       comma = j
                       break
               try:
                   first = float(text[idx+1:comma])
               except:
                   print("Please check the format of the entered coordinates")
                   raise
               for k in range(comma+1,len(text)):
                   if text[k]==')':
                       r_bracket = k
                       break
               try:
                   second = float(text[comma+1:r_bracket])
                   
               except:
                   print("Please check the format of the entered coordinates")
                   raise
               c_list.append((first,second))
        return c_list

    def distance_from_text(self,text):
        if text.strip()=="":
            raise Exception("Please enter distance")
        start = 0
        dist = []
        for idx,i in enumerate(text):
            if i == ",":
                try:
                    d = float(text[start:idx])
                    dist.append(d)
                    start = idx + 1
                except:
                    print("Please check the format of the entered distance")
                    raise
        dist.append(float(text[idx:]))
        return dist

    def wait_time_from_text(self,text):
        if self.equal_wait_time:
            try:
                return([float(text.strip())]*len(self.coordinates))
            except Exception as e:
                print("Please check the format of the entered wait time")
                print(e)
                raise
        else:
            start = 0
            wait_time = []
            for idx,i in enumerate(text):
                if i == ",":
                    try:
                        d = float(text[start:idx])
                        wait_time.append(d)
                        start = idx+1
                    except:
                        print("Please check the format of the entered wait time")
                        raise
            wait_time.append(float(text[idx:]))
            if len(wait_time) != len(self.coordinates):
                raise Exception("number of coordinates doesn't equal to that of wait time")
            return wait_time


    def start_simulation(self):

        self.plot_x = []
        self.plot_y = []

        x_min = inf
        x_max = -inf
        y_min = inf
        y_max = -inf

        for i in sim.coordinates:
            if i[0]<x_min:
                x_min = i[0]
            if i[1]<y_min:
                y_min=i[1]
            if i[0]>x_max:
                x_max=i[0]
            if i[1]>y_max:
                y_max=i[1]

        self.root = Tk.Tk()
        self.root.geometry("2000x1000")
        self.root.resizable(0, 0)

        
        fig = plt.figure()
        fig.set_dpi(100)
        fig.set_size_inches(7, 6.5)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().place(x=30,y=60)

        #self.ax = plt.axes(xlim=(x_min, x_max), ylim=(y_min, y_max))
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

        self.fig = plt.Figure()
        self.fig.set_dpi(150)
        self.fig.set_size_inches(7, 6.5)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.set_xlabel('time/s')
        self.subplot.set_ylabel('maximum age/s')
        self.canvas_1 = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_1.get_tk_widget().place(x=800,y=60)
        self.random_obs = [random.randrange(0,int(self.age)*1000,int(self.age))/200\
                           for i in range(2*self.num_obs)]
        self.random_obs.sort()
        self.random_obs = [5,12,18,26]
        self.random_time = [(random.randrange(0,len(self.coordinates)),\
                            random.randrange(10,15)) \
                            for i in range(self.num_obs)]
        self.random_time = [(0,10),(5,12)]

        self.tem_time_point = []
        self.obs_xy = []
        self.time_obs = []
        for bao in self.random_time:
            x1 = self.coordinates[bao[0]][0]
            y1 = self.coordinates[bao[0]][1]

            if bao[0]+1==len(self.coordinates):
                idx = 0
            else:
                idx = bao[0]+1
            x2 = self.coordinates[idx][0]
            y2 = self.coordinates[idx][1]

            self.obs_xy.append((x1/2+x2/2,y1/2+y2/2))
            time_obs = self.time
            time_obs[bao[0]]=bao[1]/self.speed
            obs_time_point = [0]
            for i in range(len(self.time)):
                obs_time_point.append(obs_time_point[-1]+self.wait_time[i])
                obs_time_point.append(obs_time_point[-1]+time_obs[i])
            del obs_time_point[-1]
            self.tem_time_point.append(obs_time_point)
            self.time_obs.append(time_obs)

        for idx, i in enumerate(self.coordinates):
            self.ax.add_patch(plt.Circle((i[0],i[1]),0.3,fc='k'))
            self.ax.add_line(plt.Line2D((i[0], self.coordinates[idx-1][0],), \
                                    (i[1], self.coordinates[idx-1][1]), lw=2.5))
 
        self.patch = []
        self.patch_obs = []

        if self.even_init:
            self.x_init = self.coordinates[0][0]
            self.y_init = self.coordinates[0][1]
            self.xy_init = [(self.x_init, self.y_init) for i in range(self.num_ugv)]
        else:
            self.xy_init = []
            self.random_t = [random.randrange(0,self.age*100,2)/100 for i in range(self.num_ugv)]
            self.random_t = [0,2,4]
            self.random_t.sort(reverse=True)
            self.theta = self.random_t
            self.visited_time = [[0] for i in range(len(self.coordinates))]  
            self.real_time = 0.0
            self.last_i = 0.0
            self.has_obs = False
            for idx,i in enumerate(self.random_t):
                x,y = self.get_xy(i,idx)
                self.xy_init.append((x,y))
            


        for i in range(self.num_ugv):
            self.patch.append(plt.Circle(self.xy_init[i], 0.75, fc='y'))


        
        
        anim = animation.FuncAnimation(fig, self.animate,
                                       init_func=self.init,
                                       frames=np.arange(0,self.sim_period*self.age+self.age/200,self.age/200),
                                       interval = 0.0005*self.age,
                                       blit=True,
                                       repeat=False)
        
        
        Tk.mainloop()
        

    def init(self):
        for i in range(self.num_ugv):
            self.patch[i].center = self.xy_init[i]
            self.ax.add_patch(self.patch[i])
        return self.patch

    def animate(self,i):
       
        self.real_time = i   
       
        '''for zz,bb in enumerate(self.tem_time_point):

            if i > self.random_obs[zz*2] and i < self.random_obs[zz*2+1] :
                if not self.has_obs: 
                    print('123')
                    self.time_point_obs = bb               
                    self.patch.append(plt.Circle(self.obs_xy[zz], 0.75, fc='r'))
                    self.patch[-1].center = self.obs_xy[zz]
                    self.ax.add_patch(self.patch[-1])
                    self.has_obs = True
                break            

            else:
                print(1)
                self.has_obs = False
                if len(self.patch) == self.num_ugv+1:
                    self.patch[-1].remove()'''

        if self.even_init:
            if self.sim_init:
                if i < self.age*(self.num_ugv-1)/self.num_ugv:
                    #x, y = patch.center
                    for idx in range(self.num_ugv):
                        
                        if i<self.init_wait_time[idx] and self.init_flag[idx]:
                            x,y = self.get_xy(0,idx)
                        else:

                            self.init_flag[idx] = False
                            x,y = self.get_xy(i-self.init_wait_time[idx],idx,zz)
                        self.patch[idx].center = (x, y)
                else:
                    self.sim_init = False
            else:
                for idx in range(self.num_ugv):
                    x,y = self.get_xy(i+self.random_t[idx],idx)
                    self.patch[idx].center = (x, y)

        else:
           for idx in range(self.num_ugv):
                #x,y = self.get_xy(i+self.theta[idx],idx, self.random_time[zz][0])
                x,y = self.get_xy(i+self.theta[idx],idx)
                self.patch[idx].center = (x, y)

        self.plot_result(i)
        self.last_i = i
        return self.patch

    def get_xy(self,t,index, obs_idx = -1, obs_id = -1):
        
        if self.theta[index-1]-self.theta[index] < 0:
            d = self.age + self.theta[index-1]-self.theta[index] 
        else:
            d = self.theta[index-1]-self.theta[index] 
            
        if d < 14.4/(self.num_ugv) and self.coordinate_flag:           

            if t!= self.random_t[index]:
                t = t - self.age/200            
                self.theta[index]= self.random_t[index]-self.age/200
                if self.theta[index]<0:
                    self.theta[index] = self.age+self.theta[index]

        if t<0:
            t=t+self.age
        while t>self.age:
            t = t - self.age
        end = []
        for i in range(len(self.time_point)):
            if t < self.time_point[i]:
                end = i
                break
        if end == []:
            end = 0
        
        if rem(end,2)==0:
            self.first_arrive[index] = True
            idx = int(end/2)
            '''if idx-1 == obs_idx:
                print('-----')
                x = self.coordinates[idx-1][0] + (self.coordinates[idx][0] - self.coordinates[idx-1][0])\
                                             *(t- self.tem_time_point[obs_id][end-1])/self.time_obs[obs_id][idx-1]  
                y = self.coordinates[idx-1][1] + (self.coordinates[idx][1] - self.coordinates[idx-1][1])\
                                             *(t- self.tem_time_point[obs_id][end-1])/self.time_obs[obs_id][idx-1] 

            else:
                x = self.coordinates[idx-1][0] + (self.coordinates[idx][0] - self.coordinates[idx-1][0])\
                                             *(t-self.time_point[end-1])/self.time[idx-1]  
                y = self.coordinates[idx-1][1] + (self.coordinates[idx][1] - self.coordinates[idx-1][1])\
                                             *(t-self.time_point[end-1])/self.time[idx-1] '''
            x = self.coordinates[idx-1][0] + (self.coordinates[idx][0] - self.coordinates[idx-1][0])\
                                             *(t-self.time_point[end-1])/self.time[idx-1]  
            y = self.coordinates[idx-1][1] + (self.coordinates[idx][1] - self.coordinates[idx-1][1])\
                                             *(t-self.time_point[end-1])/self.time[idx-1]
        else:
            idx = int((end-1)/2)
            x = self.coordinates[idx][0]
            y = self.coordinates[idx][1]

            if self.first_arrive[index]:
                self.first_arrive[index] = False
                self.visited_time[idx].append(self.real_time)

        return x,y

    def plot_result(self,c_t):
       
        '''if self.even_init:

            visited_time = [0]
            ugv_visited_times = []

            for i in range(len(self.coordinates)-1):
                visited_time.append(self.wait_time[i]+self.time[i])
            
            for i in range(len(self.coordinates)):
                a = [visited_time[i]+self.init_wait_time[ugv] for ugv in range(self.num_ugv)]
                a = np.tile(a,self.rounds)
                b = a + np.repeat(range(self.rounds),self.num_ugv)*self.age
                b = b.tolist()
                if b[0]!=0:
                    b.insert(0,0)
                ugv_visited_times.append(b)

        else:
            ugv_visited_times = self.visited_time'''
        ugv_visited_times = self.visited_time
        
        if c_t != 0.0:
            for i in np.arange(self.last_time,c_t+(c_t-self.last_time)/50,(c_t-self.last_time)/50):
                real_max = -inf
                for j in range(len(self.coordinates)):
                    found = False
                    max_age = -inf
                    for idx,k in enumerate(ugv_visited_times[j]):
                        if i<k and found:
                            break    
                        else:
                            max_age = i - k
                            found = True
                    real_max = max(max_age, real_max)
                self.plot_y.append(real_max)
                self.plot_x.append(i)
            self.last_time = c_t
            self.subplot.plot(self.plot_x, self.plot_y, 'k')

            self.canvas_1.draw()

            if c_t>=self.sim_period*self.age-self.age/200:
                self.canvas_1.print_figure('123.png')

    def save_as_png(self,canvas,fileName):
        # save postscipt image 
        canvas.postscript(file = fileName + '.eps') 
        # use PIL to convert to PNG 
        img = Image.open(fileName + '.eps') 
        img.save(fileName + '.png', 'png') 


        
        

if __name__ == "__main__":
   
    sim = mysim()
    sim.start_simulation()


   
    
    
       
