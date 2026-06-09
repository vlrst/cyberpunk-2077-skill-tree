
import os
import sys
import numpy
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 


# start with the parent first, then go left to right when creating children











allSkills = [Body_Levels, Cool_Levels]


print(_.name for _ in allSkills)


skills_description = []
for levels in allSkills:
    for level in levels:
        print(level)
        for skill in level:
            print("\t", skill.name)
            skills_description.append(skill.description)


#print(allSkills)

# for x in range(len(allSkills)):

#   print(f"{x+1}: {allSkills[0][x].name}")


        
# START OF WHAT YOU ARE LOOKING FOR




# print(f"\n\n\nALL DESCS IN skills_description")
# i=0
# for desc in skills_description:
#   i+=1
#   print(f"{i}: {desc}")
# print(type(skills_description))

# END OF WHAT YOU ARE LOOKING FOR

# sub_index = {1: "Body", 2: "Cool", 3: "Intelligence", 4: "Reflexes", 5:"Technical Ability"}
# subSkills = [[x] for x in range(5)]
# CCOUNTER = 0

# for skill in skills_description:
#   subSkills[CCOUNTER].append(skill)
#   CCOUNTER += 1 
# # skills_description.split('\n')

# # print(skills_description)

# print(subSkills)