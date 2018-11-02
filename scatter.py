import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
df = pd.read_csv('data/winequality-red.csv', sep=';')
dfgood = df[df.quality>=6]
dfpoor = df[df.quality<6]

trace0=go.Scatter(
        x=dfgood.alcohol,
        y=dfgood.pH,
        mode='markers',
	name='Good Quality Wine'
)

trace1=go.Scatter(
        x=dfpoor.alcohol,
        y=dfpoor.pH,
        mode='markers',
	name='Poor Quality Wine'
)
"""
trace2=go.Scatter(
        x=dfgood.pH,
        y=dfgood.pH,
        mode='markers',
        name='Good pH'
)
trace3=go.Scatter(
        x=dfpoor.pH,
        y=dfpoor.pH,
        mode='markers',
        name='Poor pH'
)
"""
data = [trace0,trace1]
layout = dict(title = 'Alcohol VS pH Scatter Graph',
              xaxis = dict(title = 'alcohol'),
              yaxis = dict(title = 'pH'),
              )
fig=dict(data=data,layout=layout)

py.plot(fig,filename='scatter-quality',sharing='public')


