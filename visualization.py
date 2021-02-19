import pycountry
import pandas as pd
import plotly.express as px


dataframe_confirm = pd.read_csv(
    'time_series_covid19_confirmed_global.csv')             # reads the csv file
# removes columns titled 'Province/State', 'Lat', and 'Long'
dataframe_confirm = dataframe_confirm.drop(
    columns=['Province/State', 'Lat', 'Long'])
dataframe_confirm = dataframe_confirm.groupby(
    'Country/Region').agg('sum')              # groups by 'Country/Region'
date_list = list(dataframe_confirm.columns)


# finds the ISO 3166-1 defined 3 letter country code
def find_iso_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None


dataframe_confirm['country'] = dataframe_confirm.index
dataframe_confirm['iso_alpha_3'] = dataframe_confirm['country'].apply(
    find_iso_country_code)

# puts the dataset into a long format
dataframe_long = pd.melt(dataframe_confirm, id_vars=[
    'country', 'iso_alpha_3'], value_vars=date_list)

# creating the map animation
map_animation = px.choropleth(dataframe_long,
                              locations="iso_alpha_3",
                              color="value",
                              hover_name="country",
                              animation_frame="variable",
                              projection="natural earth",
                              color_continuous_scale='Reds',
                              range_color=[0, 500000]
                              )
map_animation.show()
# write the result to HTML file
map_animation.write_html("example_map.html")
