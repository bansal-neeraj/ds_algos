# calling openweather API via requests library and

import requests

API_KEY = '52206525fee24adc70353b9693c65c1f'


# url = 'http://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=52206525fee24adc70353b9693c65c1f'
#
# r = requests.get(url)
#
# my_dict = r.json()
# print(my_dict['coord'])
# print(my_dict['weather'])
# print(my_dict['name'])


payload = {
    # 'q': 'london',
    'q': 'mumbai',
    'appid': API_KEY,
    'units':'metric'
}


url2 = 'http://api.openweathermap.org/data/2.5/weather'
r2 = requests.get(url2,params=payload)
print(r2.url)

print(r2.json())
my_dict = r2.json()
print(my_dict['coord'])
print(my_dict['weather'])
print(my_dict['name'])
print(my_dict['main']['temp'])

# unsplash api ---------
print('-'*50)
unsplash_api_key = 'e0MgmMq8Y1UeqzZ13T5YqDabaLaiwbBSjia3YryFJ1A'
unsplash_url = 'https://api.unsplash.com/search/photos'
unsplash_payload = {
    'query': 'mumbai',
    'client_id': unsplash_api_key,
    'per_page':1
}

r3 = requests.get(unsplash_url,params=unsplash_payload)
print(r3.json())

