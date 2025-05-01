import csv
from matplotlib import pyplot as plt
with open('datapoints.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # Skip the header row
    data = data[0:10]
    # Convert the data to a list of lists of floats    
    data = [[int(x) for x in row] for row in data]
    for i, row in enumerate(data):
        if i == 0:  # 0-based index, so 2 means the 3rd row
            x_values=row
        if i == 1:  # 0-based index, so 2 means the 3rd row
            y_values=row
        
    #makes sure everything is in the right format    
    print(x_values)
    print(y_values)
    
x_axis_x=[-10,10]
x_axis_y=[0,0]
y_axis_y=[-100,100]
y_axis_x=[0,0]
plt.plot(x_axis_x, x_axis_y)
plt.plot(y_axis_x, y_axis_y)

plt.plot(x_values, y_values, marker='o', linestyle='-')
print("done")
plt.show()
    


