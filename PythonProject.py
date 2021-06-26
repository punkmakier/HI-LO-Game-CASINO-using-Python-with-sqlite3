import sqlite3
from termcolor import colored
import random
import string

conn = sqlite3.connect('dbCasino.db')
c = conn.cursor()

##DECLARATION

##------>
result =[]
winOrLose =[]
cashintHistory =[]
money_currency =[]
cashoutHistory =[]
betting=[]
bets =[]
money =0

##<------

#<------ DATABASE TABLE --------d>#
c.execute("""CREATE TABLE IF NOT EXISTS dbCasinoTable1(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Unicode TEXT,
            Name    TEXT,
            BET REAL,
            Amount  REAL,
            Action  TEXT,
            Currencies  TEXT,
            Money   REAL,
            STATUS  TEXT
            )""")


#<------ DATABASE TABLE -------->#
c.execute("""CREATE TABLE IF NOT EXISTS dw(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Unicode TEXT,
                Name    TEXT,
                BET     REAL,
                Amount REAL,
                Action TEXT,
                Currencies  TEXT,
                Money   REAL,
                STATUS TEXT)""")
#<------ DATABASE TABLE -------->#

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def random_code(length=32, uppercase=True,numbers=True):
    character_set=''
    if uppercase:
        character_set += string.ascii_uppercase
    if numbers:
        character_set += string.digits

    return ''.join(random.choice(character_set) for i in range(length))
U_Code = random_code(length=5,uppercase=True,numbers=True)

