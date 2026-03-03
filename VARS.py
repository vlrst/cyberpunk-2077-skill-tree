perk_points = int(input("How many perk points do you have? "))
attribute_points = int(input("How many attribute points do you have? "))
build_type = input("What build type do you want (Technical Ability [TA], Reflexes, Body, Cool, Intelligence)? ")

prompt = f"I am making a build type for Cyberpunk 2077. This is the build type that I want: {build_type}. I have {perk_points} and {attribute_points}. Make my build. NOTE: THIS IS ONLY SKILLS IN THE SKILL TREE. DO NOT USE ANY IMPLANTS OR GUNS OR ANYTHING ELSE THAT HAS NOTHING TO DO WITH THE SKILL IN THE SKILL TREE. Give it to me in a list under subsections: For example [BODY]: Painkiller, Comeback Kid, Speed Junkie. Do that for every section that is required to fulfill the build. The text should include THIS ONLY. NO OTHER THING SUCH AS ADVICE OR ANYTHING ELSE OTHER THAN THE SKILLS AND SUBSECTIONS NEEDED. DO NOT ADD AN INTRO SAYING 'Okay, here’s a (body type)-focused build for Cyberpunk 2077, based solely on the skill tree, broken down by category:' or anything in that nature"


