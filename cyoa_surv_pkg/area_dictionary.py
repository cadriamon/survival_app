"""
This area_dictionary.py module contains dictionaries that acts as database to build new
area objects.

Attributes
----------
desc : dict
    desc dict attribute represents area description key pair text values

hp_change : dict
    hp_change dict attribute represents player hp adjustments in main.py
    based on string key pair int values

hunger_change : dict
    hunger_change dict attribute represents player hunger adjustments in
    main.py based on string key pair int values

thirst_change : dict
    thirst_change dict attribute represents player thirst adjustments in
    main.py based on string key pair int values

area1 : dict 
    area1 dict attribute represents player's first area option in main.py
    based on string key pair string values

area2 : dict 
    area2 dict attribute represents player's second area option in main.py
    based on string key pair string values

search_desc : dict
    search_desc dict attribute represents search description key pair 
    text values

search_hp_change : dict
    search_hp_change dict attribute represents player hp adjustments in main.py
    based on string key pair int values when player searches

search_hunger_change : dict
    search_hunger_change dict attribute represents player hunger adjustments in
    main.py based on string key pair int values when player searches

search_thirst_change : dict
    search_thirst_change dict attribute represents player thirst adjustments in
    main.py based on string key pair int values when player searches
"""

desc = {
    "HOME":
    "The place you've known all of your life. It looks rather cozy, if not for" +
    "\nthe deafening silence and emptiness. You see your garage and neighbor's" +
    "\nhouse as next opportune spots.",

    "GARAGE":
    "Its just your empty garage. You hear some noise coming from the nearby park" +
    "\nand your backyard. Will you go investigate?",

    "NEIGHBORS":
    "You look around and peek into your neighbors' house. You tap on one of their" +
    "\nglass windows once to see if their is any response. There is only silence." +
    "\nYou try this a couple of times until you are satisfied. The window opens" +
    "\nwithout issue and you slowly step inside. You remember that your neighbors'" +
    "\nhave a large shed in their yard, and behind that is a big field between you"
    "\nand the local high school.",

    "PARK": "You travel to the large field by your house to investigate the noise." +
    "\nThe sun beams down on you as you see the abandoned cars around you. Noone" +
    "\nis around. What is making that noise? As this thought passes you, a large" +
    "\nrumbling approaches and you see a helicopter above you pass by! Is this" +
    "\nyour ticket out of the city? According to your idea for direction, you" +
    "\nbelieve the helicopter is heading north, which is where the church and" +
    "\nhigh school is.",

    "BACKYARD": "The noise from the backyard interests you the most. You look" +
    "\naround in your yard to see if you could find the source of noise. You" +
    "\nnotice a person that seems to be walking around aimlessly while making" +
    "\ngroaning noises. Before you can call out to this person, you feel an" +
    "\nanimal like bite on your shoulder. Everything seems to black out after" +
    "\nthat.",

    "NEIGHBORS BACKYARD": "You promptly leave your neighbors' house after being the" +
    "\ntrespasser that you are. It's the zombie apocalypse, who cares? You see the" +
    "\nlarge shed that your neighbors' have in their backyard and recall that it was" +
    "\nmeant to store their personal boat. Could that be your ticket out of this city?" +
    "\nYou see the local church and shopping center from the large backyard.",

    "HIGH SCHOOL":
    "You cross the field without any issue and approach the local high school. There"
    "\nseems to be some movement around, but not too much. If you're careful you are" +
    "\nable to avoid most attention. The classrooms are empty and the parking lot is"
    "\nalso void. You recall that you can easily reach the courthouse and mall from" +
    "\nhere. You can hear what it seems to be a helicopter from both directions.",

    "SHOPPING CENTER":
    "The shopping center might be a good place to setup for the zombie apocalypse." +
    "\nYou assure yourself that all protaganists in any zombie movie survives by" +
    "\nsetting up base in a grocery store. You remember that this is not a movie." +
    "\nWith the amount of stores, searching here for food and water may be a good" +
    "\nidea, though there may be many zombies slowly creeping around. From the" +
    "\nshopping center, you can see a large parking garage and woods of the local" +
    "\nnational park.",

    "CHURCH":
    "You approach your local church and see that there is no sign of life anywhere" +
    "\nin what seems to be an unsettling calm from all the chaos. You silently regret" +
    "\nnot attending your local service more often after what has been going on, but" +
    "\nwho would have predicted that the dead would come back alive? Ironically, the" +
    "\nonly way forward is through the graveyard towards the inner-city or through" +
    "\nthe woods of your local national park. You look back and see that it would" +
    "\nimpossible go back due to the increase amounts of zombie movement.",

    "PARKING GARAGE":
    "You go inside the parking garage that is adjacent to the shopping center. You" +
    "\nrecall that this shopping center serves the local mall, an old motel, and the" +
    "\nshopping center so the size of the garage is very large. You look at the shopping" +
    "\ncenter and see another survivor walking through along with a large horde. There is" +
    "\nalmost no movement inside of the parking garage you are in.",

    "GRAVEYARD":
    "The graveyard? You have chosen to go to the graveyard during a zombie apocalypse." +
    "\nUnsurprisingly, you hear a horde quickly approach you from your blind spot. You see" +
    "\na hiding spot deeper inside the graveyard, or you can sprint for the courthouse.",

    "DEEP GRAVEYARD":
    "Behind a couple of monuments deeper in the graveyard, you decide to hide from the horde" +
    "\nand hold your breath to prevent making any excessive noise. Luckily, the majority of the" +
    "\nhorde passes by you. You let out a sigh of relief. Little did you know, that some stragglers" +
    "\nof the horde identifies your location. They quickly surround you and tire you out as you" +
    "\ntry to escape. The rest is history.",

    "MALL":
    "You recall that there was a movie about a mall and zombie apocalypse. Also, you recall" +
    "\nthat there may be a video game you played when you were younger as well. Those memories" +
    "\ndo not bring good feelings. There seems to be some movement from the department stores," +
    "\nbut the rest of the mall seems void. Out in the distance, you see that the mall overlooks" +
    "\na lake and is also placed right across from the local community college.",

    "MOTEL":
    "This is just another rundown motel. There is no way you can stay here for long as you see" +
    "\nsome zombies are in the motel parking lot. The motel is close to the local community college." +
    "\nOtherwise, you can try the closeby woods of the local national park.",

    "COURTHOUSE":
    "Thankfully, you make it to the courthouse without much issue. Anything that was following" +
    "\nseemed to have given up and are miles away. You observe the vastness and architecture of" +
    "\nthe courthouse. Its halls are great and spacious; spacious for potential hordes of zombies." +
    "\nThe courthouse is close to the local police station and the local community college.",

    "COLLEGE":
    "The local community college seems to be empty. It may be a good idea to look around here for" +
    "\nsupplies as there are many trade workshops and labs around. You might find a weapon or material" +
    "\nto set up a permanent base if you can't leave the city. Behind the community college are some" +
    "\nmountains notorious for difficult hard to climb but attract rock-climbing enthusiasts. Not too far" +
    "\nfrom the community college is the local gym that a lot of the college students go to.",

    "WOODS":
    "\nYou look around as you walk through the woods of your local national park. The sun is still up, but" +
    "\nmay be going down sometime soon. Your footsteps are light, but you can hear the crunching of the" +
    "\ndead leaves that make up most of the forest floor. You are pretty hard to spot here, but the dead" +
    "\ntrees cannot cover you forever. In the distance, you see an extremely vast mansion on top of a" +
    "\nsmall hill and in the other direciton you see a familiar location but are not sure if you want" +
    "\nto go back.",

    "POLICE STATION":
    "The police station is exactly what would be imagined. Many police cars are parked haphazardly" +
    "\neverywhere with open doors. Some police cars have crashed into the local infrastructure. You see" +
    "\nsome zombies that are handcuffed along the railing leading into the police station. Ironically," +
    "\nthe local drinking bars are not too far from here and there is a construction area in front of" +
    "\nlocal hospital. You are sure you can hear a helicopter in the direction of the hospital.",

    "GYM":
    "The local franchise gym is completely empty. There is not an signs of movement inside of the" +
    "\ngym. The local drinking bars are not too far from this location. Alternatively, there may be a" +
    "\npolice station a couple of miles away from here.",

    "LAKE":
    "The local lake gives off a picturesque view as the sun sets and the evening red sunlight reflects" +
    "\noff of the usual blue waters. From the lake, you can reach the local beach that the lake water runs" +
    "\noff into by following the downstream. Up closer in the direction of the mountains, you can see a" +
    "\ncabin with some light coming from the inside.",

    "MANSION":
    "The mansion grounds come into view. Large spaces of acres have been maintained and developed. There" +
    "\nis a smaller building that seems to be a shed which might be worth searching into. In the distance," +
    "\nyou can see the local lake and local beach. You recall that the local beach may potentially hold" +
    "\nboats that can be used.",

    "BEACH":
    "The beach comes into view and you see that the sun has already set. There is very little light out." +
    "\nYou do not want to chance being out here in the dark. You see a dock with some boats in the distance," +
    "\nand the local lightrail stop. You can potentially follow the lightrail lines if you are lost.",

    "MOUNTAIN":
    "You approach the mountains and recall that you do not have that much athletic ability." +
    "\nAs you look back, you see a horde of zombies approach you. Due to the steepness and" +
    "\nunevenness of the terrain, you lose your footing. Eventually, the horde catches up" +
    "\nto you. Everything seems to go black as you can feel the horde surround and approch you.",

    "CABIN":
    "After walking some distance, you approach the wooden cabin that is only about the size" +
    "\nof a large shed. With the sun soon to set, the lantern light from the cabin seems to" +
    "\nshine much brighter than usual. Though the light is on, there seems to be noone around." +
    "\nSearching the cabin may not be a bad idea. A path from the cabin leads to the local" +
    "\nbeacn and forks off into the mountains.",

    "BARS":
    "The local drinking bars is where the locals will go for a bar crawl. Unsurprisingly," +
    "\nthe area is empty. Everyone must have been focused on evacuating when everything was" +
    "\nhappening. You may be lucky if you search this area. To decrease drinking and driving" +
    "\nthe city had placed a lightrail stop for transporation close to the local drinking" +
    "\nbars, or you can drive your expensive boats at the dock after a couple of drinks." +
    "\nThere may be a boat available to exit the city at the dock. Alternatively, the" +
    "\nlightrail will take me to the hospital.",

    "DOCK":
    "It is night time and there are some zombies roaming about. You think the zombies may" +
    "\nhave become more aggressive but are unsure. You hear some zombies possibly coming" +
    "\nyour way. You remember your neighbors had a boat, and you see one on at the dock." +
    "\nYou also see a yacht and wonder whether your neighbors owned a boat or a yacht." +
    "\nThere may be only enough time to escape on one as the zombies are steadily" +
    "\napproaching.",


    "CONSTRUCTION AREA":
    "The construction area is a project that city has been working for a couple years." +
    "\nYou can see the bare cement and steel beams, so it seems progress has been halted" +
    "\nindefinitely. As the darkness slowly blankets over the sky, you hear a helicopter." +
    "\nOn the other side of this construction area is the local hospital. Do they even" +
    "\nhave a helipad? There is also a crane by the construction area. Perhaps the" +
    "\nhelicopter pilot can see you if you climb to the top and make a signal.",

    "CRANE":
    "You decide to climb the crane to get the attention of the helicopter. Thankfully," +
    "\nclimbing to the top of the crane is easy due to accessbility with the ladder." +
    "\nAs you climb the ladder, some zombies take notice of the noise of doing so." +
    "\nLuckily, the helicopter spots and signals that they will drop a ladder to climb." +
    "\nUnfortunately, the helicopter only incites more zombies to come towards your" +
    "\nlocation and they start shaking the crane vigorously as they try to climb it." +
    "\nEventually, you lose your footing before the helicopter is able to get you and" +
    "\nfall into the pit of zombies.",

    "LIGHTRAIL":
    "The lightrail stop still has one street light luminated as night approaches along" +
    "\nwith a metal bench. When in doubt, the lightrail will always lead to a known" +
    "\nlocation since there is a map. From this location, the lightrail forks into" +
    "\ntwo. One direction goes to the local hospital, and the other goes farther away" +
    "\nfrom the city towards the more rural areas. The latter's tunnel has the lights" +
    "\nshut off from the inside. Is that a good sign or bad sign?",

    "HOSPITAL":
    "The local hospital is brimming with chaos. Zombie activity is severely high around" +
    "\nhere as other human survivors, but the number of human survivors is dropping" +
    "\nexponentially. You see that many of the human survivors have setup a barricade" +
    "\nin the emergency room. The helicopter had just landed on top of the hospital as" +
    "\nwell. It seems there is a flight of stairs potentially going directly to the" +
    "\nhelipad but is blocked by zombies. You may benefit from trying to barricade" +
    "\nwith the people in the emergency room, or you can take your chances with the" +
    "\nzombies towards the helipad.",

    "EMERGENCY ROOM":
    "You decide its too risky to try to go the helipad with all of the zombie arounnd." +
    "\nPlus, you are not even sure if the path is open to the top in the first place." +
    "\nWith this in mind, you run towards the survivors towards the emergency room. As" +
    "\nyou approach, you begin to realize the survivors are not too keen on new people." +
    "\nBefore you can turn around, you hear a gunshot towards your direction. Did they" +
    "\nshoot at a zombie behind you? As the thought passes by you, you feel a coldness" +
    "\ntake over your left chest. Eventually, everything fades to black.",

    "DARK TUNNEL":
    "This is a dark tunnel with no lights illumated on the inside and you decide to" +
    "\ntraverse it. You wonder if this was the correct decision to make. The deeper" +
    "\ninside you go, you realize that you are not alone. As this feeling of dread" +
    "\ncomes, you hear something sprinting your direction from deeper inside the" +
    "\ntunnel. Eventually, you get tackled so hard to the ground that you black out." +
    "\nYou can feel a tearing of flesh from many sources and end up not waking up again.",

    "YACHT":
    "You decide to go for the yacht. If you're going to escape the zombie apocalypse," +
    "\nwhy not do it in style? As you climb inside the yacht, you immediately go for" +
    "\nthe steering wheel. The door is wide open and the keys are already in the starter." +
    "\nAs you enter the yacht, sometime feels off. As the though crosses your mind," +
    "\na group of zombies from under the yacht deck swarm you almost instantly. You" +
    "\nhad no chance to react.",

    "HELIPAD":
    "You decide to take your chances with the zombies and the helipad. You" +
    "\nskillfully dodge all of the zombies and reach the staircase. As you sprint" +
    "\nup the stairs, you hear the emergency room barricade fall apart and" +
    "\nrealize that more zombies are chasing you up the stairs. At the top" +
    "\nlevel you reach the entrance to the roof. Thankfully, it is unlocked" +
    "\nand you lock it from the other side as you enter the roof top. Doing" +
    "\nso gives you enough time for the helicopter at the helipad let you" +
    "\ninside. It seems like you are the only one who made it.",

    "BOAT":
    "You decide to go for the humble looking boat. Though the boat is humble," +
    "\nyou realize you prioritze functionality over looks. As you hop on the" +
    "\nboat, the yacht starts to spill zombies from the inside-out. Thankfully" +
    "\nyou know how to operate this boat since this is your neighbors' boat" +
    "\nand also realize that they keep spare keys in the compartment box." +
    "\nAs a horde of zombies approach, you swiftfully start the boat and drive" +
    "\noff into the sea before any could come aboard. You look back and say" +
    "\nyour final goodbyes to your home.",


    "GAMEOVER":
    "Game over! Please start new game!"
}

