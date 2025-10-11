label scene_vtuber:

    define vtuber = Character("VTuber")
    $ v_love = True
    $ v_million = True
    $ v_feet = True
    $ v_die = True

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
            v_love = False
        "Donate 1000000 dollars" if v_million:
            show v tuber confused
            vtuber "Did someone just donate..."
            vtuber "A {b}MILLION{/b} dollars!?"
            vtuber "Can you aford that"
            frank "My wife doesn't mind..."
            v_million = False
            jump VTuber_Out
        "Show feet pls" if v_feet:
            show v tuber mad
            vtuber "No."
            v_feet = False
        "I am about to die" if v_die:
            show v tuber confused
            vtuber "You are what?"
            show v tuber sad
            vtuber "Poor bankm4y3r, what illness do you have?"
            frank "An unspecified one"
            vtuber "That's the most lethal kind!"
            vtuber "I hope you are doing better soon"
            v_die = False
            
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