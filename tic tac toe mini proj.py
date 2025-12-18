def display_board(board):
    print("\n" + "="*13)
    for row in range(3):
        print("|", end="")
        for col in range(3):
            print(f" {board[row][col]} ", end="|")
        print("\n" + "="*13)

def player_input(player, board):
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
                
            if board[row][col] != " ":
                print("That position is already taken! Try again.")
                continue
                
            board[row][col] = player
            break
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def check_win(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return board[row][0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    2
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return None  
    
    return "Tie"

def play():
    print("="*40)
    print("Welcome to Tic Tac Toe!")
    print("="*40)
    print("\nInstructions:")
    print("- Players take turns entering row and column numbers (0-2)")
    print("- Player X goes first")
    print("- Enter 0, 1, or 2 for row and column")
    
   
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Game loop
    current_player = "X"
    game_over = False
    
    while not game_over:
        display_board(board)
        player_input(current_player, board)
        
        result = check_win(board)
        
        if result:
            display_board(board)
            if result == "Tie":
                print("\nIt's a tie!")
            else:
                print(f"\nPlayer {result} wins!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
    
    # Ask if players want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play()
    else:
        print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    play()