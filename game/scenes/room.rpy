init:
    transform customzoom:
        zoom 0.8
label scene_room:
    # Check if window should be opened
    $ everything_reminded = not any([ready_hangover, ready_tcg, ready_uviolatedthelaw, ready_vtuber])
    default sensitive_tcg = True
    default sensitive_hangover = True
    default sensitive_uviolatedthelaw = True
    default sensitive_vtuber = True
    screen screen_room():
        imagebutton:
            id "tcg"
            xpos 0.1
            ypos 0.1
            auto "placeholder_%s.jpg"
            action Jump("goto_scene_tcg")
            tooltip "Frank embarked on a trading card adventure"
            hovered GetTooltip()
            sensitive sensitive_tcg
            at customzoom
        imagebutton:
            xpos 0.6
            ypos 0.6
            auto "placeholder_%s.jpg"
            action Jump("goto_scene_hangover")
            tooltip "How did this get here?"
            hovered GetTooltip()
            sensitive sensitive_hangover
            at customzoom
        imagebutton:
            xpos 0.1
            ypos 0.6
            auto "placeholder_%s.jpg"
            action Jump("goto_scene_vtuber")
            tooltip "Frank spend massive amounts of money on vtubers"
            hovered GetTooltip()
            sensitive sensitive_vtuber
            at customzoom
        imagebutton:
            xpos 0.6
            ypos 0.1
            auto "placeholder_%s.jpg"
            action Jump("goto_scene_uviolatedthelaw")
            tooltip "Violating the Law felt like a good idea"
            hovered GetTooltip()
            sensitive sensitive_uviolatedthelaw
            at customzoom
        if everything_reminded:
            imagebutton:
                xpos 0.3
                ypos 0.3
                auto "placeholder_%s.jpg"
                action Jump("scene_window")
                tooltip "There is only one thing left to do..."
                hovered GetTooltip()

# Tooltipping Logic for the hover events
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]"
# Finally Call the screen
    call screen screen_room

# Jump Logic to disable the Screen Buttons on interaction
    label goto_scene_tcg:
        $ sensitive_tcg = False
        jump scene_tcg
    label goto_scene_hangover:
        $ sensitive_hangover = False
        jump scene_hangover
    label goto_scene_vtuber:
        $ sensitive_vtuber = False
        jump scene_vtuber
    label goto_scene_uviolatedthelaw:
        $ sensitive_uviolatedthelaw = False
        jump scene_uviolatedthelaw