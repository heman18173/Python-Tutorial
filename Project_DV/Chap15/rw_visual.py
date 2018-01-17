import matplotlib.pyplot as plt 
from random_walk import RamdonWalk

# Make a random walk, and plot the points.
while True:
    rw = RamdonWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove Axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #Adding plot points
    rw =  RamdonWalk(50000)
    rw.fill_walk()
    #Set size of plottig window
    plt.figure(dpi=128, figsize=(6,5))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors=None, s=1)
   
    plt.show()  

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break