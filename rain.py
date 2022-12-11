import requests
import smtplib

API_key = # open weather map api key
lat = # latitude of the place
lon = # longitude of the place
parameter = {
    'lat': lat,
    'lon': lon,
    'exclude': 'current,daily,minutely',
    'appid': API_key
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameter)

data = response.json()

hourly_data = data['hourly'][:12]
will_rain = False

for hour in hourly_data:

    condition_code = hour['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
    print(f'{hour}:{will_rain}')

if will_rain:
    email = '' # sender's email
    password = '' # senders's password (16 digit from 2 factor auth after mid 2022)
    to_address = '' # reciver's email id
    
    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
    connection.starttls()
    connection.login(user=email, password=password)

    connection.sendmail(from_addr=email, to_addrs='',
                        msg=f'subject:It is going to rain\n\nBring umbrella')

    connection.close()
    print(f"Mail has been sent to successfully")
