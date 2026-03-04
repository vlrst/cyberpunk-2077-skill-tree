import os
import sys
import numpy
from Skillset import * 
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 
from VARS import * 
from ollama import chat as MODEL
from ollama import ChatResponse


# first index is the lowest sublevel. looks can be deceiving



# Body.details()
# Cool.details()
# Intelligence.details()
# Reflexes.details()
# Technical_Ability.details()

# skills_description = [] 


# # for level in Body_Levels[0]:
    
# #     for line in level.description():
# #         skills_description.append(line.description)
  
# for level in Body_Levels[0]:
#   skills_description.append(level.description)
# print(skills_description)



prompt = f"These are the descriptions of various skills that I can buy (EACH DESCRIPTION IS ONLY ONE SKILL): {skills_description} The type of build that I want in this video gaome is {build_type}. Make my build. GIVE ME ONLY THREE SKILLS MAXIMUM. NOTE: THIS IS ONLY SKILLS IN THE SKILL TREE. DO NOT USE ANY IMPLANTS OR GUNS OR ANYTHING ELSE THAT HAS NOTHING TO DO WITH THE SKILL IN THE SKILL TREE. Give it to me in a list under the following subsections as needed: [Body, Cool, Intelligence, Reflexes, Technical Ability]. For example [BODY]: Painkiller, Comeback Kid, Speed Junkie. Make sure that even if you do not have anything for the specific subsection, you write 'None' Do that for every section that is required to fulfill the build. The text should include THIS ONLY. NO OTHER THING SUCH AS ADVICE OR ANYTHING ELSE OTHER THAN THE SKILLS AND SUBSECTIONS NEEDED. DO NOT ADD AN INTRO SAYING 'Okay, here’s a (body type)-focused build for Cyberpunk 2077, based solely on the skill tree, broken down by category:' or anything in that nature."

stream = MODEL(
    model='gemma3',
     messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

model_response = ""

for chunk in stream:
  model_response += (str(chunk['message']['content']))
  print(chunk['message']['content'], end='', flush=True)

#print(type(model_response))

sub_index = {1: "Body", 2: "Cool", 3: "Intelligence", 4: "Reflexes", 5:"Technical Ability"}
subSkills = [str("DELETE_THIS") for x in range(10)]
#print(subSkills)
counter = 0

model_response = model_response.split("\n")
for line in model_response:
  subSkills[counter] = line
  counter += 1 
# skills_description.split('\n')

# print(skills_description)

print(f"\n--------------------\nSUBSKILLS:")
counter =0
subSkillUnecessary = ""
for line in subSkills:

  if line != "DELETE_THIS":
    print(f"'{line}: [INDEX OF {counter}]'")
    counter += 1
    for char in line:
      if char != "]":
        subSkillUnecessary += char
      
  else:
    subSkills.remove(line)
  
  print(subSkillUnecessary)
  
  #print(line)
  

#print(type(list(model_response)))


count = 0
indexes = [str(x) for x in range(1, 20)]
# for word in model_response:

#   if word[0] == "[":
#     for letter in word:
#         if letter == "]":
#            count = 0
#            break
#         else:
#            indexes[count-1] += letter
#         count += 1
#     print(word)
        
    

#print(indexes)






print("\n\n")
