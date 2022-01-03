import random
def hangman() :
    words = ['world','england','india','oh']
    word = random.choice(words)
    turns = 10
    guessmade = ''
    a = set ('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0 :
        main_word =""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word == word:
            print(main_word)
            print("you won!!")
            break
        print("guess the words", main_word)
        guess = input()
        if guess in a :
            guessmade = guessmade + guess
        else:
            print("enter valid character")
            guess = input()
        if guess not in word:
            turns = turns-1
            if turns==9:
                print("9 turns left!!")
                print("-----------------")
            if turns==8:
                print("8 turns left!!")
                print("-------------")
                print("      o      ")
            if turns==7:
                print("7 turns left!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
            if turns==6:
                print("6 turns left!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
                print("     /       ")
            if turns==5:
                print("5 turns left!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
                print("     / \     ")
            if turns==4:
                print("4 turns left!!")
                print("-------------")
                print("     \o      ")
                print("      |      ")
                print("     / \     ")
            if turns==3:
                print("3 turns left!!")
                print("-------------")
                print("     \o/     ")
                print("      |      ")
                print("     / \     ")
            if turns==2:
                print("2 turns left!!")
                print("-------------")
                print("     \o/  |  ")
                print("      |      ")
                print("     / \     ")
            if turns==1:
                print("1 turns left!!")
                print("-------------")
                print("     \o/__|  ")
                print("      |      ")
                print("     / \     ")
            if turns==0:
                print("0 turns left!!")
                print("you loss the game. THE MAN DIED")
                print("-------------")
                print("      o __|  ")
                print("     /|\     ")
                print("     / \     ")
                break
name = input("ENTER YOUR NAME : ")
print("Welcome",name,"!")
print("-----------------------------")
print("try to guess the word in less than 10 attempts")
hangman()