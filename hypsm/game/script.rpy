# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    $ timer_range = 0
    $ timer_jump = 0

# time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out

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
    "Does it mean you're well-liked?"
    "Does it mean you've ammassed a large fortune?"
    "Does it mean you've accomplished some great task?"
    "..."
    "Does being successful mean you're truly happy?"

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

    

    e neutral "(Today's the first day of senior year.)"
    e "(I almost forgot...)"
    e sigh "(I should probably get to class, or my parents will kill me...)"

    "I rolled out of bed and began my usual school morning routine that felt all too familiar at this point."
    "After a few bites of breakfast, I got on my bike and rode to school, trying not to start my final year of high school tardy."

    scene bg homeroom
    #classroom chatter
    e sigh "(I made it in time for homeroom...)"
    e "(Thank goodness...)"
    Character("Student") "Hey, how was that internship you started over the summer?"
    Character("Another Student") "It went well! I think it'll look really good on my resume..."
    Character("Student") "Ugh, I'm so jealous..."
    Character("Student") "Hopefully that startup I cofounded will be enough to get me into Stanford..."

    
    e nervous "(Man, I really don't miss having to overhear these kinds of side conversations...)"
    e sigh "(I really should do more, huh...)"

    "Before I could make it to my seat, I was stopped by the homeroom teacher."

    Character("Teacher") "[name], can I speak with you for a second?"
    e neutral "?"
    Character("Teacher") "The principal would like to see you in his office."
    Character("Teacher") "You're excused from homeroom. You won't be missing anything important."

    e "Uh, okay..."
    #walking away
    scene bg hallway
    e nervous "(Am I in trouble? I don't think I should be...)"
    e "(I guess I'll go anyway.)"

    #more walking
    e "(...Where's the principal's office again?)"
    "I realized that I'd never been called to the principal's office before."
    "I almost got lost a few times, but eventually arrived at my destination."
    "Taking a deep breath, I knocked on the door."

    scene bg office

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

    
    Character("Principal") "Your team performance will allow the school to place higher in the challenge and boost our reputation."
    Character("Principal") "More details can be found in this agreement they've asked you all to sign."
    Character("Principal") "If you don't mind..."
    "He hands us each a folder."
    Character("Principal") "Read it carefully, and let me know with any questions you may have"
    call screen contract
    #waiit i have an idea what if he doesn't tell them that its individual until later....

    #Character("Principal") "But, at the end of the program..."
    #Character("Principal") "Only a limited amount of scholarships will be awarded."
    #Character("Principal") "The final scholarships and admission offers will only be made to individuals, not the entire team."
    #Character("Principal") "However, I must emphasize the importance in teamwork and group bonding in situations like these!"
    e nervous "This is a lot..."
    "I signed the contract."
    e neutral "(It looks like everyone else signed pretty quickly, too.)"
    #more exposition that i was thinking about lst night but completely forgor

    Character("Principal") "That's settled, then."
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
            e nervous "(What should I do?)"

            "Talk to Ruby":
                if talktoruby == True:
                    e neutral "(We already talked. Maybe I should try talking to someone else?)"
                    jump officetalk
                else:
                    hide eva
                    hide mason
                    hide xavier
                    show ruby at center
                    with move

                    r "You do know punctuality is paramount to success, right?"
                    e nervous "...I'm sorry, what?"
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
                    e neutral "(I guess she would be a little upset over the existence of this kind of event...)"
                    r "Well, no matter. I am certain that we will win."
                    r "But...don't you dare try to drag us down, [name]."
                    
                    e nervous "Okay, I won't...?"

                    #increase ruby relationship
                    $ruby_stats.relationship += 1
                    #unlock ruby character screen

                    hide ruby
                    $ talktoruby = True
                    $ officetalks += 1

                    if officetalks < 4:
                        jump officetalk

            "Talk to Eva":
                if talktoeva == True:
                    e neutral "(We already talked. Maybe I should try talking to someone else?)"
                    jump officetalk
                else:
                    hide ruby
                    hide mason
                    hide xavier
                    show eva at center
                    with move

                    v "Hi [name]!"
                    v "I don't know if you remember me, but we were in the same history class last year!"
                    v "Fun times, right?"
                    e nervous "Y-yeah."
                    hide eva
                    "I'm surprised {b}Eva Schafer{/b} still remembers my name, considering that we've barely ever spoken to each other."
                    "But that's just the kind of person she is."
                    "I remember that she raised thousands of dollars for children in need last winter. She probably remembers all of their names too."
                    e neutral "(Now that I think of it, her online tutoring nonprofit has also been doing pretty well recently...)"
                    e "(The girl must really love volunteering.)"
                    show eva
                    v "So, how was your summer? {p}Get up to anything interesting lately?"
                    e nervous "Not really...{p}I just stayed home and worked on college apps, for the most part...."
                    e "(Just like every other high school senior on the planet...)"
                    v "It's always nice to be productive!"
                    v "This summer, I started a community garden at that park across the street! {p}I also played piano at the senior home, but I do that every summer, so that's not too interesting..."
                    v "But, speaking of college..."
                    v "It turned out that the rumors about Ivy Gate were true, huh?"
                    v "I hope it's not too time-consuming... But then again, I guess it's worth it..."
                    v "If we work together, we'll definitely win this thing."
                    hide eva
                    $eva_stats.relationship += 1

                    $ talktoeva = True
                    $ officetalks += 1
                    if officetalks < 4:
                        jump officetalk
            "Talk to Mason":
                if talktomason == True:
                    e neutral "(We already talked. Maybe I should try talking to someone else?)"
                    jump officetalk
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
                    e nervous "(This is a high school, not a job interview...)"
                    "I awkwardly shook his hand."
                    e neutral "I'm [name]."
                    hide mason
                    #cg possibly
                    "We'd never talked before, but I'd heard his name a couple times through the school rumor mill."
                    "Apparently, this guy knew everybody. He was close to the teachers, too."
                    "He was Model UN president, and help found the Entrepeneurship Club at our school."
                    "I'd also heard that his father was a CEO and had secret connections to the school board."
                    "Also..."
                    e nervous "(Wasn't he involved in that massive cheating scandal from last year?)"
                    e "(Well, a rumor is just a rumor...)"
                    show mason
                    m "So, [name]..."
                    menu masontalk:
                        m "What's your take on this whole 'Ivy Gate' thing?"
                        "It's exciting":
                            m "I totally agree."
                        "It's strange":
                            m "Really? I never thought of it that way."
                            e nervous "Doesn't it sound too good to be true?"
                            m "Well, kind of..."
                            m "But if you really think about it, it makes sense."

                    m "This definitely sounds like the kind of thing that T10 schools would do, you know?"
                    m "I've been hearing about this thing from past seniors for years."
                    m "Besides, we're the top five students at this school for a reason, right?"
                    
                    e nervous "I guess so..."
                    m "This project is going to be a blast."
                    m "We're totally going to win. Trust me."

                    #increase mason relationship
                    $mason_stats.relationship += 1
                    #unlock mason character screen

                    hide mason
                    $ talktomason = True
                    $ officetalks += 1

                    if officetalks < 4:
                        jump officetalk
            "Talk to Xavier":
                if talktoxavier == True:
                    e neutral"(We already talked. Maybe I should try talking to someone else?)"
                    jump officetalk
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
                    e neutral "I'm [name]. You're Xavier, right?"
                    x "Yeah, that's me."
                    x "If you don't mind...I think I'll go back to class..."
                    hide xavier with dissolve
                    e "Wait."
                    show xavier
                    e nervous "It's just homeroom, right? At least stay here until the bell rings."
                    x "Right..."
                    e "(I should probably leave him alone for now. I don't want to be a nuisance...)"

                    # increase xavier relationship
                    $xavier_stats.relationship += 1
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
    show screen gameUI
    "The bell rings."

    Character("Principal") "Looks like it's time for you all to head back to class."
    Character("Principal") "I expect to meet you all inside the {b}library at 3pm after school{/b}, where we'll deliberate further."

    # principal leaves

    scene bg hallway
    "Throughout the day, I couldn't stop thinking about the Ivy Gate Initiative."
    e sigh "(A scholarship and guaranteed admission, huh...)"
    e "(Anyone would kill for an oppurtunity like this.)"
    e "(More importantly...)"
    e nervous "(Since when was I ranked {i}fifth{/i} in the entire school...?)"
    e sigh "(I guess I do study a lot compared to everyone else...)"
    e "(There must be some kind of catch.)"
    e nervous "(...Right?)"
    "The school day seemed to pass by in a blur."
    "Before I knew it, it was nearly 3PM."

    "*buzz buzz*"
    call eva1
    e nervous "(I wonder how Eva got my phone number.)"
    e neutral "Anyways, I better not show up late again..."

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

    #show screen project1
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
    e neutral "(This first task seems straightforward enough.)"
    e nervous "(But definitely not easy...)"

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
            e neutral "(Global warming's a pretty big issue...)"
            e nervous "(I don't think this is the kind of thing we could realistically solve in a week...)"
            jump issuepitch
        "Underutilization of local public transportation":
            e neutral "(Students never ride the bus anywhere...)"
            e "(I suppose raising awareness would be a pretty simple solution...)"
        "Not enough outlets in the library":
            e "(The lack of outlets make it kind of annoying to study here...)"
            e nervous "(But I think there are more important problems out there...)"
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
    e nervous "(What a day...)"
    e "(I should probably get started on some homework...)"
    "*buzz buzz*"
    e sigh "(Never mind...)"

    # group chat nonsense
    call GC1

    e neutral "(They quieted down...)"
    e "(Better head to sleep now.)"

    scene black with fade

