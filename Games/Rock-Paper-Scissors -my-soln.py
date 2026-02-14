###### ROCK-PAPER-SCISSORS Game ######

print("###### ROCK, PAPER, SCISSORS ######")
rounds = 0
wins = loses = ties = 0
moves = ['r','p','s']
moves_map = {
    '0':'ROCK',
    '1':'PAPER',
    '2':'SCISSOR'
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

    # Evaluate round result
    if p_move == c_move:
        print("Its a TIE")
        ties += 1
        continue
    elif (p_move == 'r' and c_move == 's') or \
         (p_move == 'p' and c_move == 'r') or \
         (p_move == 's' and c_move == 'p'):
           print('You WIN')
           wins += 1
           continue
    else: # all other combinations are lose for player
        print('You LOSE')
        loses += 1
        continue