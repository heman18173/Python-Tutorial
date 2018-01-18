#Obtain countries two digit code
from pygal.maps.world import COUNTRIES as cn

for cnt_cd in sorted(cn.keys()):
    print(cnt_cd, cn[cnt_cd])