import sqlite3
from sqlite3 import Error


def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def cust(conn):
    fname =    input("\nEnter customer first name :")
    lname =    input("\nEnter customer last name  :")
    mnum = int(input("\nEnter mobile number       :"))
    adar = int(input("\nEnter adhar number        :"))

    sql = '''insert into customer(First_name,Last_name,Mobile,Adhar) values(?,?,?,?)     '''
    cur = conn.cursor()
    data = (fname, lname, mnum, adar)
    cur.execute(sql, data)
    conn.commit()
    print("\nCUSTOMER DETAILS ADD SUCCESSSFULLY")

    print("\n    WELCOME TO HOTEL     ")
    print("\nPRESS 1 FOR ROOM BOOKING")
    print("\nPRESS 2 FOR DINNER")
    print("\nPRESS 3 FOR GAMES")
    #print("\nPRESS ANY KEY FOR GO BACK")
    # print("\nENTER ANY KEY FOR EXIT")

    a = int(input())
    if (a == 1):
        id = book(conn)
    elif (a == 2):
        id = order(conn)
    elif (a == 3):
        id = game(conn)
    else:
        print("  ")



def book(conn):
    global z
    cur = conn.cursor()
    fname = input("\nPlz Enter Your Name For Conform Your Room : ")

    # print("\nBook a room")
    print("\nFollowing Rooms are avaliable")
    print("\n1.With AC and TWO DOUBLE BED for family only PRICE 4000")

    print("\n2.With AC and ONE DOUBLE BED PRICE 3000 PER NIGHT")
    print("\n3.With AC and TWO seprate SINGLE BED PRICE 2000 PER NIGHT")
    print("\n4.With AC and SINGLE BED PRICE 1500 PER NIGHT")
    print("\n5.Without AC and ONE DOUBLE BED PRICE 1500 PER NIGHT")
    print("\n6.Without AC and SINGLE BED PRICE 1000 PER NIGHT")

    x = int(input("\nPLZ SELECT ROOM : "))
    n = int(input("\nHOW MANY NIGHTS DID YOU WANT TO SATY : "))
    print("\n100 rs MAINTENANCE CHARGES FOR PER NIGHT")

    if (x == 1):

        print("\nWith AC and TWO DOUBLE BED for family only you may cost", 4000 * n)
        z = 4000 * n


    elif (x == 2):
        print("\nWith AC and ONE DOUBLE BED you may cost", 3000 * n)
        z = 3000 * n
    elif (x == 3):
        print("\nWith AC and TWO seprate SINGLE you may cost", 2000 * n)
        z = 2000 * n
    elif (x == 4):
        print("\nWith AC and SINGLE BED you may cost", 1500 * n)
        z = 1500 * n
    elif (x == 5):
        print("\nWithout AC and ONE DOUBLE BED PRICE you may cost", 1500 * n)
        z = 1500 * n
    elif (x == 6):
        print("\nWithout AC and SINGLE BED PRICE you may cost", 1000 * n)
        z = 1000 * n
    else:
        print("\ninvaild input")

    print("\nMAINTENANCE CHARGES Is ", 100 * n)
    print("\nROOM BILL", z + 100 * n)
    room = z
    # t is MAINTENANCE CHARGES
    t = 100 * n
    data = (room, t, fname)
    sql = '''update customer set room=?,wait=? where First_name=? '''

    cur.execute(sql, data)
    conn.commit()
    print("\nROOM BOOK SUCCESSSFULLY")


def order(conn):
    cur = conn.cursor()
    print("\nFOOD SECTION")
    fname = input("\nPlz Enter Your Name For Conform Your FOOD ORDER : ")

    print("\n******RESTAURANT MENU******")

    print("\n1.Dessert----->100", "\n2.Drinks----->50", "\n3.Breakfast--->90", "\n4.Lunch---->110", "\n5.Dinner--->150",
          "\n6.Exit")

    e = 0
    while (1):

        c = int(input("\nEnter the number of your choice:"))

        if (c == 1):
            d = int(input("\nEnter the quantity:"))
            e = e + 100 * d

        elif (c == 2):
            d = int(input("\nEnter the quantity:"))
            e = e + 50 * d

        elif (c == 3):
            d = int(input("\nEnter the quantity:"))
            e = e + 90 * d

        elif (c == 4):
            d = int(input("\nEnter the quantity:"))
            e = e + 110 * d
        elif (c == 5):
            d = int(input("\nEnter the quantity:"))
            e = e + 50 * d

        elif (c == 6):
            break
        else:
            print("\nYou've Enter an Invalid Key")

    print("\nYOUR FOOD BILL IS", e, "RS")
    print("\nExtra Charges        50 RS")
    r = e
    f = 50

    data = (r, f, fname)
    sql = '''update customer set foood=?,tax=? where First_name=? '''
    # sql = '''insert into customer(foood,tax) values(?,?)     '''

    cur.execute(sql, data)
    conn.commit()
    print("FOOD DETAILS ADD SUCCESSSFULLY")


