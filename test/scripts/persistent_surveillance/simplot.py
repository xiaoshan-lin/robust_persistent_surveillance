import numpy as np
import matplotlib.pyplot as plt
import json
project_dir = '/home/xslin/Documents/xslin/research/rpg_ws/src/test/resource/'
traj = np.load(project_dir+'trajectory.npy', 'r')
f=np.load(project_dir+'ugvwaypoint.npz', 'rb')
old_points=f['pos']
color=[(174/255,199/255,232/255),(1,187/255,120/255),(152/255,223/255,138/255),(1,152/255,150/255)]

obs_list =  {'pos':[(0.5,1.5),(1.5,1.5),(2.5,1.5),(4.5,11.5),(4.5,12.5),(4.5,13.5),(2.5,24.5),(3.5,24.5),(4.5,24.5),(5.5,24.5),(6.5,24.5),(22.5,21.5),(21.5,20.5),(21.5,21.5),(21.5,22.5),(24.5,2.5),(24.5,3.5),(24.5,4.5),(24.5,5.5),(24.5,6.5),(24.5,7.5),(24.5,8.5),(24.5,9.5),(24.5,0.5),(24.5,1.5),(7.5,3.5),(8.5,3.5),(9.5,2.5),(7.5,7.5),(7.5,8.5),(8.5,7.5),(8.5,8.5),(5.5,18.5),(6.5,18.5),(7.5,18.5),(8.5,18.5),(5.5,19.5),(7.5,19.5),(12.5,17.5),(12.5,15.5),(15.5,9.5),(16.5,8.5),(17.5,6.5),(17.5,7.5),(17.5,8.5),(18.5,4.5),(4.5,20.5),(4.5,21.5),(20.5,21.5),(20.5,20.5),(20.5,13.5),(21.5,13.5),(21.5,12.5),(20.5,12.5),(13.5,4.5)]}

new_points = [[3.5,17.5,19.5,16.5,4.5],[18.5,21.5,16.5,2.5,9.5]]

with open('obs.json', 'w') as f:
    json.dump(obs_list,f)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

e = 0.05

for i in obs_list['pos']:
    plt.plot([[i[0]-0.5+e,i[0]-0.5+e,i[0]-0.5+e,i[0]-0.17+e,i[0]+0.16+e],\
              [i[0]-0.17-e,i[0]+0.16-e,i[0]+0.5-e,i[0]+0.5-e,i[0]+0.5-e]],\
              [[i[1]+0.17+e,i[1]-0.16+e,i[1]-0.5+e,i[1]-0.5+e,i[1]-0.5+e],\
              [i[1]+0.5-e,i[1]+0.5-e,i[1]+0.5-e,i[1]+0.17-e,i[1]-0.16-e]],'k',linewidth=0.5)
    plt.plot([i[0]-0.5,i[0]+0.5,i[0]+0.5,i[0]-0.5,i[0]-0.5],\
              [i[1]+0.5,i[1]+0.5,i[1]-0.5,i[1]-0.5,i[1]+0.5],'k',linewidth = 0.8)


# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 30, 1)

ax.set_xticks(major_ticks)
ax.set_yticks(major_ticks)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    labelbottom=True)

# And a corresponding grid

ax.grid(color='k',which='both',linewidth=0.5)
ax.set_xlim([0,25])
ax.set_ylim([0,25])
ax.set_yticklabels([])
ax.set_xticklabels([])

ax.set_aspect("equal")
plt.savefig('filename.png', dpi=1000)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for i in obs_list['pos']:
    plt.plot([[i[0]-0.5+e,i[0]-0.5+e,i[0]-0.5+e,i[0]-0.17+e,i[0]+0.16+e],\
              [i[0]-0.17-e,i[0]+0.16-e,i[0]+0.5-e,i[0]+0.5-e,i[0]+0.5-e]],\
              [[i[1]+0.17+e,i[1]-0.16+e,i[1]-0.5+e,i[1]-0.5+e,i[1]-0.5+e],\
              [i[1]+0.5-e,i[1]+0.5-e,i[1]+0.5-e,i[1]+0.17-e,i[1]-0.16-e]],'k',linewidth=0.5)
    plt.plot([i[0]-0.5,i[0]+0.5,i[0]+0.5,i[0]-0.5,i[0]-0.5],\
              [i[1]+0.5,i[1]+0.5,i[1]-0.5,i[1]-0.5,i[1]+0.5],'k',linewidth = 0.8)

plt.plot(traj[0,:],traj[1,:],c=color[3],linewidth = 1.5)
plt.scatter(new_points[0],new_points[1],color=(214/255,39/255,40/255), marker='s')
plt.scatter(old_points[0,:],old_points[1,:],color=(44/255,160/255,44/255), marker='s')
x_a = [9,18]
y_a = [9,18]
plt.plot([[9,18,0,0],[9,18,25,25]],[[0,0,9,18],[25,25,9,18]],c='k',linewidth=2)

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 30, 1)

ax.set_xticks(major_ticks)
ax.set_yticks(major_ticks)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    labelbottom=True)

# And a corresponding grid

ax.grid(color='k',which='both',linewidth=0.5)
ax.set_xlim([0,25])
ax.set_ylim([0,25])
ax.set_yticklabels([])
ax.set_xticklabels([])

ax.set_aspect("equal")
plt.savefig('filename.png', dpi=1000)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x= [0,2,4,6,8,10]
y= [1311.46, 1251.84, 1210, 1470.47, 1608.67, 1820.92]
plt.plot(x,y,'-ok')
plt.xlabel("robustness(/m)")
plt.ylabel("age(/s)")
plt.savefig('conser.png', dpi=1000)
plt.show()






