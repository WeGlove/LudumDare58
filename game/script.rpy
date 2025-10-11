# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define frank = Character("Frank Bankmayer")
define ready_tcg = True
define ready_hangover = True
define ready_vtuber = True
define ready_uviolatedthelaw = True
define everything_reminded = False


# The game starts here.

label start:

    jump scene_intro

    return
