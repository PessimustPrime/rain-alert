import requests
import smtplib

API_key = '03ff24b4b33bfc05092e79f411160734'
lat = 12.971599# 23.1815
lon = 77.594566 # 79.9864
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


if will_rain:
    email = 'trialt872@gmail.com'
    password = 'xktvdtdqtnayztsj'

    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
    connection.starttls()
    connection.login(user=email, password=password)

    connection.sendmail(from_addr=email, to_addrs='troublewood18@gmail.com',
                        msg=f'subject:It is going to rain\n\nBring umbrella')

    connection.close()
    print(f"Mail has been sent to successfully \nRain!!!!")

else:
    email = 'trialt872@gmail.com'
    password = 'xktvdtdqtnayztsj'

    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
    connection.starttls()
    connection.login(user=email, password=password)

    connection.sendmail(from_addr=email, to_addrs='troublewood18@gmail.com',
                        msg=f'subject:It is NOT going to rain\n\nHave a beautiful Day!')

    connection.close()
    print(f"Mail has been sent to successfully")
