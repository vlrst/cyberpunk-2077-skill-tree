
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


PAINKILLER = Skill("PAINKILLER", Body, "Unlocks slow health regen in combat.", None, ["Comeback_Kid", "Dorph_Head", "Speed_Junkie", "Army_Of_One"])
DORPH_HEAD = Skill("DORPH-HEAD", Body, "When using Blood Pump Cyberware or a Health Item: +100% mitigation chance for 2 sec.", PAINKILLER, None)
COMEBACK_KID = Skill("COMEBACK KID", Body, "+60% Health Regen Rate while sprinting", PAINKILLER, None)
SPEED_JUNKIE = Skill("SPEED JUNKIE", Body, "+60% Health Regen rate while sprinting.", PAINKILLER, None)
ARMY_OF_ONE = Skill("ARMY OF ONE", Body, "+10% Health Regen Rate for each nearby enemy", PAINKILLER, None)




Body_Levels = [
    [DORPH_HEAD, COMEBACK_KID, PAINKILLER, SPEED_JUNKIE, ARMY_OF_ONE],
    [],
    [],
    [],
    []
]

skills_description = []

for level in Body_Levels[0]:
  skills_description.append(level.description)
print(skills_description)