def select_all(conn):
    uname = input("\nUSERNAME  :")
    pswd =  input("\nPASSWORD  :")

    if (uname == "admin" and pswd == "admin123"):

        print("\nCustomer details")
        cur = conn.cursor()
        sql = '''select * from customer'''

        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            
            print("\nFirst Name    : ", row[0], "\nLast Name     : ", row[1], "\nMobile No      : ", row[2],
                  "\nAdhar No      : ", row[3], "\nRoom Rent     : ", row[4], "\nMAINTENANCE CHARGES : ", row[5], "\nORDER FOOD    : ",
                  row[6],
                  "\nExtra Charges : ", row[7], "\nGame Played  : ", row[8], "\nGame Charges : ", row[9]
                  )
                    
       



              
    else:
        print("---WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN---")


#def happy(conn):
#    cur = conn.cursor()
 
#    sql = '''select * from customer'''
#    cur.execute(sql)
#    rows = cur.fetchall()
    

    
#    for row in rows:
              
            
#                    if row[4] is None and row[5] is None and row[6] is None and row[7] is None:
#                        return print("\nTOTAL BILL : ", row[8] + row[9])
#                    elif row[4] is None and row[5] is None and row[8] is None and row[9] is None:
#                        return print("\nTOTAL BILL : ", row[6] + row[7])
#                    elif row[6] is None and row[7] is None and row[8] is None and row[9] is None:
#                        return print("\nTOTAL BILL : ", row[4] + row[5])
#                    elif row[4] is None and row[5] is None and row[6] is None and row[7] is None and row[8] is None and row[9] is None:
#                        return print("\nTOTAL BILL : ZERO RS")
#                    elif row[4] is None and row[5] is None:
#                        return print("\nTOTAL BILL : ", row[6] + row[7] + row[8] + row[9])
#                    elif row[6] is None and row[7] is None:
#                        return print("\nTOTAL BILL : ", row[4] + row[5] + row[8] + row[9])
#                    elif row[8] is None and row[9] is None:
#                        return print("\nTOTAL BILL : ", row[4] + row[5] + row[6] + row[7])
#                    else:
#                        return print("\nTOTAL BILL : ", row[4] + row[5] + row[6] + row[7] + row[8] + row[9])    
                                    
def select_one(conn):
    cur = conn.cursor()
    First_name = input("\nPlz Enter Your Name For Conform you are a CUSTOMER : ")
    # print("---------------------")
    sql = "select * from customer where First_name=?"
    cur.execute(sql, (First_name,))
    rows = cur.fetchall()
    for row in rows:
        print("\nFirst name:", row[0], "\nLast name:", row[1], "\nMobile no", row[2],
              "\nAdhar number", row[3])

    a = int(input("\nFOR ORDER FOOD PRESS 1 \nFOR PLAY GAME PRESS 2  \nFOR TAKE OFF PRESS 3"))

    if (a == 1):
        id = order(conn)

    elif (a == 3):
        id = take(conn)
    elif (a == 2):
        id = game(conn)


def game(conn):
    cur = conn.cursor()
    fname = input("\nPlz conform your name to play GAME : ")
    print("******GAME MENU*******")

    print("\n1.Table tennis----->Rs60", "\n2.Bowling----->Rs80", "3.\nSnooker--->Rs70", "4.\nVideo games---->Rs90",
          "\n5.Pool--->Rs50==6", "\n6.Exit")

    a = 0
    while (1):

        g = int(input("Enter your choice:"))

        if (g == 1):
            h = int(input("No. of hours:"))
            a = a + 60 * h

        elif (g == 2):
            h = int(input("No. of hours:"))
            a = a + 80 * h

        elif (g == 3):
            h = int(input("No. of hours:"))
            a = a + 70 * h

        elif (g == 4):
            h = int(input("No. of hours:"))
            a = a + 90 * h

        elif (g == 5):
            h = int(input("No. of hours:"))
            a = a + 50 * h
        elif (g == 6):

            break

        else:

            print("Invalid option")

    print("\nGAME BILL : ", a)
    print("\nEXTRA CHARGES PER HOUR :", h * 10, "\n")
    r = a
    h = 10 * h
    data = (r, h, fname)
    sql = '''update customer set game=?,game_charges=? where First_name=? '''

    cur.execute(sql, data)
    conn.commit()
    print("GAME DETAILS ADD SUCCESSSFULLY")


