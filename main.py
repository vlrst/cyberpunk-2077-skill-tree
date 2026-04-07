import os
import sys
import io 
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
import datetime

output_buffer = io.StringIO()
sys.stdout = output_buffer


prompt = f'''
These are the descriptions of various skills that I can buy (EACH DESCRIPTION IS ONLY ONE SKILL): {skills_description} 
The type of build that I want in this video gaome is {build_type}. 
Make my build. 
GIVE ME ONLY {perk_points} SKILLS MAXIMUM. 
NOTE: THIS IS ONLY SKILLS IN THE SKILL TREE:  {Body_Levels}
DO NOT USE ANY IMPLANTS OR GUNS OR ANYTHING ELSE THAT HAS NOTHING TO DO WITH THE SKILL IN THE SKILL TREE.
Give it to me in a list under the following subsections as needed: [Body, Cool, Intelligence, Reflexes, Technical Ability]. 
For example [BODY]: Painkiller, Comeback Kid, Speed Junkie. 
Make sure that even if you do not have anything for the specific subsection, you write 'None' Do that for every section that is required to fulfill the build. 
The text should include THIS ONLY. NO OTHER THING SUCH AS ADVICE OR ANYTHING ELSE OTHER THAN THE SKILLS AND SUBSECTIONS NEEDED. 
DO NOT ADD AN INTRO SAYING 'Okay, here’s a (body type)-focused build for Cyberpunk 2077, based solely on the skill tree, broken down by category:' or anything in that nature.'''


prompt = f"""
These are the descriptions of various skills that I can buy (EACH DESCRIPTION IS ONLY ONE SKILL):
{skills_description}

The type of build that I want in this video game is:
{build_type}

Use ONLY skills from this skill tree:
{Body_Levels}

You can choose a maximum of {perk_points} skills.

Rules:
- ONLY use skills from the skill tree.
- DO NOT include implants, guns, cyberware, equipment, or anything else outside the skill tree.
- Do NOT add explanations, introductions, or advice.
- Output ONLY the sections listed below.
- Even if a section has no skills, write "None".

The output should only contain the skill's names that ONLY are included from this list:
{allSkillNames}
Output format (exactly like this):


[Body]: (skill1), (skill2), (skill3) 
[Cool]: (skill1), (skill2) 
[Intelligence]: (skill1), (skill2) 
[Reflexes]: (skill1), (skill2) 
[Technical Ability]: (skill1), (skill2) 

Do not output anything else besides these sections and the skills.

"""
print("start body levels")
print(Body_Levels)
print("end body levels")

stream = MODEL(
    model='gemma3',
     messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

model_response = ""
for chunk in stream:
  model_response += (str(chunk['message']['content']))
  #print(chunk['message']['content'], end='', flush=True)


sub_index = {1: "Body", 2: "Cool", 3: "Intelligence", 4: "Reflexes", 5:"Technical Ability"}
subSkills = [str("DELETE_THIS") for x in range(perk_points+10)]

counter = 0

model_response = model_response.split("\n")
for line in model_response:
  subSkills[counter] = line
  counter += 1 


print(f"\n--------------------\nSUBSKILLS:")
counter =0
subSkillUnecessary = ""
for line in subSkills:

  if line != "DELETE_THIS":
    print(f"{line}")
    for skill in allSkills:
      # if skill.description == line:
      #print(f"'{skill.name}: [INDEX OF {counter}]'")
      pass
    counter += 1
    for char in line:
      if char != "]":
        subSkillUnecessary += char
      
  else:
    subSkills.remove(line)
  
  #print(subSkillUnecessary)

  #print(line)
  

#print(type(list(model_response)))





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


captured_text = output_buffer.getvalue()


try:
   with open(f"{datetime.datetime.now()}", "x") as f:    
    f.write(captured_text)
except Exception as e:
  pass

print(f"Time of run: {datetime.datetime.now()}")

sys.stdout