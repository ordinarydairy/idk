screen contract(show_name=False):
    viewport:
        add "contract.png"
        pos (500,30)
        xysize (1200,4181)
        child_size (1200, 4200)
        scrollbars "vertical"
        mousewheel True
        draggable True
   
        imagebutton:
            xpos 150
            ypos 3750
            idle "signatureidle"
            tooltip [name]

            action Return()
        
        $ tooltip = GetTooltip()
        if tooltip:
            text tooltip pos (180, 3810)color "#000"

screen project1:
    viewport:
        add "contract.png"
        pos (500,30)
        xysize (1000,1000)
        child_size (700,2000)
        scrollbars "vertical"
        mousewheel True
        draggable True
        vbox:
            text "Hi"
            text "Hello"
        imagebutton:
            xpos 50
            ypos 1100
            idle "building1.png"
            hover "building2.png"
            action Return()