hp_change = {
    "HOME": 0,
    "GARAGE": 0,
    "NEIGHBORS": 0,
    "PARK": 0,
    "BACKYARD": -1000,
    "NEIGHBORS BACKYARD": 0,
    "HIGH SCHOOL": 0,
    "SHOPPING CENTER": 0,
    "CHURCH": 0,
    "PARKING GARAGE": 0,
    "GRAVEYARD": 0,
    "DEEP GRAVEYARD": -1000,
    "MALL": 0,
    "MOTEL": 0,
    "COURTHOUSE": 0,
    "COLLEGE": 0,
    "WOODS": 0,
    "POLICE STATION": 0,
    "GYM": 0,
    "LAKE": 0,
    "MANSION": 0,
    "MOUNTAIN": -1000,
    "CABIN": 0,
    "BEACH": 0,
    "BARS": 0,
    "DOCK": 0,
    "CONSTRUCTION AREA": 0,
    "CRANE": -1000,
    "LIGHTRAIL": 0,
    "HOSPITAL": 0,
    "EMERGENCY ROOM": -1000,
    "DARK TUNNEL": -1000,
    "YACHT": -1000,
    "HELIPAD": 0,
    "BOAT": 0,
    "GAMEOVER": 0
}


hunger_change = {
    "HOME": 0,
    "GARAGE": -15,
    "NEIGHBORS": -10,
    "PARK": -25,
    "BACKYARD": -0,
    "NEIGHBORS BACKYARD": -15,
    "HIGH SCHOOL": -30,
    "SHOPPING CENTER": -20,
    "CHURCH": -25,
    "PARKING GARAGE": -15,
    "GRAVEYARD": -25,
    "DEEP GRAVEYARD": 0,
    "MALL": -25,
    "MOTEL": -15,
    "COURTHOUSE": -30,
    "COLLEGE": -30,
    "WOODS": -20,
    "POLICE STATION": -25,
    "GYM": -25,
    "LAKE": -50,
    "MANSION": -25,
    "MOUNTAIN": 0,
    "CABIN": -30,
    "BEACH": -30,
    "BARS": -30,
    "DOCK": -30,
    "CONSTRUCTION AREA": -40,
    "CRANE": 0,
    "LIGHTRAIL": -25,
    "HOSPITAL": -30,
    "EMERGENCY ROOM": 0,
    "DARK TUNNEL": 0,
    "YACHT": 0,
    "HELIPAD": 0,
    "BOAT": 0,
    "GAMEOVER": 0
}


