# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[name]", image="eden",color="#44caff")
define a = Character("Grace", image="grace")
define v = Character("Eva", image="eva")
define m = Character("Mason", image="mason")
define x = Character("Xavier", image="xavier")

image define eden = "side eden.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # These display lines of dialogue.

    #id card moment
    $ name = renpy.input("Enter your name:", default = "Eden", length = 10) 
    if not name:
        $ name = "Eden"

    "*BEEP BEEP*"
    e "..."

    scene bg room

    #blinking or something
    show black with dissolve
    pause 0.1
    hide black with dissolve
    pause 0.1
    show black with dissolve
    pause 0.1
    hide black with dissolve

    

    e "(Today's the first day of senior year.)"
    e "(I almost forgot...)"
    e "(I should probably get to class.)"

    "I rolled out of bed and began my usual school morning routine that felt all too familiar at this point."
    "After a few bites of breakfast, I got on my bike and rode to school, trying not to start my final year of high school tardy."

    # possible game play
    #^^^^^ ts is so ass definitely rewrite all this later

    scene bg homeroom
    #classroom chatter
    e "(I made it in time for homeroom...)"
    e "(Thank goodness...)"

    "Before I could make it to my seat, I was stopped by the homeroom teacher."

    Character("Teacher") "[name], can I speak with you for a second?"
    e "?"
    Character("Teacher") "The principal would like to see you in his office."
    Character("Teacher") "You're excused from homeroom. You won't be missing anything important."

    e "Uh, okay..."
    #walking away
    scene bg hallway
    e "(Am I in trouble? I don't think I should be...)"
    e "(I guess I'll go anyway.)"

    "The principal's office was pretty close by, so I made it there quickly."
    "I took a deep breath and knocked on the door."

    scene bg office

    "to my surprise, "







    # This ends the game.

    return
