screen freeTime:
    add "map.png"

    imagebutton:
        xpos 300
        ypos 100
        idle "library.png"
        hover "library copy.png"
        action Jump("library")

    imagebutton:
        xpos 400
        ypos 700
        idle "cafe.png"
        hover "cafe copy.png"
        action Jump("cafe")

    imagebutton:
        xpos 850
        ypos 350
        idle "park.png"
        hover "park copy.png"
        action Jump("park")

    imagebutton:
        xpos 1200
        ypos 90
        idle "bookstore.png"
        hover "bookstore copy.png"
        action Jump("bookstore")

    imagebutton:
        xpos 1500
        ypos 550
        idle "convenience.png"
        hover "convenience copy.png"
        action Jump("convenience")

    imagebutton:
        xpos 50
        ypos 400
        idle "school.png"
        hover "school copy.png"
        
    imagebutton:
        xpos 1000
        ypos 750
        idle "home.png"
        hover "home copy.png"

#library - no bonuses, sat word game (concentration)
label library:
    $ freetimelocation = "library"
    if day == 2:
        e neutral "Let's study in the library."
        scene bg library
        e "The library's pretty quiet right now..."
        e "We can study for a bit first so we don't disturb anyone."
        $ libraryday = "library2"
        $randomize_cards()
        call screen memory_game
        label library2:
            show eva
            v smile "Flashcards are really helpful for studying, aren't they?"
            v neutral "I like how they make it easy to quiz yourself on the material."
            v question "Do you use them often?"
            e nervous "Sometimes..."
            e "(I usually just make them when I'm cramming for a test...)"
            
            jump evaFT_1
        
        label evaFT_1done_library:
            scene bg library_sunset
            $eva_stats.likes = "Volunteering"
            $eva_stats.relationship += 1
            show screen gameUI
        jump TuesdayEve
    elif day == 3:
        e "Let's study in the library."
        m annoyed "...Interesting choice, but I guess it's your call."
        scene bg library
        $ libraryday = "library3"
        $randomize_cards()
        call screen memory_game
        label library3:
            jump masonFT_1
#cafe - ruby bonus, jigsaw puzzle
label cafe:
    $ freetimelocation = "cafe"
    if day == 2:
        e "Let's go to the cafe."
        scene bg cafe
        e "The cafe always has jigsaw puzzles laying around..."
        v smile "Let's work on one together!"
        #call jigsaw puzzle game once i figure that out
        $ cafeday = "cafe2"
        $setup_puzzle()
        call screen puzzle
        label cafe2:
            show eva
            v "Yay, we did it!"
            jump evaFT_1
        

        label evaFT_1done_cafe:
            scene bg cafe_sunset
            $eva_stats.likes = "Volunteering"
            $eva_stats.relationship += 1
            show screen gameUI
        jump TuesdayEve  
    elif day ==3:
        m "I think that place's closed today..." 
        jump library         

#park - eva bonus
label park:
    "[[this free time location is coming soon!]"
    jump library

#bookstore - mason bonus, cards (blackjack?) for some reason / depends on the person
label bookstore:
    if day == 3:
        e "How about the bookstore?"
        m grin "That sounds good!"
        scene bg bookstore
        jump masonFT_1
    else:
        jump library
#convenience store - xavier bonus, 
label convenience:
    "[[this free time location is coming soon!]"
    jump library

label evaFT_1:
    v question "I guess I never really asked you about this, but what do you think about this Ivy Gate project?"
    v nervous "I mean, my classes aren't really hardcore, so it's kind of hard for me to wrap my head around how this single project could change all of our lives, you know?"
    show eva neutral 
    e nervous "(Life-changing, huh...)"
    e "(That's kind of an exaggeration, but this project is pretty important...)"
    e "I guess I'm just not sure how to feel about it yet."
    v question "We should just do the best we can, and work together, right?"
    e neutral "Right. We all have strengths in different areas, I'm sure."
    v nervous "It's a team effort. Imagine if we had to compete against each other! That'd be silly."
    e sigh "(Sounds like a nightmare...)"
    show eva neutral 
    "The air between us falls silent."
    menu: 
        e neutral "(I should use this time to get to know Eva better...)"
        "Ask about hobbies":
            e "So, what do you like to do for fun?"
            v nervous "Hmm..."
            v neutral "Well, it's a three-way tie."
            v "Between running TutorToday, working at the community garden, and playing piano, I'd say they're all my favorite."
            v nervous "I guess I won't have much time to work on anything else now that we've got Ivy Gate, though..."


        "Ask about school":
            e "What classes are you taking this year?"
            v question "English, math, government..."
            v neutral "Nothing crazy, I guess."
            v nervous "I wanna take it easy for now because it's senior year, you know?"
            v smile "I also wanted to spend more time volunteering this year."

    e "How long have you been volunteering?"
    v neutral "Since eighth grade..."
    v nervous "I know a lot of people start doing it because they think it'll look good on college applications, but that's not the case with me at all...!!"
    v neutral "It kind of just started with me playing piano around town, and it's branched off into all kinds of things since."
    e "How long have you been playing piano?"
    v "I started in third grade, but it's been on and off."
    v nervous "Lately I haven't been feeling the same passion for it that I used to..."
    v "It's kind of scary when that happens, you know?"
    v smile "Or maybe that's just me, haha..."

    jump expression "evaFT_1done_" + freetimelocation

label masonFT_1:
    show mason
    m neutral "Sooo...."
    m "How are college apps going?"
    e nervous "(Talking about college right away, huh...)"
    e "They're going okay?"
    m grin "That's nice."
    m surprised "How many schools are you applying to? {p}19? 20?"
    e nervous "Uhh....no?"
    e sigh "(That's so many...wouldn't that cost a fortune?)"
    m nervous "Well, to each their own, I suppose."
    m "Personally, I want to keep it safe, you know?"
    m annoyed "With everything I've done, I REALLY don't want to be stuck with some low-tier school."
    m nervous "I guess I won't need to worry about that now that we've got this Ivy Gate thing, though..."

    menu: 
        e neutral "(I should use this time to get to know Mason better...)"
        "Ask about hobbies":
            e "So, what do you like to do for fun?"
            m neutral "Well..."
            m "Nowadays, I'm trying to talk to more people."
            m "I need to build my network, you know?"
            m grin "Currently I'm working on an AI B2B SaaS startup with some guys at Yale..."
            m "You in, or...?"
            e nervous "I think I'm good..."


        #"Ask about school":
            #e "What classes are you taking this year?"
    jump WednesdayLunch