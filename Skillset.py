
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











# ROW 1
PAINKILLER = Skill("PAINKILLER", Body, "Unlocks slow health regen in combat.", None, None)
DORPH_HEAD = Skill("DORPH-HEAD", Body, "When using Blood Pump Cyberware or a Health Item: +100% mitigation chance for 2 sec.", PAINKILLER, None)
COMEBACK_KID = Skill("COMEBACK KID", Body, "+60% Health Regen Rate while sprinting", PAINKILLER, None)
SPEED_JUNKIE = Skill("SPEED JUNKIE", Body, "+60% Health Regen rate while sprinting.", PAINKILLER, None)
ARMY_OF_ONE = Skill("ARMY OF ONE", Body, "+10% Health Regen Rate for each nearby enemy", PAINKILLER, None)
PAINKILLER.child = [DORPH_HEAD, COMEBACK_KID, SPEED_JUNKIE, ARMY_OF_ONE]

FURY_ROAD = Skill("FURY ROAD", Body, "In vehicle collisions: +50% damage to enemy vehicles and their occupants in collisions caused by you. -50% damage to your vehicles in collisions caused by enemies. You take no damage as an occupant in vehicle collisions.", None, None)






# ROW 2
DIE_DIE_DIE = Skill("DIE! DIE! DIE!", Body, "Level 1: +12.5% Crit Chance at low Stamina. Level 2: Increased fire rate as Stamina decreases (max. +25% at 0 Stamina). Bonus to weapon handling as Stamina decreases.", None, None)
LIKE_A_FEATHER = Skill("LIKE A FEATHER", Body, "No movement speed penalty with Shotguns, Light Machine Guns, and Heavy Machine Guns.", DIE_DIE_DIE, None)
DONT_STOP_ME_NOW = Skill("DON'T STOP ME NOW", Body, "When below 33% Stamina: +15% Mitigation Chance +5% Mitigation Strength", DIE_DIE_DIE, None)
BULLET_BALLET = Skill("BULLET BALLET", Body, "-25% bullet spread when moving.", DIE_DIE_DIE, None)
DIE_DIE_DIE.child = [LIKE_A_FEATHER, DONT_STOP_ME_NOW, BULLET_BALLET]




WRECKING_BALL = Skill("WRECKING BALL", Body, "Only affects blunt weapons. Level 1: -15% Stamina Cost for attacks with Blunt Weapons. Level 2: Allows you to barrel into enemies while sprinting and blocking with Blunt Weapons, causing damage and a chance to knock them down.", None, None)
KINETIC_ABSORPTION = Skill("KINETIC ABSORPTION", Body, "Only affects blunt weapons. Blocking an attack gives: +10% Stamina +30% Damage with Blunt Weapons for 5 sec.", WRECKING_BALL, None)
BREAKTHROUGH = Skill("BREAKTHROUGH", Body, "Only affects blunt weapons. -40% enemy Armor for 7 sec. after hitting them with a Strong Attack.", WRECKING_BALL, None)
CLAPBACK = Skill("CLAPBACK", Body, "Only affects blunt weapons. +100% Knockdown chance with Defensive attacks. Cooldown: 10 sec. +100% Stun Chance with Counterattacks.", WRECKING_BALL, None)
FLY_SWATTER = Skill("FLY SWATTER", Body, "Only affects blunt weapons. -40% incoming ranged damage when blocking with Blunt Weapons", WRECKING_BALL, None)
WRECKING_BALL.child = [KINETIC_ABSORPTION, BREAKTHROUGH, CLAPBACK, FLY_SWATTER]



# ROW 3












