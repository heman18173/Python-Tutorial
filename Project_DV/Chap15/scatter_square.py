import matplotlib.pyplot as plt 
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=50)
plt.title("Squares Number", fontsize=25)
plt.xlabel("NumberValue", fontsize=15)
plt.ylabel("Square Value", fontsize=15)
plt.tick_params(axis='both', which= 'major', labelsize=10)

#Calculating Data Automatically
x_values = list(range(1,1001))
y_values = [ x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors='none', c=(0.8, 0, 0.4), s=40)
# Set the range for each axis.
plt.axis([1, 1100, 0, 1100000])
#Using a Colormap
plt.scatter(x_values, y_values, edgecolors='none', c=y_values, cmap=plt.cm.Blues, s=40)
plt.show()
