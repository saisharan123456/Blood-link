

                                                                                              ##Blood  Link
import os
##def usrdt():
##    import mysql.connector as si
##    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
##    cur=mycon.cursor()
##    cur.execute("create table usrdt(Name varchar(225),DOB varchar(225),BloodGroup varchar(225),Address varchar(225),Username varchar(225),password varchar(225));")
##usrdt()
##
##def blddt():
##    import mysql.connector as si
##    mycon=si.connect(host='localhost',user='root',
## passwd = os.getenv("DB_PASSWORD"),database='blddn')
##    cur=mycon.cursor()
##
##    cur.execute("create table blddt(Hospital_Name varchar(10000),AP VARCHAR(3),AN VARCHAR(3),BP VARCHAR(3),BN VARCHAR(3),OP VARCHAR(3),ONEG VARCHAR(3),ABP VARCHAR(3),ABN VARCHAR(3));")
##blddt()
##def rpt():
##      import mysql.connector as si
##      con=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
##      cr=con.cursor()
##      cr.execute("create table Report(Hospital_name varchar(225),name varchar(225),Requested_bldgrp varchar(225))")
##      con.commit
##rpt()
##

##

##def hspdt():
##    import mysql.connector as si
##    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
##    cur=mycon.cursor()
##
##    cur.execute("create table Hspdt(Hospital_Name varchar(225),Location varchar(225),contctno varchar(225),username varchar(225),password varchar(225));")
##hspdt()

##
##def blddt():
##    import mysql.connector as si
##    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
##    cur=mycon.cursor()
##
##    cur.execute("create table blddt(Hospital_Name varchar(10000),AP VARCHAR(3),AN VARCHAR(3),BP VARCHAR(3),BN VARCHAR(3),OP VARCHAR(3),ONEG VARCHAR(3),ABP VARCHAR(3),ABN VARCHAR(3));")
##blddt()
##def rpt():
##      import mysql.connector as si
##      con=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
##      cr=con.cursor()
##      cr.execute("create table Report(Hospital_name varchar(225),name varchar(225),Requested_bldgrp varchar(225))")
##      con.commit
##rpt()
##
##


import mysql.connector
lst=['AP','AN','BP','BN','OP','ONEG','ABP','ABN']
import mysql.connector as si
mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
cr=mycon.cursor()
cr.execute("select hospital_name from hspdt")
dt=cr.fetchall()
lst2=[]
for i in dt:
      lst2.append(i[0])

def register():
      print('='*100)
      op=input('\t\t\t\t  CREATE  PROFILE AS\n 1)  User\n 2)  Hospital\n 3) Exit\n\nChoose an option  :')
      if op=='1':
            user()
      elif op=='2':
            hosp()
      elif op=='3':
            home()
      else:
            register()
      print('\t\tYou have succesfully created an account')
      print('\n\t\t\t\t\tSign In')
      signin()

def exit():
      print('Thank You')
      

def bldgrp():
      usbgr=input('A+ =AP\t\tB+ =BP\t\tAB+ =ABP\tO+ =OP\nA- =AN\t\tB- =BN\t\tAB- =ABN\tO- =ONEG \nEnter Your Blood Group : ')
      usbg=usbgr.upper()
      if usbg in lst:
            usad=input('Enter Address :')
            db=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='blddn')
            mc=db.cursor()
            mc.execute("select * from usrdt where Username='{}'".format(usnm))
            sa=mc.fetchone()
            mc.execute("insert into usrdt values('{}','{}','{}','{}','{}','{}')".format(unm,usdb,usbg,usad,usnm,usps))           
            db.commit()
      else:
                  print('='*100)
                  print('Enter valid Blood group')
                  bldgrp()

       
def user():
      print('='*100)
      print('\n\t\t\t           Creating a new Profile as User\n')
      global usnm
      global unm
      unm=input('Enter your Name :')
      usnm=input('Enter the Username :')
      db=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='blddn')
      mc=db.cursor()

      mc.execute("select * from usrdt where Username='{}'".format(usnm))
      sa=mc.fetchone()
      if db.is_connected():
            if sa==None:
                  global usps
                  global usdb
                  usps=input('Enter the Password :')
                  usdb=input('Enter the DOB(dd/mm/yyyy) :')
                  usbgr=input('A+ =AP\t\tB+ =BP\t\tAB+ =ABP\tO+ =OP\nA- =AN\t\tB- =BN\t\tAB- =ABN\t\tO- =ONEG \nEnter Your Blood Group : ')
                  usbg=usbgr.upper()
                  if usbg in lst:
                      usad=input('Enter Address :')
                      db=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='blddn')
                      mc=db.cursor()
                      mc.execute("select * from usrdt where Username='{}'".format(usnm))
                      sa=mc.fetchone()
                      mc.execute("insert into usrdt values('{}','{}','{}','{}','{}','{}')".format(unm,usdb,usbg,usad,usnm,usps))           
                      db.commit()
                  else:
                        print('='*100)
                        print('Enter valid Blood group')
                        bldgrp()
            else:
                  print('\t\tUsername already exist')
                  user()
            db.close()

