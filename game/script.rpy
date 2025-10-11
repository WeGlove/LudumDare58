# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define frank = Character("Frank Bankmayer")
define checked_tcg = False
define checked_hangover = False
define checked_vtuber = False
define checked_uviolatedthelaw = False
define everything_reminded = False


# The game starts here.

label start:

    jump scene_intro

    return
