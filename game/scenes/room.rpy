label scene_room:
    # Check if window should be opened
    $ everything_reminded = all([checked_hangover, checked_tcg, checked_uviolatedthelaw, checked_vtuber])
    
    screen screen_room():
        imagebutton:
            id "tcg"
            xpos 0.2
            ypos 0.2
            auto "placeholder_%s.jpg"
            action Jump("scene_tcg")
            tooltip "Frank embarked on a trading card adventure"
            hovered GetTooltip()
            sensitive not checked_tcg
        imagebutton:
            xpos 0.8
            ypos 0.8
            auto "placeholder_%s.jpg"
            action Jump("scene_hangover")
            tooltip "How did this get here?"
            hovered GetTooltip()
            sensitive not checked_hangover
        imagebutton:
            xpos 0.2
            ypos 0.8
            auto "placeholder_%s.jpg"
            action Jump("scene_vtuber")
            tooltip "Frank spend massive amounts of money on vtubers"
            hovered GetTooltip()
            sensitive not checked_vtuber
        imagebutton:
            xpos 0.8
            ypos 0.2
            auto "placeholder_%s.jpg"
            action Jump("scene_uviolatedthelaw")
            tooltip "Violating the Law felt like a good idea"
            hovered GetTooltip()
            sensitive not checked_uviolatedthelaw
        if everything_reminded:
            imagebutton:
                xpos 0.5
                ypos 0.5
                auto "placeholder_%s.jpg"
                action Jump("scene_window")
                tooltip "There is only one thing left to do..."
                hovered GetTooltip()

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]"
    call screen screen_room
