from distutils.log import info
from sre_parse import State
from turtle import home


students = ["hailey", "Alfred", "Joseph", "Lana"]
# print(students[1])
# print(students[-1])

foods = "hot chettos", "burger", "sushi", "steak"
# for food in foods:
  # print(f"{food} is a good foods")

# for food in foods[-2:]:
  # print(food)

# home_town = {
  
#   'City': "Oak Park",
#   "State": "Michigan",
#   "Population": 100,
# }

# print(type(home_town))

# print(f"I was born in {home_town['City']}, {home_town['State']} - population of {home_town['Population']}")

# for key, info in home_town.items():
#   print(key, info)

cohort = []
for index, student in enumerate(students):
    cohort.append({'student': student,
      'fav_food': foods[index]
    })
# for student in cohort:
  # print(student)

awesome_Students =  [f"{name} is awesome!!" for name in students]
print(awesome_Students)

for food in [food for food in foods if 'a' in food]:
  print(food)