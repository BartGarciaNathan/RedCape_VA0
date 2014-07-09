#!/usr/bin/python 

import datetime
import plotly.plotly as py
import time
import math
from plotly.graph_objs import *

username = 'bartgarcia'
api_key = 'j4x55jeevs'
tokens = ['2ie41l5593', 'token2'] 
 
 
print " Obtaining User Id \n"
py.sign_in(username, api_key)
streams = [py.Stream(token) for token in tokens]
for stream in streams:
  stream.open()
print " Stream is now open \n"
py.plot([
    {'x': [],
    'y': [],
    'name': 'SIN',
    'type': 'scatter',
    'stream': {
        'token': tokens[0],
        'maxpoints': 200
        }
    }],
  layout = Layout(
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
  ),
    filename='Pressure Sensor Data',
    fileopt='overwrite')


while True:
  
    for x in range(0,20):
      time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
      streams[0].write({'x': time_now, 'y': math.sin((x*math.pi)/10)})
      print " Printing values : \n", time_now , "and  ", math.sin((x*math.pi)/10)
      time.sleep(0.05)