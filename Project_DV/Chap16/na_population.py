import pygal

wm = pygal.maps.world.World()

wm.title = "Population of North America"
wm.add('North America',{'ca':737432974, 'mx':7323923, 'us':3873274932})
wm.render_to_file('us_population.svg')