SPONTANEOUS_OBLITERATION = Skill("SPONTANEOUS OBLITERATION", Body, "Only affects Shotguns, LMGs, and HMGs. Level 1: -15% recoil at low Stamina Level2: +10% Damage against nearby enemies Level 3: Unlocks Obliterate - the ability to sometimes instantly kill and dismember enemies at low health The chance increases as enemy health decreases (max. 20% Obliterate chance).", None, None)
SKULLCRACKER = Skill("SKULLCRACKER", Body, "Only affects Shotguns, LMGs, and HMGs. Increases damage of Quick Melee attacks as Stamina decreases (max. 200% at 0 Stamina).", SPONTANEOUS_OBLITERATION, None)
CLOSE_QUARTERS_CARNAGE = Skill("CLOSE-QUARTERS CARNAGE", Body, "Only affects Shotguns, LMGs, and HMGs. +20% reload speed for 8 sec. after dismembering an enemy.", SPONTANEOUS_OBLITERATION, None)
DREAD = Skill("DREAD", Body, "Only affects Shotguns, LMGs, and HMGs. -15% enemy armor when using ranged attacks. Dismemberment spreads the effect to nearby enemies.", SPONTANEOUS_OBLITERATION, None)
RUSH_OF_BLOOD = Skill("RUSH OF BLOOD", Body, "Only affects Shotguns, LMGs, and HMGs. Increased chance to Obliterate enemies with ranged attacks at close range (max. 10%).", SPONTANEOUS_OBLITERATION, None)
SPONTANEOUS_OBLITERATION.child = [SKULLCRACKER, CLOSE_QUARTERS_CARNAGE, DREAD, RUSH_OF_BLOOD]



ADRENALINE_RUSH = Skill("ADRENALINE RUSH", Body, "Level 1: +35 Max Health Level 2: +20% Health Regen Bonus to all Health Regen effects from all sources. Level 3: Unlocks Adrenaline Rush mode. In addition to their base effects, Blood Pump cyberware and Health Items now also give Adrenaline equal to 30% Max Health (up to a max of 50% Max Health) Adrenaline is indicated by a yellow bar and acts like extra Health by absorbing damage it also decays over time. Adrenaline Rush will remain active as long as you have Adrenaline available.", None, None)
UNSTOPPABLE_FORCE = Skill("UNSTOPPABLE FORCE", Body, "When Adrenaline Rush is active: Gain immunity to movement penalties and non-damaging status effects such as Knockdown, Blinding, etc", ADRENALINE_RUSH, None)
JUGGERNAUT = Skill("JUGGERNAUT", Body, "When Adrenaline Rush is active: +20% Movement Speed +10% Damage", ADRENALINE_RUSH, None)
CALM_MIND = Skill("CALM MIND", Body, "When Adrenaline Rush is active: +3 sec. delay before Adrenaline begins to decay.", ADRENALINE_RUSH, None)
ADRENALINE_RUSH.child =[UNSTOPPABLE_FORCE, JUGGERNAUT, CALM_MIND]

BLOODLUST = Skill("BLOODLUST", Body, "Only affects Shotguns, LMGs, and HMGs. When Adrenaline Rush is active: +50 Adrenaline on dismemberment of a nearby enemy.", [RUSH_OF_BLOOD, JUGGERNAUT])



QUAKE = Skill("QUAKE", Body, "Only affects Blunt Weapons. Level 1: -15% Stamina Cost for attacks with Blunt Weapons. Level 2: +20% attack speed with Blunt Weapons. Level 3: Press Q to violently slam the ground, damaging and staggering nearby enemies with a chance of Knocdown. Quake can also be performed from middair (a Superhero Landing) Cooldown: 10 sec.", None, None)
AFTERSHOCK = Skill("AFTERSHOCK", Body, "Only affects Blunt Weapons. +30 Stamina for each enemy hit with Quake.", QUAKE, None)
EPICENTER = Skill("EPICENTER", Body, "Only affects Blunt Weapons. When Quake is performed from midair (a Superhero Landing), its area effect and damage scale with your fall speed and fall distance.", QUAKE, None)
QUAKE.child = [AFTERSHOCK, EPICENTER]







# THE TOP SKILLS

