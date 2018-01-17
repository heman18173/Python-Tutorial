import pygal
from die import Die

#Create D6
die= Die()

#Make some rolls and store some results
results= []
for roll_num in range(1000):
    result= die.roll()
    results.append(result)
print(results)

#Analyzing the Results
frequences= []
for value in range(1, die.num_sides+1):
    freq=results.count(value)
    frequences.append(freq)
 
#print(frequences)

hist= pygal.Bar()

#hist.title("Results of die D6 Frequecy from 1 to 6")
#hist.x_title("Results")
#hist.y_title("Frequency Of Result")

hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.add('D6', frequences)
hist.render_to_file('die_visual.svg')