thirst_change = {
    "HOME": 0,
    "GARAGE": -15,
    "NEIGHBORS": -10,
    "PARK": -25,
    "BACKYARD": -0,
    "NEIGHBORS BACKYARD": -15,
    "HIGH SCHOOL": -30,
    "SHOPPING CENTER": -20,
    "CHURCH": -25,
    "PARKING GARAGE": -15,
    "GRAVEYARD": -25,
    "DEEP GRAVEYARD": 0,
    "MALL": -25,
    "MOTEL": -15,
    "COURTHOUSE": -30,
    "COLLEGE": -30,
    "WOODS": -20,
    "POLICE STATION": -25,
    "GYM": -25,
    "LAKE": -50,
    "MANSION": -25,
    "MOUNTAIN": 0,
    "CABIN": -30,
    "BEACH": -30,
    "BARS": -30,
    "DOCK": -30,
    "CONSTRUCTION AREA": -40,
    "CRANE": 0,
    "LIGHTRAIL": -25,
    "HOSPITAL": -30,
    "EMERGENCY ROOM": 0,
    "DARK TUNNEL": 0,
    "YACHT": 0,
    "HELIPAD": 0,
    "BOAT": 0,
    "GAMEOVER": 0
}


area1 = {
    "HOME": "GARAGE",
    "GARAGE": "PARK",
    "NEIGHBORS": "HIGH SCHOOL",
    "PARK": "CHURCH",
    "BACKYARD": "DEATH",
    "NEIGHBORS BACKYARD": "CHURCH",
    "HIGH SCHOOL": "COURTHOUSE",
    "SHOPPING CENTER": "PARKING GARAGE",
    "CHURCH": "GRAVEYARD",
    "PARKING GARAGE": "MALL",
    "GRAVEYARD": "COURTHOUSE",
    "DEEP GRAVEYARD": "DEATH",
    "MALL": "COLLEGE",
    "MOTEL": "COLLEGE",
    "COURTHOUSE": "POLICE STATION",
    "COLLEGE": "GYM",
    "WOODS": "MANSION",
    "POLICE STATION": "CONSTRUCTION AREA",
    "GYM": "POLICE STATION",
    "LAKE": "CABIN",
    "MANSION": "LAKE",
    "MOUNTAIN": "DEATH",
    "CABIN": "MOUNTAIN",
    "BEACH": "LIGHTRAIL",
    "BARS": "LIGHTRAIL",
    "DOCK": "YACHT",
    "CONSTRUCTION AREA": "HOSPITAL",
    "CRANE": "DEATH",
    "LIGHTRAIL": "HOSPITAL",
    "HOSPITAL": "HELIPAD",
    "EMERGENCY ROOM": "DEATH",
    "DARK TUNNEL": "DEATH",
    "YACHT": "DEATH",
    "HELIPAD": "END",
    "BOAT": "END",
    "GAMEOVER": "GAMEOVER"
}

