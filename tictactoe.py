board = [" "]  * 9

ai_symbol = "X"
user_symbol = "O"


def check_result(board):
    if board[0] == board[1] == board[2] and board[0] != " ":
        return board[0]
    if board[3] == board[4] == board[5] and board[3] != " ":
        return board[3]
    if board[6] == board[7] == board[8] and board[6] != " ":
        return board[6]
    if board[0] == board[3] == board[6] and board[0] != " ":
        return board[0]
    if board[1] == board[4] == board[7] and board[1] != " ":
        return board[1]
    if board[2] == board[5] == board[8] and board[2] != " ":
        return board[2]
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    if " " not in board:
        return "draw"
    return None

result = check_result(board)


def get_human_function(board, user_symbol):
    while True:
        try:
            get = int(input("Please chose an answer from 1-9: "))
            index = get - 1
            if index < 0 or index > 8:
                print("Please enter a number from 1-9. ")
                continue
            if board[index] != " ":
                print("The position is captured, try again. ")
                continue
            board[index] = user_symbol
        except ValueError:
            print("Enter an intiger.")
            continue 
        break
    return index



def display_board(board):
    return f""" 
 {board[0]} | {board[1]} | {board[2]}
-----------
 {board[3]} | {board[4]} | {board[5]} 
-----------
 {board[6]} | {board[7]} | {board[8]}
\r
"""

scores = (-1, 0, 1)

def ttt_minimax(board, is_max, comp_sym, usr_sym):
    result = check_result(board)
    if result == comp_sym: return 1
    if result == usr_sym: return -1
    if result == "draw": return 0
    if is_max:
        best = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = comp_sym
                score = ttt_minimax(board, False, comp_sym, usr_sym)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = usr_sym
                score = ttt_minimax(board, True, comp_sym, usr_sym)
                board[i] = " "
                best = min(best, score)
        return best

def get_best_move(board, comp_sym, usr_sym):
    best_score = -999
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = comp_sym
            score = ttt_minimax(board, False, comp_sym, usr_sym)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


while result is None:
    print(display_board(board))
    move = get_best_move(board, ai_symbol, user_symbol)
    board[move] = ai_symbol
    result = check_result(board)
    if result is not None:
        break 

    print(display_board(board))
    get_human_function(board, "O")
    result = check_result(board)
    if result is not None:
        break
    
print(f"\nResult: {result}\n", display_board(board))
