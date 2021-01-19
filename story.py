import random
import string

reward = [
    "friendship", "five bucks", "a speedboat", "a vicuna", "two vicunas",
    "a burrito someone left in the MistCoaster", "world peace"
]
phr_adj = [
    "Edgy", "Existential", "Cool", "Creepy", "Disturbing", "Very questy",
    "Classy", "You do you I guess", "I mean, to each their own",
    "We'll workshop that", "I'll consider that a rough draft",
    "They can't all be winners", "Love it", "Inspiring"
]

name = input(
    "\n\nWelcome to Rescue Dezell: A Select-Your-Own-Quest Story! Type your name to begin.\n"
)
print(
    "\nYou are enjoying a pleasant day at MistLand, the mistiest mist park in the entire world. "
    "(Like a water park, but on a budget.) The sun is shining, the humidity is high, and the water is wet "
    "(contrary to popular belief). Suddenly, you spy a figure racing toward you. It’s Duncan the Droplet, "
    "the official mascot of MistLand! Though he is inside an anthropomorphic water droplet costume, you can "
    "tell he is quite distraught.")
print(
    "\n“" + name +
    "! Your friend… Dezell… he’s…” Duncan pants. You give him a second to catch his breath. "
    "“Dezell is MISSING!” he finally spits out. \n“Will you help us find him? There’s a reward in it for you…”"
)
while True:
    action = input(
        "\nType “A” to accept this quest. Type “B” to say “No. The reward is probably something lame, like friendship.”\n"
    )
    if action.lower() == "a" or action.lower() == "b":
        break
c = 0
if action.lower() == "b":
    c = 1
    while action.lower() != "a" and c < len(reward):
        print("Frustrated, Duncan says, “What if I give you " + reward[c] +
              "?”")
        action = input(
            "\nType “A” to accept this quest. Type “B” to say “No. That sounds even lamer than "
            + reward[c - 1] + ".”\n")
        c = c + 1
    if c == len(reward) and action.lower() != "a":
        print(
            "Duncan is exasperated. “Fine! I’ll find someone else who will accept this quest.\nYou should’ve taken world peace when you had the chance.”\nTHE END"
        )