area2 = {
    "HOME": "NEIGHBORS",
    "GARAGE": "BACKYARD",
    "NEIGHBORS": "NEIGHBORS BACKYARD",
    "PARK": "HIGH SCHOOL",
    "BACKYARD": "DEATH",
    "NEIGHBORS BACKYARD": "SHOPPING CENTER",
    "HIGH SCHOOL": "MALL",
    "SHOPPING CENTER": "WOODS",
    "CHURCH": "WOODS",
    "PARKING GARAGE": "MOTEL",
    "GRAVEYARD": "DEEP GRAVEYARD",
    "DEEP GRAVEYARD": "DEATH",
    "MALL": "LAKE",
    "MOTEL": "WOODS",
    "COURTHOUSE": "COLLEGE",
    "COLLEGE": "MOUNTAIN",
    "WOODS": "SHOPPING CENTER",
    "POLICE STATION": "BARS",
    "GYM": "BARS",
    "LAKE": "BEACH",
    "MANSION": "BEACH",
    "MOUNTAIN": "DEATH",
    "CABIN": "DOCK",
    "BEACH": "DOCK",
    "BARS": "DOCK",
    "DOCK": "BOAT",
    "CONSTRUCTION AREA": "CRANE",
    "CRANE": "DEATH",
    "LIGHTRAIL": "DARK TUNNEL",
    "HOSPITAL": "EMERGENCY ROOM",
    "EMERGENCY ROOM": "DEATH",
    "DARK TUNNEL": "DEATH",
    "YACHT": "DEATH",
    "HELIPAD": "END",
    "BOAT": "END",
    "GAMEOVER": "GAMEOVER"
}