def take(conn):
    print("\nTOTAL BILL")
    cur = conn.cursor()
    First_name = input("Enter name: ")
    # print("---------------------")
    sql = "select * from customer where First_name=?"
    cur.execute(sql, (First_name,))
    rows = cur.fetchall()
    for row in rows:
        print("\nFirst name:", row[0], "\nLast name:", row[1], "\nMobile no", row[2],
              "\nAdhar number", row[3], "\nRoom rent", row[4], "\nMAINTENANCE CHARGES", row[5], "\nORDER FOOD", row[6],
              "\nAdd FOOD chagers", row[7], "\nGAME CHARGES", row[8], "ADD GAME CHARGERS", row[9])
        # if row[4] is None and row[5] is None:
        #    return print("\nTOTAL BILL : ",row[6]+row[7])
        # elif row[6] is None and row[7] is None:
        #    return print("\nTOTAL BILL :",row[4]+row[5])
        # else:
        #   return print("\nTOTAL BILL :",row[4]+row[6]+row[7]+row[5]+row[8]+row[9])
        if row[4] is None and row[5] is None and row[6] is None and row[7] is None:
            return print("\nTOTAL BILL : ", row[8] + row[9])
        elif row[4] is None and row[5] is None and row[8] is None and row[9] is None:
            return print("\nTOTAL BILL : ", row[6] + row[7])
        elif row[6] is None and row[7] is None and row[8] is None and row[9] is None:
            return print("\nTOTAL BILL : ", row[4] + row[5])
        elif row[4] is None and row[5] is None and row[6] is None and row[7] is None and row[8] is None and row[
            9] is None:
            return print("\nTOTAL BILL : ZERO RS")
        elif row[4] is None and row[5] is None:
            return print("\nTOTAL BILL : ", row[6] + row[7] + row[8] + row[9])
        elif row[6] is None and row[7] is None:
            return print("\nTOTAL BILL : ", row[4] + row[5] + row[8] + row[9])
        elif row[8] is None and row[9] is None:
            return print("\nTOTAL BILL : ", row[4] + row[5] + row[6] + row[7])
        else:
            return print("\nTOTAL BILL : ", row[4] + row[5] + row[6] + row[7] + row[8] + row[9])

def delete(conn):
    uname = input("\nUSERNAME  :")
    pswd = input("\nPASSWORD  :")

    if (uname == "admin" and pswd == "admin123"):
         fname = input("ENTER CUSTOMER NAME ")
         #print("---------------------------")
         sql = 'delete from customer where First_name=?'
         cur = conn.cursor()
         cur.execute(sql,(fname,))
         conn.commit()
         print("Data deleted succefully")

    else:
        print("---WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN---")

def up(conn):
    cur = conn.cursor()
    uname = input("\nUSERNAME  :")

    pswd = input("\nPASSWORD  :")

    if (uname == "admin" and pswd == "admin123"):
        fname =    input("\nENTER YOUR FIRST NAME FOR UPDATE                 : ")
        uname =    input("\nCHANGE your First name Enter your First name     : ")
        lname =    input("\nCHANGE Your last  name Enter customer last name  : ")
        mnum = int(input("\nCHANGE Your Mobile no Enter mobile number        : "))
        adar = int(input("\nCHANGE Your adhar name Enter adhar number        : "))
        data=(uname,lname,mnum,adar,fname)
        sql='''update customer set First_name=?,Last_name=?,Mobile=?,Adhar=? where First_name=?'''
        cur.execute(sql, data)
        conn.commit()
        print("Data Updated Successfully!")

        cur.close()
    else:
        print("---WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN---")



def cus(conn):
    uname = input("\nUSERNAME  :")
    pswd = input("\nPASSWORD  :")

    if (uname == "admin" and pswd == "admin123"):
        a = int(input("\nPRESS 1 FOR UPDATE CUSTOMER DETAILS \nPRESS 2 FOR DELETE CUSTOMER DETAILS \nPRESS 3 FOR ALL CUSTOMER DETAILS"))
        if (a==1):
            id = up(conn)
        elif (a==2):
            id = delete(conn)
        elif(a==3):
            id = select_all(conn)
        else:
            print("\nINVALID INPUT TRY AGAIN")
    else:
        print("---WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN---")


def main():
    try:
        database = r"E:\Amey Borade\A14_HOTEL MANAGEMENT\pythnproject\final"
        conn = connection(database)
        with conn:
            while (1):
                print("---------------------------------------------")
                print("|           HOTEL MANAGEMENT SYSTEM         |")
                print("---------------------------------------------")
                print("|              1.New CUSTOMER               |")
                print("---------------------------------------------")
                print("|           2.Already a customer            |")
                print("---------------------------------------------")
                print("|    3.UPDATE\DELETE\ALL CUSTOMER DETAILS   |")
                print("---------------------------------------------")
                # print("|          5.only bill               |")
                # print("---------------------------------")
                print("|                   4.Exit                  |")
                print("---------------------------------------------")

                ch = int(input("\nPLZZ Enter your choice AS 1,2,3,4 --  "))
                print("---------------------")
                if (ch == 1):
                    id = cust(conn)
                elif (ch == 2):
                    id = select_one(conn)
                elif (ch == 3):
                    id = cus(conn)
               # elif(ch==5):
               #     id=happy(conn)
                elif (ch == 4):
                    quit()
                else:
                    print("INVALID INPUT")
    except Error as e:
        print("Error in DB Connection", e)


if __name__ == "__main__":
    main()
