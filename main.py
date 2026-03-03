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

stream = MODEL(
    model='gemma3',
     messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

model_response = ""

for chunk in stream:
  model_response += (str(chunk['message']['content']))
  #print(chunk['message']['content'], end='', flush=True)


#print(type(list(model_response)))

model_response = model_response.split(" ")
count = 0
indexes = [str(x) for x in range(1, 20)]
for word in model_response:
  
  if word[0] == "[":
    for letter in word:
        if letter == "]":
           break
        else:
           indexes[count-1] += letter
    count += 1
  print(word)

print(indexes)






print("\n\n")



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

# Body.details()
# Cool.details()
# Intelligence.details()
# Reflexes.details()
# Technical_Ability.details()



# for level in Body_Levels[0]:
#     for line in level.details():
#         print(line)