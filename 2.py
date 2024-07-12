justice_league =["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print("number of members in the Justice League:", len(justice_league) )
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:",justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder woman")
print("After moving Wonder Woman to the beginning:",justice_league)
justice_league.remove("Superman")
justice_league.insert(justice_league.index("Aquaman")+1, "Green Lantern")
print("After separating Aquaman and Flash with Green Lantern:",justice_league)
justice_league=["Cyborg", "Shazam", "Hawkgirl", "Martin Manhunter", "Green Arrow"]
print("New justice League team:",justice_league)
justice_league.sort()
new_leader=justice_league[0]
print("Justice_League after sorting alphabetically with{}as the  new leader:".format(new_leader),justice_League)
