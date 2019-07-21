def city_country(city,country):
    return (city.title() + ',' + country.title())

city = city_country('shanghai', 'china')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)