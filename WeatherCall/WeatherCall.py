import requests
import json

API_Key = 'a6919dd2e20c5ca67bcf1c727a0b36bf'
params = dict(key=API_Key)

# Getting data for London in Celsius
urlLondon = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a6919dd2e20c5ca67bcf1c727a0b36bf'

response = requests.get(urlLondon, params=params)

print('The data for London  from URL is: \n' + response.text + '\n')
# I used the code below  as it is returning success for any code between 200 and 400

if response:
    print('Success!\n')
else:
    print('An error has occurred.\n')

print('The status code for the request is :  ' + str(response.status_code) + '\n')

# Verifies that the status code is 200

if response.status_code == 200:
    print('Success!\n')
else:
    print('An error has occurred.\n')

dictL = response.json()
print ('\nOur dictionary is the following: \n')
print(dictL)
print ('\nThe country in our dictionary is : \n')
print (dictL['sys']['country'])

# Getting data for London in Fahrenheit
urlLondonFahrenheit = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=imperial&APPID=a6919dd2e20c5ca67bcf1c727a0b36bf'
responseLondonF = requests.get(urlLondonFahrenheit, params=params)

print('\nThe data for London  from URL with Fahrenheit units is: \n' + responseLondonF.text + '\n')
dictLondonF = responseLondonF.json()
# Gets the temperature in Fahrenheit for London
print ('\nThe temperature in Fahrenheit in London is : \n')
print (dictLondonF['main']['temp'])

# Getting data for Tel-Aviv

urlTelAviv = 'http://api.openweathermap.org/data/2.5/weather?id=293397&APPID=a6919dd2e20c5ca67bcf1c727a0b36bf'

responseTelAviv = requests.get(urlTelAviv, params=params)

print('\nThe data for Tel-Aviv  from URL is: \n' + responseTelAviv.text + '\n')

dictTelAviv = responseTelAviv.json()
# Gets the temperature in Celsius for Tel-Aviv
print ('\nThe temperature in Celsius in Tel-Aviv is : \n')
print (dictTelAviv['main']['temp'])

# Verifies that the country is IL in the case of Tel-Aviv
if dictTelAviv['sys']['country'] == 'IL':
    print('\nThe country for Tel-Aviv is IL. Correct!')
else:
    print ('The country is not IL for Tel-Aviv. Incorrect!')

# Gets the temperature in Fahrenheit for New York

urlNY = 'http://api.openweathermap.org/data/2.5/weather?id=5128638&units=imperial&APPID=a6919dd2e20c5ca67bcf1c727a0b36bf'

responseNY = requests.get(urlNY, params=params)

print('\nThe data for NY  from URL is: \n' + responseNY.text + '\n')

dictNY = responseNY.json()
# Gets the temperature in Fahrenheit for Tel-Aviv
print ('\nThe temperature in Fahrenheit in NY is : \n')
print (dictNY['main']['temp'])
