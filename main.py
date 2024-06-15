import random
win = ""
vals = [1,2,3,4,"X",6,7,8,9]
def get_ops(vals):
    ops = list()
    for val in vals:
        if val == "O":
            continue
        elif val == "X":
            continue
        else:
            ops.append(val)
    return ops
def print_board(vals):
    board = f"""+-------+-------+-------+
|       |       |       |
|   {vals[0]}   |   {vals[1]}   |   {vals[2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {vals[3]}   |   {vals[4]}   |   {vals[5]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {vals[6]}   |   {vals[7]}   |   {vals[8]}   |
|       |       |       |
+-------+-------+-------+"""
    print(board)
def comp(vals):
    move = random.choice(get_ops(vals))
    return move
def place_usr(move,vals):
    vals[move-1] = "O"
    return vals
def place(move,vals):
    vals[move-1] = "X"
    return vals
def winner(vals):
    u = "O"
    u = [u, u, u]
    b = "X"
    b = [b, b, b]
    ret = ""
    
    if vals[:3] == u:
        return "user"
    elif vals[3:6] == u:
        return "user"
    elif vals[6:] == u:
        return "user"
    elif vals[::3] == u:
        return "user"
    elif vals[1::3] == u:
        return "user"
    elif vals[2::3] == u:
        return "user"
    elif vals[::4] == u:
        return "user"
    elif vals[2::2][:3] == u:
        return "user"
        
    if vals[:3] == b:
        return "bot"
    elif vals[3:6] == b:
        return "bot"
    elif vals[6:] == b:
        return "bot"
    elif vals[::3] == b:
        return "bot"
    elif vals[1::3] == b:
        return "bot"
    elif vals[2::3] == b:
        return "bot"
    elif vals[::4] == b:
        return "bot"
    elif vals[2::2][:3] == b:
        return "bot"
    return ""
    
        
while win == "":
    try:
        print_board(vals)
        usr = int(input("Pick a value from the board to make a placement (must be a integer on board)!"))
        if usr not in get_ops(vals):
            print("Not on board!")
            continue
        vals = place_usr(usr,vals)
        win = winner(vals)
        if win != "":
            break
        vals = place(comp(vals),vals)
        win = winner(vals)
        if win != "":
            break
    except ValueError:
        print("Invalid input")
print_board(vals)
print("the", win, "has won!")