#tuesday
    $ day = 2

    "*BEEP BEEP*"
    scene bg room

    #blinking or something
    show black with dissolve
    pause 0.1
    hide black with dissolve
    pause 0.1
    show black with dissolve
    pause 0.1
    hide black with dissolve
    
    "Stumbling out of bed, I reached for my phone."
    $ phone.system.date = datetime.datetime(year=2025, day=16, month=8, hour=7, minute=21)
    phone discussion "EvaChat":
        time year 2025 day 16 month 8 hour 7 minute 21
        "v" "heyy [name]"
        "v" "sorry for not bringing it up earlier, but I was thinking that we should start interviewing people at lunch today?"
        "v" "since that's when most people will be around, you know?"
        "v" "wanna meet up before school to talk about it really quick?"
        "e" "Sounds good"
        "v" "great!"
        "v" "meet me in the courtyard"
    phone end discussion


    e sigh "(Shoot, I better hurry to school right now before class starts...)"

    scene bg courtyard
    e neutral "(It's weird to be here early for once.)"
    e "(As you'd expect, barely anyone came to school early on a Tuesday...)"

    show eva
    v "Hey [name]!"
    e nervous "Oh, hi..."
    v "Sorry for making you come here so early. I was worried we wouldn't have time to talk since we don't have classes together..."
    e neutral "It's okay, I don't mind."
    v "Anyways, let's go over what we should ask about." 
    v "Have you written down any questions we should ask?"
    e sigh "(I didn't even think about that...)"
    e nervous "Actually, I haven't..."
    v "That's okay, I made a list with a ton of questions last night!"
    v "Some of them not be very good, but..."
    v "It'll definitely make things easier!"
    e neutral "Thanks, that'll be a huge help."
    v "Anyways..."
    v "Do you have much experience interviewing people, [name]?"
    e nervous "Not really..."
    v "Me neither, but it shouldn't be too hard, right?"
    v "As long as we follow a set template..."
    v "And make sure our sample is good! I learned that in AP Stats!"
    e neutral "Okay, I'll try to come up with a template during class..."
    "The bell rings."
    v "Well, see you at lunch, [name]!"
    e nervous "See you..."
    hide eva

    scene bg hallway

    e neutral"(It's lunch now...)"

    show eva
    v "Hey [name]!"
    v "Shall we get going?"

    #image map thing to simulate walking around instead of a menu
    #or not!

    scene bg courtyard
    v "I think we should interview this first person together, then split up."
    v "Do you want to start?"
    e nervous "Sure..."

    # walking sfx

    v "Excuse me, would you be willing to be interviewed for our research project?"
    Character("Student A") "Uh, sure?"
    

    hide eva
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

    label interviewA:
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'interviewA_timer'
        e neutral "(This is the list of questions Eva came up with. If I just follow this, hopefully things will work out.)"
        label interviewA_Q1:
            show screen countdown
            menu:
                "What do you usually do after school?":
                    hide screen countdown
                    e "What do you usually do after school?"
                    Character("Student A") "Well, I usually just study at the library..."
                    e nervous "(I don't think this is going anywhere...)"
                    e sigh "(I need to get back on task...)"
                    jump interviewA_Q1
                    
                "How do you usually get around?":
                    hide screen countdown
                    e "How do you usually get around?"
                    Character("Student A") "Well, I can't drive yet..."
                    Character("Student A") "So I try to walk places when I can."
                    Character("Student A") "Sometimes I get a ride from one of my friends."
                    e "(Since they don't drive, they make pretty a good person to be interviewed about public transport.)"
                    $ time = 5
                    jump interviewA_Q2

                "Do you have a job?":
                    hide screen countdown
                    e "Do you have a job?"
                    Character("Student A") "Actually, I don't..."
                    Character("Student A") "I'm too busy with school at the moment..."
                    e nervous "(I don't think this is going anywhere...)"
                    e sigh "(I need to get back on task...)"
                    jump interviewA_Q1


        label interviewA_Q2:
            show eva
            v "Okay, I'll go next!"
            v "How aware are you of local public transportation options in the area?"
            v "Also, what are your friends and classmates saying about public transport?"
            hide eva
            Character("Student A") "Pretty aware, I guess?"
            Character("Student A") "I know the bus exists...and there's a train that goes to other cities nearby."
            Character("Student A") "Honestly, I couldn't tell you where the stops are, or what the schedules are, or anything like that."
            Character("Student A") "Most of my friends don't really talk about public transport at all."
            Character("Student A") "It's mostly viewed as a last resort..."
            show eva
            v "I see..."
            v "[name], your turn!"
            hide eva
        label interviewA_Q3:
            show screen countdown
            menu:
                "Would your parents approve of you taking public transportation?":
                    hide screen countdown
                    e "Would your parents approve of you taking public transportation?"
                    Character("Student A") "Well, yes..."
                    Character("Student A") "So that's not really the issue..."
                    e nervous "(I need to get back on task...)"
                    jump interviewA_Q3

                "Can you tell me more about your friends?":
                    hide screen countdown
                    e "Can you tell me more about your friends?"
                    Character("Student A") "Um, I don't see how that's relevant..."
                    e sigh "Never mind, then..."
                    e nervous "(I need to get back on task...)"
                    jump interviewA_Q3

                "Have you ever used public transportation?":
                    hide screen countdown
                    e "Have you ever used public transportation?"
                    Character("Student A") "Yes, I have."
                    e "How was that experience like for you?"
                    Character("Student A") "I ride the bus sometimes, but not regularly."
                    Character("Student A") "It's just kind of easier to coordinate rides and walk instead of figuring out bus schedules."
                    Character("Student A") "And it usually takes longer to take public transport, right?"
                    $ time = 5
                    jump interviewA_Q4
        label interviewA_Q4:
            show eva
            v "My turn..."
            v "Are there places you want to go that you think would be more or less accessible through public transport"
            hide eva
            Character("Student A") "Well, I know that getting to the mall would be much easier by bus or train, and you don't even need to worry about parking..."
            Character("Student A") "But a lot of my friends live in neighborhoods on the outskirts of the city, and I'm not sure that there are any buses that can get there..."
            show eva
            v "I see..."
            v "[name], your turn!"
            hide eva
        label interviewA_Q5:
            show screen countdown
            menu:
                e neutral "Last question..."
                "If you could take a bus anywhere in the world, where would you go?":
                    hide screen countdown
                    e "If you could take a bus anywhere in the world, where would you go?"
                    Character("Student A") "Um, I don't see how that's relevant..."
                    e sigh "Never mind, then..."
                    e "(I need to get back on task...)"
                    jump interviewA_Q5
                    
                "What would make you more likely to try public transit?":
                    hide screen countdown
                    e "What would make you more likely to try public transit?"
                    Character("Student A") "Well, I think that making it cheaper or even free for students would be really helpful."
                    Character("Student A") "I know it doesn't cost much, but all those little fees really add up, right?"
                    Character("Student A") "Also, I would probably take the bus or train more if my friends were all doing it."
                    $ time = 5
                    jump interviewA_done
                
    
    label interviewA_timer:
        Character("Student A") "...Uh, I'm gonna go now..."
        e "(Let's try this again...)"
        jump interviewA
    
    label interviewA_done:
        v "Yay, thanks for helping us!!"
        e sigh "First person down..."
        e neutral "I think I'm getting the hang of this."
        e "Hopefully we interview enough people before lunch ends."

    scene bg hallway
    "The rest of the interviews happened without trouble."
    # bell rings  
    e nervous "Phew, that was a lot of talking..."
    e neutral "But it's time to head back to class."

    scene bg homeroom
    "It was a pretty uneventful day, all things considered."
    "I spent some of my work time during class typing up my findings."
    show eva
    "When the school day ended, I was surprised to see Eva waiting for me."
    v "Hey!"
    v "Thanks for sending me your results, by the way!"
    v "I think Ruby and the others are pretty locked in on their portion of the project right now, so we aren't meeting after school today."
    v "Since we're both free, how about we go do something together?"


    $ freeTimewith = "Eva"

    call screen freeTime
    label TuesdayEve:
        "The sun had begun to set, so we parted ways."
        "[[You have learned something new about Eva.]"
        "[[Your relationship with Eva increased by 1.]"

    scene bg room_night
    # group chat moment
    # ruby updates everyone with the research
    phone discussion "GC":
        $ phone.system.date = datetime.datetime(year=2025, day=16, month=8, hour=9, minute=12)
        time year 2025 day 16 month 8 hour 9 minute 12
        "r" "Good evening, everyone."
        "r" "Nice work today."
        "r" "From the research [name] and Eva have done today, it appears that accessibility is a major issue when it comes to public transportation."
        "r" "I think we should keep that in mind going forward."
        "r" "Mason, Xavier, and I are still working on the design portion, so we probably won't meet tomorrow either."
    phone end discussion

    "*Phone ringing*"
    e "It's Mason..."
    phone call "m"
    m "Hey."
    e nervous "H-hi..."
    m "This is [name], right?"
    m "Ruby sent everyone your research from today."
    m "Good work, by the way. I think your findings are pretty interesting."
    e "Thanks..."
    e neutral "How has the design portion been going? Have you guys come up with potential solutions yet?"
    m "It's been alright, you know?"
    m "I can brief you on it tomorrow."
    m "Speaking of..."
    m "Want to grab coffee or something together at lunch tomorrow?"
    e nervous "Sure, why not..."
    m "Cool."
    m "See ya!"
    phone end call 

    "Soon after talking to Mason, I fell asleep."
    scene black with fade

