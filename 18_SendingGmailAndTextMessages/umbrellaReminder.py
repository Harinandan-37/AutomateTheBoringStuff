import bs4, requests
import datetime, time
from twilio.rest import Client

while True:
    morning = datetime.datetime.now()
    print(morning)
    time.sleep(1)
    if (morning.hour, morning.minute) == (6, 30):
        break

accountSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+19854016625'
myCellPhone = '+917299497118'

url = 'https://forecast.weather.gov/MapClick.php?lat=42.93708397900008&lon=-75.61070144699994'

res = requests.get(url)
res.raise_for_status()

weather_soup = bs4.BeautifulSoup(res.text,'html.parser')
match = weather_soup.find('p', class_='short-desc')

weather_description = match.text.strip().lower()

if 'rain' in weather_description:
    message = twilioCli.messages.create(body='There is a chance of Rain today. Bring an umbrella!!',from_=myTwilioNumber, to=myCellPhone)

    print("Rain Alert!!")
else:
    message = twilioCli.messages.create(body='No need to bring umbrella!',from_=myTwilioNumber, to=myCellPhone)
    print("No need for umbrella today")