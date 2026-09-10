import os
import time
from colorama import init, Fore, Back, Style
import random


quotes = [
      '''Give yourself time. Ideas'll come. Life'll shake you, roll you, maybe embrace you. The music'll find you.
      - Johnny Silverhand''',

      '''Wake the fuck up, Samurai! We have a city to burn.
      - Johnny Silverhand''',

      '''Guess I meant, I dunno... a happier ending... for everyone involved.
      - V (Male Player)
      
      Here, for folks like us? Wrong city, wrong people.
      - Johnny Silverhand''',

      '''The time has come for a close encounter of the third kind... A small step for V, but a giant leap for humankind. Who're you bettin' on showin' up? The reptilians or techno-necromancers?
      - Johnny Silverhand
      
      The Spanish Inquisition.
      - V (Male Player)
      
      I admit, I didn't expect that.
      - Johnny Silverhand''',

      '''You look like a cut of fuckable meat. Are you?
      - Adam Smasher''',

      '''Just promise me one thing, asshole. You won't forget me.
      - V (Male Player)''',

      '''Goodbye, V, and never stop fighting.
      - Johnny Silverhand''',

      '''You've never backed down from anything in your life, even when you maybe should've. You go through Night City knowing a stray bullet could end you while hailing a cab. But that's never stopped you from taking action, going where you needed to go. And it won't stop you now.
      - Skye
      
      But how do I keep up with everything that's changing?
      - V (Male Player)
      
      You have been keeping up. You've made an impact. Not a single thing in this world isn't in the process of becoming something else. Likewise you. Never look back. If you gotta kill, kill. If you gotta burn it all to the ground, then let it burn.
      - Skye''',

      '''[What is free often proves most costly]''',

      '''Haven't forgotten a thing. Never will.
      - Johnny Silverhand''',

      '''You're a dick, you know?
      - V (Male Player)
      
      And you're a cunt. Maybe we'll fit together after all.
      - Johnny Silverhand''',

      '''So, Padre. You think Jackie's looking down upon us... from up there?
      - V (Male Player)
      
      I believe he has met God, stood before Him.
      - Sebastian "Padre" Ibarra
      
      That's it?
      - V (Male Player)
      
      I don't know if God left the meeting happy, but I'm pretty certain Jackie did.
      - Sebastian "Padre" Ibarra''',

      '''He's fucked in the head, the world's fucked in the head, and YOU'RE fucked in the head because MY fucked up head is inside it. Guess if you wanna save the world, that's the first step; get fucked in the head.
      - Johnny Silverhand''',

      '''Sabotage a corpo power station, jump a corpo transport, kidnap a corpo suit...
      - Johnny Silverhand
      
      This a plug for the word corpo or do you have a point?
      - V (Male Player)
      
      Know what? You're starting to remind me of me, fifty years back. Minus the charisma... and impressive cock.
      - Johnny Silverhand''',

      '''G'night, Valarie. Today was a good day.
      - Johnny Silverhand''',

      '''Don't like it, Don't listen.
      - V (Female Player)
      
      Oh, yeah, real mature! Not like I can cover my ears and go 'lalalalala' whenever you open your trap.
      - Johnny Silverhand''',

      '''[as Panam falls asleep] On behalf of the staff of Independent California Motel, I wish you sweet dreams.
      - Johnny Silverhand''',

      '''Test of a person's true value? Death. Facing it, staring it down. You still got a chance to be somebody.
      - Johnny Silverhand''',

      '''I have found that people lie, most often deceiving themselves. Not so the dead... The dead are so very, very loud. And yet, lying is not in their nature. It is so... humbling - to listen to the dead speak.
      - Saburo Arasaka''',

      '''Swap meat for chrome, live a BD fantasy, whatever, but at the end of it all, it's the code you live by that defines who you are.
      - Johnny Silverhand''',

      '''Now, as that old Greek dawg says, life's a banquet - so don't go thirsty, but don't get drunk, either.
      - Dexter 'Dex' DeShawn''',

      '''G'night, Vincent. Today was a good day.
      - Johnny Silverhand''',

      '''Johnny, remember the plan?
      - Rogue Amendiares
      
      Get the payload on the elevator, arm it, let gravity do its thing. Explosion rocks the foundation, tower crumbles - chaos, screaming, roll credits.
      - Johnny Silverhand''',

      '''Would you rather live in peace as Mr. Nobody, die ripe, old and smelling slightly of urine? Or go down for all times in a blaze of glory, smelling near like posies, without seeing your thirtieth?
      - Dexter 'Dex' DeShawn''',

      '''Yorinobu and his puppets grin at the cameras and insist that everything is under control... but the wider the smile, the bigger the lies.
      - Goro Takemura''',

      '''I ca-- I can't belive it. Everything. All we did - it was pointless.
      - V (Male Player)''',

      '''Doesn't it bother you?
      - V (Male Player)
      
      What?
      - Ozob
      
      The grenade. You know, the one on your face?
      - V (Male Player)
      
      Eh, you get used to it. I just gotta be careful not to pull the pin when I wanna pick my nose.
      - Ozob''',

      '''"The greatest crimes issue from a desire for excess and not from necessity."
      - T-Bug
      
      Say what now?
      - Jackie Welles
      
      Aristotle. Guess you read me, then?
      - T-Bug
      
      Yeah, I read you. Not so much your Greek friend, though it was kind of exciting.
      - Jackie Welles''',

      '''Did you think I wouldn't know it was taken from me?
      - Saburo Arasaka
      
      Actually, I don't think of you at all. Ever. You see, that's your problem. You think the world revolves around you. Arrogant.
      - Yorinobu Arasaka
      
      Yorinobu...
      - Saburo Arasaka
      
      Why did you come? To humiliate me? To personally see to it that your son knows his place?
      - Yorinobu Arasaka
      
      "The nail that protrudes from the wall gets hammered..."
      - Saburo Arasaka
      
      Couldn't think of anything original to say?
      - Yorinobu Arasaka
      
      And do you think it "original" to sell our greatest achievement to Westerners - our future to these... barbarians?
      - Saburo Arasaka
      
      Our future? Ours? You are mistaken. You've only ever cared about yourself... and your sick schemes!
      - Yorinobu Arasaka
      
      I knew this day would come. That sooner or later, your impudence would cross the line. There is much for which I could forgive you, but for treason? No. I'm just glad your mother didn't live to see this. The heart should break but once.
      - Saburo Arasaka
      
      You shall never have to forgive me for anything again!
      - Yorinobu Arasaka''',

      '''Experiencing migraines, nausea, hypersensitivity to bright lights?
      - Viktor Vektor'''
  ]





# for x in list(quote):
#     print(Fore.MAGENTA + f"\033[3m{x}\033[0m", end='')
#     time.sleep(0.7)