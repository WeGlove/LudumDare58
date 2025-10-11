label scene_vtuber:

    define vtuber = Character("VTuber")
    define chatter = Character("Some random chatter")
    $ v_love = True
    $ v_million = True
    $ v_feet = True
    $ v_die = True
    $ v_dollar_a = True
    $ v_food = True
    $ v_blood = True

    $ attention_points = 0

    frank "What else could I be spending my money on"
    frank "Oh I know, I could donate to the computer television woman!"
    frank "I have to get her attention!"

    show v tuber normal
    vtuber "Hiya evryone, it's FireAnt-chan!!"

    label ChatLoop:
    
    frank "What should i write?"

    menu:
        "I love you" if v_love:
            vtuber "Aww how cute, thank you!"
            $ v_love = False
            $ attention_points += 1
        "Donate 1000000 dollars" if v_million and attention_points > 2 and not v_dollar_a:
            show v tuber confused
            vtuber "Did someone just donate..."
            vtuber "A {b}MILLION{/b} dollars!?"
            vtuber "Can you aford that"
            frank "My wife doesn't mind..."
            $ v_million = False
            jump VTuber_Out
        "Show feet pls" if v_feet:
            show v tuber mad
            vtuber "No."
            vtuber "Mods?"
            show v tuber game over 1
            "Frank Bankmayer was banned from the chat."
            "The End."
            return
        "I am about to die" if v_die:
            show v tuber confused
            vtuber "You are what?"
            show v tuber sad
            vtuber "Poor bankm4y3r, what illness do you have?"
            frank "An unspecified one"
            vtuber "That's the most lethal kind!"
            vtuber "I hope you are doing better soon"
            $ v_die = False
            $ attention_points += 1
        "Donate a dollar" if v_dollar_a:
            "She completeley ignores the donation, because a rock in the game she is playing looks a little like a funny face."
            $ v_dollar_a = False
        "What is your favorite food" if v_food:
            vtuber "Chat somebody is asking what my favorite food is"
            vtuber "Is it bad that it is just plain rice crackers?"
            chatter "That's not Gouda!"
            chatter "completely lost lol"
            $ v_food = False
        "What is your blood type" if v_blood:
            vtuber "My favorite blood type"
            vtuber "Dairy"
            "The chat goes wild after that"
            frank "I really don't get the youth sometimes."
            $ v_blood = False
        "I am Completely parmeseaned, totally Pestoed out!":
            chatter "Cringe"

    jump ChatLoop

    label VTuber_Out:

    vtuber "Chat this can't go on like this..."

    show v tuber transition 
    "I am ..."
    show v tuber wife
    vtuber "Bankm4y3rs wife"
    frank "..."
    vtuber "I will sue you out of all your money"

    scene bg black

    frank "All according to plan!"

    $ ready_vtuber = False
    jump scene_room