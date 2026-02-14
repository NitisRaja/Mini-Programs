###### ROCK-PAPER-SCISSORS-LIZARD-SPOCK Game ######

print("###### ROCK, PAPER, SCISSORS, LIZARD, SPOCK ######")
rounds = 0
wins = loses = ties = 0
moves = ['r','p','sc','sp','l']  # r->p->sc->sp->l this is the winning cycle
moves_map = {
    0:'ROCK',
    1:'PAPER',
    2:'SCISSOR',
    3:'SPOCK',
    4:'LIZARD'
}

while True:
    print(f"\nTotal Rounds played: {rounds}")
    print(f"Wins: {wins} | Loses: {loses} | Ties: {ties}")
    user_input = input("Enter your move: (r)ock (p)aper (sc)issor (l)izard (sp)ock or (q)uit\n>").lower()

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
    c_move = randint(0,4) # computer's move
    print(f"{moves_map[p_move]} vs {moves_map[c_move]}")

    # Evaluate winner
    result = (p_move - c_move) % 5
    if result==3 or result==1:
        print("You WIN")
        wins += 1
    elif result==4 or result==2:
        print("You LOSE")
        loses += 1
    else:
        print("Its a TIE")
        ties += 1
    
    # Logic behind this evaluation approach
    # rock-paper-scissor-spock-lizard has a circular winning property 
    # where each move is beaten by the one immediately following it
    # result = (p_move - c_move) % 5
    # diff can be in the interval [-4, 4]
    # as denominator is +5, mod will be in the interval [0,4]
    # this modulo operation wraps our numbers around a circle
    # where the result tells us the "distance" forward in the winning cycle
    # winning cyle: r->p->sc->sp->l->r->p->sc->sp->l
    # 4 => p is 4a,1b = p loses
    # 3 => p is 3a,2b = p wins
    # 2 => p is 2a,3b = p loses
    # 1 => p is 1a,4b = p wins
    # so, FOR CIRCULAR LOGIC - USE MODULO FOR BUILDING THE CYCLE