#wednesday
    $ day = 3

    "*BEEP BEEP*"
    scene bg room

    #blinking or something
    show black with dissolve
    pause 0.1
    hide black with dissolve
    pause 0.1
    show black with dissolve
    pause 0.1
    hide black with dissolve

    e "(We pretty much completed all the research yesterday.)"
    e "(I wonder how the other group is progressing...)"
    e "Guess I'll ask Mason about it at lunch today..."

    scene bg courtyard

    show mason
    m "Hey [name], how's it going?"
    e nervous "I'm doing okay..."
    m "Good, good!"
    
    # talk to mason (project related) at lunch
    m "You guys are completely finished with your portion of the project, huh?"
    m "Must be nice..."
    m "Although I can't really complain, since Ruby keeps insisting on doing a majority of the work by herself..."
    m "Anyways, I'll catch you up to speed on what we've done so far, since you're interested."
    "He begins to recall the past few meetings in intense detail."
    e nervous "(This guy can really talk.)"
    m "Basically, we're planning to make something that addresses students' lack of awareness of the public transportation system"
    e "Probably an app, but we'd also like to work with the city to increase frequency, as well as implement a free or discounted transit plan for students."
    e neutral "I see."
    e "(Looks like the other group has everything under control.)"
    
    # hang out with mason (free time)
    m "There's still a couple of minutes left of lunch."
    m "Want to go somewhere?"
    $ freeTimewith = "Mason"
    call screen freeTime

    label WednesdayLunch:
        m "I think we should head back to class soon."
        m "It was nice talking to you, though!"

        hide mason
        $mason_stats.likes = ""
        $mason_stats.relationship += 1
        "[[You have learned something new about Mason.]"
        "[[Your relationship with Mason increased by 1.]"        
    
    scene bg hallway
    "The rest of the day happened as normal."
    "Since we didn't have a meeting that day, I got some work done at home like usual."
    scene bg room

    "*buzz buzz*"
    $ phone.system.date = datetime.datetime(year=2025, day=17, month=8, hour=4, minute=3)
    phone discussion "GC":
        time year 2025 day 17 month 8 hour 4 minute 3
        "v" "any status updates?"
        "m" "I feel bad that Rubys the only one talking here so Ill take this one"
        "m" "Were currently designing an app that makes transport more accessible and socially appealing"
        "m" "Which is only a small part of our overall plan"
        "v" "ooh okay"
        "r" "I appreciate the sentiment, but I'd like you to stop texting during work time, Mason."
        "x" "yikes"
    phone end discussion

    scene bg room_night
    "Before I knew it, the day was over."
    e "Better go to sleep...."
    
    scene black with fade
    