def usrintr():
    print('='*100)
    import mysql.connector as si
    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=mycon.cursor()
    cr.execute("select * from usrdt where Username='{}'".format(usrnm))
    dat=cr.fetchall()
    print()
    print('\t\tWelcome',dat[0][0])
    print(dat[0][0])
    print('Blood group:',dat[0][2])
    n=input("\nWould you like to \n1.Donate Blood.Save a life\n2.Recieve\n3.Delete the account\n4.Log out\nEnter Your Choice : ")
    if n=='1':
        donate()     
    elif n=='2':
        print('='*100)
        recieve()
    elif n=='3':
          delus()
    elif n=='4':
          home()

    else:
        print('='*100)
        print('Enter a valid opton')
        usrintr()
        

def donate():
     print('='*100)
     import mysql.connector as si
     cn=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
     cr=cn.cursor()
     hsptnm()
     cr.execute("Select Name from usrdt where username='{}'".format(usrnm))
     dt=cr.fetchone()
     name=dt[0]
     cr.execute("Select bloodgroup from usrdt where username='{}'".format(usrnm))
     dt=cr.fetchone()
     bld=dt[0]
     print('Enter 0 to Exit')
     honm=input('Enter your nearest hospital name :')
     if honm in lst2:
           cr.execute("insert into report values('{}','{}','{}')".format(honm,name,bld))
           cn.commit()
           cr.execute("select  * from hspdt where Hospital_Name='{}'".format(honm))
           data=cr.fetchone()
           if data!=None:
                 dt=input('Enter the date(dd/mm/yyyy) :')
                 cntno=input('Enter contact no. :')
                 print('\n\n\t\tYour slot has been booked\n\t\t             Thank you')
                 usrintr()
           else:
                  print('The selected hospital is not Registered for Blood donation.')
                  donate()
     elif honm=='0':
           usrintr()
     else:
              print('Enter valid hospital')
              donate()

         
def recieve():
    import mysql.connector as si
    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=mycon.cursor()
    print('A+ =AP\tB+ =BP\tAB+ =ABP\tO+ =OP\nA- =AN\tB- =BN\tAB- =ABN\tO- =ONEG')
    bltyr=input('Enter the required Blood Type :')
    blty=bltyr.upper()
    if blty in lst:
          st="select Hospital_name from blddt where {}='Y'".format(blty)
          cr.execute(st)
          dt=cr.fetchall()
          if dt!=[]:
                print('\nThe Selected blood is available in:')
                global lst2
                lst2=[]
                for i in dt:
                      print(i[0])
                      lst2.append(i[0])
                honm=input('\nEnter the hospital name :')
                if honm in lst2:
                      cr.execute("select contctno from hspdt where Hospital_Name='{}'".format(honm))
                      data=cr.fetchone()
                      print('Contact No :',end='')
                      print(data[0])
                      print('\nYou may contact the Hospital for further details')
                      print('\nGet well Soon')
                      usrintr()
                else:
                      print('Enter a valid Hospital name')
                      hsptnmc()
          else:
                print('\nSorry the blood is not available in any nearby Hospitals :-(')
                usrintr()
    else:
          print('='*100)
          print('Enter a valid Blood group')
          recieve()
            

def hsptnmc():
    import mysql.connector as si
    mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=mycon.cursor()
    honm=input('\nEnter the hospital name :')
    if honm in lst2:
          cr.execute("select contctno from hspdt where Hospital_Name='{}'".format(honm))
          data=cr.fetchone()
          print('Contact No :',end='')
          print(data[0])
          print('\nYou may contact the Hospital for further details')
          print('\nGet well Soon')
          usrintr()
    else:
          print('Enter a valid Hospital name')
          hsptnmc()



            #To create a new account for hospital
