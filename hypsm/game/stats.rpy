init python:
    class Student:
        def __init__ (self, name = "", birthday = "", height = "", likes = "", dislikes ="", relationship = 0, imageName =""):
            self.name = name
            self.birthday = birthday
            self.height = height
            self.likes = likes
            self.dislikes = dislikes
            self.relationship = relationship
            self.imageName = "images/" + imageName + ".png"

default mc_stats = Student(name="[name]", birthday="April 1st", height="64in.", likes = "???", dislikes = "???", relationship = 0, imageName ="eden")

default ruby_stats = Student(name="Ruby Hartford", birthday="May 8th", height="67in.", likes = "???", dislikes = "???", relationship = 0, imageName ="ruby")
default eva_stats = Student(name="Eva Schafer", birthday="August 27th", height="65in.", likes = "???", dislikes = "???", relationship = 0, imageName ="eva")
default mason_stats = Student(name="Mason Espinoza", birthday="June 1st", height="63in.", likes = "???", dislikes = "???", relationship = 0, imageName ="mason")
default xavier_stats = Student(name="Xavier Lim", birthday="November 14th", height="70in.", likes = "???", dislikes = "???", relationship = 0, imageName ="xavier")

default selectedCharacter = mc_stats

screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("character_screen")

screen character_screen():
    tag character_screen_tag
    add "UI/bg.png"
    hbox:
        #left frame
        frame:
            background "UI/statsbg.png"
            style_prefix "character"
            ysize 1080
            xsize 640
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton _(mc_stats.name):
                    action SetVariable ("selectedCharacter", mc_stats)
                    xsize 640
                textbutton _(ruby_stats.name):
                    action SetVariable ("selectedCharacter", ruby_stats)
                    xsize 640
                textbutton _(eva_stats.name):
                    action SetVariable ("selectedCharacter", eva_stats)
                    xsize 640
                textbutton _(mason_stats.name):
                    action SetVariable ("selectedCharacter", mason_stats)
                    xsize 640
                textbutton _(xavier_stats.name):
                    action SetVariable ("selectedCharacter", xavier_stats)
                    xsize 640
                textbutton _("Return"):
                    yoffset 10
                    xsize 640
                    action Return()
        
        #right frame
        frame:
            $ CharName = selectedCharacter.name
            $ CharBday = selectedCharacter.birthday
            $ CharHeight =selectedCharacter.height
            $ CharLikes = selectedCharacter.likes
            $ CharDislikes = selectedCharacter.dislikes
            $ CharRelationship = selectedCharacter.relationship
            background None
            ysize 1080
            xsize 1280
            vbox:
                xalign 0.5
                xsize 600
                xoffset -300
                yoffset 200
                spacing 20
                if selectedCharacter == mc_stats:
                    text "{b}[name]{/b}"
                    text "Birthday: April 1st"
                else:
                    text "{b}[CharName]{/b}"
                    text "{b}Birthday:{/b} [CharBday]"
                    text "{b}Height:{/b} [CharHeight]"
                    text "{b}Likes: {/b}[CharLikes]"
                    text "{b}Dislikes: {/b}[CharDislikes]"
                    hbox: 
                        spacing 20
                        text "{b}Relationship{/b}"
                        bar value StaticValue(selectedCharacter.relationship, 10) xsize 300 yalign 0.75
            add selectedCharacter.imageName xalign 1.0 yalign 0.5

style character_button_text:
    xalign 0.5



