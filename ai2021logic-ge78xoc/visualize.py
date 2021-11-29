"""
draw function created on Thu Nov  5 10:26:36 2020
Preceding code created on Thu Nov  5 10:17:08 2020

@author: benel

Merged the previously separated files on Thu Nov  12 10:18:50
Added some cosmetics to the signs as well.
Finally, changed the form of the walls.
by Adrian K
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math

# Color Display
# Black = Wall
# Red = Agent


# Initializing number of dots
steps_between_points = 100

global paths
global walls_in_model

paths = []
walls_in_model = []

# Creating dot class
class Dot(object):
    
    def __init__(self, x, y, agent):
        self.agent = agent
        self.x = x
        self.y = y
        self.pathsegment = 1
        self.velx = 0
        self.vely = 0
        self.steps_taken = 0


    def generate_vel(self):
        
        
        if self.pathsegment < len(paths[self.agent])-1:
            vel = np.array(paths[self.agent][self.pathsegment + 1]) - np.array(paths[self.agent][self.pathsegment])
        else:
            vel = [0,0]
        return vel

    def move(self):

        self.steps_taken += 1
        
        # If we reach a new vertex of our path we need to update the pathsegment we are in
        # and restart our counter
        if self.steps_taken == steps_between_points:
            self.steps_taken = 0
            self.pathsegment += 1

        # Move the dot in the needed direction
        self.x = self.x + self.generate_vel()[0]/steps_between_points
        self.y = self.y + self.generate_vel()[1]/steps_between_points
        return

class wall(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
def visualize(paths_to_visualize, walls, stop_sign, right_of_way):
    global paths
    global walls_in_model
    
    paths = paths_to_visualize
    walls_in_model = walls
    
    
         
            
    # Initializing dots
    dots = []
    
    # Initializing walls
    # @@ We need to deactivate the next line if we want to make the modified walls.
    #walls = [wall(walls_in_model[i][0], walls_in_model[i][1]) for i in range(len(walls_in_model))]
    
    stop_sign = [wall(stop_sign[0], stop_sign[1]) for i in range(len(stop_sign))]
    
    right_of_way = [wall(right_of_way[0], right_of_way[1]) for i in range(len(right_of_way))]
    
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(5, 10.5), ylim=(5, 10.5))
    
    # Setting the Plot
    ax.spines['bottom'].set_color('grey') 
    ax.text(4.5, 0, 'Vehicle 0', weight = 'bold', fontsize = 12)
    ax.text(11.3, 4.6, 'Vehicle 1', rotation = -90, weight = 'bold', fontsize = 12)
    ax.text(4.5, 10.6, 'Vehicle 2', weight = 'bold', fontsize = 12)
    ax.text(-0.5, 4.6, 'Vehicle 3', rotation = 90, weight = 'bold', fontsize = 12)
    ax.spines['top'].set_color('grey') 
    ax.xaxis.label.set_color('white') 
    ax.tick_params(axis='x', colors='white')

    # @@
    #if False:
    #    ax.plot(4, 7, marker = '$WOW$, c = 'red', markersize = 22)
    #    ax.plot(5, 7, marker = '$YOU$', c = 'red', markersize = 19)
    #    ax.plot(6, 7, marker = '$FOUND$', c = 'red', markersize = 25)
    #    ax.plot(7, 7, marker = '$ME!$', c = 'red', markersize = 19)
    #    ax.plot(5, 6, marker = '$GOOD$', c = 'red', markersize = 25)
    #    ax.plot(6, 6, marker = '$JOB!$', c = 'red', markersize = 19)
    #    ax.plot(4, 5, marker = '$NOW$', c = 'red', markersize = 19)
    #    ax.plot(5, 5, marker = '$BACK$', c = 'red', markersize = 20)
    #    ax.plot(6, 5, marker = '$TO$', c = 'red', markersize = 13)
    #    ax.plot(7, 5, marker = '$WORK$', c = 'red', markersize = 25)
    #    ax.plot(7.6, 5, marker = '$!$', c = 'red', markersize = 10)
    #    ax.plot(5.5, 4, marker = '$:)$', c = 'red', markersize = 19)
    
    ax.spines['left'].set_color('grey') 
    ax.spines['right'].set_color('grey') 
    ax.xaxis.label.set_color('white') 
    ax.tick_params(axis='y', colors='white')

    
    plt.style.use('seaborn-whitegrid')

    # @@ If the grid and axes are removed, the next few lines are useless
    #minor_ticks = np.arange(0.5, 11, 1)
    
    #ax.set_xticks(minor_ticks)
    #ax.set_yticks(minor_ticks)

    # @@ This makes sure that all the drawings look nice and accurate.
    plt.axis('equal')

    # @@ And this removes the grid; in my opinion it looks better that way.
    ax.grid(False)
    plt.axis('off')
    
    
    
    d, = ax.plot([dot.x for dot in dots],
                 [dot.y for dot in dots], 'ro', c = 'black',  markersize = 15)
    
    # @@ The next lines give the orginal walls
    #ax.plot([wall.x for wall in walls],
    #             [wall.y for wall in walls], 's', c = 'black', markersize = 10)
    # @@ Here are the modified ones:
    for w in walls:
        ax.plot(w[0], w[1], w[2], c = 'black', markersize = 53.5)


    # @@ Now we come to the stop sign. First, we delete what is in the background of the sign
    # @@ by plotting a white square...
    ax.plot([stop.x for stop in stop_sign],
            [stop.y for stop in stop_sign], 's', c = 'white', markersize = 25)
    
    # @@ ... now we need a small, black contour...
    ax.plot([stop.x for stop in stop_sign],
            [stop.y for stop in stop_sign], '8', c = 'black', markersize = 25)

    # @@ ... then there is a slight white padding...
    ax.plot([stop.x for stop in stop_sign],
            [stop.y for stop in stop_sign], '8', c = 'white', markersize = 23)
    
    ax.plot([stop.x for stop in stop_sign],
            [stop.y for stop in stop_sign], '8', c = 'red', markersize = 22)

    ax.plot([stop.x for stop in stop_sign],
            [stop.y for stop in stop_sign], marker = '$STOP$', c = 'white', markersize = 19)




    # @@ Now creating a Right-of-Way sign. First, we delete what is in the background of the sign
    # @@ by plotting a white square...
    ax.plot([right.x for right in right_of_way],
            [right.y for right in right_of_way], 's', c = 'white', markersize = 25)

    # @@ ... then we make the black contour of the sign...
    ax.plot([right.x for right in right_of_way],
            [right.y for right in right_of_way], 'D', c = 'black', markersize = 16)

    # @@ ... then the white part...
    ax.plot([right.x for right in right_of_way],
            [right.y for right in right_of_way], 'D', c = 'white', markersize = 15)

    # @@ ... and again a smaller, black contour for the yellow part...
    ax.plot([right.x for right in right_of_way],
            [right.y for right in right_of_way], 'D', c = 'black', markersize = 12.5)

    # @@ ... and finally the yellow center.
    ax.plot([right.x for right in right_of_way],
            [right.y for right in right_of_way], 'D', c = 'yellow', markersize = 12)

    

    
    
    # Animation function.  This is called sequentially
    def animate(i):
        
        current_timestep = i/steps_between_points

        for dot in dots:
            if dot.pathsegment < len(paths[dot.agent])-1:
                dot.move()
            else:
                dots.remove(dot)

        for path in paths:
            if current_timestep == float(path[0]):
                dots.append(Dot(path[1][0], path[1][1], paths.index(path)))                
            
        d.set_data([dot.x for dot in dots],
                   [dot.y for dot in dots])
        

        return d,
    
    # Call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, frames=25000, interval=5, blit = True, repeat = False)
    
    return anim



# Input is a tuple of (problem_setting, solution)
def draw(input):
    paths = [[0,[6,3], [6,4], [6,5], [6,6], [6,7], [6,8], [6,9]],
             [0,[8,6], [7,6], [6,6], [5,6], [4,6], [3,6], [2,6]],
             [0,[5,8], [5,7], [5,6], [5,5], [5,4], [5,3], [5,2]],
             [0,[3,5], [4,5], [5,5], [6,5], [7,5], [8,5], [9,5]]]
    
    
    sign_positions = [[7,3], [8,7], [4,8], [3,4]]
    
    stop_sign = []
    right_of_way = []
    
    # Gives us the signn positions based on the input
    for i in range(len(input[0])):
        if input[0][i] == 'right of way':
            right_of_way = sign_positions[i]
            
        if input[0][i] == 'stop':
            stop_sign = sign_positions[i]
            
    # Configurates the paths according to the ordering of the vehicles   
    for i in range(len(input[1])):
        for j in range(input[1][i]-1):
            for k in range(7):
                paths[i].insert(1,paths[i][1])
    
    indices = []
    for i in range(len(input[1])):
        if input[1][i] == 0:
            indices.append(i)
            
    for i in sorted(indices, reverse = True):
        del paths[i]
            
    # This is just for 4 vehicles
    walls = [[4,1], [4,2], [4,3], [4,4], [3,4], [2,4], [1,4], [1,7], [2,7], [3,7], [4,7], [4,8], [4,9], [4,10], [7,10], [7,9], [7,8], [7,7], [8,7], [9,7], [10,7],
             [10,4], [9,4], [8,4], [7,4], [7,3], [7,2], [7,1]]
    # @@ What follows is a different modell of the walls
    walls = [[4,1,'|'], [4,2,'|'], [4,3,'|'], [4,4,''], [3,4,'_'], [2,4,'_'], [1,4,'_'], [1,7,'_'], [2,7,'_'], [3,7,'_'], [4,7,''], [4,8,'|'], [4,9,'|'], [4,10,'|'], [7,10,'|'], [7,9,'|'], [7,8,'|'], [7,7,''], [8,7,'_'], [9,7,'_'], [10,7,'_'],
             [10,4,'_'], [9,4,'_'], [8,4,'_'], [7,4,''], [7,3,'|'], [7,2,'|'], [7,1,'|']]
    
    # This draws our animation
    outer_anim = visualize(paths, walls, stop_sign, right_of_way)
    
    return outer_anim
