import requests
from bs4 import BeautifulSoup
import pandas as pd

#page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.969670000000065&lon=-118.249935#.YnarU-hBxPY')
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.Yna14OhBxPY')
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.findAll('a'))
week = soup.find(id='seven-day-forecast-body')
items = week.findAll(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_descriptions)
print(temperatures)

weather_stuff = pd.DataFrame({
    'period':period_names,
    'short-description':short_descriptions,
    'temperature':temperatures
})

print(weather_stuff)
# Delete earlier file have same name otherwise use unique name of file to avoid error.
weather_stuff.to_csv('weather.csv')

