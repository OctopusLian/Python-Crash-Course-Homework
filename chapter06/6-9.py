favorite_places = {
    'znn': ['chengdu', 'shanghai', 'hangzhou'],
    'yl': ['chengdu', 'huang montains'],
    'other': ['xian', 'xinjiang', 'nanji']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())