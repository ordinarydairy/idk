# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[name]", image="eden",color="#ADA97A")
define r = Character("Ruby", image="ruby", color="#B2493F")
define v = Character("Eva", image="eva", color="#9AD2D8")
define m = Character("Mason", image="mason", color="#BE9DE8")
define x = Character("Xavier", image="xavier", color="#EBC38F")

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

    "What does it mean to be successful?"
    "Is it "

#monday
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

    #more walking
    e "(...Where's the principal's office again?)"
    "I realized that I'd never been called to the principal's office before."
    "I almost got lost a few times, but eventually arrived at my destination."
    "Taking a deep breath, I knocked on the door."

    scene bg office
#also note to self!!!!!! make sure to establish competetivyness more so the tone shift isnt as crazy
    transform middleleft:
        xpos 400
        ypos 60

    transform middleright:
        xpos 800
        ypos 60
    transform short.middleright:
        xpos 800
        ypos 50


    show ruby at left
    show eva at middleleft
        
    show mason at short.middleright
    show xavier at right
    with dissolve


    "To my surprise, four other students, along with the principal, were there inside the office."
    "They turned as if they had been waiting for me."

    hide eva
    hide mason
    hide xavier

    show ruby at center
    with move
    Character("Girl With Red Bow") "Took you long enough."
    hide ruby

    Character("Principal") "Ah, [name]. Have a seat."


    #interlude narration here that i didn't think of yet


    Character("Principal") "Now that everyone is settled, let's get started."
    Character("Principal") "I know you're probably all wondering why I've gathered you here today."
    Character("Principal") "As you may or may not have heard..."
    Character("Principal") "Every year, our school takes part in a special academic program. Only a few schools in the country are selected for it."
    Character("Principal") "It is called... {p}the{b} Ivy Gate Initiative. {/b}"

    show mason at center
    Character("Clean-cut Boy") "No way...that Ivy Gate thing is real?!"
    hide mason
    show eva at center
    Character("Girl") "The rumors really were true..."
    hide eva

    Character("Principal") "The Ivy Gate Initiative is a multi-week scholarship and admissions challenge."
    Character("Principal") "It is designed to identify students who can do more than score highly on exams."
    Character("Principal") "The five highest-ranking students from each school will work together to complete a series of tasks and projects over the course of six weeks."
    Character("Principal") "The initiative offers winners a {b}full scholarship{/b} and {b}guaranteed admission offers{/b} to any top 10 university in the United States."
    Character("Principal") "And that is where you come in."

    #interlude

    
    Character("Principal") "Your team performance will allow the school to place higher in the challengeand boost our reputation"
    
    #waiit i have an idea what if he doesn't tell them that its individual until later....

    #Character("Principal") "But, at the end of the program..."
    #Character("Principal") "Only a limited amount of scholarships will be awarded."
    #Character("Principal") "The final scholarships and admission offers will only be made to individuals, not the entire team."
    #Character("Principal") "However, I must emphasize the importance in teamwork and group bonding in situations like these!"
    
    #more exposition that i was thinking about lst night but completely forgor

    #also maybe theres a contract that you need to sign

    Character("Principal") "Now, feel free to stay here and chat amongst yourselves until the bell rings."
    #principal disappearing animation
    
    default officetalks = 0

    define talktoruby = False
    define talktoeva = False
    define talktomason = False
    define talktoxavier = False

    label officetalk:  
        transform middleleft:
            xpos 400
            ypos 60

        transform middleright:
            xpos 800
            ypos 60
        transform short.middleright:
            xpos 800
            ypos 50  

        show ruby at left
        show eva at middleleft
        
        show mason at short.middleright
        show xavier at right
        with dissolve

        menu officetalkmenu:
            "(What should I do?)"

            "Talk to Ruby":
                if talktoruby == True:
                    e "(We already talked. Maybe I should try talking to someone else?)"
                    jump officetalk
                else:
                    hide eva
                    hide mason
                    hide xavier
                    show ruby at center
                    with move

                    r "You do know punctuality is paramount to success, right?"
                    e "...I'm sorry, what?"
                    r "We spent over five minutes waiting for you today. Does the phrase {i}as soon as possible{/i} mean anything to you?"
                    e "(It's just five minutes...)"
                    e "Sorry, I got lost..."
                    r "*sigh*"
                    r "Since we're already talking to each other, I suppose we should introduce ourselves."
                    r "I'm {b}Ruby Hartford{/b}."
                    e "I'm [name]."
                    hide ruby
                    #cg possibly
                    "I was in the same geometry class as Ruby in freshman year. Obviously, she doesn't remember me."
                    "I don't think I've ever seen her miss school. And her test scores were always the highest in the class."
                    "It doesn't seem like she changed in the slightest over the past four years..."
                    "Student council president, captain of the cheer team, mock trial, show choir, yearbook, National Honor Society, valedictorian..."
                    "Her list of accomplishments goes on and on."
                    "No wonder half the school is scared of her..."
                    show ruby
                    r "So, it turned out those ridiculous 'Ivy Gate' rumors were true."
                    e "(I guess she would be a little upset over the existence of this kind of event...)"
                    r "Well, no matter. I am certain that we will win."
                    r "But...don't you dare try to drag us down, [name]."
                    e "Okay, I won't...?"

                    #increase ruby relationship
                    #unlock ruby character screen

                    hide ruby
                    $ talktoruby = True
                    $ officetalks += 1

                    if officetalks < 4:
                        jump officetalk

            "Talk to Eva":
                if talktoeva == True:
                    e "(We already talked. Maybe I should try talking to someone else?)"
                else:
                    hide ruby
                    hide mason
                    hide xavier
                    show eva at center
                    with move

                    v "Hi [name]!"
                    v "I don't know if you remember me, but we were in the same history class last year!"
                    v "Fun times, right?"
                    e "Y-yeah."
                    hide eva
                    "I'm surprised {b}Eva Schafer{/b} still remembers my name, considering that we've barely ever spoken to each other."
                    "But that's just the kind of person she is."
                    "I remember that she raised thousands of dollars for children in need last winter. She probably remembers all of their names too."
                    e "(Now that I think of it, her online tutoring nonprofit has also been doing pretty well recently...)"
                    e "(The girl must really love volunteering.)"
                    show eva
                    v "So, how was your summer? {p}Get up to anything interesting lately?"
                    e "Not really...{p}I just stayed home and worked on college apps, for the most part...."
                    e "(Just like every other high school senior on the planet...)"
                    v "It's always nice to be productive!"
                    v "This summer, I started a community garden at that park across the street! {p}I also played piano at the senior home, but I do that every summer, so that's not too interesting..."
                    v "But, speaking of college..."
                    v "It turned out that the rumors about Ivy Gate were true, huh?"
                    v "I hope it's not too time-consuming... But then again, I guess it's worth it..."
                    v "If we work together, we'll definitely win this thing."
                    hide eva
                    $ talktoeva = True
                    $ officetalks += 1
                    if officetalks < 4:
                        jump officetalk
            "Talk to Mason":
                if talktomason == True:
                    e "(We already talked. Maybe I should try talking to someone else?)"
                else:
                    hide eva
                    hide ruby
                    hide xavier
                    show mason at center
                    with move

                    m "Hey."
                    m "My name is {b}Mason Espinosa{/b}. I don't believe we've met."
                    "He held out his hand for me to shake."
                    m "And you are?"
                    e "(This is a high school, not a job interview...)"
                    "I awkwardly shook his hand."
                    e "I'm [name]."
                    hide mason
                    #cg possibly
                    "We'd never talked before, but I'd heard his name a couple times through the school rumor mill."
                    "Apparently, this guy knew everybody. He was close to the teachers, too."
                    "He was Model UN president, and help found the Entrepeneurship Club at our school."
                    "I'd also heard that his father was a CEO and had secret connections to the school board."
                    "Also..."
                    e "(Wasn't he involved in that massive cheating scandal from last year?)"
                    e "(Well, a rumor is just a rumor...)"
                    show mason
                    m "So, [name]..."
                    menu masontalk:
                        m "What's your take on this whole 'Ivy Gate' thing?"
                        "It's exciting":
                            m "I totally agree."
                        "It's strange":
                            m "Really? I never thought of it that way."
                            e "Doesn't it sound too good to be true?"
                            m "Well, kind of..."
                            m "But if you really think about it, it makes sense."

                    m "This definitely sounds like the kind of thing that T10 schools would do, you know?"
                    m "I've been hearing about this thing from past seniors for years."
                    m "Besides, we're the top five students at this school for a reason, right?"
                    e "I guess so..."
                    m "This project is going to be a blast."
                    m "We're totally going to win. Trust me."

                    #increase mason relationship
                    #unlock mason character screen

                    hide mason
                    $ talktomason = True
                    $ officetalks += 1

                    if officetalks < 4:
                        jump officetalk
            "Talk to Xavier":
                if talktoxavier == True:
                    e "(We already talked. Maybe I should try talking to someone else?)"
                else:
                    hide eva
                    hide mason
                    hide ruby
                    show xavier at center
                    with move

                    x "Hey, man."
                    hide xavier
                    "I was a bit nervous to talk to {b}Xavier Lim{/b} for the first time. Everyone at school knows about him."
                    "He's been winning math competitions since elementary school...{p}Published his first scientific paper at 13...{p}He even won a national physics competition and got to meet the president..."
                    "The kind of person that your parents compare you to...{p}The literal definition of an academic weapon."
                    e "(He looks so tired... He must study a lot.)"
                    e "(He doesn't seem like the social type.)"
                    show xavier
                    e "I'm [name]. You're Xavier, right?"
                    x "Yeah, that's me."
                    x "If you don't mind...I think I'll go back to class..."
                    hide xavier with dissolve
                    e "Wait."
                    show xavier
                    e "It's just homeroom, right? At least stay here until the bell rings."
                    x "Right..."
                    e "(I should probably leave him alone for now. I don't want to be a nuisance...)"

                    # increase xavier relationship
                    #unlock xavier character screen

                    hide xavier
                    $ talktoxavier = True
                    $ officetalks += 1

                    if officetalks < 4:
                        jump officetalk
      
    hide ruby
    hide eva
    hide mason
    hide xavier

    "The bell rings."

    Character("Principal") "Looks like it's time for you all to head back to class."
    Character("Principal") "I expect to meet you all inside the {b}library at 3pm after school{/b}, where we'll deliberate further."

    # principal leaves

    scene bg hallway
    "Throughout the day, I couldn't stop thinking about the Ivy Gate Initiative."
    e "(A scholarship and guaranteed admission, huh...)"
    e "(Anyone would kill for an oppurtunity like this.)"
    e "(More importantly...)"
    e "(Since when was I ranked {i}fifth{/i} in the entire school...?)"
    e "(Something seems off...)"
    e "(There must be some kind of catch.)"
    e "(...Right?)"
    "The school day seemed to pass by in a blur."
    "Before I knew it, it was nearly 3PM."

    "*buzz buzz*"
    call eva1
    e "(I wonder how Eva got my phone number.)"
    e "Anyways, I better not show up late again..."

    #walking sounds
    #navigation gameplay depending on if i add that

    scene bg meetingroom

    show eva at center
    v "Hi [name]!"
    v "I see you got my message!"
    v "The others thought we should meet in here from now on."
    hide eva
    show eva at middleleft
    show ruby at middleright
    r "We've reserved this room for the rest of the quarter."
    hide eva
    hide ruby
    show xavier at center
    "Xavier was quietly working at his computer in the corner."
    hide xavier
    "Fortunately, this time I wasn't the last person to arrive."
    show mason at center
    with dissolve
    m "Hey, everyone."
    hide mason
    Character("Principal") "Ahem."
    Character("Principal") "Now that we're all here, we should get started."
    Character("Principal") "I'll briefly introduce this week's task, then leave you guys alone."

    # epic graphic explaining the task
    # its a presentation. research a problem in your community, come up with a solution, present it 
    # (they could possibly drive over the weekend to the presenting place if its inperson)
    # you will be graded on your speaking skills, research, presentation, idk, idk.
    # everyones individual scores will be added to make the group score. (the individual scores are private though idk)
    # * The final scoring is out of 100 points, and will be determined by the group's overall performance.

    show eva at center
    v "An entire research project, idea, and presentation in a single week..."
    hide eva
    show ruby at center
    r "It's doable."
    r "If all of us put in a sufficient amount of effort, I don't see any problem with us being able to finish before the deadline."
    hide ruby
    show mason at center
    m "I dunno, it seems like an awful lot of work to me..."
    hide mason
    show xavier at center
    x "....."
    hide xavier
    
    show ruby at left
    show eva at middleleft    
    show mason at short.middleright
    show xavier at right
    e "(This first task seems straightforward enough.)"
    e "(But definitely not easy...)"

    hide eva
    hide mason
    hide xavier
    show ruby at center
    r "There's no use wasting any more time on this matter."
    r "Considering we all signed up for this, we have no choice but to prepare for this presentation."
    r "To start..."
    r "We should come up with an issue together that we all feel relatively passionate about."
    hide ruby
    show mason at center
    m "Wait a minute, who died and made you king?!"
    hide mason
    show ruby at middleleft    
    show mason at short.middleright
    r "Considering you were the last to arrive this afternoon, you're in no position to petition for leader."
    m "Alright, fine..."
    m "But don't try to commandeer this project like one of your student council initiatives, got it?"
    hide ruby
    hide mason
    
    show ruby at left
    show eva at middleleft    
    show mason at short.middleright
    show xavier at right
    e "Let's get back on topic..."
    e "Should we spend a couple of minutes brainstorming ideas?"
    hide eva
    hide mason
    hide xavier
    hide ruby
    "We gathered around the whiteboard, and people took turns writing ideas down."
    "Suddenly, the marker fell into my hands."

    menu issuepitch:
        e "(What issue should our project focus on?)"
        "Global warming":
            e "(Global warming's a pretty big issue...)"
            e "(I don't think this is the kind of thing we could realistically solve in a week...)"
            jump issuepitch
        "Underutilization of local public transportation":
            e "(Students never ride the bus anywhere...)"
            e "(I suppose raising awareness would be a pretty simple solution...)"
        "Not enough outlets in the library":
            e "(The lack of outlets make it kind of annoying to study here...)"
            e "(But I think there are more important problems out there...)"
            jump issuepitch
    
    show ruby at left
    show eva at middleleft    
    show mason at short.middleright
    show xavier at right

    e "How about we research teens' utilization of public transportation?"
    e "We could interview people and make a survey for research..."
    e "...And make a pamphlet or social media campaign to raise awareness."
    hide ruby
    hide eva
    hide mason
    hide xavier
    show xavier at center
    x "Hmmm...."
    x "That sounds good."
    hide xavier
    show eva at center
    v "That's a good idea! I like it!"
    hide eva
    show ruby at center
    r "I agree. It's perfectly reasonable."
    r "Though perhaps not the most creative..."
    r "I'd settle for it."
    hide ruby
    show mason at center
    m "Same here."
    hide mason

    show eva
    v "That's perfect! We all agree."
    v "Is it decided, then?"
    hide eva
    "We looked around at each other in resounding agreement."
    show ruby
    r "Okay, let's divide up the work next."
    r "Remember: we only have until Sunday to complete research, design, and prepare the presentation."
    r "Today is Monday, and I think it would be best to leave Friday and Saturday for presentation planning and finishing touches."
    r "Therefore, we only have Tuesday, Wednesday, and Thursday for the research and design portions."
    hide ruby
    show ruby at middleleft    
    show mason at short.middleright
    m "So, we should make two teams work simultaneously that each focus on either research or design."
    r "...Yes, I was just going to say that."
    m "Hey, just trying to show that I'm listening."
    hide mason
    hide ruby
    show ruby at center
    r "Considering that [name] pitched the transportation idea, they'd likely be the best person to conduct research."
    r "Does anyone else want to join them?"
    hide ruby
    show eva
    "I was surprised to see Eva raise her hand."
    v "I'll do it!"
    hide eva
    show ruby
    r "Great. That leaves me, Xavier, and Mason to work on the design portion."
    hide ruby

    scene bg meetingroom_sunset
    "We spent the rest of the afternoon discussing our research and design plans for the next day."
    "Before we knew it, the sun had begun to set and it was time to go home."

    show ruby
    r "Before we leave..."
    r "Would you all mind leaving me your phone numbers? A group chat would make communication much more efficient."
    hide ruby

    scene bg room_night
    e "(What a day...)"
    e "(I should probably get started on some homework...)"
    "*buzz buzz*"
    e "(Never mind...)"

    # group chat nonsense
    call GC1

    e "(They finally quieted down...)"
    e "(Better head to sleep now.)"

    scene black with fade

#tuesday

# am: interviewing ppl
# pm: free time w eva, introduce free time mechanic

#wednesday

# free time w mason (lunch)

#thursday

# free time w xavier

#friday

# free time w ruby (coffee date or smth)
#

#saturday

#group lock in or osmething

#to-dos:

#graphics (me) - refine character sprites + poses/expressions
#                map
#                general ui (text box)

#assets (find) - sounds (mostly footsteps, classroom chatter, bell)
# 

#monday - finish intro monologue, 
#         add some banter in office scene, 
#         write texting dialogue
#         work on contract signing/task graphic, 
#         add character relationships/character page

    return
