# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import datetime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, assets_external_path = external_stylesheets)

app.scripts.config.serve_locally = True


############################################################## crops plot



coffee_all_year = pd.read_csv("https://raw.githubusercontent.com/R-Akira/Crop-Productivity-Dashboard/master/Assets/coffee_all_years.csv")
maize_all_year  = pd.read_csv("https://raw.githubusercontent.com/R-Akira/Crop-Productivity-Dashboard/master/Assets/maize_all_years.csv")
lemon_all_year  = pd.read_csv("https://raw.githubusercontent.com/R-Akira/Crop-Productivity-Dashboard/master/Assets/lemon_all_years.csv")


crops_fig = make_subplots(rows=1, cols=3, subplot_titles=("Coffee", "Maize", "Lemon"))


crops_fig.add_trace(
    go.Scatter(x=coffee_all_year['Year'], y= coffee_all_year['Value'], marker_color = 'green'),
    row=1, col=1
)

crops_fig.add_trace(
    go.Scatter(x=maize_all_year['Year'], y=maize_all_year['Value'], marker_color = 'green'),
    row=1, col=2
)


crops_fig.add_trace(
    go.Scatter(x=lemon_all_year['Year'], y=lemon_all_year['Value'], marker_color = 'green'),
    row=1, col=3
)

crops_fig.update_layout(
    title_text="Crop Productivity by Year (hg/ha)", 
    title_x = 0.5,
    plot_bgcolor='white',
    paper_bgcolor = 'white',
    showlegend = False,
    )
crops_fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
crops_fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

############################################################## rain plot


rain    = pd.read_csv("https://raw.githubusercontent.com/R-Akira/Crop-Productivity-Dashboard/master/Assets/complete_rain.csv")



rain_fig = go.Figure(data=[
                      go.Bar(x=rain.date, y=rain.precipitation, marker_color='gray', name = 'Value'),
                      go.Scatter(x=rain.date, y=rain.MA_2, name = 'Moving Average',line=dict(color='green', width=1))],
                      layout= {
                          'paper_bgcolor' : 'rgba(0,0,0,0)', 
                          'plot_bgcolor' : 'rgba(0,0,0,0)'
                          })


rain_fig.update_layout(
    title_text="Rain Activity", 
    title_x = 0.5, 
    xaxis_tickformat = '%Y',
    #xaxis_range =[datetime.datetime(1920, 10, 17), datetime.datetime(2013, 11, 20)]
    )


rain_fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
rain_fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

############################################################## sunspot plot


sunspot = pd.read_csv("https://raw.githubusercontent.com/R-Akira/Crop-Productivity-Dashboard/master/Assets/complete_sunspot.csv")

sunspot_fig = go.Figure(data=[
                      go.Bar(x=sunspot.Date, y=sunspot.Monthly_Mean_Total_Sunspot_Number, marker_color='gray', name = 'Value'),
                      go.Scatter(x=sunspot.Date, y=sunspot.ma_2, name = 'Moving Average',line=dict(color='green', width=1))],
                      layout= {
                          'paper_bgcolor' : 'rgba(0,0,0,0)', 
                          'plot_bgcolor' : 'rgba(0,0,0,0)'
                          })


sunspot_fig.update_layout(
    title_text="Sunspot Activity", 
    title_x = 0.5, 
    xaxis_tickformat = '%Y',
    #xaxis_range =[datetime.datetime(1920, 10, 17), datetime.datetime(2013, 11, 20)]
    )

sunspot_fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
sunspot_fig.update_yaxes(showline=True, linewidth=2, linecolor='black')



############################################################## markdown

profile = '''

Authors: [Newton Greco](https://www.linkedin.com/in/newtongreco/) & [Reyner Akira](https://www.linkedin.com/in/reyner-akira/)

'''


summary = '''

***
### Summary


In order to create a model to predict productivity from rain and sun activity it was necessary to select a specific region with a known rain pattern. The reason for that is that rain is variable that has particular cycle according to each region. The sunspot otherwise has the same pattern at its origin and even though it will impact each region differently the variation for all of them will follow the same cycles. The third dataset is the productivity dataset for the selected crops and from the region matching the rain data.
In our case we have selected Brazil as our focus region and coffee, lemon and maize as our crops.

![alt text][id]

[id]: https://github.com/R-Akira/Crop-Productivity-Dashboard/blob/master/Assets/globe.png?raw=True "Title"



'''

