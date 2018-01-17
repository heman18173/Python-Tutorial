import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_valu es, squares, linewidth=5)
plt.title("Squares Number", fontsize=25)
plt.xlabel("NumberValue", fontsize=15)
plt.ylabel("Square Value", fontsize=15)
plt.tick_params(axis='both', labelsize=14)
plt.show()
#plt.savefig('myfirstGp.png', bbox_inches= 'tight')