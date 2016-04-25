ages = {'alice':42, 'bob':35, 'charles':35}

#how old is Alice?
print("Alice is", ages['alice'])

#who is 35?
persons35 = []
for person in ages:
    if ages[person] == 35:
        persons35.append(person)

print(persons35, "are 35")



favorites_dict = person['favorites']
fav_nums = favorites_dict['numbers']
fav_nums[0]