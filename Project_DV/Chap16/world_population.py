import json
#Obtain countries two digit code
from pygal.i18n import countries as cn

for cnt_cd in sorted(cn.keys()):
    print(cnt_cd, cn[cnt_cd])

filename = 'population_data.json'
#Load data into list
with open(filename) as f:
    pop_data = json.load(f)
#Print 2010 population for each country
for pop_d in pop_data:
    if pop_d['Year'] == '2010':
        country_name = pop_d['Country Name']
        pop_val = pop_d['Value']
        print(country_name + ':' + pop_val)
