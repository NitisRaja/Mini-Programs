###### ROCK-PAPER-SCISSORS Game ######

print("###### ROCK, PAPER, SCISSORS ######")
rounds = 0
wins = loses = ties = 0
moves = ['r','p','s']
moves_map = {
    0:'ROCK',
    1:'PAPER',
    2:'SCISSOR'
}

while True:
    print(f"\nTotal Rounds played: {rounds}")
    print(f"Wins: {wins} | Loses: {loses} | Ties: {ties}")
    user_input = input("Enter your move: (R)ock (P)aper (S)cissor or (Q)uit\n>").lower()

    if (user_input=='q'):
        print("Thank You for playing the game. Have a nice day:)")
        break
    elif (user_input not in moves):
        print("You've entered an invalid input")
        continue
    else:
        rounds +=1
    
    # convert moves to numbers
    p_move = moves.index(user_input) # player's move
    from random import randint
    c_move = randint(0,2) # computer's move
    print(f"{moves_map[p_move]} vs {moves_map[c_move]}")

    # Evaluate winner
    result = (p_move - c_move) % 3
    if result == 1:
        print("You WIN")
        wins += 1
    elif result == 2:
        print("You LOSE")
        loses += 1
    else:
        print("Its a TIE")
        ties += 1
    
    # Logic behind this evaluation approach
    # rock-paper-scissor has a circular winning property 
    # where each move is beaten by the one immediately following it
    # result = (p_move - c_move) % 3
    # diff can be in the interval [-2, 2]
    # as denominator is +3, mod will be in the interval [0,2]
    # this modulo operation wraps our numbers around a circle
    # where the result tells us the "distance" forward in the winning cycle
    # 1 => p is 1 step ahead in the winning cyle
    # 2 => p is 2 steps ahead, which is 1 step behind in the cycle
    # so, FOR CIRCULAR LOGIC - USE MODULO FOR BUILDING THE CYCLE

    # version using purely substraction alone
    # moves = ['r','p','s','r','p']  # build circle explicitly
    # p_move = moves.index(user_input)
    # c_move = randint(p_move, p_move+2)
    # result = c_move - p_move  # always +ve cuz c_move will be greater always
    # diff = 1 => c_move 1 step ahead so p_move loses
    # diff = 2 => c_move 2 steps ahead (ie c 1 step behind p in cycle) so p_move wins