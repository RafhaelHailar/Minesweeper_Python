import keyboard
import os


BOARD = []
column = 30
row = 30

CURSOR = [10,10]
choices = ["Dig","Flag","Cancel"]
prompt_choosed = 2 # choosing the 'cancel' by default
choosed = None

f_choices = ["YES","NO LOL"]
f_choosed = 1 # default to 'no'

is_choosing = False
is_finalizing = False


# 0 digged, 1 not digged, 2 flag

def create_board():
  for y in range(0,column):
      row_items = []
      for x in range(0,row):
         row_items.append({
            "item": ".",
            "type": 1
         })
      BOARD.append(row_items)

def draw_board():
    for y in range(0,column):
        row_items = ""
        for x in range(0,row):
           row_items += BOARD[y][x]["item"]
        print(row_items)

def update_board():
    for y in range(0,column):
        for x in range(0,row):
             cell_type = BOARD[y][x]["type"]
             display = "."

             cursor_x = CURSOR[0]
             cursor_y = CURSOR[1]

             if cell_type == 0:
                 display = "1"
             elif cell_type == 2:
                 display = "$"

             if not(cursor_x == x and cursor_y == y):
                 if cell_type == 0:
                     display = "(" + display + ")"
                 else:
                     display = " " + display + " "

             BOARD[y][x]["item"] = display

def draw_choice():
    if not(is_choosing): 
        return;
    print("\nChoose Action My Man:")
    
    for i in range(0,len(choices)):
        choice = choices[i]
        if i == prompt_choosed:
            print(" [" + choice + "]")
        else:
            print("  " + choice)

def draw_finalize():
    if not(is_finalizing):
        return;
    print("Are you really sure?")
    
    for i in range(0,len(f_choices)):
        choice = f_choices[i]
        if i == f_choosed:
            print(" [" + choice + "]")
        else:
            print("  " + choice)

def draw_cursor():
    update_board()

    y = CURSOR[1]
    x = CURSOR[0]

    item = BOARD[y][x]["item"].strip() 
    BOARD[y][x]["item"] = "[" + item + "]"
    
    clear_screen()
    draw_board()
    draw_choice()
    draw_finalize()

def move_cursor(add_x,add_y):
    x = CURSOR[0]
    y = CURSOR[1]

    edge_x = row - 1
    edge_y = column - 1

    new_x = x + add_x
    new_x %= row
    new_x = edge_x if new_x < 0 else new_x 
    
    new_y = y + add_y
    new_y %= column
    new_y = edge_y if new_y < 0 else new_y 

    CURSOR[0] = new_x
    CURSOR[1] = new_y


   # What should I have written
   # if add_x == -1:
   #     if x == 0:
   #         CURSOR[0] = edge_x
   #     else:
   #         CURSOR[0] -= 1
   # elif add_x == 1:
   #     if x == edge_x:
   #         CURSOR[0] = 0
   #     else:
   #         CURSOR[0] += 1


def move_choice(x):
    global prompt_choosed

    new_choosed = prompt_choosed + x

    new_choosed %= len(choices)
    new_choosed = 2 if new_choosed < 0 else new_choosed

    prompt_choosed = new_choosed

def move_finalize(x):
    global f_choosed

    new_choosed = f_choosed + x

    new_choosed %= len(f_choices)
    new_choosed = 2 if new_choosed < 0 else new_choosed

    f_choosed = new_choosed


def make_choice():
    global is_choosing,prompt_choosed,is_finalizing,choosed

    print("You choose:")
    print(choices[prompt_choosed])

    if prompt_choosed == 0:
      choosed = 0 
    elif prompt_choosed == 1:
      choosed = 1

    if prompt_choosed != 2:
       is_finalizing = True

    # reset values
    is_choosing = False
    prompt_choosed = 2

def make_finalize():
    global is_finalizing,choosed

    if f_choosed == 0:
        finalize_choice()

    is_finalizing = False
    choosed = None

def finalize_choice():
    x = CURSOR[0]
    y = CURSOR[1]
    cell_type = BOARD[y][x]["type"]
    new_type = cell_type

    if choosed == 0:
        new_type = 0
    elif choosed == 1:
        new_type = 2

    BOARD[y][x]["type"] = new_type
    
def is_digged():
    x = CURSOR[0]
    y = CURSOR[1]

    return BOARD[y][x]["type"] == 0

def update_cursor():
    global is_choosing

    key = keyboard.read_event()
    
    if key.event_type == "down":
        if not(is_choosing or is_finalizing): 
            if key.name == "a":
               move_cursor(-1,0) 
            elif key.name == "d":
               move_cursor(1,0)
            elif key.name == "w":
               move_cursor(0,-1)
            elif key.name == "s":
               move_cursor(0,1)
            elif key.name == "enter":
                if not(is_digged()): 
                    is_choosing = True
        elif not(is_finalizing): 
            if key.name == "w":
               move_choice(-1)
            elif key.name == "s":
               move_choice(1)
            elif key.name == "enter":
               make_choice()
        else:
            if key.name == "w":
               move_finalize(-1)
            elif key.name == "s":
               move_finalize(1)
            elif key.name == "enter":
               make_finalize()

    draw_cursor()

def clear_screen():
    os.system("cls")


"""
<<<<<<<<<<<<<<<<<<<|
UTILS<<<<..........|
<<<<<<<<<<<<<<<<<<<|
"""

def init():
    create_board()
    draw_board()
    update()

def update():
    global is_called
    draw_cursor()
    while True:
        update_cursor()
init()