RIP_AND_TEAR = Skill("RIP AND TEAR", Body, "Only affects Shotguns. +100% damage for the next Quick Melee Attack after shooting an enemy with a Shotgun +100 damage for the next Shotgun shot after hitting an enemy with a Quick Melee Attack.", SPONTANEOUS_OBLITERATION, None)
ONSLAUGHT = Skill("ONSLAUGHT", Body, "Only affects LMGs. +20% ammo refill after neutralizing an enemy with a Light Machine Gun.", SPONTANEOUS_OBLITERATION, None)
PAIN_TO_GAIN = Skill("PAIN TO GAIN", Body, "When Adrenaline Rush is active: +20% Health Item recharge after neutralizing an enemy.", ADRENALINE_RUSH, None)
FINISHER_SAVAGE_SLING = Skill("FINISHER: SAVAGE SLING", Body, "Only affects Blunt Weapons. Unlocks a Blunt Weapon Finisher. Press F when an enemy's Health is low. Enemies affected by Stun are more susceptible. Restores 20% Health Hold F to Throw the enemy instead, killing them and damaging other enemies while they land.", QUAKE, None)





# DOUBLE PARENT SKILLS

BLOODLUST = Skill("BLOODLUST", Body, "Only affects Shotguns, LMGs, and HMGs. When Adrenaline Rush is active: +50 Adrenaline on dismemberment of a nearby enemy.", [RUSH_OF_BLOOD, JUGGERNAUT])
RIPPLE_EFFECT = Skill("RIPPLE EFFECT", Body, "Only affects Blunt Weapons. +15% Health for each enemy hit by Quake", [CALM_MIND, AFTERSHOCK], None)






# THIS SECTION WILL CONNECT THE PARENTS WITH OTHER PARENTS


PAINKILLER.child.append(ADRENALINE_RUSH) 
ADRENALINE_RUSH.parent = PAINKILLER # adding the parents later for organization and management

DIE_DIE_DIE.child.append(SPONTANEOUS_OBLITERATION)
SPONTANEOUS_OBLITERATION.parent = DIE_DIE_DIE


WRECKING_BALL.child.append(QUAKE)
QUAKE.parent = WRECKING_BALL




# this is how the row ordering works
# [
#    row 3
#    row 2
#    row 1
# ]
allSkills = [
    RIP_AND_TEAR, ONSLAUGHT, PAIN_TO_GAIN, FINISHER_SAVAGE_SLING,
    SPONTANEOUS_OBLITERATION, SKULLCRACKER, CLOSE_QUARTERS_CARNAGE, DREAD, RUSH_OF_BLOOD, BLOODLUST, ADRENALINE_RUSH, UNSTOPPABLE_FORCE, JUGGERNAUT, CALM_MIND, RIPPLE_EFFECT, QUAKE, AFTERSHOCK, EPICENTER, # row 3
    DIE_DIE_DIE, LIKE_A_FEATHER, DONT_STOP_ME_NOW, BULLET_BALLET, WRECKING_BALL, BREAKTHROUGH, KINETIC_ABSORPTION, CLAPBACK, FLY_SWATTER, # row 2 
    PAINKILLER, DORPH_HEAD, COMEBACK_KID, SPEED_JUNKIE, ARMY_OF_ONE, FURY_ROAD # row 1
]



allSkillNames = []
for skill in allSkills:
  allSkillNames.append(skill.name)


# pretty sure this line of code will soon be rendered useless
# IN EACH SUBLIST, KEEP THE PARENT AS THE FIRST ELEMENT 
#   THEN GO LEFT -> RIGHT
Body_Levels = [
    [RIP_AND_TEAR], [ONSLAUGHT], [PAIN_TO_GAIN], [FINISHER_SAVAGE_SLING],
    [SPONTANEOUS_OBLITERATION, SKULLCRACKER, CLOSE_QUARTERS_CARNAGE, DREAD, RUSH_OF_BLOOD], [BLOODLUST], [ADRENALINE_RUSH, UNSTOPPABLE_FORCE, JUGGERNAUT, CALM_MIND], [RIPPLE_EFFECT], [QUAKE, AFTERSHOCK, EPICENTER], # row 3
    [DIE_DIE_DIE, LIKE_A_FEATHER, DONT_STOP_ME_NOW, BULLET_BALLET], [WRECKING_BALL, BREAKTHROUGH, KINETIC_ABSORPTION, CLAPBACK, FLY_SWATTER], # row 2 
    [PAINKILLER, DORPH_HEAD, COMEBACK_KID, SPEED_JUNKIE, ARMY_OF_ONE], [FURY_ROAD] # row 1
]

skills_description = []

for level in Body_Levels:
    for skill in level:
      skills_description.append(skill.description)







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