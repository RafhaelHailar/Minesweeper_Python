import keyboard
import os


BOARD = []
column = 30
row = 30

CURSOR = [10,10]
is_choosing = False

is_called = False

def create_board():
  for y in range(0,column):
      row_items = []
      for x in range(0,row):
         row_items.append(" . ")
      BOARD.append(row_items)

def draw_board():
    for y in range(0,column):
        row_items = ""
        for x in range(0,row):
           row_items += BOARD[y][x]
        print(row_items)

def update_board():
    for y in range(0,column):
        for x in range(0,row):
            BOARD[y][x] = " . "

def draw_cursor():
    global is_called

    if is_called:
        return

    update_board()

    y = CURSOR[1]
    x = CURSOR[0]

    BOARD[y][x] = "[.]"
    
    clear_screen()
    draw_board()


def update_cursor():
    global is_choosing

    key = None
    if not(is_choosing):
        key = keyboard.read_event()
    
    if key != None:
        if key.event_type == "down":
            if key.name == "a" and CURSOR[0] != 0:
                CURSOR[0] -= 1
            elif key.name == "d" and CURSOR[0] != row - 1:
                CURSOR[0] += 1
            elif key.name == "w" and CURSOR[1] != 0:
                CURSOR[1] -= 1
            elif key.name == "s" and CURSOR[1] != column - 1:
                CURSOR[1] += 1
            elif key.name == "enter":
                is_choosing = True
                print("Choose: ")
                print(" [x] Explode \n[y] Flag")
        if not(is_choosing):
            draw_cursor()

def clear_screen():
    os.system("cls")

def init():
    create_board()
    draw_board()
    update()

def update():
    global is_called
    while True:
        update_cursor()
init()
