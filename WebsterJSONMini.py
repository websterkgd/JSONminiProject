# -*- coding: utf-8 -*-

# Webster JSON Mini Project

#Tasks

#Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
#1.	Find the 10 countries with most projects
#2.	Find the top 10 major project themes (using column 'mjtheme_namecode')
#3.	In 2. above you will notice that some entries have only the code and the 
#3. name is missing. Create a dataframe with the missing names filled in.

#clear environment
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

#import packages for data analysis 
import pandas as pd
import json
import os 

#change directory to directory with data
os.chdir('D:\\a_Desktops_Git\\Current\\SpringBoard\\JSONMiniProject\\data_wrangling_json\\data\\')

#import the data
with open('world_bank_projects.json') as file:
    WB = json.load(file)

#transform the data to a dataframe
countries = pd.DataFrame(WB, columns=['countryname'])

#count the entries
cc = countries.countryname.value_counts()

#Find the 10 countries with the most projects
t10_cc = cc.head(10)
print(t10_cc)

#rename index 
t10_ni =[]
for c in t10_cc.index:
    t10_ni.append(c.split()[-1])
    
t10_cc.index = t10_ni

#create a barplot of the data
import matplotlib.pyplot as plt
import numpy as np 

t10_cc.plot(kind='bar')
plt.xticks(rotation=60) 
plt.ylabel('Number of Projects')
plt.ylim(0,20)
plt.yticks(np.arange(0, 22, step=2))
plt.title('World Bank Projects by Country')
plt.show()

## Find the 10 major project themes
countries['themes'] = pd.DataFrame(WB, columns=['mjtheme_namecode'])

#count the themes
tc = countries.themes.value_counts()

#find the top 10
t10_tc = tc.head(10)
print(t10_tc)

# count individual themes
pt = []
for l in countries['themes']:
    for d in l:
        pt.append(d)

pt = pd.Series(pt)
pt = pt.value_counts()
pt_t10 = pt.head(10)

#rename index for top themes
ptt10_ni =[]
for c in pt_t10.index:
    ptt10_ni.append('Code ' + str(c['code']))
       
pt_t10.index = ptt10_ni

#plotting the top 10
pt_t10.plot(kind='bar')
plt.xticks(rotation=60) 
plt.ylabel('Theme Occurrence')
plt.ylim(0,250)
plt.yticks(np.arange(0, 250, step=20))
plt.title('Top 10 World Bank Project Theme')
plt.show()

## Fill in the missing names
tbf1 = countries['themes']

#a more elegant solution # works on d but doesn't update l
#creates a list of all themes
e = []
for l in tbf1:
    for d in l:
        e.append(d)

#eliminates duplicate themes
e = [i for n, i in enumerate(e) if i not in e[n + 1:]]

#eliminates the theme if the name is null
r =[]
for i in e: 
    if i['name'] == '': 
        r.append(i)

for i in r:
    if i in e:
        e.remove(i)

#sorts the resulting list 
e = sorted(e, key = lambda i: (int(i['code'])))

#counts the themes
ptu = []
for l in tbf1:
    for d in l:
        if d not in e:
            d = e[int(d['code'])-1]
        assert d['name'] != ''
        ptu.append(d)

#count the updated themes
tcu = pd.Series(ptu).value_counts()

#find the top 10
t10_tcu = tcu.head(10)
print(t10_tcu)

#plot the top 10
#rename index for top themes
ptt10u_ni =[]
for c in t10_tcu.index:
    ptt10u_ni.append('Code ' + str(c['code']))
       
t10_tcu.index = ptt10u_ni

#plotting the top 10
t10_tcu.plot(kind='bar')
plt.xticks(rotation=60) 
plt.ylabel('Theme Occurrence')
plt.ylim(0,250)
plt.yticks(np.arange(0, 260, step=20))
plt.title('Updated Top 10 World Bank Project Theme')
plt.show()

#brute force approach
for l in tbf1.head(20):
    for d in l:
        if d['code'] == '1':
            d['name'] = 'Economic management'
        elif d['code'] == '2':
            d['name'] = 'Public sector governance'
        elif d['code'] == '3':
            d['name'] = 'Rule of law'
        elif d['code'] == '4':
            d['name'] = 'Financial and private sector development'
        elif d['code'] == '5':
            d['name'] = 'Trade and integration'
        elif d['code'] == '6':
            d['name'] = 'Social protection and risk management'
        elif d['code'] == '7':
            d['name'] = 'Social dev/gender/inclusion'
        elif d['code'] == '8':
            d['name'] = 'Human development'
        elif d['code'] == '9':
            d['name'] = 'Urban development'
        elif d['code'] == '10':
            d['name'] = 'Rural development'
        elif d['code'] == '11':
            d['name'] = 'Environment and natural resources'
        print(d)
        print(l)
        assert d['name'] != ''
 
#count the updated themes
tcu = tbf1.value_counts()
 
#find the top 10
t10_tcu = tcu.head(10)
print(t10_tcu)