#thursday
    $ day = 4

# meeting after school
    scene bg hallway
    "*buzz buzz*"
    $ phone.system.date = datetime.datetime(year=2025, day=18, month=8, hour=3, minute=1)
    phone discussion "GC":
        time year 2025 day 18 month 8 hour 3 minute 1
        "r" "We're meeting in the library today."
        "r" "I have some business to attend to, so I'll be there at 3:10."
        "r" "Apologies."
    phone end discussion

    scene bg meetingroom
    "When I got to the meeting room, Mason and Xavier were already there staring at their phones."
    e nervous "Hey..."
    show eva
    v "Hi everyone!"
    v "C'mon, put your phones away...!"
    v "How have you guys been doing?"
    e neutral "Pretty good."
    e "(It's only the first week of school, so nothing too crazy has happened yet.)"
    hide eva
    show mason
    m "I've gotten to network with so many people this week."
    m "Including you guys, obviously."
    m "It's pretty exciting, actually."
    e nervous "Interesting..."
    hide mason
    show eva
    v "What about you, Xavier?"
    hide eva
    show xavier
    x "I'm doing fine..."
    x "Kind of wish I was home doing practice problems right now..."
    e nervous "Well, hopefully this meeting doesn't run too long, haha..."
    hide xavier
    show ruby
    r "Sorry I'm late."
    r "Let's get started..."
    hide ruby
    show eva
    v "No worries, we were just chatting!"
    hide eva
    "We all settled down and began the meeting."
    show ruby
    r "Firstly..."
    r "Eva and [name], would you two like to summarize your research quickly to start?"
    hide ruby
    show eva
    v "Okay!"
    e nervous "Okay..."
    v "We found that students are generally aware of public transit options but rarely use them consistently."
    v "Mostly because it's simply harder than getting rides from parents or friends."
    e "Some key barriers include the percieved complexity of planning routes and understanding how to use the system,"
    e "Infrequent service, accumulating costs, and social stigma among peers."
    v "The core insight is that transit needs to be easier than asking for a ride to become students' first choice rather than a backup plan."
    hide eva
    show ruby
    r "Well said."


    scene bg meetingroom_sunset
    "We concluded the meeting."
    "The others quickly packed up and left until Mason and I were the only ones remaining."
    show mason
    m "You know..."
    m "He may seem kind of like a bum, but Xavier's actually really smart."
    e nervous "I know..."
    e sigh "(I've heard so much about him, but it's kind of hard to believe that the kid so many people call a genius is...)"
    e "(Is...)"
    m "I don't think he's had many opportunities to apply himself due to the nature of this first task..."
    m "Just trust me, he's really smart."
    e nervous "He seems like he's under a lot of stress right now..."
    m "In the long run, I don't think we can win without him."
    m "Well, see ya."
 

