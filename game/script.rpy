# Harper's Adventure game script

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Harper")
define b = Character("Boozman")
define s = Character("Scabs")
define d1 = Character("Favorite Dad")
define d2 = Character("Other Favorite Dad")
define n = Character("Neighbor")
define dog = Character("Dog")
define c = Character("Cat")

# Flipped images
image harper big surprised flip = im.Flip("harper big surprised.png", horizontal=True)
image harper big flip = im.Flip("harper big.png", horizontal=True)
image bo big happy flip = im.Flip("bo big happy.png", horizontal=True)
image bo big flip = im.Flip("bo big.png", horizontal=True)

# Start of Day 1 (and start of the game)

label start:
    stop music fadeout 1
    
    play music "harpers_apartment.wav" fadein 2.0
    
    # Day 1 Begins here

    scene bg black
    with Dissolve(.5)
    
    show title bright with Dissolve(0.5):
        xalign 0.5 yalign 0.5 size(1180,108)
    
    pause 2.0

    scene bg apartment
    with Dissolve(1)

    show harper big:
        xalign -1 yalign 0.99
        linear 2.0 xalign 0.5
        
    pause 1.5

    h "Meow... meeeeeeooooo--- {i}*cough cough*{/i} Um excuse me... hairball..."
    
    show harper big happy with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    h "Good morning! I'm Harper. Welcome to my home."
    
    h "These are my dads. They're the best people in the entire universe."
    
    show harper big sad with Dissolve(0.25):
        xalign 0.5 yalign 0.99
        
    play sound "sad_tone.wav"
    
    h "Except when they leave me..."
    
    #Show dad 1 here
    
    d1 "Bye, Harper! Be good!"
    
    #Show dad 2 here
    
    d2 "Stay out of the clean clothes today, okay?"
    
    "{i}Harper's dads kiss her goodbye and leave.{/i}"
    
    play sound "door_close.wav"
    
    pause 1.0
    
    h "I'll consider it..."
    
    show harper big happy with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    "{i}Harper goes to her pile of toys and plays with one of her squeaky mice.{/i}"
    
    "{i}*squeak squeak... squeak...... squeak*{/i}"
    
    show harper big sad with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    h "{i}*sigh*{/i} There has to be more to life than this."
    
    h "My dads leave every day to go on adventures. Why should I stay here and just wait for them?"
    
    show harper big with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    h "I deserve excitement."
    
    h "I could get a job..."
    
    h "I could go to space..."
    
    show harper big happy with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    h "I could find out where the cat food comes from!"
    
    show harper big with Dissolve(0.25):
        xalign 0.5 yalign 0.99
    
    h "Maybe, today, I'll settle for leaving the apartment."
    
    menu:
        
        "Did my dads lock the door? They're always forgetting, silly humans.":
            jump choiceday1_door
        
        "Maybe I should check on the clean clothes first, just in case...":
            jump choiceday1_laundry
        
    label choiceday1_door:
        $ door_checked = True
        
        "{i}The door is unlocked and slightly ajar. Harper steps into the hallway.{/i}"
        jump day1_hallway
        
    label choiceday1_laundry:
        $ door_checked = False
        
        show bg laundry with Dissolve(1.0)
        
        "{i}Harper walks to the laundry room and lies on the warm, freshly laundered clothes.{/i}"
        
        "{i}There is a cool draft.{/i}"
        
        show harper big surprised with Dissolve(0.25):
            xalign 0.5 yalign 0.99
        
        h "There's a hole behind the big cleaning machine! I've never explored that way!"
        
        show harper big with Dissolve(0.25):
            xalign 0.5 yalign 0.99
            linear 1.0 xalign 2.0
        
        "{i}Harper scurries through the hole.{/i}"
        jump day1_hallway
        
    label day1_hallway:
        hide harper with Dissolve(0.25)
        
        play music "hallway.wav"
         
        scene bg hallway with Dissolve(0.5)
         
        show harper big with Dissolve(0.25):
            xalign 0.5 yalign 0.99
            
        "{i}Harper finds herself in the hallway. She shivers.{/i}"
        
        h "Get it together, Harper. The hallway doesn't always mean you're going to the vet."
        
        show harper big surprised with Dissolve(0.25):
            xalign 0.5 yalign 0.99
            
        play sound "surprise.wav"
        
        "{i}Harper hears footsteps.{/i}"
        
        h "What was that?"
        
        show harper big surprised flip:
            xalign 0.5 yalign 0.99
            
        pause .5
        
        show harper big surprised:
            xalign 0.5 yalign 0.99
            
        pause .5
        
        show harper big surprised flip:
            xalign 0.5 yalign 0.99
            linear 1.5 xalign -2.0
        
        "{i}Harper quickly jumps into the nearest trash can.{/i}"
        
        show bo big happy with Dissolve(0.25):
            xalign 5.0 yalign 0.99
            linear 2.5 xalign 0.5
        
        "{i}A dog and his owner walk down the hallway.{/i}"
        
        n "Bo, stay."
        
        play sound "door_open.wav"
        
        n "{i}*mumbles*{/i} I really thought I brought the bags with me..."
        
        show bo big with Dissolve(0.25):
            xalign 0.5 yalign 0.99
        
        "{i}The woman goes into the apartment.{/i}"
        
        hide bo big happy with Dissolve(0.25)
        
        "{i}The hallway falls into silence.{/i}"
        
        show harper big with Dissolve(0.25):
            xalign -1.0 yalign 0.99
            linear 2.5 xalign -.25
            
        pause 2.5
        
        "{i}Harper peeks her head out of the trashcan.{/i}"
        
        show bo big:
            xalign 1.25 yalign 0.99
            
        show harper big surprised:
            xalign -.25 yalign 0.99
            
        play sound "surprise.wav"
        
        stop music fadeout 1.0
        
        play music "boozmans_theme.wav" fadein 1.0
        
        dog "Oh hi! I thought I smelled something that wasn't trash. You smell nice."
        
        show harper big with Dissolve(0.25):
            xalign -.25 yalign 0.99
        
        menu:
            
            "{i}Stare in silence.{/i}":
                jump day1_silence
            
            "Hello!":
                jump day1_greet
                
            "Thank you, I bathe frequently. You should try it...":
                jump day1_bathe
                
        label day1_silence:
            
            b "You smell very nice. Hi! I'm Boozman, but you can call me Bo. I'm so happy to meet you. Do you live here in this trashcan?"
            jump choiceday1_respond1
            
        label day1_greet:
            
            b "Hi! I'm Boozman, but you can call me Bo. I'm so happy to meet you. Do you live here in this trashcan?"
            jump choiceday1_respond1
                    
        label day1_bathe:
            
            dog "Baths are fun. There are bubbles and my human always slips and falls."
            
            b "By the way, I'm Boozman, but you can just call me Bo. Do you live here in this trashcan?"
            jump choiceday1_respond1
            
        label choiceday1_respond1:
            $ live_trashcan = False
            
            menu:
                
                "No. I live in that apartment.":
                    jump day1_boresponse1
                    
                "No, silly. My dads and I live next door.":
                    jump day1_boresponse2
                    
                "Yes, I just moved in. I'm just redecorating.":
                    jump day1_boresponse3
                    
        label day1_boresponse1:
            
            b "Oh, that must be very nice. My home is very nice. Is yours like mine?"
            jump choiceday1_respond2a
        
        label day1_boresponse2:
            
            b "You have more than ONE dad? That must be so fun."
            
            b "I just have my mom. She's the best. You should meet her. Is your apartment nice like mine?"
            jump choiceday1_respond2a
            
        label day1_boresponse3:
            
            b "It is a very nice trashcan. I have a friend that lives in a box. It smells much nicer then this though."
            jump choiceday1_respond2b
            
        label choiceday1_respond2a:
            
            menu:
                
                "I think all of the units are very similar.":
                    jump day1_boresponse4a
                    
                "It's the best apartment.":
                    jump day1_boresponse4a
                    
        label choiceday1_respond2b:
            
            menu:
                
                "...I was kidding. I have an apartment.":
                    jump day1_boresponse4b
                    
                "I bet it does...":
                    $ live_trashcan = True
                    jump day1_boresponse4b
                    
        label day1_boresponse4a:
            
            b "That is great. It is a nice place to live. I'm glad yours is nice too."
            jump day1_hallway2
            
        label day1_boresponse4b:
            
            b "That is great. It is a nice place to live."
            jump day1_hallway2
            
        label day1_hallway2:
            
            b "Will you be back in the trashcan tomorrow? I have to go for a walk now, but I want to see my new friend again!"
            jump choiceday1_respond3
            
        label choiceday1_respond3:
            
            menu:
                
                "Okay, I'll come back tomorrow.":
                    jump day1_hallway3
                    
                "I'll see you tomorrow!":
                    jump day1_hallway3
                    
                "I'll try my best.":
                    jump day1_hallway3
                    
        label day1_hallway3:
            
            play sound "surprise.wav"
            
            show harper big surprised:
                xalign -.25 yalign 0.99
                
            pause .5
            
            show harper big surprised flip:
                xalign -.25 yalign 0.99
                linear 1.0 xalign -1.0
            
            "{i}Boozman's apartment door begins to open. Harper quickly ducks back into the trashcan.{/i}"
            
            b "Byyyeeeeeeee!"
            
            show bo big happy flip:
                xalign 1.25 yalign 0.99
                linear 2.5 xalign 2.5
                
            play sound "door_close.wav"
            
            stop music fadeout 3.0
            
            "{i}Boozman and his owner walk down the hallway and around the corner.{/i}"
            
            "{i}The hallway is once again silent.{/i}" 
            
            show harper big with Dissolve(0.25):
                xalign -1.0 yalign 0.99
                linear 2.5 xalign 0.5
            
            pause 2.5
            
            "{i}Harper peeks back out of the trash and takes a deep breath.{/i}"
                
            h "That is definitely enough adventure for one day."
            
            "{i}Harper jumps down from the trashcan and makes her way back inside.{/i}"
            
            show harper big:
                xalign 0.5 yalign 0.99
                linear 2.0 xalign 2.0
            
            pause 2.0
            
            play music "harpers_apartment.wav"
            
            scene bg apartment with Dissolve(1.0)
            
            show harper big happy with Dissolve(0.25):
                xalign 0.5 yalign 0.99
            
            "{i}Harper curls up on her bed and lets out a long sigh.{/i}"
            
            h "I could be a great explorer. I am so brave."
            
            "{i}Harper falls asleep.{/i}"
            
            stop music fadeout 1.0
            
            jump day2_apartment
            
    # End of Day 1
    
    # Start of Day 2
    
    label day2_apartment:
        
        scene bg black with Dissolve(.5)
        
        show title day2 with Dissolve(0.5):
            xalign 0.5 yalign 0.5 size(260,108)
            
        pause 2.0
        
        play music "harpers_apartment.wav"
        
        scene bg apartment with Dissolve(1)
        
        "{i}Harper wakes with a stretch.{/i}"
        
        show harper big with Dissolve(.5):
            xalign 0.5 yalign 0.99
            
        "{i}She waits impatiently until her dads leave.{/i}"
        
        "{i}They kiss her goodbye.{/i}"
        
        play sound "door_close.wav"
        
        pause 1.0
        
        if door_checked:
            jump day2_exitdoor
            
        else:
            jump day2_exitvent
            
    label day2_exitdoor:
        
        "{i}Harper paces in front of the door.{/i}"

        h "You did it yesterday. You can do it again. Just go outside."
        
        "{i}She jumps to open the door, only to discover that it's locked.{/i}"
        
        h "Dads! The one time I'm counting on you to screw up!"
        
        h "How else can I leave? Think. Think. Think!"
        
        show bg laundry with Dissolve(0.5)
        
        h "To my thinking spot! The clean laundry basket!"
        
        b "{i}*faintly*{/i} Kitty friend?"
        
        h "Did that come from behind the big cleaning machine?"
        
        "{i}Harper finds the vent behind the washing machine.{/i}"
        jump day2_exitvent
        
    label day2_exitvent:
        
        show harper big with Dissolve(0.25):
            xalign 0.5 yalign 0.99
            linear 1.0 xalign 2.0
        
        "{i}She goes out the laundry vent.{/i}"
        
        stop music fadeout 2.0
        
        pause 2.0
        
        scene bg hallway with Dissolve(0.5)
        
        show bo big happy with Dissolve(0.5):
            xalign 1.25 yalign 0.99
            
        show harper big with Dissolve(0.5):
            xalign -1.0 yalign 0.99
            linear 2.0 xalign -.25
        
        play music "boozmans_theme.wav" fadein 1.0
        
        b "Kitty friend!"
        
        show bo big with Dissolve(0.5):
            xalign 1.25 yalign 0.99
        
        menu:
            
            "Boozman!":
                jump day2_boresponse1
                
            "Dog friend!":
                jump day2_boresponse2
                
            "The name is Harper, actually.":
                jump day2_boresponse3
                
    label day2_boresponse1:
        
        b "Kitty! What is your name, new friend?"
        
        menu:
            
            "Harper!":
                jump day2_boresponse3
                
            "Harper the Norwegian Forest!":
                jump day2_boresponse3
                
    label day2_boresponse2:
        
        b "I'm so happy you came today. SO happy!"
        
        h "I am too! My name is Harper, by the way."
        jump day2_boresponse3
        
    label day2_boresponse3:
        
        b "Harper! That is the coolest name I've ever heard!"
        
        menu: 
            
            "How did you get out of your apartment?":
                jump day2_boresponse4
                
            "Do you leave your house very often?":
                jump day2_boresponse5
                
    label day2_boresponse4:
        
        b "My human is not very good at closing things."
        
        b "Like the cabinet to the food..."
        
        b "Or that box of cake..."
        
        b "Or the door."
        jump day2_boresponse6
        
    label day2_boresponse5:
        
        b "Usually only when my human leaves..."
        jump day2_boresponse6
        
    label day2_boresponse6:
        
        b "I am so happy to have a new friend. Why haven't we met before?"
        
        h "I'm more of an indoor cat. I just decided yesterday to have some fun while my dads are out during the day."
        
        menu:
            
            "What is there to do around the building?":
                jump day2_boresponse7
                
            "Will you help me find an adventure?":
                jump day2_boresponse8
                
            "How do we escape?":
                jump day2_boresponse9
                
    
    label day2_boresponse7:
        
        b "This building is very exciting!"
        
        b "We can go sniff doors and see if we can smell food. Or sometimes there is food in trashcans."
        
        h "Um... is there anything else to do?"
        
        b "Outside is even MORE interesting!"
        
        menu:
            
            "Well, I guess I could see what it's like outside...":
                jump day2_boresponse10
                
            "I don't know, it sounds kind of dangerous outside...":
                jump day2_boresponse11
                
    label day2_boresponse8:
        
        b "The best place to find adventure is outside! Let's go!"
        
        b "Um... Okay. If you say so..."
        jump day2_boresponse9
        
    label day2_boresponse9:
        
        b "To the FIRE ESCAPE!"
        
        h "Fire? Where?"
        jump day2_street1
        
    label day2_boresponse10:
        
        b "Let's go!"
        jump day2_boresponse9
        
    label day2_boresponse11:
        
        b "Oh, please come outside. Please please please!"
        
        h "Well, okay. What's the worst that could happen?"
        jump day2_boresponse9
        
    label day2_street1:
        
        show bo big happy flip:
            xalign 1.25 yalign 0.99
            linear 1.0 xalign 2.5
            
        pause 1.0
        
        show harper big:
            xalign -.25 yalign 0.99
            linear 3.0 xalign 2.0
        
        "{i}Boozman darts away and Harper cautiously follows him down the fire escape.{/i}"
        
        stop music fadeout 1.5
        
        pause 1.5
        
        scene bg black with Dissolve(.5)
        
        pause 1.0
        
        scene bg alley with Dissolve(1.0)
        
        play music ("harpers_alleyway_redone.wav")
        
        show bo big happy flip:
            xalign -2.5 yalign 0.99
            linear 4.0 xalign 1.25
            
        show harper big:
            xalign-2.0 yalign 0.99
            linear 3.0 xalign -.25
        
        "{i}Harper finds herself on a busy street.{/i}"
        
        show bo big with Dissolve(0.5):
            xalign 1.25 yalign 0.99
        
        h "Everything looks so much bigger than from my window!"
    
        #Car screech here
        play sound "car_skidding.mp3"
        
        pause 1.5
        
        show harper big surprised with Dissolve(0.5):
            xalign -.25 yalign 0.99
            linear 1.0 xalign 1.25
        
        "{i}A car turns the corner and Harper goes running, only to stop short when Boozman steps on her tail.{/i}"
        
        b "Little Harper, cars are not so scary. You don't have to be afraid."
        
        show harper big with Dissolve(0.5):
            xalign 1.25 yalign 0.99
            linear 2.0 xalign -.25
        
        "{i}Harper takes a deep breath.{/i}"
        
        h "Be cool, kitty."
        
        play sound "rain.wav"
        
        show bg alley rainy with Dissolve(0.5)
        
        "{i}It begins to rain.{/i}"
        
        "{i}Although every instinct is telling her to hide, Harper stands tall and walks with Boozman, ignoring the heavy, cold drops that catch in her fur.{/i}"
        
        #Thunderclap here
        play sound "thunderclap.mp3"
        
        show harper big surprised with Dissolve(0.5):
            xalign -.25 yalign 0.99
            linear 1.0 xalign 2.0
            
        hide bo with Dissolve(0.5)
        
        "{i}Thunder roars and Harper cannot help herself. She runs.{/i}"
        
        "{i}Without a thought, she darts into the nearest shelter: a large cardbaord box.{/i}"
        
        stop music fadeout 1.0
        
        scene bg black with Dissolve(.5)
        
        "{i}In the darkness, a pair of yellow eyes blink open.{/i}"
        
        c "I'm not very fond of sharing my boxes..."
        
        menu:
            
            "I'm so sorry to disturb you!":
                jump day2_scabsresponse1
                
            "{i}RUN{/i}":
                jump day2_scabsresponse2
                
    label day2_scabsresponse1:
        
        c "Sorry can't save you."
        
        "{i}Harper backs out of the box very slowly.{/i}"
        
        scene bg alley rainy with Dissolve(1.0)
        
        stop music fadeout 1.0
        
        play music ("scabs_theme.wav")
        
        show bo big flip with Dissolve(0.5):
            xalign -.7 yalign 0.99
            
        show harper big with Dissolve(0.5):
            xalign 2.0 yalign 0.99
            linear 3.0 xalign 0.0
        
        b "Oh, that's just Scabs. She won't actually hurt you."
        
        show scabs big angry with Dissolve(0.5):
            xalign 2.0 yalign 0.99
            linear 2.0 xalign 1.25
        
        "{i}Scabs peeks her head out of the box.{/i}"
        
        s "Oh, yes I would."
        jump day2_alley2
        
    label day2_scabsresponse2:
        
        "{i}Harper sprints out of the box.{/i}"
        
        scene bg alley rainy with Dissolve(1.0)
        
        stop music fadeout 1.0
        
        play music ("scabs_theme.wav")
        
        show bo big flip with Dissolve(0.5):
            xalign -.7 yalign 0.99
            
        show harper big surprised flip with Dissolve(0.5):
            xalign 2.0 yalign 0.99
            linear 1.0 xalign 0.0
            linear 0.5 xalign 0.5
        
        "{i}And slams into Boozman.{/i}"
        
        b "Woah, Kitty Friend, what's so scary?"
        
        h "It's a monster..."
        
        show bo big flip:
            xalign -.7 yalign 0.99
            linear 3.0 xalign 1.25
            
        show harper big surprised:
            xalign 0.5 yalign 0.99
            linear 1.0 xalign 0.0
        
        "{i}Boozman peeks into the box.{/i}"
        
        b "Silly Harper, that's just Scabs. She's my friend!"
        
        show bo big flip:
            xalign 1.25 yalign 0.99
            linear 3.0 xalign -.7
            
        show harper big with Dissolve(0.5):
            xalign 0.0 yalign 0.99
        
        show scabs big angry with Dissolve(0.5):
            xalign 2.0 yalign 0.99
            linear 2.0 xalign 1.25
            
        pause 3.0
        
        jump day2_alley2
        
    label day2_alley2:
        
        show scabs big with Dissolve(0.5):
            xalign 1.25 yalign 0.99
        
        "{i}Scabs comes out of the box, blinking in the rain.{/i}"
        
        b "Scabs, this is my new friend, Harper."
        
        if live_trashcan:
            b "She lives in a trashcan in my building!"
            
        else:
            b "She lives next door to me with her dads!"
            
        b "Harper, this is my friend, Scabs! I bet she could show you all kinds of places to find adventure!"
        
        "{i}Harper shivers.{/i}"
        
        b "Oh, Kitty! You're soaking wet. Maybe we should go back inside for the day."
        
        b "We can go on an adventure tomorrow! Right, Scabs?"
        
        "{i}Scabs examines her claws nonchalantly.{/i}"
        
        s "Tomorrow can only be better."
        
        "{i}Boozman gives Scabs a goodbye lick.{/i}"
        
        b "Bye-bye, Scabs! Come on, Harper!"
        
        menu:
            
            "Bye Scabs, nice to meet you!":
                jump day2_scabsresponse3
                
            "I'll come back if she plays nice.":
                jump day2_scabsresponse4
                
    label day2_scabsresponse3:
        
        s "Bye, Harper."
        
        show harper big flip:
            xalign -.35 yalign 0.99
            linear 2.0 xalign -2.0
        
        show bo big happy flip:
            xalign -.7 yalign 0.99
            linear 2.0 xalign -2.0
        
        "{i}Scabs winks. Harper smiles nervously and follows Boozman back to the building.{/i}"
        jump day2_apartment2
        
    label day2_scabsresponse4:
        
        show harper big surprised flip:
            xalign -.35 yalign 0.99
            linear 1.75 xalign -2.0
        
        show bo big happy flip:
            xalign -.7 yalign 0.99
            linear 2.0 xalign -2.0
            
        show scabs big angry with Dissolve(0.5):
            xalign 1.25 yalign 0.99
        
        "{i}Scabs hears Harper mumbling and hisses playfully. Harper jumps and heads back to the building quickly, Boozman trailing behind her.{/i}"
        jump day2_apartment2
        
    label day2_apartment2:
        
        stop music fadeout 1.0
        
        pause 1.0
    
        play music "harpers_apartment.wav" fadein 2.0

        scene bg black with Dissolve(.5)
    
        pause 1.0

        scene bg laundry with Dissolve(1)
        
        "{i}Home safe again, Harper curls up in a basket of fresh laundry to dry off.{/i}"
        
        show harper big sad with Dissolve(0.5):
            xalign 0.5 yalign 0.99
        
        h "I should have just gone to space. It would have been easier."
        
        "{i}She closes her eyes and is asleep within minutes.{/i}"
        
        stop music fadeout 1.0

        scene bg black with Dissolve(.5)
    
        pause 1.0

        scene bg apartment night with Dissolve(1)
        
        "{i}It's 3AM...{/i}"
        
        "{i}Harper mumbles in her sleep.{/i}"
        
        h "Not the box! Anything but the box!"
        
        play sound "surprise.wav"
        
        show harper big surprised with Dissolve(0.5):
            xalign 0.5 yalign 0.99
        
        "{i}Harper jerks awake in her cat bed.{/i}"
        
        show harper big with Dissolve(0.5):
            xalign 0.5 yalign 0.99
        
        h "Phew, it was just a dream."
        
        menu:
            
            "Just go back to sleep, Harper. You're safe in your comfy bed.":
                jump day2_apartment3
                
            "I bet if I woke my dads, they would feed me.":
                jump day2_apartment4
        
    label day2_apartment4:
        
        hide harper with Dissolve(0.5)
        
        play sound "door_open.wav"
        
        "{i}Harper paws at the bedroom door and it creaks open.{/i}"
        
        h "Meow..."
        
        h "Meoooooow..."
        
        h "{i}*cough cough*{/i} MEOOOOOOOOW!"
        
        d1 "What Harper?"
        
        h "Meow... meow..."
        
        d2 "Really? Now? It's 3 o'clock in the morning!"
        
        h "Meoooooooow."
        
        d1 "Will you please go feed her?"
        
        d2 "Ugh, fine..."
        
        play sound "bowl_fill.ogg"
        
        "{i}Harper's brown haired dad fills up her bowl.{/i}"
        
        d2 "There you go."
        
        "{i}Harper begins to chow down on the food immediately.{/i}"
        
        d2 "Brat..."
        
        "{i}Harper's dad goes back to the bedroom and closes the door tightly.{/i}"
        
        "{i}Harper finishes off the bowl and begins to clean herself.{/i}"
        
        show harper big happy with Dissolve(0.5):
            xalign 0.5 yalign 0.99
        
        h "And that's how it's done."
        
        "{i}Harper heads back to the warmth of her bed and falls asleep.{/i}"
        jump day2_apartment3
        
    label day2_apartment3:
        
        stop music fadeout 3.0
        
        scene bg black with Dissolve(3.0)
        
    # This ends the game.

    return
