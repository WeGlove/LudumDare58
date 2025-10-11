define deliverer = Character("Delivery Driver")
define buddha = Character("Budhha")
define tiger = Character("Tiger")


label scene_hangover:
    $ checked_hangover = True

    $ hangover_frank = False
    $ hangover_frank_state = -1
    $ hangover_window = False
    $ hangover_buddha = False
    $ hangover_NK = False
    $ hangover_alc = False
    $ hangover_art = False
    $ hangover_car = False

    scene bg black
    "Hmm let me remember"

    #show blurry

    "Yes I know I was thinking..."

    show hangover 1

    frank "Oh god, I feel like I am about to live"

    frank "What happened here?"
    frank "and where is my..."
    frank "oh {b}NO{/b}" # pause hier zwischen
    frank "Where the hell is the USB drive with all the customer data!?"

    frank "I would literally go to hell for that"
    frank "I still don't have a backup!"

    hide hangover 1
    show bg black

    "The developers of the game would like to deliver a message to you."

    "Would you like to see it?"
    menu:
        "Yes":
            "Very good!"
        "No":
            "To bad!"

    "Do you feel lonley in your life?"
    "Did you not achieve what your second cousin's girlfriend expected of you?"
    "Did you accidetally put on {b}2{/b} pairs of underpants this morning?"

    "Then we have the cure for you!"

    show ad_break

    "Create a much better life for yourself by helping Frank Bankmayer get his Kundendaten USB Stick in the previous game"
    "wow"
    "amazing"
    "great"
    "epic"
    "wonderful"
    "literally the best thing ever"
    "wow"

    hide ad_break

    show bg black

    "Thank you for listening to our message!"
    "Now where were we?"
    "Ah yes, Frank and drugs!"

    hide bg black

    show hangover 1

    label hang_menu:
    frank "Now where do I look?"
    menu:
        "The Car" if not hangover_car:
            "There is car sticking out half the building"
                
            if not hangover_frank:
                "A man is inside and seems to be pretending to be asleep"
                frank "Yeah, I look terrible, maybe I should clean myself up first"
            else:
                "A man is inside and seems to be pretending to be asleep"
                frank "Hey, are you alright"
                "Frank tugs at the man"
                "He opens his eyes slowly"
                frank "Can I help you?"
                "The man jolts into a working posture"
                "The car rocks concerningly"
                deliverer "Here is your food sir! One Ramen Special (Limited Edition)! Thank you for ordering at Refi's Ramen Restaurant"
                "He hold out a box with food."
                "It seems cold"
                frank "Uh, yeah thanks"
                if hangover_frank_state == 0:
                    deliverer "Your eyes seem to be red sir, are you alright?"
                elif hangover_frank_state == 1:
                    deliverer "Excuse me sir, but you rather smell of beer"
                elif hangover_frank_state == 2:
                    deliverer "Oh, I just noticed you are wearing the bathrobe inverted"
                else:
                    ""
                "The weight of the car shifts slightly, it begins to fall"
                menu:
                    "Try extending a hand":
                        "Frank tried to extend a hand but is not fast enough. The car falls out of the building"
                        show hangover 5
                        ""
                        show hangover 6
                        ""
                        buddha "The universe wanted this. Death is part of life, never save anyone"
                    "Don't":
                        "The car falls out of the building"
                        show hangover 5
                        ""
                        show hangover 6
                        ""
                        buddha "You were correct to do this, he will be reincarnated into a better life"
                frank "What?"
                buddha "..."
                frank "But that reminds me, I remember something about the statue."
                frank "If only I could get myself into the same state as last night"
                if hangover_alc:
                    frank "Wait I have the expensive alcohol! I should try to go to the statue!"
                $ hangover_car = True

        "Yourself" if not hangover_frank:
            "Frank finds himself to have bought a limited edition Gucci bathrob lined in black lined with real gold threads"
            "He is currently rocking a Mohawk and has a dollar sign tatooed on his face."
            frank "Well this could have gone worse."
            frank "Best to clean myself up a bit"
            frank "What should I do?"

            menu:
                "Cover Tattoo with flour that is lying around for some reason":
                    frank "Crap that wasn't flour"
                    show hangover 4
                    frank "..."
                    show  hangover 1
                    frank "woah"
                    $ hangover_frank_state = 0
                "Try to comb the Mowahwk using beer":
                    frank "Well it didn't do much for the color..."
                    frank "but this is at least..."
                    frank "wait"
                    frank "How did I get hair in the first place, I am bald!?"
                    $ hangover_frank_state = 1
                "Wear the barthrobe on the inside to conceal wealth":
                    frank "Doesn't look as good, but I guess"
                    $ hangover_frank_state = 2

            $ hangover_frank = True
        "Alcohol" if not hangover_alc:
            frank "I remember there was a really good bottle of something some here"
            frank "But..."
            "No, I am not making another one of these dumb interactions."
            "Here you go Frank, gift from above, an expensive bottle of blueberry licour, your favorite."
            frank "Thank you, glad I reandomly found this."
            $ hangover_alc = True
        "Broken Window":
            "You can here shuffeling outside, but the window is locked."
            if hangover_buddha:
                "The window unlocks using the key."
                "Frank looks outside"
                jump hang_tiger
            else:
                frank "I wonder if there is a key around?"
        "North Korea?" if not hangover_NK:
            frank "The glorious North Korean flag."
            frank "If you are privately insured, you really can get anywhere!"
            $ hangover_NK = True
        "Buddha" if not hangover_buddha:
            if hangover_car and hangover_alc:
                "Holding the bottle of alcohol and the food you ordered in hand you remember the event of last night."
                "You put the key under the statue because you really didn't want to open the window for some reason"
                $ hangover_buddha  = True
            elif hangover_car:
                frank "I seem to remember something about this statue, if only I had sometihg to remind me of yesterday."
            else:
                "A statue of Buddha"
                "You kind of feel bad now"
        "The Mona Lisa" if not hangover_art:
            frank "A priceless art piece, at least my good taste did not leave while getting drunk!"
            frank "Is that a mustache?"
            $ hangover_art = True
    jump hang_menu

    label hang_tiger:
    show hangover 2
    "Instead of water a tiger apces around the luxiouriouus hotel pool"
    frank "Wait, ist that!?"
    show hangover 3

    frank "The USB stick!"

    frank "But how do I get it!"
    menu:
        "Throw the statue at him":
            buddha "Catch, motherfucker!"
            "The statue shatters the tigers skull..."
            "And the USB drive"
            show hangover gameover 2
            return 
        "Get into hand to hand combat":
            frank "You aren't tougher than my wife"
            frank "Let's dance"
            show hangover gameover
            "But Frank was a deathly ill man in his fifties"
            "The End"
            return
        "Try distracting it with the cold Ramen Special (Limited Edition)!":
            "The ramen splatters on the tigers head."
            "It is now a lot angrier."
            "It pounces on Frank!"
            show hangover gameover
            "The End"
            return
        "Throw the flag at it!":
            "The tiger salutes the flag."
            "Frank sucessfully snatches his data from the tigers collar"
        "Show it the Mona Lisa":
            tiger "Truly a great work of art."
            tiger "While I was upset about being stolen from my enclosure at the zoo last night,"
            tiger "I have now come to understand that anger will not help resolve my situation."
            tiger "I noticed you talking about my USB drive"
            tiger "I don't know why you straped it to my collar in the first place, but you can have it back"
            tiger "Have a nice day sir!"
            frank "Thank you!"

    $ ready_hangover = False
    jump scene_room