# free time w xavier (nighttime)
# forces you to go to the convenience store because everywhere else is closed
    scene bg room_night
    
    e nervous "(It's so late...)"
    e "(I just got back from the meeting...)"
    e "Better catch up on some homework."
    Character("Sister") "[name]!!"
    Character("Sister") "We're all out of dish soap."
    Character("Sister") "Can you run to the store and buy more?"
    e sigh "Or not..."

    scene bg store
    e "(There's only one place in town that's open right now.)"
    e "(Good thing I live close...)"

    #footsteps
    "As expected, the convenience store was basically empty."
    e "(I feel bad for the employees...)"
    e "(Hopefully they have dish soap here...)"
    
    show xavier
    e "(Wait a minute, isn't that...?)"
    "I spotted Xavier in the back of the store, grabbing an energy drink from the drinks section."
    #footsteps
    e nervous "Hey, Xavier..."
    x "Oh hi, [name]."
    e "Funny running into you here, huh?"
    e "Do you live nearby too?"
    x "Yeah."
    x "Just grabbing something for my nighttime study section."
    e "Isn't it a bit late for energy drinks?"
    x "No, this is pretty normal for me..."
    e "(That can't be healthy...)"
    e sigh "(But you can't win all those competitions without risking it a little, right?)"
    e neutral "What are you studying for?"
    e "Isn't it only the first week of school?"
    x "You know, other stuff..."
    x "There's a math competition coming up."
    x "I'm taking a few community college courses on the side, too..."
    x "And there are a few college essays I need to finish up..."
    e nervous "That sounds like a lot..."
    e "(And we're spending all our time working on the Ivy Gate project now...)"
    x "..."
    menu:
        e "(I should probably change the subject.)"
        "Ask about hobbies":
            e "So, what do you like to do for fun?"
            x "That's a...good question..."
            x "I used to play tennis as a kid."
            x "I didn't make the team when I tried out here, though, so I quit."
            x "What else..."
            x "Um..."
            e neutral "I didn't know you played tennis."
            e "That's pretty interesting..."
        "Ask about school":
            e "So, how has senior year been?"
            e "What kind of classes have you been taking?"
            x "Well..."
            x "I took AP Physics and Chemistry in sophomore and junior year, so I'm taking AP Bio now..."
            x "Also Macroeconomics and Government..."
            x "AP Research... Music Theory..."
            e "(I'm getting stressed just listening to this schedule...)"
            e "(Maybe I shouldn't have asked about school...)"
    x "Anyways, are you here to buy something?"
    e neutral "Yeah, I need to buy dish soap."
    x "I come here a lot..."
    x "Dish soap would probably be somewhere over there."
    x "I should probably get going..."
    e "See you tomorrow!"
    x "...Yup."
    hide xavier
    e "(What an interesting guy...)"

    scene bg room_night
    "I bought the dish soap and went home."
    "I realized how tired I was, and fell asleep straight after completing my homework."
    scene black with fade

