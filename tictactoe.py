from random import randrange

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

first_play = True

def display_board(board):
    print("+-------+-------+-------+\n" \
          "|       |       |       |\n" \
         f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n" \
          "|       |       |       |\n" \
          "+-------+-------+-------+\n" \
          "|       |       |       |\n" \
         f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n" \
          "|       |       |       |\n" \
          "+-------+-------+-------+\n" \
          "|       |       |       |\n" \
         f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n" \
          "|       |       |       |\n" \
          "+-------+-------+-------+\n" \
    )

#Player movement
def enter_move(board):
    try:
        free_fields = make_list_of_free_fields(board)

        if len(free_fields) == 0:
            print("There are no places to play")
            return
        
        movement = int(input("Elige la casilla: "))
        x = (movement - 1) // 3
        y = (movement - 1) % 3

        if type(board[x][y]) is int:
            board[x][y] = "O"
        else:
            print("Casilla ocupada")
            enter_move(board)

    except:
        print("Posicion erronea")
        enter_move(board)

#Bot movement
def draw_board(board):
    global first_play
    if first_play:
        board[1][1] = "X"
        first_play = False
    else:
        free_fields = make_list_of_free_fields(board)
        if len(free_fields) == 0:
            print("There are no places to play")
            return
        
        bot = randrange(0, len(free_fields))
        mark = free_fields[bot]
        x = mark[0]
        y = mark[1]

        board[x][y] = "X"

    display_board(board)
    
def make_list_of_free_fields(board):
    free_fields = []

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if type(board[i][j]) is int:
                free_fields.append((i, j))

    return free_fields

def victory_for(board):
    status = 0
    #Horizontal win bot
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        status = 1
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        status = 1
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        status = 1
    #Vertical win bot
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        status = 1
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        status = 1
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        status = 1
    #Diagonal win bot
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        status = 1
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        status = 1
    #Horizontal win player
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        status = 2
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        status = 2
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        status = 2
    #Vertical win player
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        status = 2
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        status = 2
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        status = 2
    #Diagonal win player
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        status = 2
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        status = 2
    elif len(make_list_of_free_fields(board)) == 0:
        status = 3

    return status

while True:
    draw_board(board)
    if victory_for(board) == 1:
        print("Victory for the machine!")
        break

    enter_move(board)
    if victory_for(board) == 2:
        print("You won!")
        break

    display_board(board)
    if victory_for(board) == 3:
        print("DRAW")
        break