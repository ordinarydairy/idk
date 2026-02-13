# ...existing code...
#matching
default card_amount = 12
default card_rows = 3
default cards = []
default selected_cards = []
default hidden_cards = 0
default match_found = False

#puzzle 
default page_pieces = 12
default full_page_size = (711,996)
default piece_coordinates = [(451,149), (719, 139), (868,238), (421,399), (658,318),(700,488),(796,538), (453,718), (776,773), (464,925), (743,958), (921,888)]
default initial_piece_coordinates =[]
default finished_pieces = 0

# new: example term-definition image pairs — replace with your image filenames (put images in game/images/)
default term_defs = [
    ("cards/2.png", "cards/3.png"),
    ("cards/4.png", "cards/5.png"),
    ("cards/6.png", "cards/7.png"),
    ("cards/8.png", "cards/9.png"),
    ("cards/10.png", "cards/11.png"),
    ("cards/12.png", "cards/13.png"),
]

init python:
    #matching
    def randomize_cards():
        global cards, card_amount
        cards = []
        # ensure card amount matches number of term/definition cards
        card_amount = len(term_defs) * 2

        for idx, td in enumerate(term_defs):
            term_img, def_img = td
            # store the image filename in card[3]
            cards.append(["pair-%s" % idx, "deselected", "visible", term_img])
            cards.append(["pair-%s" % idx, "deselected", "visible", def_img])

        renpy.random.shuffle(cards)

    def select_card(card_index):
        global selected_cards
        global match_found

        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
            match_found = True
    
    def deselect_cards():
        global selected_cards

        if len(selected_cards) == 2:
            for card in cards:
                if card[1] == "selected":
                    card[1] = "deselected"
        selected_cards = []

    def hide_matches():
        global selected_cards
        global match_found
        global hidden_cards

        cards[selected_cards[0]][2] = "hidden"
        cards[selected_cards[1]][2] = "hidden"
        hidden_cards += 2
        deselect_cards()
        match_found = False

    def reset_memory_game():
        global match_found
        global hidden_cards

        match_found = False
        hidden_cards = 0
        randomize_cards()
    
    #puzzle
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x,end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)

    def piece_drop(dropped_on,dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x,dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("".join([cafeday]))
        

    
transform card_fadein:
    alpha 0.0
    easein 0.5 alpha 1.0

screen memory_game:
    image "bg library.jpg"
    grid int(card_amount/card_rows) card_rows:
        align(0.5, 0.5)
        spacing 5
        for u, card in enumerate(cards):
            # face-down card (click to reveal)
            if card[1] == "deselected" and card[2] == "visible":
                imagebutton idle "cards/1.png" sensitive If(len(selected_cards) !=2, True, False) action Function(select_card, card_index =u) at card_fadein
            # revealed: show the term or the definition as an image
            elif card[1] == "selected" and card[2] == "visible":
                vbox at card_fadein:
                    spacing 2
                    add card[3] xalign 0.5 yalign 0.5
            else:
                null    
    if match_found:
        timer 1.0 action Function(hide_matches) repeat True
    elif len(selected_cards) ==2:
        timer 1.0 action Function(deselect_cards) repeat True
    elif hidden_cards == card_amount:
        $ card_amount = 12
        $card_rows = 3
        $cards = []
        $selected_cards = []
        $hidden_cards = 0
        $match_found = False
        timer 0.5 action [Function(reset_memory_game),Jump("".join([libraryday]))] repeat False
# ...existing code...



screen puzzle:
    image "background.png"
    frame:
        background "puzzle-frame.png"
        xysize full_page_size
        anchor (0.5, 0.5)
        pos(650, 535)

    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5,0.5)
                focus_mask True
                drag_raise True
                image "pieces/piece-%s.png" % (i + 1)
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5,0.5)
                focus_mask True
                image "pieces/piece-%s.png" % (i + 1) alpha 0.0




label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Return(1) )
    # the "key detector" (ends qte_event by returning 1)

    text "Score: [score]":
        pos (100,100)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            #outlines [ (2,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%

label debate:
    $ import time
    $ score = 0
    $ arr_keys = ["e","t","y","u","i","g","h","j","k","x","c","b","n","m"]
    $ start_time = time.time()

    while time.time() - start_time < 30.0:
        call qte_setup(0.8, 0.8, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        if cont == 1:
            $ score += 1
        else:
            $ score -= 1

    "Time's up. Final score: [score]"
    jump expression "" + debateindex