search_desc = {
    "HOME": "You find some water in the sink and food in the cupboards.",
    "GARAGE": "There is some dry food on the shelves.",
    "NEIGHBORS": "The place has been ransacked. No food or water here.",
    "PARK": "The park is so large there is nothing in it.",
    "BACKYARD": "DEATH",
    "NEIGHBORS BACKYARD": "You find some food and water in the shed. No boat though.",
    "HIGH SCHOOL": "The high school has a first aid kit by the entrance.",
    "SHOPPING CENTER": "You got a large hull of supplies! Nice!",
    "CHURCH": "There is some water in the pedastal, but I shouldn't.",
    "PARKING GARAGE": "You end up falling over the stairs.",
    "GRAVEYARD": "Nothing here. While searching, a zombie scratches me.",
    "DEEP GRAVEYARD": "DEATH",
    "MALL": "The food court has some hidden goodies!",
    "MOTEL": "The motel has some food and water in the back vending machines.",
    "COURTHOUSE": "I try to search the area, but end up tripping over.",
    "COLLEGE": "The dorms ended up having ton of ramen.",
    "WOODS": "You run into some wildlife. You fluster and twist your ankle.",
    "POLICE STATION": "I find food and water, but had to fight through zombies.",
    "GYM": "No food, but plenty of water from the bottled water machine.",
    "LAKE": "The water here is safe to drink. There is plenty of it.",
    "MANSION": "You get into a scuffle with a zombie but find some food and water.",
    "MOUNTAIN": "DEATH",
    "CABIN": "You look inside. No survivors, but plenty of dried food!",
    "BEACH": "There is plenty of water. None of it drinkable.",
    "BARS": "In desperation, you drink alcohol. This worsens your thirst.",
    "DOCK": "No food or water. There are plenty of zombies. One hits my torso.",
    "CONSTRUCTION AREA": "Thankfully, there are water bottles near the entrance.",
    "CRANE": "DEATH",
    "LIGHTRAIL": "It is empty. Quiet and empty.",
    "HOSPITAL": "Before I could search, a zombie manages to break my arm.",
    "EMERGENCY ROOM": "DEATH",
    "DARK TUNNEL": "DEATH",
    "YACHT": "DEATH",
    "HELIPAD": "END",
    "BOAT": "END"
}