def Delete_manually():
    c.execute("SELECT * FROM dbCasinoTable1")
    if len(c.fetchall()) == 0:
        print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
        print(color.BOLD+colored(color.RED+"System: There is no Data to Delete!")+color.END)
        print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")

    else:
        while True:
            c.execute("SELECT * FROM dbCasinoTable1")
            print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
            print('\033[1m' + colored('OPENING DATABASE SUCCESSFULLY', 'green'))
            print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(color.BOLD + colored(color.YELLOW + "\n[(ID)|(U_Code)|(Name)|(BET)|(M_Amount)|(Action)|(M_Currency)|(Balance)|(Status)]\n") + color.END)
            for row in c.fetchall():
                print(color.CYAN, row, color.END)
            c.execute("SELECT * FROM dbCasinoTable1")
            print("\n••••••••••••••••••••••••••••")
            print(color.BOLD + colored('\t    Total Data: ', 'yellow'), len(c.fetchall()))
            print("••••••••••••••••••••••••••••\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
            u = input(color.BOLD + "Enter Unicode to delete row of data: " + color.END)
            c.execute("SELECT Unicode FROM dbCasinoTable1 WHERE Unicode=(?)", [u])
            for i in c.fetchall():
                if c.__eq__(i):
                    c.execute("SELECT * FROM dbCasinoTable1 WHERE Unicode=(?)", [u])
                    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
                    for row in c.fetchall():
                        print(color.BOLD + color.RED, row, color.END)
                    c.execute("SELECT * FROM table WHERE Unicode=(?)", [u])
                    print(color.BOLD + colored('\n\n\t Total Data Deleted: ', 'yellow'), len(c.fetchall()))
                    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
                    print(color.BOLD + colored('\n\t\t\t\t\tDeleting Data Successfully!', 'yellow') + color.END)
                    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                    c.execute("DELETE FROM dbCasinoTable1 WHERE Unicode=(?)", [u])
                    conn.commit()
                    admin()
            print(color.BOLD+colored(color.RED+u+" NOT FOUND!"))







def Delet_Data():
    while True:
        inp = input(color.BOLD+"Choose: "+color.BOLD+colored(color.DARKCYAN+"[a] Delete Manually ")+color.BOLD+colored(color.PURPLE+"[b] Delete All Data\n")+color.END)
        if inp.__eq__('a'):
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            print(color.BOLD+colored(color.DARKCYAN+"DELETE MANUALLY")+color.END)
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            Delete_manually()
            break

        elif inp.__eq__('b') or inp.__eq__('B'):
            c.execute("SELECT * FROM dbCasinoTable1")
            if len(c.fetchall())==0:
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
                print(color.BOLD+colored(color.RED+"System: There is no Data to Delete!")+color.END)
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                break
            else:
                c.execute("DELETE FROM dbCasinoTable1")
                conn.commit()
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
                print(color.BOLD+colored('System: Deleting All Data for this Month Successfully!' , 'yellow'))
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                break
        else:
            print(color.BOLD+colored(color.RED+"Invalid key input please try again.")+color.END)

def All_Data():
    while True:
        print("\n\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print(color.BOLD+colored('\t\t\t\t\t\t\t\tYOUR COPIED DATA','yellow'))
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        c.execute("SELECT * FROM dw")
        if len(c.fetchall()) == 0:
            print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            print(color.BOLD + colored(color.RED + "System: Your Database is Empty!"))
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
            break
        else:
            c.execute("SELECT * FROM dw")
            print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
            print('\033[1m' + colored('OPENING DATABASE SUCCESSFULLY', 'green'))
            print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(color.BOLD + colored(color.YELLOW + "\n[(ID)|(U_Code)|(Name)|(BET)|(M_Amount)|(Action)|(M_Currency)|(Balance)|(Status)]\n") + color.END)
            for row in c.fetchall():
                print(color.CYAN, row, color.END)
            c.execute("SELECT * FROM dw")
            print("\n••••••••••••••••••••••••••••")
            print(color.BOLD + colored('\t    Total Data: ', 'yellow'), len(c.fetchall()))
            print("••••••••••••••••••••••••••••\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
            break


def admin():
    while True:
        print("\n*******************")
        print('\033[1m' + colored('   Administrator','yellow'))
        print("*******************")
        ad = input(color.BOLD+"What do you want to do?\t"+color.BOLD+colored(color.CYAN+"[a] Delete Data"+color.BOLD+colored(color.YELLOW+"\t[b] View Data of this month")+color.BOLD+colored(color.GREEN+"\t[c] Copied Data\n")))
        if(ad.__eq__('a') or ad.__eq__('A')):
            Delet_Data()
        elif(ad.__eq__('b') or ad.__eq__('B')):
            #View Data
            while True:
                c.execute("SELECT * FROM dbCasinoTable1")
                if len(c.fetchall()) == 0:
                    print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
                    print(color.BOLD + colored(color.RED + "System: Your Database is Empty!"))
                    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                    break
                else:
                    c.execute("SELECT * FROM dbCasinoTable1")
                    print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
                    print('\033[1m' + colored('OPENING DATABASE SUCCESSFULLY','green'))
                    print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(color.BOLD+colored(color.YELLOW+"\n[(ID)|(U_Code)|(Name)|(BET)|(M_Amount)|(Action)|(M_Currency)|(Balance)|(Status)]\n")+color.END)
                    for row in c.fetchall():
                        print(color.CYAN,row,color.END)
                    c.execute("SELECT * FROM dbCasinoTable1")
                    print("\n••••••••••••••••••••••••••••")
                    print(color.BOLD+colored('\t    Total Data: ','yellow'),len(c.fetchall()))
                    print("••••••••••••••••••••••••••••\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
                    break
        elif ad.__eq__('c') or ad.__eq__('C'):
            All_Data()
        else:
            print(color.BOLD+colored(color.RED+"Invalid key input! Please try again."))
            continue
        adminChoose = input(color.BOLD + "Do you want to go back ? Press " + colored(color.DARKCYAN + '(y) Lobby') + " | " + color.BOLD + colored(color.BLUE + '(n) Back to Admin Panel\n') + color.END)
        if (adminChoose.__eq__('y') or adminChoose.__eq__('Y')):
            break

        elif (adminChoose.__eq__('n') or adminChoose.__eq__('N')):
            continue
        else:
            print(color.BOLD + colored(color.RED + '\nInvalid key input! Back to Admin Panel.\n'))
            continue



print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
print('\033[1m' + colored('\t\t\t\t\tMADAX Casino','cyan'))
print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
while True:
    choose = input('\033[1m' + colored('(a) [Teller] | (b) [Administrator]','yellow')+"\n" )
    if(choose.__eq__('a') or choose.__eq__('A')):
        print("************")
        print('\033[1m' + colored('  Teller','yellow'))
        print("************")
        name = input(color.BOLD+"Please enter your name: "+color.END)
        print("Hello",'\033[1m' + colored(name,'green'),"your entry code is:", '\033[1m' + colored(U_Code,'cyan')+"\n")
        break
    elif (choose.__eq__('b') or choose.__eq__('B')):
        admin()
    else:
        print(color.BOLD + color.RED + 'Invalid key! Please try again.\n' + color.END)


while True:
    print('\033[1m' + colored('Please choose your category here: ','grey'))
    print("******************************************************************************************************************************************************************")
    print(color.BOLD+colored(color.PURPLE+"\t \t \t\t\t\t\t\t[a] HI - LO Game | [b] Cash In | [c] Cash Out |")+color.BOLD+colored(color.PURPLE+" [d] View "+name+"'s Summary | [e] Exit"))
    category = input("******************************************************************************************************************************************************************\n")


    if (category.__eq__('a') or category.__eq__('A')):
        if (money < 100):
            print(color.BOLD+colored('Sorry we cant let you enter here. Please make a cash in for at least 100 Pesos above\n', 'red'))
            continue
        # Mechanics of the Game here:
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print("\n\t\t\t**********************| "+color.BOLD+colored(color.PURPLE+"Welcome to HI-LO Game")+" |*************************\n"+color.END)
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(color.BOLD+colored(color.DARKCYAN+"Game Mechanics: ")+color.END)
        print("\t• You need to enter your desire amount to bet")
        print("\t• The number was generating randomly")
        print("\t• You need to choose H / L . H stands for HIGH and L is for LOW")
        print("\t• The latest random numbers was your basis to choose if you want H or L")
        print("\t• Example: Random numbers result: 3765 , and you choose H. The next number will generate : 6884. THEN YOU WIN.")
        print("\t• If you win, you will receive the same amount you bet otherwise you will lose the same amount you bet")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # Mechanics of the Game here:
        result1 = random.randint(1, 10000)
        result.append(result1)
        print("********************")
        print(color.BOLD + colored(color.GREEN + 'Result : ') + colored(result1, 'red'))
        print("********************")
        while True:
            while True:
                try:
                    bet = float(input(color.BOLD+colored('Place your bet here: ','grey')))
                    if (bet > money):
                        print(color.BOLD+colored(color.RED+'Insufficient balance. Please make a cash in.')+color.END)
                        continue

                    else:
                        break
                except:
                    print(color.BOLD+colored(color.RED+'Invalid input. Please try again.')+color.END)
            while True:
                ch = input(color.BOLD+colored('Choose H to High / L to Low / E Exit / C Cancel bet : ','grey'))
                result2 = random.randint(1, 10000)
                if (ch.__eq__('h') or ch.__eq__('H')):
                    if (result2 > result[-1]):
                        print("--------------------------------------------------------------")
                        print("************************")
                        print(color.BOLD+colored(color.GREEN+'Latest Result : ')+ colored(result2, 'red'))
                        print("************************")
                        print("You", colored('*WIN*', 'cyan'), "Receive: ", colored("%.2f" % bet, 'green')," added to your wallet")
                        money += bet
                        print("Your current balance: ", colored("%.2f" % money, 'magenta'))
                        print("--------------------------------------------------------------")
                        result.append(result2)
                        winOrLose.append("Win")
                        bets.append("%.2f"%bet)
                        betting.append("HIGH")
                        c.execute("INSERT INTO dw (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code, name, bet, 'PESOS', money, 'WIN'))
                        conn.commit()
                        c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'WIN'))
                        conn.commit()
                        break


                    elif (result2 < result[-1]):
                        print("--------------------------------------------------------------")
                        print("************************")
                        print(color.BOLD+colored(color.GREEN+'Latest Result : ')+ colored(result2, 'red'))
                        print("************************")
                        print("You", colored('*LOSE*', 'cyan'), "Your: ", colored("%.2f" % bet, 'red')," will be deducted to your wallet")
                        money -= bet
                        print("Your current balance: ", colored("%.2f" % money, 'magenta'))
                        print("--------------------------------------------------------------")
                        result.append(result2)
                        winOrLose.append("Lose")
                        bets.append("%.2f"%bet)
                        betting.append("HIGH")
                        c.execute("INSERT INTO dw (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'LOSE'))
                        conn.commit()
                        c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'LOSE'))
                        conn.commit()
                        break


                elif (ch.__eq__('l') or ch.__eq__('L')):
                    if (result2 < result[-1]):
                        print("--------------------------------------------------------------")
                        print("************************")
                        print(color.BOLD + colored(color.GREEN + 'Latest Result : ') + colored(result2, 'red'))
                        print("************************")
                        print("You", colored('*WIN*', 'cyan'), "Receive: ", colored("%.2f" % bet, 'green')," added to your wallet")
                        money += bet
                        print("Your current balance: ", colored("%.2f" % money, 'magenta'))
                        print("--------------------------------------------------------------")
                        result.append(result2)
                        winOrLose.append("Win")
                        bets.append("%.2f"%bet)
                        betting.append("LOW")
                        c.execute("INSERT INTO dw (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'WIN'))
                        conn.commit()
                        c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'WIN'))
                        conn.commit()
                        break

                    elif (result2 > result[-1]):
                        print("--------------------------------------------------------------")
                        print("************************")
                        print(color.BOLD+colored(color.GREEN+'Latest Result : ')+ colored(result2, 'red'))
                        print("************************")
                        print("You", colored('*LOSE*', 'cyan'), "Your: ", colored("%.2f" % bet, 'red')," will be deducted to your wallet")
                        money -= bet
                        print("Your current balance: ", colored("%.2f" % money, 'magenta'))
                        print("--------------------------------------------------------------")
                        result.append(result2)
                        winOrLose.append("Lose")
                        bets.append("%.2f"%bet)
                        betting.append("LOW")
                        c.execute("INSERT INTO dw (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code, name, bet, 'PESOS', money, 'LOSE'))
                        conn.commit()
                        c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,BET,Currencies,Money,Status) VALUES(?,?,?,?,?,?)",(U_Code,name,bet,'PESOS',money,'LOSE'))
                        conn.commit()
                        break

                elif (ch.__eq__('e') or ch.__eq__('E')):

                    exit = input(color.BOLD+"Are you sure do you want to exit?  "+ colored(color.DARKCYAN+"[Y] Yes")+" | " +color.BOLD+colored(color.BLUE+"[N] No")+"\n")
                    if (exit.__eq__('y') or exit.__eq__('Y')):
                        break
                    else:
                        continue

                elif (ch.__eq__('c') or ch.__eq__('C')):
                    print(color.BOLD + colored('BET CANCELLED\n', 'red'))
                    break


                else:
                    print(color.BOLD + color.RED + 'Invalid key input. Please try again.\n' + color.END)
                    continue

            out = input(color.BOLD + "Do you want to bet again? (" + colored(color.DARKCYAN + '[Y] Yes') + " | " + color.BOLD + colored(color.BLUE + '[N] No') +")\n"+ color.END)
            if (out == 'Y' or out == 'y'):
                if (money == 0):
                    print(color.BOLD + color.RED + 'Sorry you dont have enough money to bet. Please make a cash in to play again.\n' + color.END)
                    break
                else:
                    continue
            else:
                break

    elif (category.__eq__('b') or category.__eq__('B')):
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print(color.BOLD + colored(color.PURPLE+'\t\t\t\t\t\t\tCASH IN ') + color.END)
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print(color.BOLD+"Note: All money currency will converted into Pesos when going to cash in."+color.END)
        while True:
            print(color.BOLD+"Choose currency to cash in: ",end="")
            currency=input(color.BOLD + colored(color.CYAN+'[a] DOLLAR') +color.BOLD+ colored(color.GREEN+'  [b] Kuwait Dinar') +color.BOLD+ colored(color.YELLOW+'  [c] Pesos')+ color.BOLD+colored(color.RED+'  [d] Exit\n')+color.END)
            if (currency.__eq__('a') or currency.__eq__('A')):
                print(color.BOLD + '♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦|'+colored(color.CYAN+' ($) US DOLLAR ')+'|♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦' + color.END)
                while True:
                    try:
                        cashin = float(input(color.BOLD+"Desire amount to Cash In: "))
                        if cashin >9742.790335:
                            print(color.BOLD+colored(color.RED+"System: We apology, we won't you allow to make a Cash In more than 9,742.790335 US DOLLAR or 500,000 in PESOS.")+color.END)
                            continue
                        else:
                            convert = (cashin * 51.32)
                            cashintHistory.append("%.2f" % convert)
                            money_currency.append('US DOLLAR')
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Your money: ", colored("%.2f" % cashin, 'green'), " $ converted into PESOS: ",
                                  colored("%.2f" % convert, 'green'))
                            money += convert
                            print("Successfully!", colored("%.2f" % convert, 'green'), " PESOS will be added to your wallet\n")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            c.execute("INSERT INTO dw (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" % convert, 'CASH IN', 'US DOLLAR', money))
                            conn.commit()
                            c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)", (U_Code, name,"%.2f" %convert, 'CASH IN','US DOLLAR',money))
                            conn.commit()
                            break
                    except:
                        print(color.BOLD+color.RED+'Invalid input.Please try again\n'+color.END)

            elif (currency.__eq__('b') or currency.__eq__('B')):
                #CASH IN MUST NOT EXCEED 300,000
                print(color.BOLD + '♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦|'+colored(color.GREEN+'  Kuwait Dinar ')+'|♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦' + color.END)
                while True:
                    try:
                        cashin = float(input(color.BOLD+"Desire amount to Cash In: "))
                        if cashin >2957.005145:
                            print(color.BOLD+colored(color.RED+"System: We apology, we won't you allow to make a Cash In more than 2,957.005145 KWD or 500,000 in PESOS.")+color.END)
                            continue
                        else:
                            convert = (cashin * 169.09)
                            cashintHistory.append("%.2f" % convert)
                            money_currency.append('KWD')
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Your money: ", colored("%.2f" % cashin, 'green'), " Kuwait Dinar converted into PESOS: ",
                                  colored("%.2f" % convert, 'green'))
                            money += convert
                            print("Successfully!", colored("%.2f" % convert, 'green'), " PESOS will be added to your wallet\n")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            c.execute("INSERT INTO dw (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" % convert, 'CASH IN', 'KWD', money))
                            conn.commit()
                            c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" %convert, 'CASH IN','KWD',money))
                            conn.commit()
                            break
                    except:
                        print(color.BOLD + color.RED + 'Invalid input.Please try again\n' + color.END)

            elif (currency.__eq__('c') or currency.__eq__('C')):
                print(color.BOLD + '♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦|'+colored(color.YELLOW+'  PESOS ')+'|♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦' + color.END)
                while True:
                    try:
                        cashin = float(input(color.BOLD+"Desire amount to Cash In: "))
                        if cashin > 500000:
                            print(color.BOLD + colored(color.RED + "System: We apology, we won't you allow to make a Cash In more than 500,000 PESOS.") + color.END)
                            continue
                        else:
                            convert = (cashin*1)
                            money += cashin
                            cashintHistory.append("%.2f" % cashin)
                            money_currency.append('PESOS')
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Successfully!", colored("%.2f" % cashin, 'green'), " PESOS will be added to your wallet\n")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            c.execute("INSERT INTO dw (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" % convert, 'CASH IN', 'PESOS', money))
                            conn.commit()
                            c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" %convert, 'CASH IN','PESOS',money))
                            conn.commit()
                            break
                    except:
                        print(color.BOLD + color.RED + 'Invalid input.Please try again\n' + color.END)
            elif(currency.__eq__('d') or currency.__eq__('D')):
                break
            else:
                print(color.BOLD + color.RED + 'Invalid input please try again.\n' + color.END)
                continue

            out=input(color.BOLD + "Do you want to cash in again? "+colored(color.DARKCYAN + '(y) Yes') +" | "+color.BOLD+colored(color.BLUE + '(n) No\n')+ color.END)
            if(out.__eq__('y') or out.__eq__('Y')):
                continue
            else:
                break

    elif(category.__eq__('c') or category.__eq__('C')):
        #CASH OUT NOT EXCEED 500,000
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print(color.BOLD + colored(color.PURPLE+'\t\t\t\t\t\t\tCASH OUT ') + color.END)
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        while True:
            while True:
                try:
                    cashout = float(input(color.BOLD+"Enter your desire amount to cash out: "+color.END))
                    if (cashout > money):
                        print(color.BOLD + color.RED + 'Insufficient balance. Please try again.\n' + color.END)
                        break
                    elif cashout > 500000:
                        print(color.BOLD+colored(color.RED+"System: We apology, We won't allow you to make a Cash Out more than 500,000 Pesos.\nAdvice: Cash Out 500,000 Pesos and another Cash Out of your desire amount if you wish to get all your money."))
                        continue
                    else:
                        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
                        print("Your ammount of ", colored("%.2f" % cashout, 'red'),"was successfully Cash Out! Thank you have a nice day.")
                        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
                        money -= cashout
                        cashoutHistory.append("%.2f" % cashout)
                        c.execute("INSERT INTO dw (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" % cashout, 'CASH OUT', 'PESOS', money))
                        conn.commit()
                        c.execute("INSERT INTO dbCasinoTable1 (Unicode,Name,Amount,Action,Currencies,Money) VALUES (?,?,?,?,?,?)",(U_Code, name, "%.2f" % cashout, 'CASH OUT', 'PESOS',money))
                        conn.commit()
                        break

                except:
                    print(color.BOLD + color.RED + 'Invalid key. Please try again.\n' + color.END)
                    continue
            out = input(color.BOLD + "Do you want to cash out again? " + colored(color.DARKCYAN + '(y) Yes') + " | " + color.BOLD + colored(color.BLUE + '(n) No\n') + color.END)
            if (out.__eq__('y') or out.__eq__('Y')):
                continue
            else:
                break

    elif(category.__eq__('d') or category.__eq__('D')):
        while True:
            print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
            print(color.BOLD+colored(color.GREEN+"\t\t\t\t\t\t"+name+"'s Summary"))
            print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
            # VIEW CURRENT BALANCE
            print(color.BOLD+"\t• Your current balance is: PESOS "+color.BOLD+colored("%.2f"%money,'green'))
            # CASH IN HISTORY
            if(len(cashintHistory)==0):
                print(color.BOLD+"\t• Your CASH IN HISTORY: ",color.BOLD+colored('Cash In History is Empty','red'))
            else:
                print(color.BOLD+"\t• Your CASH IN HISTORY: ",color.BOLD+colored(cashintHistory,'green'))
            #MoneyCurrencyCashIn
            if (len(money_currency) == 0):
                print(color.BOLD + "\t• Money Currency Cash In: ",color.BOLD + colored('Money Currency Cash In History is Empty', 'red'))
            else:
                print(color.BOLD + "\t• Money Currency Cash In: ", color.BOLD + colored(money_currency, 'yellow'))
            # CASH OUT HISTORY
            if(len(cashoutHistory)==0):
                print(color.BOLD + "\t• Your CASH OUT HISTORY: ", color.BOLD + colored('Cash Out History is Empty', 'red'))
            else:
                print(color.BOLD + "\t• Your CASH OUT HISTORY: ", color.BOLD + colored(cashoutHistory, 'red'))
            # BET
            if (len(bets) == 0):
                    print(color.BOLD + "\t• Your bet(s): ", color.BOLD + colored('Bet(s) is Empty', 'red'))
            else:
                    print(color.BOLD + "\t• Your bet(s): ", color.BOLD + colored(bets, 'magenta'))
            #BETTING
            if (len(betting) == 0):
                    print(color.BOLD + "\t• HIGH / LOW Bet History: ", color.BOLD + colored('HIGH / LOW Bet is Empty', 'red'))
            else:
                    print(color.BOLD + "\t• HIGH / LOW Bet History: ", color.BOLD + colored(betting,'green'))
            # WIN OR LOSE
            if (len(winOrLose) == 0):
                print(color.BOLD + "\t• Game Status Result History: ",color.BOLD + colored('Game Result History is Empty', 'red'))
            else:
                print(color.BOLD + "\t• Game Status Result History: ",color.BOLD + colored(winOrLose, 'blue'))
            # RESULT
            if(len(result)==0):
                print(color.BOLD + "\t• Game Result History: ", color.BOLD + colored('Result(s) History is Empty', 'red')+"\n")
            else:
                print(color.BOLD + "\t• Game Result History: ", color.BOLD + colored(result, 'cyan')+"\n")


            userChoose = input(color.BOLD + "Do you want to go back ? Press " + colored(color.DARKCYAN + '(y) Yes') + " | " + color.BOLD + colored(color.BLUE + '(n) No\n') + color.END)
            if (userChoose.__eq__('y') or userChoose.__eq__('Y')):
                break
            elif(userChoose.__eq__('n') or userChoose.__eq__('N')):
                continue
            else:
                print(color.BOLD+colored(color.RED+'\nInvalid key input! Back to '+color.BOLD+colored(color.DARKCYAN+name)+color.BOLD+colored(color.RED+"'s Summary\n")))


    elif(category.__eq__('e') or category.__eq__('E')):
        U_Code = random_code(length=5, uppercase=True, numbers=True)
        # RECEIPT HERE
        print("\n\n-----------------------------------------------------------")
        print(color.BOLD + colored('TELLER: ', 'yellow') + color.BOLD+" Here's your receipt: ",color.BOLD+colored(color.BLUE+name))
        print("-----------------------------------------------------------\n")
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print(color.BOLD + colored(color.GREEN + "\t\t\t\t\t\t" + name + "'s Summary"))
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        # VIEW CURRENT BALANCE
        print(color.BOLD + "\t• Your current balance is: PESOS " + color.BOLD + colored("%.2f" % money, 'green'))
        # CASH IN HISTORY
        if (len(cashintHistory) == 0):
            print(color.BOLD + "\t• Your CASH IN HISTORY: ", color.BOLD + colored('Cash In History is Empty', 'red'))
        else:
            print(color.BOLD + "\t• Your CASH IN HISTORY: ", color.BOLD + colored(cashintHistory, 'green'))
        # MoneyCurrencyCashIn
        if (len(money_currency) == 0):
            print(color.BOLD + "\t• Money Currency Cash In: ",
                  color.BOLD + colored('Money Currency Cash In History is Empty', 'red'))
        else:
            print(color.BOLD + "\t• Money Currency Cash In: ", color.BOLD + colored(money_currency, 'yellow'))
        # CASH OUT HISTORY
        if (len(cashoutHistory) == 0):
            print(color.BOLD + "\t• Your CASH OUT HISTORY: ", color.BOLD + colored('Cash Out History is Empty', 'red'))
        else:
            print(color.BOLD + "\t• Your CASH OUT HISTORY: ", color.BOLD + colored(cashoutHistory, 'red'))
        # BET
        if (len(bets) == 0):
            print(color.BOLD + "\t• Your bet(s): ", color.BOLD + colored('Bet(s) is Empty', 'red'))
        else:
            print(color.BOLD + "\t• Your bet(s): ", color.BOLD + colored(bets, 'magenta'))
        # BETTING
        if (len(betting) == 0):
            print(color.BOLD + "\t• HIGH / LOW Bet History: ",color.BOLD + colored('HIGH / LOW Bet is Empty', 'red'))
        else:
            print(color.BOLD + "\t• HIGH / LOW Bet History: ", color.BOLD + colored(betting, 'green'))
        # WIN OR LOSE
        if (len(winOrLose) == 0):
            print(color.BOLD + "\t• Game Status Result History: ",color.BOLD + colored('Game Result History is Empty', 'red'))
        else:
            print(color.BOLD + "\t• Game Status Result History: ", color.BOLD + colored(winOrLose, 'blue'))
        # RESULT
        if (len(result) == 0):
            print(color.BOLD + "\t• Game Result History: ", color.BOLD + colored('Result(s) History is Empty', 'red')+"\n")
        else:
            print(color.BOLD + "\t• Game Result History: ", color.BOLD + colored(result, 'cyan')+"\n")
        # RECEIPT HERE
        print(color.RED+"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(color.BOLD+colored(color.YELLOW+'\n\n\t\t\t\t\t\t\t\t\tSystem: Thank you '+color.BOLD+colored(color.BLUE+name.upper())+color.BOLD+colored(color.YELLOW+" for coming! Hope we'll see you again here in "+color.BOLD+colored(color.DARKCYAN+'MADAX Casino.\n\n'))))
        print(color.RED+"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        result.clear()
        winOrLose.clear()
        cashintHistory.clear()
        money_currency.clear()
        cashoutHistory.clear()
        bets.clear()
        money = 0

        print(color.GREEN+"\n\n\n\n\n\n\n\n\n\n\n♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
        print('\033[1m' + colored('\t\t\t\t\tMADAX Casino', 'cyan'))
        print(color.GREEN+"♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
        while True:
            choose = input('\033[1m' + colored('(a) [Teller] | (b) [Administrator]', 'yellow') + "\n")
            if (choose.__eq__('a') or choose.__eq__('A')):
                print("************")
                print('\033[1m' + colored('  Teller', 'yellow'))
                print("************")
                name = input(color.BOLD + "Please enter your name: " + color.END)
                print("Hello", '\033[1m' + colored(name, 'green'), "your entry code is:",'\033[1m' + colored(U_Code, 'cyan') + "\n")
                break
            elif (choose.__eq__('b') or choose.__eq__('B')):
                admin()
            else:
                print(color.BOLD + color.RED + 'Invalid key! Please try again.\n' + color.END)

    else:
        print(color.BOLD + color.RED + 'Invalid key! Try again, back to category.\n' + color.END)