import requests
import io
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Lat-Lon of New York
URL = "https://weather.com/weather/today/l/40.75,-73.98"
resp = requests.get(URL)
print(resp.status_code)
# print(resp.text)
soup = BeautifulSoup(resp.text, "lxml")
elements = soup.select(
    'span[data-testid="TemperatureValue"][class^="CurrentConditions"]')
print(f"Temp is {elements[0].text} Celcius")


# URL1 = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10YIE&cosd=2017-04-14&coed=2022-04-14"
# resp = requests.get(URL1)
# if resp.status_code == 200:
#     csvtext = resp.text
#     csvbuffer = io.StringIO(csvtext)
#     df = pd.read_csv(csvbuffer)
#     # print(df)


# URL2 = "https://api.github.com/users/jbrownlee"
# resp = requests.get(URL2)
# if resp.status_code == 200:
#     data = resp.json()
#     print(data)
