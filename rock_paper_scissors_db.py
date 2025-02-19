
#?<<<< MohsenPrd: Create DB and table >>>>#?
import sqlite3

connect = sqlite3.connect('rock_paper_scissors.db')
myCursor = connect.cursor()

myCursor.execute('''CREATE TABLE IF NOT EXISTS semi_final (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player1 TEXT,
                    player2 TEXT,
                    player1_choice TEXT,
                    player2_choice TEXT,
                    winner TEXT
                    )''')

myCursor.execute('''CREATE TABLE IF NOT EXISTS final (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player1 TEXT,
                    player2 TEXT,
                    player1_choice TEXT,
                    player2_choice TEXT,
                    winner TEXT
                    )''')

connect.commit()

#?<<<< MohsenPrd: Function for save semi_final results to DB >>>>#?
def save_semi_final(player1, player2, player1_choice, player2_choice, winner):
    
    sql = "INSERT INTO semi_final (player1, player2, player1_choice, player2_choice, winner) VALUES (?, ?, ?, ?, ?)"
    val = (player1, player2, player1_choice, player2_choice, winner)
    myCursor.execute(sql, val)
    connect.commit()
    
#?<<<< MohsenPrd: Function for save final results to DB >>>>#?
def save_final(player1, player2, player1_choice, player2_choice, winner):
    
    sql = "INSERT INTO final (player1, player2, player1_choice, player2_choice, winner) VALUES (?, ?, ?, ?, ?)"
    val = (player1, player2, player1_choice, player2_choice, winner)
    myCursor.execute(sql, val)
    connect.commit()


##### rock - paper - scissors #####

b = True
c = True
d = True
e = True
f = True

##############################################################################################################################
########  First group  ########

print ("\nFirst Round Group 1")
a = int(input("\nhow many rounds do you want to play : "))
if a == 0 :
    b = False
player1_score = 0
player2_score = 0

name1 = input("please enter your name : ")
name2 = input("please enter your name : ")
print("\n1) rock\n2) paper\n3) scissors")