def hosp():
      print('='*100)
      print('\n\t\t\t        Creating a new Profile as Hospital \n')
      hnm=input('Enter Hospital Name     :')
      hlo=input('Enter Location               :')
      hcn=input('Enter contact no.            :')
      hunm=input('Enter the Username       :')
      hps=input('Enter the Password       :')
      db=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='blddn')
      mc=db.cursor()
      mc.execute("select * from hspdt where Username='{}'".format(hunm))
      sb=mc.fetchone()
      if db.is_connected():
            if sb==None:
                  mc.execute("insert into hspdt values('{}','{}','{}','{}','{}')".format(hnm,hlo,hcn,hunm,hps))           
                  db.commit()
            else:
                  print('username already exist')
                  hosp()
            mc.execute("insert into blddt values('{}','N','N','N','N','N','N','N','N')".format(hnm))
            db.commit()
            db.close()

         #To display the availability of the blood group at a Hospital 
def disply():
    print('='*100)
    import mysql.connector as ms
    cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=cn.cursor()
    st="select Hospital_Name from hspdt where username='{}'".format(usrnm)
    cr.execute(st)
    dt=cr.fetchone()
    nm=dt[0]
    a=cr.execute("select * from blddt where Hospital_Name='{}'".format(nm))
    inf=cr.fetchall()
    print('\tA+\tA-\tB+\tB-\tO+\tO-\tAB+\tAB-')
    for i in range(len(inf[0])):
          print(inf[0][i],end='\t')
    print()
    print('='*100)
    hspint()

           #To Request Blood
def bldreq():
    N=input("Enter the blood group to be requested \nA+ =AP\t\tB+ =BP\t\tAB+ =ABP\tO+ =OP\nA- =AN\t\tB- =BN\t\tAB- =ABN\tO- =ONEG \nEnter the Blood Group : ")
    n=N.upper()


    if n in lst:
          print('A Notification has been sent to the users for ',N, "blood group")
          print()
          
          hspint()
    else:
          print('='*100)
          print('Enter a valid blood group')
          bldreq()

             #Hospital Interface
def hspint():
    import mysql.connector as ms
    cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=cn.cursor()
    print('1.Update')
    print('2.Request')
    print('3.Diplay Blood Bank Information')
    print('4.Donation Waiting List in ')
    print('5.Log Out')
    print('6.Delete account:')
    n=input('\tEnter:')
    print('='*100)
    if n=='1':
          update()
    elif n=='2':
          bldreq()
    elif n=='3':
          disply()
    elif n=='6':
          delhs()
    elif n=='5':
          home()
    elif n=='4':
          print('Name of donor\tBlood group')
          st="select Hospital_Name from hspdt where username='{}'".format(usrnm)
          cr.execute(st)
          dt=cr.fetchone()
          nm=dt[0]
          cr.execute("Select Name,requested_bldgrp from report where hospital_name='{}'".format(nm))
          dt=cr.fetchall()
          for i in dt:
            print(i[0],'\t\t',i[1])
          print('='*100)
          hspint()
    else:
          print('Enter a Valid option')
          hspint()


def update():
    print('='*100)
    import mysql.connector as ms
    cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=cn.cursor()
    st="select Hospital_Name from hspdt where username='{}'".format(usrnm)
    cr.execute(st)
    dt=cr.fetchone()
    nm=dt[0]
    print('A+ =AP\tB+ =BP\tAB+ =ABP\tO+ =OP\nA- =AN\tB- =BN\tAB- =ABN\tO- =ONEG')
    bg=input('Enter the blood group to be updated:')
    bgc=bg.upper()
    if bgc in lst:
        print('1.Change availability to Yes')
        print('2.Change availability to No')
        k=input('Enter:')
        if k=='1':
            st="update blddt set {}='{}' where Hospital_Name='{}';".format(bgc,'Y',nm)
            print('\t\tSuccesfully Updated')
            print('='*100)
            cr.execute(st)
            cn.commit()
            hspint()
        elif k=='2':
              st="update blddt set {}='{}' where Hospital_Name='{}';".format(bgc,'N',nm)
              print('\t\tSuccesfully updated')
              print('='*100)
              cr.execute(st)
              cn.commit()
              hspint()
              cn.close()
        else:
              print('Enter  a valid option')
              update()              
    else:
          print('Enter a valid Blood Group')
          update()
          
      
      
                      #Signin interface if USER or HOSPITAL
