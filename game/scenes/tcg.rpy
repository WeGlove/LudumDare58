label scene_tcg:

    scene bg black

    "Ahh that thing..."

    "I still do not know what exactly is the worth of that."
    show tgc 1 at top
    "I should have just sticked to Battle Lawyers Evolution. It's the best TCG anyways."
    show tgc 2 at top

    define clerk = Character("Clerk")
    define teen_1 = Character("Timothy")
    define teen_2 = Character("Benny")
    define teen_3 = Character("Antoine-Jerome")

    frank "Hello there! I would like to acquire 'cards'."

    clerk "For your  grandchild? What exactly do they like?" 
    frank "Uhh no... I don't even have children. In fact, I'm glad I am still married I'll tell you that hehe."
    clerk "In that case... Which ones exactly? We have Byssmon, Digihell Live, Aurafarmers and Uno Boosters."
    frank "B-Boosters? I think you misunderstood me. I am looking for 'cards'!"
    clerk "Yeah like I said, we have Byssmon..."
    frank "Cardboard. About the size of a credit card. You know. To play and collect."
    clerk "Yes exactly we have a huge assortment of different boosters to acquire."
    frank "TRADING CARDS! Do you have them?"
    clerk "Here!"
    "Frank is handed some booster boxes."
    frank "Those are boxes... I am looking for"
    clerk "Yes. You need to rip open the boosters and then you get your cards."
    frank "Uhh... Is that the new fun thing to do? Seems like a waste of time and money to me."
    clerk "Just try it sir. You'll see!"
    "Which Boosters does Frank want to open?"
    jump scene_tcg_choice

label scene_tcg_choice:
    menu:
        "Byssmon":
            "Frank opens up Byssmon Boosters."
            $ randfloat = renpy.random.random()
            if randfloat < 0.25:
                clerk "Tough Luck. You just pulled bulk."
                frank "Damn it!"
                "Frank is infuriated, but his thirst has not been quenched."   
                jump scene_tcg_choice
            elif randfloat< 0.5:
                clerk "OH! That's nice! A Reverse Holo Refi! We only have like 400 of those in the community binder."
                frank "Damn it!"
                "Frank is infuriated, but his thirst has not been quenched."   
                jump scene_tcg_choice
            elif randfloat < 0.75:
                show tgc business card at top
                clerk "A limited edition Marriage Councellor of the Abyss card."
                frank "HEY! That's just the guys business card! What the hell!"
                "Frank is infuriated, but his thirst has not been quenched."   
                hide tgc business card
                show tgc 2 at top
                jump scene_tcg_choice
            else:
                clerk "Oh Sorry! We don't have any left... I can offer you some Digihell Boosters for the same prize though."
                clerk "There you go!"
                jump scene_tcg_digihell
        "Digihell Live":
            jump scene_tcg_digihell
        "Aurafarmers":
            "Frank opens up an Aurafarmer Booster."
            clerk "Sorry we have only one left."
            frank "That's fine."
            "Frank rips up the pack."
            show tgc mr cheezt at top
            frank "WOAH That looks like a great card! Mr.Cheezt Full ART! And a signature?!"
            clerk "Ugh... Go figure... It's yet another fake pack... Lots of scalpers nowadays, selling fake packs even to stores."
            frank "But I bought it off of you. Aren't you a store? How the hell do you get fake packs?"
            clerk "I'm sorry sir! But take a look at that signature. That's clearly been added before the printing. So it is not a legit card."
            frank "What a scam..."
            clerk "Yeah, it is quite sad. Here let me make it up to you with a box of Digihell Live Boosters."
            hide tgc mr cheezt
            show tgc 2 at top
            jump scene_tcg_digihell
        "Uno":
            show tgc uno opening at top
            "Frank opens up Uno Boosters"
            hide tgc uno opening
            $ randfloat = renpy.random.random()
            if  randfloat > 0.50:
                clerk "OH! That's fun! You just opened up a Draw Four! That's rare! They even have a collab with Digihell Live right now."
                frank "Uhh meaning?"
                clerk "Whenever you draw a Draw Four, you are entitled to a Digihell Live Booster box."
                frank "I feel like that is just a convenient way to get me to open Digihell Live Boosters."
                clerk "They are worth it, trust me. Here you go!"
                jump scene_tcg_digihell
            else:
                frank "Wait.... Why am I even doing this? Why do you have Uno Booster Boxes?"
                clerk "They are really popular. They released a new color recently."
                frank "But... That does not ewven change the game! It is still Uno!"
                clerk "Yeah. They really did a good job with balancing the new cards."
                frank "Thats BECAUSE it it still just Uno!"
                "Frank is infuriated, but his thirst has not been quenched."   
                jump scene_tcg_choice                         

label scene_tcg_end:
    $ ready_tcg = False
    jump scene_room

