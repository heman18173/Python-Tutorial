import json
from countries_codes import get_country_code

filename = 'population_data.json'
#Load data into list
with open(filename) as f:
    pop_data = json.load(f)
#Print 2010 population for each country
for pop_d in pop_data:
    if pop_d['Year'] == '2010':
        country_name = pop_d['Country Name']
        pop_val = int(float(pop_d['Value']))
        code = get_country_code(country_name)
        if code:
            print(code  + ':' + str(pop_val))
        else:
            print('Error:' + country_name)

