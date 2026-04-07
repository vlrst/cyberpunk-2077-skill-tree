
import os
import sys
import numpy
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 
from VARS import * 
from ollama import chat as MODEL
from ollama import ChatResponse

# start with the parent first, then go left to right when creating children
PAINKILLER = Skill("PAINKILLER", Body, "Unlocks slow health regen in combat.", None, None)
DORPH_HEAD = Skill("DORPH-HEAD", Body, "When using Blood Pump Cyberware or a Health Item: +100% mitigation chance for 2 sec.", PAINKILLER, None)
COMEBACK_KID = Skill("COMEBACK KID", Body, "+60% Health Regen Rate while sprinting", PAINKILLER, None)
SPEED_JUNKIE = Skill("SPEED JUNKIE", Body, "+60% Health Regen rate while sprinting.", PAINKILLER, None)
ARMY_OF_ONE = Skill("ARMY OF ONE", Body, "+10% Health Regen Rate for each nearby enemy", PAINKILLER, None)
PAINKILLER.child = [DORPH_HEAD, COMEBACK_KID, SPEED_JUNKIE, ARMY_OF_ONE]



DIE_DIE_DIE = Skill("DIE! DIE! DIE!", Body, "Level 1: +12.5% Crit Chance at low Stamina. Level 2: Increased fire rate as Stamina decreases (max. +25% at 0 Stamina). Bonus to weapon handling as Stamina decreases.", None, None)
LIKE_A_FEATHER = Skill("LIKE A FEATHER", Body, "No movement speed penalty with Shotguns, Light Machine Guns, and Heavy Machine Guns.", DIE_DIE_DIE, None)
DONT_STOP_ME_NOW = Skill("DON'T STOP ME NOW", Body, "When below 33% Stamina: +15% Mitigation Chance +5% Mitigation Strength", DIE_DIE_DIE, None)
BULLET_BALLET = Skill("BULLET BALLET", Body, "-25% bullet spread when moving.", DIE_DIE_DIE, None)
DIE_DIE_DIE.child = [LIKE_A_FEATHER, DONT_STOP_ME_NOW, BULLET_BALLET]


allSkills = [
  LIKE_A_FEATHER, DIE_DIE_DIE, DONT_STOP_ME_NOW, BULLET_BALLET, 
  DORPH_HEAD, COMEBACK_KID, PAINKILLER, SPEED_JUNKIE, ARMY_OF_ONE                                          
]

allSkillNames = []
for skill in allSkills:
  allSkillNames.append(skill.name)


# pretty sure this line of code will soon be rendered useless
Body_Levels = [
    [LIKE_A_FEATHER, DIE_DIE_DIE, DONT_STOP_ME_NOW, BULLET_BALLET], 
    [DORPH_HEAD, COMEBACK_KID, PAINKILLER, SPEED_JUNKIE, ARMY_OF_ONE],

]

skills_description = []

for level in Body_Levels:
    for skill in level:
      skills_description.append(skill.description)

print(f"\n\n\nALL DESCS IN skills_description")
i=0
for desc in skills_description:
  i+=1
  print(f"{i}: {desc}")
print(type(skills_description))



# sub_index = {1: "Body", 2: "Cool", 3: "Intelligence", 4: "Reflexes", 5:"Technical Ability"}
# subSkills = [[x] for x in range(5)]
# CCOUNTER = 0

# for skill in skills_description:
#   subSkills[CCOUNTER].append(skill)
#   CCOUNTER += 1 
# # skills_description.split('\n')

# # print(skills_description)

# print(subSkills)