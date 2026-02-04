# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character("MC", phone.asset("mc_icon.png"), "mc", 35, "#484848")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "mon", 40, "#0a0")
default pc_natsuki = phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")

default pc_eden = phone.character.Character("[name]", phone.asset("side eden.png"), "e", 10, "#80c39a")
default pc_eva = phone.character.Character("Eva", phone.asset("eva pfp.png"), "v", 11, "#36d7ff")
default pc_ruby = phone.character.Character("Ruby", phone.asset("ruby pfp.png"), "r", 12, "#B2493F")
default pc_mason = phone.character.Character("Mason", phone.asset("mason pfp.png"), "m", 13, "#BE9DE8")
default pc_xavier = phone.character.Character("Xavier", phone.asset("xavier pfp.png"), "x", 14, "#363636")


define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mc = Character("MC", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

default pov_key = "e"

init python:
    import datetime

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Eva":
        add "v" add "e"
        icon "eva pfp.png" key "EvaChat"

default group_chat = phone.group_chat.GroupChat("GC", phone.asset("default_icon.png"), "GC").add_character("x").add_character("r").add_character("v").add_character("m").add_character("e")


init phone register:
    define "Welcome":
        add "s" add "mc" add "y" add "m" add "n" 
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"


label eva1:
    $ phone.system.date = datetime.datetime(year=2025, day=15, month=8, hour=2, minute=56)
    phone discussion "EvaChat":
        time hour 2 minute 56
        "v" "Hey [name], it's Eva"
        "v" "We're in Library Meeting Room B"
    phone end discussion

    return

label GC1:
    $ pov_key = "e"
    $ phone.system.date = datetime.datetime(year=2025, day=15, month=8, hour=8, minute=24)
    phone discussion "GC":
        label "'Ruby' added 'Eva' to the group" delay -1
        label "'Ruby' added 'Mason' to the group" delay -1
        label "'Ruby' added 'Xavier' to the group" delay -1
        label "'Ruby' added '[name]' to the group" delay -1
        "e" "hi"
        "r" "hi"
        "v" "hi"
        "m" "hi"
        "x" "hi"

    phone end discussion    
    return



label phone_discussion_test:
    phone discussion "ddu":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
        label "'Sayori' has been added to the group" delay -1
        label "'MC' has been added to the group" delay -1
        label "'Yuri' has been added to the group" delay -1
        label "'Monika' has been added to the group" delay -1
        label "'Natsuki' has been added to the group" delay 0.2
        "m" "Hey there!"
        "n" "Thank you for using my framework."
        "n" "I mean {i}of course{/i} you're using {b}this{/b} framework."
        "n" "...not like there are any better ones out there~"
        "s" "natsuki!!!!! {emoji=EllenScream}"
        "s" "no being a meanie!!!!!!!{emoji=EllenScream}{emoji=EllenScream}{emoji=EllenScream}"
        "y" "If you are interested in DDLC mods, be sure to check out our mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}! {emoji=Melody}"
        "mc" "In case you encounter an issue (or wanna make a suggestion),"
        "mc" "you can:"
        "mc" "DM me at {i}elckarow{/i} on Discord,"
        "mc" "open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a},"
        "mc" "make a post on the phone's {a=https://elckarow.itch.io/better-emr-phone}Itch page{/a}."
        "s" "Happy coding!" 
    phone end discussion

    return

label phone_call_test:
    phone call "s"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_mc "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."

    return