search_hp_change = {
    "HOME": 0,
    "GARAGE": 0,
    "NEIGHBORS": 0,
    "PARK": 0,
    "BACKYARD": 0,
    "NEIGHBORS BACKYARD": 0,
    "HIGH SCHOOL": 20,
    "SHOPPING CENTER": 20,
    "CHURCH": 0,
    "PARKING GARAGE": -30,
    "GRAVEYARD": -40,
    "DEEP GRAVEYARD": 0,
    "MALL": 0,
    "MOTEL": 0,
    "COURTHOUSE": -30,
    "COLLEGE": 0,
    "WOODS": -50,
    "POLICE STATION": -60,
    "GYM": 0,
    "LAKE": 0,
    "MANSION": -10,
    "MOUNTAIN": 0,
    "CABIN": 0,
    "BEACH": 0,
    "BARS": 0,
    "DOCK": -50,
    "CONSTRUCTION AREA": 0,
    "CRANE": 0,
    "LIGHTRAIL": 0,
    "HOSPITAL": -100,
    "EMERGENCY ROOM": 0,
    "DARK TUNNEL": 0,
    "YACHT": 0,
    "HELIPAD": 0,
    "BOAT": 0
}

search_hunger_change = {
    "HOME": 10,
    "GARAGE": 5,
    "NEIGHBORS": 0,
    "PARK": 0,
    "BACKYARD": 0,
    "NEIGHBORS BACKYARD": 15,
    "HIGH SCHOOL": 0,
    "SHOPPING CENTER": 30,
    "CHURCH": 0,
    "PARKING GARAGE": 0,
    "GRAVEYARD": 0,
    "DEEP GRAVEYARD": 0,
    "MALL": 20,
    "MOTEL": 10,
    "COURTHOUSE": 0,
    "COLLEGE": 30,
    "WOODS": 0,
    "POLICE STATION": 15,
    "GYM": 0,
    "LAKE": 0,
    "MANSION": 10,
    "MOUNTAIN": 0,
    "CABIN": 50,
    "BEACH": 0,
    "BARS": 0,
    "DOCK": 0,
    "CONSTRUCTION AREA": 0,
    "CRANE": 0,
    "LIGHTRAIL": 0,
    "HOSPITAL": 0,
    "EMERGENCY ROOM": 0,
    "DARK TUNNEL": 0,
    "YACHT": 0,
    "HELIPAD": 0,
    "BOAT": 0
}

search_thirst_change = {
    "HOME": 10,
    "GARAGE": 0,
    "NEIGHBORS": 0,
    "PARK": 0,
    "BACKYARD": 0,
    "NEIGHBORS BACKYARD": 15,
    "HIGH SCHOOL": 0,
    "SHOPPING CENTER": 30,
    "CHURCH": 0,
    "PARKING GARAGE": 0,
    "GRAVEYARD": 0,
    "DEEP GRAVEYARD": 0,
    "MALL": 20,
    "MOTEL": 10,
    "COURTHOUSE": 0,
    "COLLEGE": 0,
    "WOODS": 0,
    "POLICE STATION": 15,
    "GYM": 40,
    "LAKE": 50,
    "MANSION": 10,
    "MOUNTAIN": 0,
    "CABIN": 0,
    "BEACH": 0,
    "BARS": -20,
    "DOCK": 0,
    "CONSTRUCTION AREA": 10,
    "CRANE": 0,
    "LIGHTRAIL": 0,
    "HOSPITAL": 0,
    "EMERGENCY ROOM": 0,
    "DARK TUNNEL": 0,
    "YACHT": 0,
    "HELIPAD": 0,
    "BOAT": 0
}