#friday
    $ day = 5

    "*BEEP BEEP*"
    scene bg room

    #blinking or something
    show black with dissolve
    pause 0.1
    hide black with dissolve
    pause 0.1
    show black with dissolve
    pause 0.1
    hide black with dissolve

    e "(Wow, it's Friday already...)"
# free time w ruby (coffee date or smth) (morning)
    "*buzz buzz*"
    e "(Who could it possibly be...?)"
    $ phone.system.date = datetime.datetime(year=2025, day=19, month=8, hour=7, minute=30)
    phone discussion "Ruby":
        time year 2025 day 19 month 8 hour 7 minute 30
        "r" "Good morning."
        "r" "Could you meet me at the cafe before school today?"
    e "(What could she possibly want...)"
    phone discussion "Ruby":
        "e" "Sure"
        "r" "Okay."
        "r" "See you then."
    phone end discussion

    scene bg cafeterrace
    show ruby
    "When I arrived at the cafe, Ruby was already there."
    e nervous "(Early as usual...)"
    r "Hello."
    r "Are you going to order anything?"
    e "I guess I could..."
    e "(I don't usually drink coffee...)"
    r "...This place is one of my favorites."
    r "Personally, I'd reccommend the Americano."
    e "Okay..."
    "I got up to order from the counter, then sat back down."
    e "So, what did you want to talk to me about?"
    r "Well..."
    r "I just wanted to check in."
    r "See you at the meeting this afternoon."



