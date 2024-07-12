cities={
    "Australia": ["Sydney","Melbourne","Brisbane","Perth"],
    "UAE": ["Dubai","Abu Dhabi","Sharjah","Ajman"],
    "India": ["Mumbai","Bangalore","Chennai","Delhi"]
}
city=input("Enter a city name:")

country=None
for c, city_list in cities.items():
    if city in city_list:
        country=c
        break
if country:
    print(f"{city} is in {country}")
else:
    print("City not found in the list")
if country1 and country2 and country1==country2:
    print("Both cities are in",country1)
else:
    print("They don't belong to the same country")