while b == True :

    try :
        player_1 = int(input(f"\n{name1} please make your move : "))
        if player_1 > 3 or player_1 < 1 :
            print ("Not in the options !")
            continue
        else :
            pass
        
    except ValueError :
        print ("Only numbers are allowed !")
        continue

    if player_1 == 1:
        player1Move = "rock"
    elif player_1 == 2:
        player1Move = "paper"
    elif player_1 == 3:
        player1Move = "scissors"
    player1 = player1Move
    
    while d == True:
        try :
            player_2 = int(input(f"{name2} please make your move : "))
            if player_2 > 3 or player_2 < 1 :
                print ("Not in the options !")
                continue
            else :
                d = False
                pass
        
        except ValueError :
            print ("Only numbers are allowed !")
            continue
    d = True
    if player_2 == 1:
        player2Move = "rock"
    elif player_2 == 2:
        player2Move = "paper"
    elif player_2 == 3:
        player2Move = "scissors"
    player2 = player2Move
        
    if player1 == "rock" and player2 == "scissors":
        print (f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "rock" and player2 == "paper":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == "paper" and player2 == "rock":
        print(f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "paper" and player2 == "scissors":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == "scissors" and player2 == "paper":
        print(f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "scissors" and player2 == "rock":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == player2:
        print ("\nYou are tied !\n")
        
        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,'Draw')
        
    else:
        print("something went wrong !\n")
    print (50 * "–")
    

    if player1_score == a or player2_score == a :
        b = False
        if player1_score == a :
            print(f"\n{name1} is the winner !")
            winner1 = name1
        elif player2_score == a :
            print(f"\n{name2} is the winner !")
            winner1 = name2
        break
print (" ")
print (120 * "=")

##############################################################################################################################
########  Second group  ########

print ("\n Second Round Group 2 ")
a = int(input("\nhow many rounds do you want to play : "))
if a == 0 :
    b = False
player1_score = 0
player2_score = 0

name1 = input("\nplease enter your name : ")
name2 = input("please enter your name : ")
print("\n1) rock\n2) paper\n3) scissors")
b = True

while b == True :

    try :
        player_1 = int(input(f"\n{name1} please make your move : "))
        if player_1 > 3 or player_1 < 1 :
            print ("Not in the options !")
            continue
        else :
            pass
        
    except ValueError :
     print ("Only numbers are allowed !")
     continue
  
    if player_1 == 1:
     player1Move = "rock"
    elif player_1 == 2:
       player1Move = "paper"
    elif player_1 == 3:
        player1Move = "scissors"
    player1 = player1Move
    while e == True :
        try :
            player_2 = int(input(f"{name2} please make your move : "))
            if player_2 > 3 or player_2 < 1 :
                print ("Not in the options !\n")
                continue
            else :
             e = False
             pass
         
        except ValueError :
         print ("Only numbers are allowed !\n")
         continue
     
    e = True
    if player_2 == 1:
     player2Move = "rock"
    elif player_2 == 2:
        player2Move = "paper"
    elif player_2 == 3:
        player2Move = "scissors"
    player2 = player2Move
        
    if player1 == "rock" and player2 == "scissors":
        print (f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "rock" and player2 == "paper":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == "paper" and player2 == "rock":
        print(f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "paper" and player2 == "scissors":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == "scissors" and player2 == "paper":
        print(f"\n{name1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name1)

    elif player1 == "scissors" and player2 == "rock":
        print(f"\n{name2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,name2)

    elif player1 == player2:
        print ("\nYou are tied !\n")
        
        #?<<<< MohsenPrd: Save semi_final results to DB >>>>#?
        save_semi_final(name1,name2,player1,player2,'Draw')

    else:
        print("something went wrong !\n")
    print (100 * "-")


    if player1_score == a or player2_score == a :
        b = False
        if player1_score == a :
            print(" ")
            print(f"{name1} is the winner !")
            winner2 = name1
        elif player2_score == a :
            print(" ")
            print(f"{name2} is the winner !")
            winner2 = name2
        break
print (" ")
print (120 * "=")

##############################################################################################################################
########  Final  ########

print ("\n Final ")
a = int(input("\nhow many rounds do you want to play : "))
if a == 0 :
 b = False
player1_score = 0
player2_score = 0

print("\n1) rock\n2) paper\n3) scissors")
b = True

while b == True :

    try :
        player_1 = int(input(f"\n{winner1} please make your move : "))
        if player_1 > 3 or player_1 < 1 :
            print ("Not in the options !")
            continue
        else :
            pass
        
    except ValueError :
        print ("Only numbers are allowed !")
        continue

    if player_1 == 1:
        player1Move = "rock"
    elif player_1 == 2:
        player1Move = "paper"
    elif player_1 == 3:
        player1Move = "scissors"
    player1 = player1Move
    
    while f == True :
        try :
            player_2 = int(input(f"{winner2} please make your move : "))
            if player_2 > 3 or player_2 < 1 :
                print ("Not in the options !")
                continue
            else :
                f = False
                pass

        except ValueError :
            print ("Only numbers are allowed !")
            continue
    f = True
    if player_2 == 1:
        player2Move = "rock"
    elif player_2 == 2:
        player2Move = "paper"
    elif player_2 == 3:
        player2Move = "scissors"
    player2 = player2Move
        
    if player1 == "rock" and player2 == "scissors":
        print (f"\n{winner1} wins !\n")
        player1_score = player1_score + 1
        
        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner1)

    elif player1 == "rock" and player2 == "paper":
        print(f"\n{winner2} wins !\n")
        player2_score = player2_score + 1
        
        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner2)

    elif player1 == "paper" and player2 == "rock":
        print(f"\n{winner1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner1)
        
    elif player1 == "paper" and player2 == "scissors":
        print(f"\n{winner2} wins !\n")
        player2_score = player2_score + 1
        
        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner2)
    
    elif player1 == "scissors" and player2 == "paper":
        print(f"\n{winner1} wins !\n")
        player1_score = player1_score + 1

        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner1)

    elif player1 == "scissors" and player2 == "rock":
        print(f"\n{winner2} wins !\n")
        player2_score = player2_score + 1

        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,winner2)
        
    elif player1 == player2:
        print ("\nYou are tied !\n")
        
        #?<<<< MohsenPrd: Save final results to DB >>>>#?
        save_final(winner1,winner2,player1,player2,'Draw')

    else:
        print("something went wrong !\n")
    print (100 * "-")


    if player1_score == a or player2_score == a :
        b = False
        if player1_score == a :
            print(f"\n! {winner1} is the winer !")
            winner3 = winner1
        elif player2_score == a :
            print(f"\n! {winner2} is the winer !")
            winner3 = winner2
        break

input ()


#?<<<< MohsenPrd: Close connection >>>>#?
connect.close()