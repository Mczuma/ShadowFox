cities ={
    "Australia": ["Sydney","Melbourne","Brisbane","Perth"],
    "UAE": ["Dubai","Abu Dhabi","Sharjah","Ajman"],
    "India": ["Mumbai","Bangalore","Chennai","Delhi"]
}
city1= input("Enter the first city:")
city2= input("Enter the second city:")
country1 = None
country2 = None
for c, city_list in cities.items():
    if city1 in city_list:
        country1=c
    if city2 in city_list:
        country2=c
if country1 and country2 and country1==country2:
    print("Both cities are in", country1)
else:print("They don't belong to the same country")