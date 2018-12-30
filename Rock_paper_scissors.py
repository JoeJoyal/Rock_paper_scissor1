import os

#validate 
def validate_user_input(user_input,first_player,second_player):
    valid_input =['r','p','s']
    user_input =user_input.lower()
    user_input_letter_separation =list(user_input)
    if(user_input_letter_separation[0] in valid_input):
        return user_input_letter_separation[0]
    else:
        get_user_input(first_player,second_player)

#User inputs
def getting_name_from_user():
    first_player = str(input("Enter 1st player :"))
    second_player = str(input("Enter 2nd player :"))
    get_user_input(first_player,second_player) 

#Choose the events
def get_user_input(first_player,second_player):
    print("Select the choice from the following list :- \n1.Rock \n2.Paper \n3.Scissors")
    print(first_player)
    player_1_choice = str(input("Enter any one of the item avaible from the list please Enter your choice here :"))
    player_1_choice =validate_user_input(player_1_choice,first_player,second_player)
    os.system("cls")
    print("Enter any one of the following in the list avaible below inorder to play the game ")
    print(second_player)
    player_2_choice = str(input("Enter any one of the item avaible form the list please Enter your choice here :"))
    player_2_choice =validate_user_input(player_2_choice,first_player,second_player)
    Test(player_1_choice,player_2_choice,first_player,second_player)

#conditions
def Test(player_1_choice,player_2_choice,first_player,second_player):
    concatennated_user_input = player_1_choice + player_2_choice
    if(player_1_choice == player_2_choice):
        print("THE MATCH GET DRAW")
    elif(("rs"==concatennated_user_input)or ("pr"==concatennated_user_input)or("ps"==concatennated_user_input)or("sp"==concatennated_user_input)):
        print(first_player)
        print("is the winner...\n")
        print(second_player)
        print("is the runner in this match...")

    else:
        print(second_player)
        print("is the winner...\n")
        print(first_player)
        print("is the runner in this match...")


getting_name_from_user()