import os
import sys
import numpy
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 

print("\n\n")

Body.details()
Cool.details()
Intelligence.details()
Reflexes.details()
Technical_Ability.details()


# start with the parent first, then go left to right when creating children
PAINKILLER = Skill("PAINKILLER", Body, "Unlocks slow health regen in combat.", None, ["Comeback_Kid", "Dorph_Head", "Speed_Junkie", "Army_Of_One"])
DORPH_HEAD = Skill("DORPH-HEAD", Body, "When using Blood Pump Cyberware or a Health Item: +100% mitigation chance for 2 sec.", PAINKILLER, None)
COMEBACK_KID = Skill("COMEBACK KID", Body, "+60% Health Regen Rate while sprinting", PAINKILLER, None)
SPEED_JUNKIE = Skill("SPEED JUNKIE", Body, "+60% Health Regen rate while sprinting.", PAINKILLER, None)
ARMY_OF_ONE = Skill("ARMY OF ONE", Body, "+10% Health Regen Rate for each nearby enemy", PAINKILLER, None)





# first index is the lowest sublevel. looks can be deceiving
Body_Levels = [
    [DORPH_HEAD, COMEBACK_KID, PAINKILLER, SPEED_JUNKIE, ARMY_OF_ONE],
    [],
    [],
    [],
    []
]


for level in Body_Levels[0]:
    for line in level.details():
        print(line)