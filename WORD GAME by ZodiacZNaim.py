def intro(): # this gets printed when you enter the game
    print("""
    WORD GAME
    To play the game enter PLAY.
    To see the help document enter HELP.
    To quit the game enter QUIT.
    """)
    print()
def game_intro(): # this is how you need to play the game
    print()
    print("""
    Welcome to WROD GAME.
    The way you play this game is really simple. It got 2 modes namely Multiplayer and Singleplayer.
    Singleplayer mode is just for practice purposes. It is recomended to play in Multiplayer mode.

    The game works like this: 
    You will enter a word first and depending on the last letter of that word the person whose turn it is next has to say
    a word that starts with the last letter of the previous word entered. This way the game continues.
    If a player is unable to say a word within your given time or any other conditions you set you can strike a player.
    When a player is striked he gets eleminated from the game and the rest of the players continue playing the game.
    When there is only one player left he gets declared the winner and the game ends.

    This is pretty much how you play the word game.
    """)
    print()
def game_start(): # this is printed when the game starts
    print()
    print("""
    Alright let's get started.
    Please use UPPERCASE LETTERS for entering values.
    To read the help document and see all the commands enter GAMEHELP.
    """)
    print()
def game_quit(): # this is the function for quiting the game
    print("""
    Would you like to save the game-data in a separate file?
    Enter "Y" to continue and
    Enter "N" to quit.
    """)
    while True:
        game_quit_conf = input(": ").upper()
        if game_quit_conf == "Y": # still cant install a system how to save all the playernames in an independent list and print it
            print("""
            An external file is going to be created in order to save the game data.
            The file will contain the name of the players that played the game and the winner if it was in multiplayer mode.
            Then all the words used in-game will be listed.
            """)
            print()
            filename = input("Give a name to the file you want to save: ")
            file = open(str(filename + ".txt"), "w")
            file.writelines("The gamesession was named: \n")
            file.writelines(filename)
            if play_type == "M":
                if len(winner) == 1:
                    file.writelines("\n The player that won the round was: ")
                    file.writelines(str(winner))
            file.writelines("\n The words used in game were: \n")
            file.writelines("\n")
            file.write(str(words))
            file.close()
            print()
            print("The list have been saved in the file ", filename, " in the defult directory.")
            print()
            print("The words that have been saved into the file are: ")
            print()
            print(words)
            print()
            break       
        if game_quit_conf == "N":
            break
def strike(): # use this to strike players
    while True:
        print("""
        Striking a player will eleminate him or her from the game.
        Are you sure you want to continue?
        Enter "Y" to continue and
        Enter "N" to resume the game.
        """)
        strike_inp = input(": ").upper()
        if strike_inp != "":
            if strike_inp == "Y":
                strike_inp = input("Strike: ").upper()
                if strike_inp in players:
                    print()
                    print(strike_inp, " has been removed from the game.")
                    players.remove(strike_inp)
                    print()
                    break
                if strike_inp not in players:
                    print("Player not found. Game resumed.")
                else:
                    print("Invalid input.")
                    print("Game Resumed.")
                    break
            if strike_inp == "N":
                print("Player wasn't striked game resumed.")
                nxtp = "prvp"
                break
def gamereview(): # the quit from game function
    while True:    
        gamereview_inp = input(": ").upper()
        if gamereview_inp != "":
            if gamereview_inp == "Y":
                print("Thanks for your effort but I don't know how to gather feedback.")
                print("Thanks for playing.")
                break
            if gamereview_inp == "N":
                print("""
                Thanks for playing!

                Made by ZodiacZNaim.

                Visit me at ZodiacZNaim in YouTube.
                """)
                break
def help_doc(): # this is the game commands file
    print()
    print("""
    This is your help document!

    Follow the instructions that are given in the menus correctly and avoid inputting incorrect values.

    !!! It is extremely important to use UPPERCASE LETTERS at all times or else the game might break. !!!

    In-game commands:
    1. QUITGAME = Quits the game to the MAIN MENU.
    2. RMLAST = Removes the last registered word in case of any typing mistakes.
    3. PLAYERSLEFT = Print the current list of players that are in game.
    4. PRINTWORDS = Print the words that have been registered so far.
    5. HOWTOPLAY = Print the methods to play this game.

    """)
    print()
