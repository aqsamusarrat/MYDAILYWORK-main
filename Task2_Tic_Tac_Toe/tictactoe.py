import random

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

scores = {"Human": 0, "AI": 0, "Draw": 0}

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_combos:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None

def minimax(board, depth, is_max):
    result = check_winner(board)
    if result == AI:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if result == "Draw":
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, depth+1, False))
                board[i] = EMPTY
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, minimax(board, depth+1, True))
                board[i] = EMPTY
        return best

def best_move(board):
    best_score = -1000
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

def ai_move(board, level):
    if level == "easy":
        return random.choice([i for i in range(9) if board[i] == EMPTY])
    elif level == "medium":
        return best_move(board) if random.random() > 0.5 else random.choice([i for i in range(9) if board[i] == EMPTY])
    else:
        return best_move(board)

def play_game():
    board = [EMPTY]*9
    level = input("Choose AI level (easy / medium / hard): ").lower()

    while True:
        print_board(board)
        user = input("Enter position (1-9) or 'hint': ")

        if user == "hint":
            print(f"Suggested move: {best_move(board)+1}")
            continue

        pos = int(user) - 1
        if board[pos] != EMPTY:
            print("Invalid move!")
            continue

        board[pos] = HUMAN
        if check_winner(board):
            break

        board[ai_move(board, level)] = AI
        if check_winner(board):
            break

    print_board(board)
    result = check_winner(board)

    if result == HUMAN:
        print(" You Win!")
        scores["Human"] += 1
    elif result == AI:
        print(" AI Wins!")
        scores["AI"] += 1
    else:
        print(" It's a Draw!")
        scores["Draw"] += 1

    print("Scoreboard:", scores)

while True:
    play_game()
    if input("Play again? (y/n): ").lower() != 'y':
        break
