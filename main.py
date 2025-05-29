import csv
from matplotlib import pyplot as plt
with open('Push_Back/redblocks.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # Skip the header row
    data = data[0:]
    # Convert the data to a list of lists of floats    
    data = [[int(x) for x in row] for row in data]
    for i, row in enumerate(data):
        if i == 0: 
            x_values_red=row
        if i == 1: 
            y_values_red=row
        
    #makes sure everything is in the right format    
with open('Push_Back/blueblocks.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # Skip the header row
    data = data[0:]
    # Convert the data to a list of lists of floats    
    data = [[int(x) for x in row] for row in data]
    for i, row in enumerate(data):
        if i == 0: 
            x_values_blue=row
        if i == 1: 
            y_values_blue=row
        
    #makes sure everything is in the right format    
with open('Push_Back/MiddleGoallow.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # Skip the header row
    data = data[0:]
    # Convert the data to a list of lists of floats    
    data = [[int(x) for x in row] for row in data]
    for i, row in enumerate(data):
        if i == 0: 
            x_values_low_goal=row
        if i == 1: 
            y_values_low_goal=row
            
with open('Push_Back/MiddleGoalhigh.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # Skip the header row
    data = data[0:]
    # Convert the data to a list of lists of floats    
    data = [[int(x) for x in row] for row in data]
    for i, row in enumerate(data):
        if i == 0: 
            x_values_high_goal=row
        if i == 1: 
            y_values_high_goal=row
        
#    makes sure everything is in the right format    

    
#coordinates for the game grid and axis
x_axis_x=[-1800,1800]
x_axis_y=[0,0]
y_axis_y=[-1800,1800]
y_axis_x=[0,0]
y_grid=[-1800,1800]
xy_grid=[-1800,-1800]
xy_grid2=[-1200,-1200]
xy_grid3=[-600,-600]
xy_grid4=[600,600]
xy_grid5=[1200,1200]
xy_grid6=[1800,1800]
xy_grid7=[1500,1500]
xy_grid8=[-1500,-1500]

#main Axis
plt.style.use('dark_background')
plt.plot(x_axis_x, x_axis_y, color='white')
plt.plot(y_axis_x, y_axis_y, color='white')

#game grid
plt.plot(xy_grid, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(xy_grid2, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(xy_grid3, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(xy_grid4, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(xy_grid5, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(xy_grid6, y_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid2, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid3, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid4, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid5, color='white', linestyle='dashed', zorder=0)
plt.plot(y_grid, xy_grid6, color='white', linestyle='dashed', zorder=0)

#starting lines
plt.plot(xy_grid7,y_grid , color='white', linestyle='solid', linewidth=0.5)
plt.plot(xy_grid8, y_grid, color='white', linestyle='solid', linewidth=0.5)

plt.scatter(x_values_red, y_values_red, marker='o', color='red', s=60 )
plt.scatter(x_values_blue, y_values_blue, marker='o', color='blue', s=60)
plt.plot(x_values_low_goal, y_values_low_goal, color='Yellow', linewidth=5)
plt.plot(x_values_high_goal, y_values_high_goal, color='Yellow', linewidth=5)
plt.xticks(range(-1800, 1801, 600))
plt.yticks(range(-1800, 1801, 600))
print("done")
plt.show()