analysis_one = '''

***

### Crop Productivity 

We can see all three crops are showing productivity growth over time. In order to deploy the regression we have selected the period from 1998 until 2017 to train our model and kept 2018 separate in order to test the model and evaluate its accuracy. The reason for this specific period is the available rain data that comprehends from 1998 until 2018 only.
Another important characteristic is that coffee and lemon are permanent crops, while maize is a temporary, what could possibly impact these models.

'''

analysis_two = '''

***

### Rain and Sunspot Activity Analysis

As we can see underneath both sunspots and rain have very clear cycles what allows us to work with seasonal factors. An alternative method would be to use dummy variables, but we chose the first method for simplicity and because it provides more actionable insights.

'''


analysis_three = '''

***

### Seasonal Factors

Looking at the seasonal factors for each crop, we can see that coffee has a very clear differentiation in terms of rain seasonality, while lemon and maize only display minimal variation for the two year cycle.
Regarding sunspots cycle we can see that all three crops are significantly impacted by it, with coffee oscillating up to 25%, lemon up to 10% and maize up to 36%


![alt text][id]

[id]: https://github.com/R-Akira/Crop-Productivity-Dashboard/blob/master/Assets/Seasonal_Factors.jpg?raw=True "Title"

'''


analysis_four = '''

***

### Productivity Model

Since the objective of the models is to make predictions we have selected for each crop the one with the lowest RMSE, in order to be as close as possible to the actual productivity.


![alt text][id]

[id]: https://github.com/R-Akira/Crop-Productivity-Dashboard/blob/master/Assets/Productivity_Models.jpg?raw=True "Title"


'''

analysis_five = '''

***

### Model Evaluation

In order to evaluate the accuracy of these models we have saved the data from year 2018 and compared with the predicted forecast for 2018.
In the table underneath we can see that the coffee model produced the most accurate prediction with na error of 2.3%. Lemon and Maize both produced less accurate predictions with erros around 10%.

![alt text][id]

[id]: https://github.com/R-Akira/Crop-Productivity-Dashboard/blob/master/Assets/Model_Evaluation.jpg?raw=True "Title"

'''

appendix = '''

Source:    
http://www.fao.org/faostat/en/#data/QC      
https://www.kaggle.com/fabiopotsch/precipitation-in-brazil      
https://www.kaggle.com/robervalt/sunspots    

'''

##############################################################

app.layout = html.Div(children=[
    html.H1(children='Crop Productivity Model', style = {
        'textAlign' : 'left',
        'marginLeft' : 20
    }),

    html.H4(children=
    'Analyzing Sun Activity and Rain Cycles to Predict Crop Productivity ', style = {
        'textAlign' : 'left',
        'marginLeft' : 20
    }),

    dcc.Markdown(children= profile
    , style = {
        'textAlign' : 'left',
        'marginLeft' : 20
    }),

    dcc.Markdown(children=summary, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
        #'backgroundColor':'#000000',
        #'border': 'thin lightgrey',
        #'color': 'white',
        #'font-family':'Sans Forgetica Regular'
    }),

    dcc.Markdown(children=analysis_one, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),

    dcc.Graph(
        id='graph1',
        figure= crops_fig
    ),

    dcc.Markdown(children=analysis_two, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),

    dcc.Graph(
        id='graph2',
        figure= rain_fig
    ),


    dcc.Graph(
        id='graph3',
        figure= sunspot_fig
    ),

    dcc.Markdown(children=analysis_three, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),


    dcc.Markdown(children=analysis_four, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),


    dcc.Markdown(children=analysis_five, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),

    dcc.Markdown(children=appendix, style = {
        'textAlign' : 'left'
    })

], style= 
{
    'backgroundColor':'#FFFFFF',
    'color': 'black',
    'font-family':'Candara'

}

)


if __name__ == '__main__':
    app.run_server()