def signin():
      print('='*100)
      global usrnm
      import mysql.connector as ms
      cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
      cr=cn.cursor()
      print('\nSign in as')
      print('1.User')
      print('2.Hospital')
      print('3.Exit')
      n=input('Enter:')
      if n=='1':
            print('\nEnter your username and password.')
            usrnm=input('Username:')
            cr.execute('Select username from usrdt')
            dt=cr.fetchall()
            lst=[]
            for i in range(len(dt)):
                lst.append(dt[i][0])
            x=1
            if str(usrnm) in lst:
                  pswd=input('Password:')
                  st="select password from usrdt where Username='{}'".format(usrnm)
                  cr.execute(st)
                  psd=cr.fetchone()
                  if pswd==psd[0]:
                        usrintr()
                        x=0
                  else:
                        print("Username and password doesn't match\n")
            else:
                  print('No username Found !!\n')
            while x==1:
                  signin()
      elif n=='2':
            print('Enter your username and password.')
            usrnm=input('Username:')
            cr.execute('Select username from hspdt')
            dt=cr.fetchall()
            lst=[]
            for i in range(len(dt)):
                lst.append(dt[i][0])
            x=1
            if str(usrnm) in lst:
                  pswd=input('Password:')
                  st="select password from hspdt where Username='{}'".format(usrnm)
                  cr.execute(st)
                  psd=cr.fetchone()
                  if pswd==psd[0]:
                        st="select Hospital_Name from hspdt where username='{}'".format(usrnm)
                        cr.execute(st)
                        dt=cr.fetchone()
                        nm=dt[0]
                        print('='*100)
                        print('\t\tWelcome',nm)
                        st="select Location from hspdt where username='{}'".format(usrnm)
                        cr.execute(st)
                        dt=cr.fetchone()
                        print(nm)
                        print('Location =',dt[0])
                        print()
                        hspint()
                        x=0
                  else:
                        print("Username and password doesn't match\n")
            else:
                  print('No username Found !!\n')
            while x==1:
                  signin()
      elif n=='3':
            home()
      else:
            print('\tEnter a valid option\n')
            signin()

            # To delete a Hospital
def delhs():
    print('='*100)
    import mysql.connector as ms
    cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=cn.cursor()
    nm=usrnm
    cr.execute("select * from hspdt where username='{}'".format(nm))
    lm=cr.fetchone()
    n=input('Are you sure? (Y/N):')
    print()
    if n=='Y' or n=='y':
          if lm!=None:
              st="select Hospital_Name from hspdt where username='{}'".format(usrnm)
              cr.execute(st)
              dt=cr.fetchone()
              nm=dt[0]
              cr.execute("delete  from hspdt where username='{}'".format(nm))
              cn.commit()
              cr.execute("delete  from blddt where Hospital_Name='{}'".format(nm))
              cn.commit()
              
          else:
               print('User not found.')
    elif n=='N' or n=='n':
          hspint()
    else:
          print('Enter a valid option:')
          delhs()

         
                          #To Delete a User
def delus():
    print('='*100)
    import mysql.connector as ms
    cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
    cr=cn.cursor()
    cr.execute("select * from usrdt where Username='{}'".format(usrnm))
    lm=cr.fetchone()
    n=input('Are you sure? (Y/N):')
    print()
    if n=='Y' or n=='y':
          if lm!=None:
                cr.execute("delete  from usrdt where Username='{}'".format(usrnm))
                print('We are sad to see you go :-(\n')
                cn.commit()
                home()
                
          else:
                print('User not found.\n')
    elif n=='N' or n=='n':
          import mysql.connector as si
          mycon=si.connect(host='localhost',user='root',passwd='123456',database='blddn')
          cr=mycon.cursor()
          cr.execute("select * from usrdt where Username='{}'".format(usrnm))
          dat=cr.fetchall()
          print()
          print(dat[0][0])
          print('Blood group:',dat[0][2])
          n=int(input("\n1.Donate Blood.Save a life\n2.Recieve\n3.Delete the account\nEnter Your Choice : "))
          if n==1:
              donate()     
          elif n==2:
              recieve()
          elif n==3:
                delus()
                
          else:
              print('Enter a valid opton')
              usrintr()
    else:
          print('Enter a valid option:')
          delus()

                        # Main Menu            
def home():
      while True:
            print('='*100)
            print("")
            
            print(' \t\t\t\t Welcome to Blood Link')
            print('\t\t\t   Be the reason for someones heartbeat')
            print("")
            print('='*100)
            print("\n")
            print('1.Register')
            print('2.Already a user?Sign In.')
            print('3.Enter any other key to exit')
            n=input('Enter :-)')
            if n=='1':
                register()
            elif n=='2':
                signin()
            else:
                  exit()
                  
                  break
          

def hsptnm():
      import mysql.connector as ms
      cn=ms.connect(host='localhost',user='root',passwd='123456',database='blddn')
      cr=cn.cursor()
      cr.execute("select Hospital_Name from hspdt")
      dt=cr.fetchall()
      if dt!=[]:
             print('Available Hospitals:\n')
             list=[]
             for i in range(len(dt)):
                 print(dt[i][0])
                 list.append(dt[i][0])
      else:
            print('No Hospitals available')
home()











