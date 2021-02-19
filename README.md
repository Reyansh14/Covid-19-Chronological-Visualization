# Covid-19-Chronological-Visualization
This is a Covid-19 Chronological Visualization made in Python using the Pandas and Plotly libraries. The program creates a Choropleth map of the world, ranging in color white to dark-red based on countries having 0 cases to 500,000+ respectively. 

The data is sourced from John Hopkins University using their CSSE COVID-19 dataset on Github. I used Pandas to load their "time_series_covid19_confirmed_global.csv" file to dataframe and to format it. Then, I used Plotly Express in order to map the data and create a visualization by the date in order to track the progression of the virus.

To Do: 
* Let the program automatically update the dataset every day 
* Add more visualizations for the total recovered cases and total deaths by country
* Create a heatmap of the virus' spread


