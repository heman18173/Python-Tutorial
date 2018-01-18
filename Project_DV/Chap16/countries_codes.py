#Obtain countries two digit code
from pygal.maps.world import COUNTRIES as cn

def get_country_code(country_code):
    """Return the Pygal 2-digit for given country code"""
    for code, name in cn.items():
        if name == country_code:
            return code
        # If country wasnt not found, return None
    return None
    
#print(get_country_code('India'))
#print(get_country_code('Sri Lanka'))
#print(get_country_code('Afghanistan'))


