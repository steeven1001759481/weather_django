import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=5c06753ea6edff1007c1c28521e97764'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            # Check if the city already exists in the database
            if not City.objects.filter(name=city_name).exists():
                form.save()
    form = CityForm()

    cities = City.objects.all()
    city_weather = []
    for city in cities:
        # city = request.POST.get('city_name')
        r = requests.get(url.format(city)).json()
        if r['cod'] != '400' and r['cod'] != '404':
            weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
            }
            city_weather.append(weather)
    context = {'weather': city_weather, 'form':form}

    return render(request, 'weather\index.html', context)


# from django.shortcuts import render
# import requests
# from .models import City
# from .forms import CityForm

# def index(request):
#     cities = City.objects.all() #return all the cities in the database

#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

#     if request.method == 'POST': # only true if form is submitted
#         form = CityForm(request.POST) # add actual request data to form for processing
#         form.save() # will validate and save if validate

#     form = CityForm()

#     weather_data = []

#     for city in cities:

#         city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
#         if city_weather['cod'] != '400':
#             weather = {
#                 'city' : city,
#                 'temperature' : city_weather['main']['temp'],
#                 'description' : city_weather['weather'][0]['description'],
#                 'icon' : city_weather['weather'][0]['icon']
#             }

#             weather_data.append(weather) #add the data for the current city into our list
        
#         context = {'weather_data' : weather_data, 'form' : form}

#     return render(request, 'weather/index.html', context) #returns the index.html template