import random

# Defining some variables.
game_list = ['Snake', 'Water', 'Gun']
player_points = 0
computer_points = 0

for i in range(10):
    # Explicitly defined here for change in it, on each iteration.
    computer_choice = random.randint(0, 2)
    computer = game_list[computer_choice]
    ask_player = input('Snake, Water, or Gun?: ').capitalize()  # Since user can enter lower or uppercase letters.
    if ask_player in game_list:
        if ask_player == computer:
            print(f'Player: {ask_player}, and Computer: {computer}')
            print("It's a tie!")
            computer_points += 1
            player_points += 1
        else:
            if ask_player == 'Snake' and computer == 'Water':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You win, and got 1 point!')
                player_points += 1
            elif ask_player == 'Water' and computer == 'Gun':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You win, and got 1 point!')
                player_points += 1
            elif ask_player == 'Gun' and computer == 'Snake':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You win, and got 1 point!')
                player_points += 1
            elif computer == 'Snake' and ask_player == 'Water':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You lose, and computer got 1 point!')
                computer_points += 1
            elif computer == 'Water' and ask_player == 'Gun':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You lose, and computer got 1 point!')
                computer_points += 1
            elif computer == 'Gun' and ask_player == 'Snake':
                print(f'Player: {ask_player}, and Computer: {computer}')
                print('You lose, and computer got 1 point!')
                computer_points += 1
    else:
        print('Something went wrong!')
        print(computer_points)

# Explicitly defined here, because the last iteration of the for loop executes only one condition.
if computer_points > player_points:
    print(f'Player: {player_points}, and Computer: {computer_points}')
    print('You have lost the game!')
elif player_points > computer_points:
    print(f'Player: {player_points}, and Computer: {computer_points}')
    print('You have won the game!')
elif player_points == computer_points:
    print(f'Player: {player_points}, and Computer: {computer_points}')
    print("No one wins! It's a draw!")