# afternoon meeting, plan presentation/saturday/divvy up presenter roles
    scene bg meetingroom
    "I was the last person to arrive that day."
    show ruby
    r "Since we're all here, let's get started."
    r "To summarize..."

    show eva
    v "Maybe we could meet at someone's house tomorrow to prepare more?"
    hide eva
    show ruby
    r "That's a good idea."
    m "In that case, I'd be happy to volunteer."
    m "My house is pretty big, and I'm sure my parents don't mind."

#saturday
    scene bg masonhouse
    "get ready."
    $debateindex = debate1
    jump debate
    label debate1:
        if score <= 20:
            r "Fortunately, that was just practice."
            r "I strongly encourage you to rehearse on your own time before tomorrow's presentation"
        else:
            r "Well done."
            v "That was great, [name]!"
            r "Just remember that the actual presentation will be a lot more difficult than this."
    r "Okay, I think that's enough for now."


#group lock in or osmething
#they become closer

#sunday
#they drive to the event
    scene bg auditorium
# they meet the opps who seem like theyll be important but actually arent rlly that important
# they present their thing
# they celebrate
# the principal reveals that theres been a change of plans and theyve actually been competing against each other this whole time
# end chapter 0 oooooOOOOOOOooo

#to-dos:

#graphics (me) - refine character sprites + poses/expressions
#                map

#eden
    # happy 
    ## nervous (sweat)
    ## thinking?
    ## normal
    # despair

#eva
    ##normal 
    #happy (joyful)
    #questioning/thinking?
    ##nervous 
    #scared

#mason
    #normal
    #shocked
    #nervous
    #skeptical/annoyed
    #happy

#ruby
    #normal
    #annoyed
    #shy


#assets (find) - sounds (mostly footsteps, classroom chatter, bell)
# 

#monday - finish intro monologue, <--- done! (kinda)
#         add some banter in office scene, <---not doing this anymore?
#         write texting dialogue
#         work on contract signing/task graphic, 

#tuesday - DONE

#wednesday - write mason freetime

#thursday - write meeting thing



    return
