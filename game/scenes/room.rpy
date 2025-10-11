init:
    transform tcg_transform:
        xzoom 0.2
        yzoom 0.2
    transform hangover_transform:
        xzoom 0.45
        yzoom 0.45
    transform vtuber_transform:
        xzoom 0.2
        yzoom 0.2
    transform window_transform:
        xzoom 0.4
        yzoom 0.4
label scene_room:
    scene frank room background
    # Check if window should be opened
    $ everything_reminded = not any([ready_hangover, ready_tcg, ready_vtuber])
    default sensitive_tcg = True
    default sensitive_hangover = True
    default sensitive_vtuber = True
    default sensitive_window = False
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
            at tcg_transform
        imagebutton:
            xpos 0.4
            ypos 0.65
            auto "tiger_%s.png"
            action Jump("goto_scene_hangover")
            tooltip "How did this get here?"
            hovered GetTooltip()
            sensitive sensitive_hangover
            at hangover_transform
        imagebutton:
            xpos 0.1
            ypos 0.6
            auto "poster_%s.png"
            action Jump("goto_scene_vtuber")
            tooltip "Frank spend massive amounts of money on vtubers"
            hovered GetTooltip()
            sensitive sensitive_vtuber
            at vtuber_transform
        imagebutton:
            xpos 0.6
            ypos 0.2
            auto "window_%s.png"
            action Jump("scene_window")
            tooltip "There is only one thing left to do..."
            hovered GetTooltip()
            sensitive sensitive_window
            at window_transform

# Tooltipping Logic for the hover events
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]"
# Finally Call the screen
    call screen screen_room

# Jump Logic to disable the Screen Buttons on interaction
    label goto_scene_tcg:
        $ sensitive_tcg = False
        $ sensitive_window = not any([sensitive_hangover, sensitive_tcg, sensitive_vtuber])
        jump scene_tcg
    label goto_scene_hangover:
        $ sensitive_hangover = False
        $ sensitive_window = not any([sensitive_hangover, sensitive_tcg, sensitive_vtuber])
        jump scene_hangover
    label goto_scene_vtuber:
        $ sensitive_vtuber = False
        $ sensitive_window = not any([sensitive_hangover, sensitive_tcg, sensitive_vtuber])
        jump scene_vtuber