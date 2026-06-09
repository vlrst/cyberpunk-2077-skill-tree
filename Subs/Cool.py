import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Skill import Skill
from Sub import Sub

Cool = Sub("Cool", 3)


# ROW 1

ROAD_WARRIOR = Skill("ROAD WARRIOR", Cool, "Allows you to use Sandevistan to slow time while driving. Allows Kerenzikov to be activated when aiming and handbraking simultaneously. +25% weapon damage when your vehicle is drifting or airborne.")

FELINE_FOOTWORK = Skill("FELINE FOOTWORK", Cool, "When crouched: +15% Movement Speed +15% Mitigation Chance Mitigation - grants a chance to reduce incoming damage by current Mitigation Strength (Default: 50%)", [None], [None])
BLIND_SPOT = Skill("BLIND SPOT", Cool, "When crouched, the higher your Mitigation Chance, the longer it takes for enemies to detect you.", [FELINE_FOOTWORK], [None])
SMALL_TARGET = Skill("SMALL TARGET", Cool, "+20% Mitigation Chance when crouched and not moving", [FELINE_FOOTWORK], [None])
UNEXPOSED = Skill("UNEXPOSED", Cool, "+20% Mitigation Chance when aiming from cover", [FELINE_FOOTWORK], [None])

FELINE_FOOTWORK.child = [BLIND_SPOT, SMALL_TARGET, UNEXPOSED]

KILLER_INSTINCT = Skill("KILLER INSTINCT", Cool, "+25% damage with knives, axes, and silenced guns outside of combat. They also provide a preview of estimated damage.", [None], [None])
QUICK_GETAWAY = Skill("QUICK GETAWAY", Cool, "+10% movement speed after neutralizing an enemy while undetected. Duration: 30 sec, or until you are detected. Stacks 2 times. New stacks reset duration. All stacks are removed when duration ends", [KILLER_INSTINCT], [None])
GAG_ORDER = Skill("GAG ORDER", Cool, "Landing an attack on an enemy right after they detect you will delay detection from other nearby enemies", [KILLER_INSTINCT], [None])

KILLER_INSTINCT.child = [QUICK_GETAWAY, GAG_ORDER]

# ROW 2

FOCUS = Skill("FOCUS", Cool, "Level 1: +10% headshot and weakspot damage. Level 2: Unlocks Focus mode. This mode automatically activates when you aim while at full Stamina. When active: No Stamina cost for shooting, allowing for more accurate shots. When it ends: -40 Stamina Duration: 2.5 sec.", [None], [None])
NO_SWEAT = Skill("NO SWEAT", Cool, "-50% Stamina Cost from Focus for each enemy neutralized while it was active", [FOCUS], [None])
RINSE_AND_RELOAD = Skill("RINSE AND RELOAD", Cool, "+10% Reload Speed for your next reload after neutralizing an enemy while aiming. Stacks 2 times. The stack resets to whenever you start aiming", [FOCUS], [None])
PULL = Skill("PULL!", Cool, "When Focus is active, shooting grenades out of the air is easier and their effects are more powerful", [FOCUS], [None])
HEAD_TO_HEAD = Skill("HEAD TO HEAD", Cool, "When Focus is active, neutralizing an enemy with a ranged attack resets its duration", [FOCUS], [None])

DEEP_BREATH = Skill("DEEP BREATH", Cool, "Time slows by 25% for you and enemies when Focus is active", [HEAD_TO_HEAD], [None]) # son to HEAD_TO_HEAD


FOCUS.child = [NO_SWEAT, RINSE_AND_RELOAD, PULL, HEAD_TO_HEAD]

SCORPION_STING = Skill("SCORPION STING", Cool, "Level 1: -15% Recovery Time for throwable Weapons. Level 2: Crit hits, headshots and hits to weakspots with throwable weapons apply Poison for 5 sec.", [None], [None])
PARASITE = Skill("PARASITE", Cool, "+15% Health on Crit Hits and Headshots with thrown weapons", [SCORPION_STING], [None])
NEUROTOXIN = Skill("NEUROTOXIN", Cool, "Applying Poison to an enemy via Scorpion Sting now also applies Blinding and disables sprinting for 6 sec.", [SCORPION_STING], [None])
ACCELERATED_TOXIN_ABSORPTION = Skill("ACCELERATED TOXIN ABSORPTION", Cool, "Strong attacks and thrown weapons used against Poisoned enemies instantly deal any remaining Poison damage and remove the effect.", [SCORPION_STING], [None])
CORROSION = Skill("CORROSION", Cool, "Allows you to apply Poison to mechs, robots, drones and turrets", [SCORPION_STING], [None])
SCORPION_STING.child = [PARASITE, NEUROTOXIN, ACCELERATED_TOXIN_ABSORPTION, CORROSION]

# ROW 3

DEADEYE = Skill("DEADEYE", Cool, "Level 1: +10% Headshot and weakspot damage. Level 2: -25% Stamina cost for shooting. Level 3: Unlocks Deadeye mode, which is active above 85% Stamina. When active: +20% Headshot Damage +20% Weakspot Damage No bullet spread", [None], [None])
CALIFORNIA_REAPER = Skill("CALIFORNIA REAPER", Cool, "+30% Stamina after neutralizing an enemy with a ranged attack via headshot or weakspot", [DEADEYE], [None])
HIGH_NOON = Skill("HIGH NOON", Cool, "When Deadeye is active: +35% reload speed for your next reload after neutralizing an enemy via headshot or weakspot. Effect available for 3 sec. Slows time by 50% during reload", [DEADEYE], [None])
LONG_SHOT = Skill("LONG SHOT", Cool, "When Deadeye is active, your shots always deal full damage regardless of distance.", [DEADEYE], [None])
QUICK_DRAW = Skill("QUICK DRAW", Cool, "+30% Weapon swap speed when swapping to Pistols, Revolvers, Sniper Rifles and Precision Rifles. +30% Stamina when swapping during combat.", [DEADEYE], [None])
DEADEYE.child = [CALIFORNIA_REAPER, HIGH_NOON, LONG_SHOT, QUICK_DRAW]

