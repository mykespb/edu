# (C) Mikhail Kolodin 2021-10-14
# 2021-10-14 2021-10-14 0.2
# testing mendeleev package 

import sys
import mendeleev
from mendeleev import element, get_all_elements

print(sys.version)

fe = element('Fe')
print(fe.name)
for iso in fe.isotopes:
    print(iso)
    
#Iron
#   26    54   53.93961 0.058
#   26    56   55.93494 0.918
#   26    57   56.93539 0.021
#   26    58   57.93327 0.003

els = get_all_elements()

print(els)