while True: # this is the actual game
    words   = [] # this contains all the words that are used in game
    players = [] # this stores the name of the players
    winner  = [] # this is the name of the game winner
    intro()
    uip_ope = input("What do you want to do: ").upper()
    print()
    if uip_ope == "HELP": 
        help_doc()
    if uip_ope == "QUIT":
        print("Quitting the game.")
        print("""
        Would you like to leave a review on this game?
        Enter "Y" for writing a review and
        Enter "N" for quitting the game.
        """)
        gamereview()     
        break
    if uip_ope == "PLAY":
        while True:
            print("Do you want to play in SinglePlayer or in Multiplayer? S / M to confirm. Or QUIT to quit to main menu.")
            print()
            play_type = input(": ").upper()
            if play_type == "":
                print("!!! Please enter a valid character. !!!")
                print()
            if play_type == "QUIT":
                break
            if play_type != "":
                if play_type == "S": # this is the singleplayer gamemode
                    words.clear()
                    game_start()
                    while True:
                        uip_w = input("Enter first word: ").upper()
                        print()
                        if uip_w == "":
                            print("!!! Please input valid charecters. !!!")
                            print()
                        if uip_w != "":
                            words.append(uip_w)
                            print("Registered: ", uip_w)
                            last_word = words[-1]
                            last_letter = last_word[-1]
                            break
                    while True:
                        print("Enter a word with ", "'", last_letter,"'")
                        print()
                        uip_w = input(": ").upper()
                        print()
                        if  uip_w == "QUITGAME":
                            print("""
                                Quitting the game right now will delete all it's progress.
                                Are you sure you want to continue? 
                                Enter "Y" for quitting the game and 
                                Enter "N" for resuming the game. 
                                """)
                            quitgame_conf = input(": ").upper()
                            if quitgame_conf != "":
                                if quitgame_conf == "Y":
                                    game_quit()
                                    print("Quitting back to main menu.")
                                    print()
                                    break
                                if quitgame_conf == "N":
                                    print("Game resumed.")
                        elif uip_w == "PRINTWORDS":
                            print("The words that have been used in this game session so far are: ")
                            print()
                            print(words)
                            print()
                        elif uip_w == "RMLAST":
                            if len(words) <= 1:
                                print("Can't remove the first word. Please quit the game to reset.")
                            else:
                                print()
                                print("Word removed: ", last_word)
                                print()
                                words = words[:-1]
                                last_word = words[-1]
                                last_letter = last_word[-1]
                        elif uip_w == "GAMEHELP":
                            help_doc()
                        elif uip_w == "HOWTOPLAY":
                            game_intro()
                        else:
                            if uip_w in words:
                                print("!!! This word already exists. Please choose a different one. !!!")
                            elif uip_w[0] != last_letter:
                                print()
                                print("!!! Word doesn't start with ", "'", last_letter, "' !!!")
                                print()
                                print()
                            elif uip_w[0] == last_letter:
                                words.append(uip_w)
                                print("Registered: ", uip_w)
                                last_word = uip_w
                                last_letter = last_word[-1]
                if play_type == "M": # this is the multiplayer gamemode
                    words.clear()
                    while True:
                        players.clear()
                        print()
                        print("!!! Please enter the values carefully. !!!")
                        print()
                        players_num = input("Enter the number of players: ")
                        print()
                        if players_num != "": # still cant figure out how to stop people from entering non integer values 
                            if int(players_num) <= 1:
                                print("!!! Multiplayer mode is ment to be played by at least 2 people. !!!")
                                print("!!! You will win by default once you enter the game. !!!")
                                break
                            if int(players_num) >= 2:
                                for i in range(int(players_num)):
                                    players.append(input("Enter name of the player: "))
                                print()
                                print("People that are currently playing the game are: ")
                                print()
                                for player in players:
                                    print(player)
                                print()
                                print("Are you sure these people are playing?")
                                print("To edit the list enter EDIT.")
                                print("To continue press Enter.")
                                edit_conf = input(": ").upper()
                                if edit_conf == "EDIT":
                                    print("Re-enter all the information.")
                                if edit_conf == "":
                                    game_start()
                                    break
                    while True:
                        uip_w = input("Enter first word: ").upper()
                        print()
                        if uip_w == "":
                            print("!!! Please input valid charecters. !!!")
                            print()
                        if uip_w != "":
                            words.append(uip_w)
                            print("Registered: ", uip_w)
                            last_word = words[-1]
                            last_letter = last_word[-1]
                            break
                    i = -1
                    nxtp = "cp"
                    while True: 
                        if nxtp == "prvp": 
                            i = (i-1)%len(players)
                        if nxtp != "prvp":
                            i = (i+1)%len(players)
                        print("Enter a word with ", "'", last_letter,"'")
                        print()
                        print(players[i], ": ")
                        uip_w = input().upper()
                        print()
                        if uip_w == "":
                            i = (i-1)%len(players) # having issues with player turns after RMLAST
                        if uip_w != "":
                            if  uip_w == "QUITGAME":
                                print("""
                                    Quitting the game right now will delete all it's progress.
                                    Are you sure you want to continue? 
                                    Enter "Y" for quitting the game and 
                                    Enter "N" for resuming the game. 
                                    """)
                                quitgame_conf = input(": ").upper()
                                if quitgame_conf != "":
                                    if quitgame_conf == "Y":
                                        game_quit()
                                        print("Quitting back to main menu.")
                                        print()
                                        break
                                    if quitgame_conf == "N":
                                        print("Game resumed.")
                            elif uip_w == "PRINTWORDS":
                                print("The words that have been used in this game session so far are: ")
                                print()
                                print(words)
                                print()
                            elif uip_w == "STRIKEPLAYER":
                                strike()
                            elif uip_w == "GAMEHELP":
                                help_doc()
                            elif uip_w == "HOWTOPLAY":
                                game_intro()
                            elif len(players) == 1:
                                winner.append(players)
                                print()
                                print("!!!                                             !!!")
                                print("The game has ended and the winner is ", winner)
                                print("!!!                                             !!!")
                                print()
                                game_quit()
                                break
                            elif uip_w == "RMLAST":
                                if len(words) <= 1:
                                    print("Can't remove the first word. Please quit the game to reset.")
                                else:
                                    print()
                                    print("Word removed: ", last_word)
                                    print()
                                    words = words[:-1]
                                    last_word = words[-1]
                                    last_letter = last_word[-1]
                                    nxtp = "prvp"                            
                            else:
                                if uip_w[0] != last_letter:
                                    print()
                                    print("!!! Word doesn't start with ", "'", last_letter, "' !!!")
                                    print()
                                    print()
                                    i = (i-1)%len(players)
                                elif uip_w in words:
                                    print("!!! This word already exists. Please choose a different one. !!!")
                                    i = (i-1)%len(players)
                                elif uip_w[0] == last_letter:
                                    words.append(uip_w)
                                    print("Registered: ", uip_w)
                                    last_word = uip_w
                                    last_letter = last_word[-1]
                                    nxtp = "cp"