import lxml
from requests import get as rget
from os import mkdir
from time import sleep
tum = "https://www.tum.de/en/studies/degree-programs"
stanford = 'https://gradadmissions.stanford.edu/programs'
oxford = 'https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing'

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"
}

tumsrc = rget(tum)
oxfordsrc = rget(oxford)
stasrc = rget(stanford)
try:
    mkdir("sites")
except Exception as ex:
    print(ex)
with open('sites/tum.html','w') as f:
    f.write(tumsrc.text)
with open('sites/oxford.html','w') as f:
    f.write(oxfordsrc.text)    
with open(f'sites/stanford.html','w') as f:
    f.write(stasrc.text)