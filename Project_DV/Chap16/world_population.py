import json
import pygal
from countries_codes import get_country_code
from pygal.style import RotateStyle

filename = 'population_data.json'
#Load data into list
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_d in pop_data:
    if pop_d['Year'] == '2010':
        country_name = pop_d['Country Name']
        pop_val = int(float(pop_d['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = pop_val

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
       
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
