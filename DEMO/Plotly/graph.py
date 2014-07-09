#!/usr/bin/python 

import datetime
import plotly.plotly as py
import time
import math
from plotly.graph_objs import *

username = 'bartgarcia'
api_key = 'j4x55jeevs'
token = '2ie41l5593'
 
print " Obtaining User Id \n"
py.sign_in(username, api_key)
print " Stream is now open \n"

py.plot({
    'data' : [{
        'x': [],
        'y': [],
        'name': 'SIN',
        'type': 'scatter',
        'stream': {
            'token': token,
            'maxpoints': 200
        }
    }],
    'layout' : Layout(
        title='Test Graph',
        xaxis=XAxis(
            title='Time',
            titlefont=Font(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
                )
            ),
        yaxis=YAxis(
            title='Preasure in mBar',
            titlefont=Font(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
                )
        )
    )},
    filename='Pressure Sensor Data',
    fileopt='overwrite'
    )

stream = py.Stream(token)
stream.open()
while True:
  
    for x in range(0,20):
      time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
      stream.write({'x': time_now, 'y': math.sin((x*math.pi)/10)})
      print " Printing values : \n", time_now , "and  ", math.sin((x*math.pi)/10)
      time.sleep(0.5)