label scene_tcg_digihell:
    "Frank takes an awkward amount of time to open the Digihell Live packs."
    teen_1 "Hey that old guy is shredding up some  FAC!"
    "A group of teenagers gathers around him and opens the other 23 packs left inside the box, before he is even able to open his own."
    teen_1 "Wow sir, that is the worst box I have seen anyone pull in here!"
    teen_2 "Wait I still need this Tentacle Slap card for my FireAnt-Chan deck. Can I have this sir?"
    frank "I uhh.."
    teen_2 "Thanks!"
    teen_3 "Come on!!! Just open the pack old man! Do you have arthritis or what?!"
    clerk "Sir... Other customers want to buy cards as well. Could you please hurry up?"

    # show karten hier
    show tgc pack opening at top
    pause
    show tgc pack opening 2 at top
    pause
    frank "Well that was a dissapointment..."
    teen_1 "OH MY GOD YOU PULLED THE FIREANT-CHAN SPECIAL ILLUSTRATION RARE AS A STARLIGHT RARE?!"
    teen_3 "Wait I need that! Please! I'll give you my whole Aurafarmers collection. Even the sealed boosters from 15 years ago."
    teen_2 "Totally BANK! Pesto'ed pull. Completely parmesan'd. Old man has all the cheese! Old man Aura!"
    frank "What are you even talking about? I just did the most menial task known to mankind. Opening a pack of something!"
    teen_1 "Oh my god he doesn't know!"
    teen_2 "He lacking that critical shred. That's not Gouda."

    "Frank is quickly surrounded by the teenagers. He needs to go find a way to get out of the shop. This is becoming ridiculous!"
    hide tgc pack opening 2
    hide tgc pack opening
    show tgc 2 at top
    jump scene_tcg_survive

label scene_tcg_survive:
    menu:
        "Hit the teenagers":
            define tim = Character("Tim")
            "Frank thinks about just hitting the teenagers and quickly running out of the shop. They would never see it coming!"
            tim "Actually. You are not allowed to do that?"
            frank "What do you mean I can not do that?"
            tim "You just simply can't you have sworn an oath."
            frank "Oath? What kind of oath?"
            tim "You are a doctor. You have sworn a hippocratic oath."
            frank "That's not how it works."
            tim "That is exactly how it works."
            frank "It really is not. I have a doctorate in taxes..."
            tim "No. You can't do this because of your oath. The end. Epic."
            show tgc hypokratischer eid at top
            pause
            return
        "Bend the Card":
            "After what feels like an eternity of getting 'cheesed out' by the teenagers, Frank bursts out in anger."
            frank "ENOUGH IS ENOUGH!"
            frank "This is just cardboard!"
            "Frank takes the card...."
            show tgc card bend 1 at top
            # show epic
            "And bends it in front of the teenagers!"
            show tgc card bend 2 at top
            teen_1 "NOOOOOOOOOOOOOOOOOOOOO!!!!!!"
            teen_2 "WHY WOULD YOU DO THAT?! ITS THE BEST CARD IN THE SET!"
            teen_3 "These feelings of emptyness... Like a Cheese full of holes.... I hate you old man."
            "Content with how thinks turned out, Frank goes back home, knowing full well, that these new Trading Card Games are bad anyways."
            frank "In my days, you could just buy a deck of cards and have fun with it."
            jump scene_tcg_end
        "Play a game of Uno to get out":
            frank "You know what? How about we play a game of Uno. And when I win, I can just go home. If I lose, winner gets the card."
            teen_1 "You can cheese your ass I'm taking up that offer."
            teen_2 "Brie it on old man!"
            teen_3 "It's time to bring out the new cards."
            "The game starts. Frank is pretty happy about his hand."
            "A few Draw 2. Even a Wild Card. He's got this!"
            "..."
            "....."
            "......."
            ".........."
            "Frank finds himself with 25 cards in hand, a lost turn and three 'UNO' calls before even having a first turn."
            frank "This.... This is not the Uno I remember."
            teen_1 "You need to get with the times old man!"
            teen_2 "Playing the OG RGBY layup. Did you really think that stuff holds up in the modern meta?"
            frank "What do you mean modern meta? This is UNO!"
            teen_3 "Anyways. I'm gonna hit you with a purple Draw Fourty-Six. Since a Purple 6 is on the stack right now, you are also unable to play for the next 6 turns."
            "Frank finds himself in a bit of a UNO pickle..."
            # epic stunlock
            show tgc gameover 2 at top
            pause
            return
        "Trade your way out":
            "Frank tried his best to trasde his way out of his dilemma."
            "He ends up selling all the stuff he trades to the store, just to buy more Digihell Live Boosters just for the heck of it."
            "Eventually he opens up yet another FireAnt-Chan Special Illustration Rare and is surrounded by even more teenagers now."
            jump scene_tcg_survive