NINJUTSU = Skill("NINJUTSU", Cool, "Level 1: +15% Crouch movement Speed. Level 2: +15% Mitigation chance when crouched. Level 3: Unlocks the ability to sprint while crouched. Press Left Shift while crouching. Crouch-sprinting allows you to move more quickly while staying silent, but it consumes Stamina", [None], [None])
SHINOBI_SPRINT = Skill("SHINOBI SPRINT", Cool, "-75% Stamina Cost for crouch-sprinting during combat", [NINJUTSU], [None])
CREEPING_DEATH = Skill("CREEPING DEATH", Cool, "When Optical Camo is active or you are undetected, neutralizing an enemy grants: +15% Health +15% Stamina +10% Movement Speed for 6 sec.", [NINJUTSU], [None]) 
SERPENTINE = Skill("SERPENTINE", Cool, "+30% Mitigation Chance when crouch-sprinting", [NINJUTSU], [None])

NINJUTSU.child = [SHINOBI_SPRINT, CREEPING_DEATH, SERPENTINE]

VANISHING_ACT = Skill("VANISHING ACT", Cool, "Optical Camo activates automtically when you crouch-sprint or slide. Automatic activation still consumes its charge", [None], [None]) # son of CREEPING_DEATH

JUGGLER = Skill("JUGGLER", Cool, "Level 1: -15% Recovery Time for throwable weapons. Level 2: +20% Headshot and weakspot damage with throwable weapons. Level 3: Instant Cooldown Reset for all throwable weapons after netrualizing an enemy with a throwable weapon via headshot, weakspot, or Poison", [None], [None])
SLEIGHT_OF_HAND = Skill("SLEIGHT OF HAND", Cool, "+20% Crit Damage for 8 sec, whenever Juggler is activated. Stacks 5 times. New stacks reset duration. All stacks are removed when duration ends.", [JUGGLER], [None])
FINISHER_ACT_OF_MERCY = Skill("FINISHER: ACT OF MERCY", Cool, "Unlocks a Throwable Weapon Finisher. Press F when an enemy's Health is low. Automatically activates Juggler. Restores 25% Health.", [JUGGLER], [None])
PAY_IT_FORWARD = Skill("PAY IT FORWARD", Cool, "After retrieving a thrown knife or axe from an enemy, your first melee attack with a throwable weapon gains +200% damage", [JUGGLER], [None])

POUNCE = Skill("POUNCE", Cool, "Allows you to perform Finishers from a greater distance if you've hit the enemy with a throwable weapon. Each succesful throw also makes them more susceptible to Finishers. To perform a Finisher, press F when an enemy's health is low.", [FINISHER_ACT_OF_MERCY], [None]) # son of FINISHER_ACT_OF_MERCY
FINISHER_ACT_OF_MERCY.child.append(POUNCE)


JUGGLER.child = [SLEIGHT_OF_HAND, FINISHER_ACT_OF_MERCY, PAY_IT_FORWARD]

# ROW 4




NERVES_OF_TUNGSEN_STEEL = Skill("NERVES OF TUNGSTEN-STEEL", Cool, "When Deadeye is active: Guaranteed Crit Hits for headshots and weaksposts. Increases damage as distance increases (max. +25%)", [DEADEYE], [None])
RUN_N_GUN = Skill("RUN 'N' GUN", Cool, "Hip-firing does not consume Stamina. When Focus is active: +25% Movement Speed.", [DEADEYE], [None])
STYLE_OVER_SUBSTANCE = Skill("STYLE OVER SUBSTANCE", Cool, "Guaranteed Crit Hits with Throwable weapons when crouch-sprinting, sliding, dodging or Dashing. No movement speed penalty when aiming a throwable weapon.", [NINJUTSU, JUGGLER], [None])

DEADEYE.child.append(NERVES_OF_TUNGSEN_STEEL)
DEADEYE.child.append(RUN_N_GUN)
NINJUTSU.child.append(STYLE_OVER_SUBSTANCE)
JUGGLER.child.append(STYLE_OVER_SUBSTANCE)

# PAINKILLER = Skill("PAINKILLER", Body, "Unlocks slow health regen in combat.", [None], None)

Cool_Levels = [
    [NERVES_OF_TUNGSEN_STEEL], [RUN_N_GUN], [STYLE_OVER_SUBSTANCE],
    [DEADEYE, CALIFORNIA_REAPER, HIGH_NOON, LONG_SHOT, QUICK_DRAW], [NINJUTSU, SHINOBI_SPRINT, CREEPING_DEATH, SERPENTINE, VANISHING_ACT], [JUGGLER, SLEIGHT_OF_HAND, FINISHER_ACT_OF_MERCY, PAY_IT_FORWARD, POUNCE],  # row 3
    [FOCUS, NO_SWEAT, RINSE_AND_RELOAD, PULL, HEAD_TO_HEAD, DEEP_BREATH], [SCORPION_STING, PARASITE, NEUROTOXIN, ACCELERATED_TOXIN_ABSORPTION, CORROSION], # row 2 
    [ROAD_WARRIOR], [FELINE_FOOTWORK, BLIND_SPOT, SMALL_TARGET, UNEXPOSED], [KILLER_INSTINCT, QUICK_GETAWAY, GAG_ORDER] # row 1
]