if action.lower() == "a":
    print(
        "\n“Great!” Duncan says. He furrows his dropletish brow. “Only thing is, you can’t really do a quest without a catchphrase. What’s yours gonna be?”"
    )
    phrase = input("\nEnter your catchphrase.\n")
    random.seed(len(phrase))
    while phrase[len(
            phrase
    ) - 1] in string.punctuation:  #while last character is punctuation mark
        phrase = phrase[0:len(phrase) - 1]  #cut off last character
    print(
        "\n“Oooh. ‘" + phrase + ".’ " + random.choice(phr_adj) +
        ",” Duncan remarks. “Okay, Dezell is probably somewhere in "
        "this park. He was last seen at Kate’s Swampilicious Bog Bash, and on the MistCoaster before that. Maybe check one of those places first?”"
    )
    while True:
        action = input(
            "\nType “A” to check Kate’s Swampilicious Bog Bash. Type “B” to check the MistCoaster.\n"
        )
        if action.lower() == "a" or action.lower() == "b":
            break
    if action.lower() == "a":
        print(
            "\nYou walk over to Kate’s Swampilicious Bog Bash. You don’t know what the heck you were expecting, but it sure wasn’t this:"
            " a massive artificial swamp inside MistLand! You hear loud music, and you realize that it’s coming from a small record player"
            " in the corner that’s blasting an Alvin and the Chipmunks cover of “Run Rudolph Run.”"
        )
        keepgoing = input("\nHit enter to keep exploring.")
        print(
            "\nYou continue exploring the swamp and discover a group of bipedal alligators having a tea party. The gators are engaged in "
            "an intense discussion — when suddenly one sees you approaching. “Hey. Name’s Kate. Care to join us?”\nshe says, her dagger-like"
            " teeth glistening in the sunlight. Hesitant, you sit next to her. \n“We don’t often get company,” she adds.\n“Well, except for Dezell,”"
            " another gator recalls. “He always talked with us.”\n“Yeah,” said a third gator. “It’s a shame he had to go missing.”"
        )
        print(
            "\nOut of the corner of your eye, you see an Iron Man t-shirt floating in the swamp water.\nDidn’t Dezell always wear that? And what exactly is Kate picking out of her teeth?"
        )
        print(
            "\nKate grins ominously. “You know, if you’re looking for Dezell,” she says, “I could help you find him.”"
        )
        print(
            "\nThat record player must be stuck, because the Chipmunks keep singing “Run… Run… Run… RUN…”"
        )
        while True:
            action = input(
                "\nType “A” to say, “Okay!” Type “B” to get the heck out of there.\n"
            )
            if action.lower() == "a" or action.lower() == "b":
                break
        if action.lower() == "a":
            print(
                "\nKate points to the t-shirt floating in the water. “Dezell went for a swim. Said he was going to get some food.”"
            )
            print(
                "\nKate steps away and returns with a kayak in her mouth. You thank Kate and her fellow gators for the help, and "
                "they thank you for the lively conversation. You begin paddling the canoe in search of the nearest restaurant, "
                "when you notice a dog swimming next to your kayak.")
            keepgoing = input("\nHit enter to continue.")
        elif action.lower() == "b":
            print(
                "\n“Nope!” you yell. “See ya later, alligators! " + phrase +
                "!” \nYou begin to run, but you hear loud weeping behind you. "
                "You turn around to see the gators sobbing. \n“Why?” Kate whimpers. “Why are they always so mean?” You aren’t buying it though. "
                "\n“Crocodile tears, Kate? Really?” \nAnother alligator puts his arm around her. “Insensitive human!” he screams. “We’re ALLIGATORS!”"
            )
            print(
                "\nWow, you really blew it with them. Time to go to the MistCoaster and look for clues there."
            )
            keepgoing = input("\nHit enter to continue, you meanie.")
    if action.lower(
    ) == "b":  #not elif, because player sent this way if they mess up at Swamp
        print(
            "\nYou approach the monstrous MistCoaster, which is like a normal rollercoaster, but misty. You prepare to wait in line, but there "
            "isn’t one. The only person you can see nearby is an angsty park worker."
        )
        print("\n“Hello and welcome to the MistCoaster,” she says apathetically. “I’m Henrietta Humidity and I can’t wait to take you on this mist-erious journey.” (Her tone of voice suggests that she definitely *can* wait.)")
        keepgoing = input("\nHit enter to continue.")
        print("\n“Have you seen Dezell?” you ask.")
        print("“No,” she says.")
        print("“Are you sure? Duncan says he was here.”")
        print("“No,” she says.")
        print("“Is that the only word you’re gonna say?”")
        print("She nods.")
        print(
            "\nYou then hear someone calling for help, and it appears to be coming from a nearby drinking fountain. When you\nlook over there, Henrietta "
            "shakes her head vigorously.")
        while True:
            action = input(
                "\nType “A” to investigate the drinking fountain. Type “B” to search the MistCoaster.\n"
            )
            if action.lower() == "a" or action.lower() == "b":
                break
        if action.lower() == "a":
            print(
                "\n“What’s in there?” you ask, motioning to the fountain.\nHenrietta suddenly seems less apathetic. “I’m warning you, kid. Don’t.”\nYou walk over anyway.\n“TURN KNOB!” a voice shouts, apparently from inside the fountain.\nYou turn the knob. Henrietta runs for cover. "
            )
            print(
                "Out of the fountain jumps the longest dachshund you have ever seen. It is quite unclear how he got in there in the first place. He licks your face, then smirks at Henrietta."
            )
            print(
                "“GET OUT!” Henrietta screams. “LEAVE HERE WITH THAT FILTHY DOGGO AT ONCE!” For once, you do as you’re told."
            )
            keepgoing = input(
                "\nHit enter to suffer the consequences of your incessantly rebellious ways!"
            )
        elif action.lower() == "b":
            print(
                "\nYou sit down on the MistCoaster and buckle in. As your cart climbs the giant hill, robotic arms come out from the walls and spray you with spray bottles. "
                "Feeling mistier by the second, you realize that this ride isn’t half bad."
            )
            print(
                "An unpleasant odor begins to fill your nostrils, however. It takes your brain a bit to identify the odor, but it reminds you of a wet dog. "
                "You feel your ankle becoming misty as well. You look down. A dog is hiding under your seat, licking your ankle. Once he sees that you "
                "have spotted him, he climbs up into the seat next to yours.")
            keepgoing = input("\nHit enter to continue.")
    #Dog path
    print("\n“Henlo,” the pupper says. “Do not be afeared, " + name +
          ". It am me, your doggo.")
    print("“Uh, no you aren’t,” you say, confused.")
    print("“Oh, not yet. I is your doggo from DA FUTURE.”")
    print("“Prove it,” you say.")
    print("“You say, ‘" + phrase + "’ a lot.”")
    print("You are visibly impressed. You give him a scratch behind the ears.")
    print(
        "“Listen closely,” he says. “We hab no time to lose. Dezell in danger. Get me to Mistaurant.”"
    )
    print("“Mistaurant?” you question.")
    print(
        "“Mistaurant,” he repeats. “Like restaurant, but with humidity, and big mold problem.”")
    print("You agree to take him to the Mistaurant.")
    print("“When hooman and doggo arrive, buy BACON. Understand?”")
    while True:
        action = input(
            "\nType “A” to say, “Got it!” Type “B” to say, “Not really.”\n")
        if action.lower() == "a" or action.lower() == "b":
            break
    count = 0
    dog_say = [
        "Capeesh", "Get it", "Catch doggo’s drift",
        "Comprehend doggo’s meaning", "Picking up what doggo laying down",
        "Smelling what doggo cooking",
        "\nDo you grasp the nature, significance, or meaning of the words I have put before you, hooman", "Can hooman and doggo go now", "There an echo in here", "Is doggo in some kind of time loop", "Isn't there a word for this feeling? That doggo seen this moment before", "Merriam Webster says, \'déjà vu is a feeling that one has seen or heard something before.\' Sounds like this moment, right", "\nThe food will be ours, ours for the takin'.\nWe will hold fast and not be shaken.\nFor 'tis history that we are makin'.\n\nNow doggo will ask (and likely regret it),\nCan hooman now say that hooman get it?!", "Will hooman say anything other than \'Not really\'", "Fine. Is hooman ready to start this convo all over again"
    ]
    #Loop through doggo responses until A is input
    while action.lower() != "a":
        choose = count % len(dog_say)
        print("\n“When hooman and doggo arrive, buy BACON. " + dog_say[choose] +
              "?”")
        action = input(
            "\nType “A” to say, “Got it!” Type “B” to say, “Not really.”\n")
        count = count + 1
    print(
        "\nYou and your newfound canine sidekick arrive at the Mistaurant.\nYou take a deep breath, "
        "savoring the misty air, the moldy smell, and the adventurous ambience!"
    )
    print(
        "\nA waiter approaches. “Welcome to the Mistaurant, home of the MistMeal! What can I get for you?”"
    )
    print("\nYour canine friend winks at you. You know what to do.")
    while True:
        action = input(
            "\nType “A” to order a vegan burger. Type “B” to order bacon.\n")
        if action.lower() == "a" or action.lower() == "b":
            break
    if action.lower() == "a":
        print("\n“I see,” the waiter says. “Right this way.”")
        print(
            "He leads you down a dark hallway. “Here we are,” he says, as you enter a room. Suddenly, you hear"
            " a loud CLANG behind you. The lights come on. You’ve been led into a jail cell!"
        )
        print(
            "\nOn the other side of the bars is your doggo. “You set me up!” you shout."
        )
        print(
            "“Yes, hooman. Doggo knew that hooman would do reverse of what doggo said, so doggo lured hooman into"
            " trap. Maybe now hooman will gib treatos when doggo ask!”")
        keepgoing = input("\nNow hit enter and think about what you've done.")
        print("\nYou feel your phone buzzing in your pocket. It’s Dezell!")
        print("“Hey " + name + ", where are you?” he asks.")
        print(
            "“Where am I?” you question, exhausted. “Where the heck are you? I’ve been looking for you all day!”"
        )
        print(
            "“Oh, I went home!” he says. “Where are you?”\nYou hang up.\n\nTHE END"
        )
    if action.lower() == "b":
        print(
            "\n“Bacon?” the waiter asks. “So the prophecy is true!”\nHe hands you a rubber duck. “Quickly, use this "
            "to save Dezell, before it is too late!”")
        while True:
            action = input(
                "\nType “A” to eat the rubber duck. Type “B” to throw the rubber duck.\n"
            )
            if action.lower() == "a" or action.lower() == "b":
                break
        if action.lower() == "a":
            print(
                "\nYou take a bite of the rubber duck. The waiter begins to cry. The doggo begins to howl.\n“Guess "
                "the prophecy wasn’t true,” the waiter says between sobs.\n“In fairness,” the canine says, "
                "“Doggo would have eaten ducko too.”")
            print(
                "\nWelp, guess Dezell will forever be stuck who-knows-where. And all because you got hungry.\n\nTHE END"
            )
        if action.lower() == "b":
            print(
                "\n“" + phrase.upper() +
                "!” you shout as you throw the duck against the wall.\nIt sticks there, "
                "and begins to glow a shade of chartreuse. A portal opens up around the duck,\nand through the "
                "haze of its ethereal glow, you can see Dezell on the other side!"
            )
            print("You reach through and grab him faster than you can say “" +
                  phrase + ".”")
            print(
                "\n“Whoa, thanks " + name +
                "!” he says. “The planet DKUC-1973 was pretty weird. Glad to be back.”"
            )
            print("“How did you get there, anyway?” you ask.")
            print("He smiles. “That’s a story for another time.”")
            print(
                "\nYou give Duncan the Droplet the good news. “So, where’s my reward?” you ask."
            )
            print(
                "Duncan puts his hand on your shoulder. “Isn’t adventure its own reward?”"
            )
            # If user negotiated for reward
            if c > 0:
                print("\nYou frown. “I was promised " + reward[c - 1] + ".”")
            print("\nTHE END")
