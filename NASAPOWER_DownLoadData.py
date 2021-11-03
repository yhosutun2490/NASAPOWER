#載入套件
import os
import json
import urllib
import requests
import webbrowser
import pprint
import pandas as pd
import numpy as np

##網路爬取NASA歷史資料
startDate=20000101
endDate=20210930
lat=-9.37473
lon=147.2364
url='https://power.larc.nasa.gov/api/temporal/daily/point?parameters=GWETTOP,GWETROOT,GWETPROF,QV2M,RH2M,PRECTOTCORR,T2M_RANGE,T2M_MAX,T2M_MIN&community=AG&longitude={}&latitude={}&start={}&end={}&format=json'.format(lon,lat,startDate,endDate)
r=requests.get(url)
  #if r.status_code==requests.codes.ok:
data=r.json()
#pprint.pprint(data)
  #Basic Lat,Lon
GPS=data['geometry']['coordinates']
lat=GPS[1]
lon=GPS[0]
  #Climate Data
Climate=data['properties']['parameter']
Rain=list(Climate['PRECTOTCORR'].values())
RH=list(Climate['RH2M'].values())
TMAX=list(Climate['T2M_MAX'].values())
TMIN=list(Climate['T2M_MIN'].values())
df_first=pd.DataFrame(Climate)
df_first['lat']=lat
df_first['lon']=lon
df_first['GDD_Rice']=(df_first.T2M_MAX+df_first.T2M_MIN)/2-10
df_first
df_first.to_csv('Laloki農場NASA氣候資料2000-202009',index=True)
