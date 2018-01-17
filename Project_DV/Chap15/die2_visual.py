import pygal
from die import Die

#Create 2 D6
die1= Die()
die2= Die()


#Make some rolls and store some results
results= []
for roll_num in range(1000):
    result= die1.roll() + die2.roll()
    results.append(result)

#Analyzing the Results
frequences= []
max_results = die1.num_sides + die2.num_sides

for value in range(2, max_results+1):
    freq=results.count(value)
    frequences.append(freq)
 
hist= pygal.Bar()

#hist.title("Results of die D6 Frequecy from 1 to 6")
#hist.x_title("Results")
#hist.y_title("Frequency Of Result")

hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.add('D6-D12', frequences)
hist.render_to_file('die2_visual.svg')
