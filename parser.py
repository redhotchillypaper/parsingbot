from bs4 import *
from json import dump,load
from pprint import pprint
from os import remove
with open('sites/tum.html','r') as f:
    srctum = f.read()
with open('sites/oxford.html') as f:
    srcoxf = f.read()
with open('sites/stanford.html') as f:
    srcsta = f.read()

souptum = BeautifulSoup(srctum,'lxml')
soupoxf = BeautifulSoup(srcoxf,'lxml')
soupsta = BeautifulSoup(srcsta,'lxml')

selectsta = soupsta.find_all('table',class_="views-view-grid cols-2")
selectoxf = soupoxf.find('div',class_='view-content clearfix')
selecttum = souptum.find(class_='c-in2studyfinder-filter__select js-in2studyfinder-select2')
hrefs = souptum.find('select').find_all('option')
sta = []
for i in selectsta:
    sta.append(i.text)
sta = [i.replace('\n','') for i in sta if i != '']
tmp = ''
for i in sta:

    for j in i:
        tmp += j

sta = tmp.split('\xa0')
sta = [i.strip() for i in sta]
stan = {}
for i in sta:
    stan[i] = {'degree':['Bachelor'],'url':'https://gradadmissions.stanford.edu/programs/'+i.lower().replace(' ','-')}
# pprint(stan)
links = {
    'oxford':{},
    'tum':{},
    'stanford':stan
    }

for i in selectoxf.find_all('div',class_="course-title"):
    for j in i.text.split():
        if j.lower() in ['msc','dphil','bachelor','pgdip']:
            tmp = j
            textmp = i.text.replace(tmp,'').strip()
        else:
            tmp = None
            textmp = i.text
    links['oxford'][textmp] = {'degree':[tmp],'url':f'https://www.ox.ac.uk'+str(i.find('a').get('href'))}

for i in hrefs:
    if i.text != '':  
        links['tum'][str(i.text[:i.text.index('-')]).strip()] = {'degree':[str(i.text[i.text.index('-')+1:].strip())],'url':f'https://www.tum.de'+i.get('data-url')}
with open('degrees.json','w') as f:
    dump(links,f)

if __name__ == '__main__':
    print()