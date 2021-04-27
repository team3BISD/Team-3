#Program: Ampersand Reward System
#Developer: Python Ninjas
#Due Date: 4/27
#Purpose: The application allows the user to input information to create a rewards records that later enables the system to calculate the rewards assigned to each client

from tkinter import * # Import tkinter
import random #import random for Rewards Number
from tkinter import messagebox as msg

class System:
    def __init__(self):
        self.initialPage()

# Window Transition Functions

    def gotoInitialfromRedeem(self): #creates function to Home Page from Redeem Page for use on button with functionality to update and read the Customer_data.txt
        RRP=int(self.redeemRewardsVar.get())
        valid=True

        if RRP<=self.ActualRP:
            New_RP=self.ActualRP-RRP
            New_discount=0.1*RRP
            data=open("C:\\Customers_data.txt","r") #please update file path as needed to match your file destination
            lines=data.readlines()
            data.close()
            for line in lines:
                fields=line.split()
                if self.ActualPT==fields[10]:
                    client=line
            client_list=client.split()
            client_list[11]=str(New_RP)
            
            new_line="\n"
            for field in client_list:
                new_line+=field+"   "
            lines.remove(client)
            data=open("C:\\Customers_data.txt","w") #please update file path as needed to match your file destination
            for line in lines:
                data.write(line)
            data.write(new_line)
            data.close()            
        else:
            msg.showwarning("Invalid Input","You cannot spend more Points\nthan you already have >:(")
            valid=False
            self.redeemRewardsEntry.focus_set()
        
        if valid:
            self.redewin.quit()
            self.redewin.destroy()
            self.initialPage()

    def gotoInitialfromlogRewards(self): #creates function to Home Page from Log Rewards Page for use on button with function to update the Customer_data.txt
        phone=self.phoneNumberLogRVar.get()
        rewardID=self.rewardsIDVar.get()
        purchase=self.purchaseTotalVar.get()
        data=open("C:\\Customers_data.txt","r")
        lines=data.readlines()
        data.close()
        verif=False
        valid=True
        if phone!="":
            for line in lines:
                cust=line.split()
                if cust[2]==phone:
                    verif=True
                    client=line
                    print(client)
        
        if rewardID!="":
            for line in lines:
                cust=line.split()
                if cust[9]==rewardID:
                    verif=True
                    client=line
        
        if purchase=="" and verif:
            msg.showwarning("Empty Field","The purchase field is empty")
            valid=False
        
        if not(verif):
            msg.showwarning("No coincident","the entered data is not registered")
            self.purchaseTotalEntry.focus_set()
            
        if valid and verif:
            client_list=client.split()
            
           
            client_list[11]=str(int(client_list[11])+int(purchase)//10)     #add rewards points
            new_line=""
            for field in client_list:
                new_line+=field+"   "
            lines.remove(client)
            data=open("C:\\Customers_data.txt","w")
            for line in lines:
                data.write(line)
            data.write(new_line)
            data.close()

            self.logrewin.quit()
            self.logrewin.destroy()
            self.initialPage()

    def gotoInitialfromConfirmation(self): #creates function to Homepage from Confirmation Page for use on button
        self.confwin.quit()
        self.confwin.destroy()
        self.initialPage()

    def gotoCustomer(self): #creates function to Customer Page from Home Page for use on button
        self.initwin.quit()
        self.initwin.destroy()
        self.customerPage()

    def gotoEmployee(self): #creates function to Employee Page from Home Page for use on button
        self.initwin.quit()
        self.initwin.destroy()
        self.employeePage()

    def gotoRedeem(self): #creates function to Redeem Page from Customer Page for use on button with validation of data using the Customer_data.txt
        phone=self.phoneNumberlogVar.get()
        rewardID=self.rewardIDVar.get()
        data=open("C:\\Customers_data.txt","r")
        verif=False
        if phone!="":
            for line in data:
                cust=line.split()
                print(cust[2])
                print(phone)
                print(rewardID)
                if cust[2]==phone:
                    verif=True
                    name=cust[0]+" "+cust[1]
                    purchasetotal=cust[10]
                    RP=cust[11]
        if rewardID!="":
            for line in data:
                cust=line.split()
                if cust[9]==rewardID:
                    verif=True
                    name=cust[0]+" "+cust[1]
                    purchasetotal=cust[10]
                    RP=cust[11]
        
        data.close()

        if not(verif):
            msg.showwarning("No coincident","the entered data is not registered")
            self.phnumlogEntry.focus_set()
        else:
            self.custwin.quit()
            self.custwin.destroy()
            self.redeemPage(name,purchasetotal,RP)    
    
    def gotoSingup(self): #creates function to Sign Up Page from Customer Page for use on button
        self.custwin.quit()
        self.custwin.destroy()
        self.signUpPage()

    def gotoLogRewards(self): #creates function to Log Rewards Page from Employee Page for use on button with validation of employee login data using Employee_data.txt
        valid=True
        ID=self.employeeID.get()
        if ID=="":
            self.emptymsg("ID")
            self.EmployeeIDEntry.focus_set()
            valid=(False)
        ID=int(ID)
        
        data=open("C:\\Employees_data.txt","r")
        verif=False
        for line in data:
            employee=line.split()
            if employee[2]!='ID':
                if int(employee[2])==ID:
                    verif=True
                    name=employee[0]+" "+employee[1]
        
        data.close()

        if not(verif):
            msg.showwarning("No coincident","the entered ID is not registered")
            self.EmployeeIDEntry.focus_set()

        if valid and verif:
            self.emplwin.quit()
            self.emplwin.destroy()
            self.logRewardsPage(name)

    def gotoConfirmation(self): #creates function to Confimration Page from Sign Up Page for use on button

        empty=self.verificateSignUpEntries()
        valid=self.validateSignUp()

        if empty and valid:
            new_client=self.NewClientRegister()
            self.supwin.quit()
            self.supwin.destroy()
            self.confirmationPage(new_client)

# Verification & Validation Functions

    def VerificateNumber(self,text):
        return text.isdecimal()

    def VerificateText(self,text):
        return text.isalpha()
    
    def VerificateAlNum(self,text):
        return text.isalnum()

    def emptymsg(self,name):
        msg.showwarning("Empty Field","The %s Field is Empty" % name)
    
    def verificateSignUpEntries(self): #sign up page validation statements
        if self.firstNameVar.get()=="":
            self.emptymsg("First Name")
            self.FnameEntry.focus_set()
            return(False)
        elif self.lastNameVar.get()=="":
            self.emptymsg("Last Name")
            self.LnameEntry.focus_set()
            return(False)
        elif self.phoneNumberVar.get()=="":
            self.emptymsg("Phone Number")
            self.PhoneEntry.focus_set()
            return(False)
        elif self.emailVar.get()=="":
            self.emptymsg("Email")
            self.EmailEntry.focus_set()
            return(False)
        elif self.streetAddressVar.get()=="":
            self.emptymsg("Street Address")
            self.StreetEntry.focus_set()
            return(False)
        elif self.cityVar.get()=="":
            self.emptymsg("City")
            self.CityEntry.focus_set()
            return(False)
        elif self.StateVar.get()=="":
            self.emptymsg("State")
            self.StateMenu.focus_set()
            return(False)
        elif self.zipCodeVar.get()=="":
            self.emptymsg("Zip Code")
            self.ZipEntry.focus_set()
            return(False)
        elif self.birthdayVar.get()=="":
            self.emptymsg("Birthday")
            self.BirthdayEntry.focus_set()
            return(False)
        return(True)

    def validateSignUp(self):
        #email=self.emailVar.get()
        phone=self.phoneNumberVar.get()
        zip=self.zipCodeVar.get()
        #if not(email.count("@")==1) or email.count(".")==0:
        #    msg.showwarning("Invalid Input","The email inserted is not valid")
        #    self.EmailEntry.focus_set()
        #    return(False)
        if not(self.validateEmail()):
            return(False)
        if not(self.validateBirthday()):
            return(False)
        if len(phone)!=10:
            msg.showwarning("Invalid Input","The phone number inserted is not valid")
            self.PNEntry.focus_set()
            return(False)
        if len(zip)!=5:
            msg.showwarning("Invalid Input","The Zip Code inserted is not valid")
            self.ZipEntry.focus_set()
            return(False)
        return(True)

    def validateEmail(self):
        email=self.emailVar.get()
        if not(email.count("@")==1) or email.count(".")==0:
            msg.showwarning("Invalid Input","The email inserted is not valid")
            self.EmailEntry.focus_set()
            return(False)
        l=email.split("@")
        user=l[0]
        domain=l[1]
        if user=="":
            msg.showwarning("Invalid Input","The email inserted is not valid")
            self.EmailEntry.focus_set()
            return(False)
        if domain=="" or not((domain.replace(".","")).isalpha()) or domain.count(".")!=1:
            msg.showwarning("Invalid Input","The email inserted is not valid")
            self.EmailEntry.focus_set()
            return(False)
        return(True)

    def validateBirthday(self):
        bday=self.birthdayVar.get()
        if bday.count("/")==0:
            msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
            self.BirthdayEntry.focus_set()
            return(False)
        numbers=bday.split("/")
        if len(numbers)!=3:
            msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
            self.BirthdayEntry.focus_set()
            return(False)
        for i in range(len(numbers)):
            if numbers[i].isdecimal():
                numbers[i]=int(numbers[i])
            else:
                msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
                self.BirthdayEntry.focus_set()
                return(False)
        if numbers[0]>12:
            msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
            self.BirthdayEntry.focus_set()
            return(False)
        if numbers[1]>31:
            msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
            self.BirthdayEntry.focus_set()
            return(False)
        if int(numbers[2]//1000)==0 or numbers[2]>2021:
            msg.showwarning("Invalid Input","The Birthday inserted is not valid\nit mustbe in format: mm/dd/aaaa\nTry to insert a valid date")
            self.BirthdayEntry.focus_set()
            return(False)
        return(True)

    def NewClientRegister(self):
        Fname=self.firstNameVar.get()
        Lname=self.lastNameVar.get()
        phone=self.phoneNumberVar.get()
        email=self.emailVar.get()
        street=self.streetAddressVar.get()
        city=self.cityVar.get()
        state=self.StateVar.get()
        zipcode=self.zipCodeVar.get()
        birthday=self.birthdayVar.get()
        new_client="\n"+Fname+"   "+Lname+"   "+phone+"   "+email+"   "+street+"   "+city+"   "+state+"   "+zipcode+"   "+birthday
        return(new_client)

#User Pages

    def initialPage(self):
        #self.buttonExample = Button(self.win, 
        #      text="Create new window",
        #      command=self.createNewWindow)
        #self.buttonExample.pack()
        
        self.initwin=Tk() #our initial Home Page window
        self.initwin.title("Home Page") # Set title of the window
        self.initwin.configure(background='white')
        self.initwin.geometry("500x400") #sets window size

        photo = PhotoImage(file=r'C:\Users\htcam\iCloudDrive\Documents\TCU\BIS Systems Development\APPLICATION\Ampersand.png') #company logo file path; change as needed to work for your file system
        Label(self.initwin, image=photo, bg='White').place(x=130,y=10) #put the image in a label to display it in the window

        Label(self.initwin, text = "Welcome to Ampersand Reward System", justify=CENTER, bg='White', font=("Arial", 18)).place(x=33, y=250) #displays title on page with larger text
        self.CustomerButton=Button(self.initwin, text = "Customer", width=12, bg='Black', fg='White', font=("Arial", 14), command = self.gotoCustomer) #creates cutsomer button using the gotoCustomer function
        self.CustomerButton.place(x=60, y=320)
        self.EmployeeButton=Button(self.initwin, text = "Employee", width=12, bg='Black', fg='White', font=("Arial", 14), command = self.gotoEmployee) #creates employee button using the gotoEmployee function
        self.EmployeeButton.place(x=290, y=320)

        self.initwin.mainloop()

    def customerPage(self): #creates our Customer page window
        self.custwin=Tk()
        self.custwin.title("Customer Page") # Set title of the window
        self.custwin.configure(background='white')
        self.custwin.geometry("500x500") #sets window size

        Label(self.custwin, text = "Welcome to the reward system Customer Page!", bg='White', justify=CENTER, font=('Arial', 16)).place(x=17, y=35) #adds large text title to page


        self.SingupButton=Button(self.custwin, text = "Sign Up", width=12, bg='Black', fg='White', font=("Arial",14), command = self.gotoSingup) #creates sign up button using the gotoSignup function and proper validation associated
        self.SingupButton.place(x=170, y=100)
        Label(self.custwin, text = "Already have an account?", bg='White', font=("Arial",12), justify=CENTER).place(x=150, y=160)
        Label(self.custwin, text = "Reward number", bg='White', font=("Arial",12), justify=CENTER).place(x=180, y=200)
        Label(self.custwin, text = "OR", bg='white', font=("Arial",12), justify=CENTER).place(x=220, y=275)
        Label(self.custwin, text = "Phone number", bg='White', font=("Arial",12), justify=CENTER).place(x=180, y=320)

        #creates window input boxes
        self.rewardIDVar = StringVar()
        self.rewardIDEntry=Entry(self.custwin, textvariable = self.rewardIDVar, justify = LEFT, validate="key", validatecommand=(self.custwin.register(self.VerificateNumber), "%S"))
        self.rewardIDEntry.place(x=180, y=230)
        self.phoneNumberlogVar = StringVar()
        self.phnumlogEntry=Entry(self.custwin, textvariable = self.phoneNumberlogVar, justify = LEFT, validate="key", validatecommand=(self.custwin.register(self.VerificateNumber), "%S"))
        self.phnumlogEntry.place(x=180, y=350)

        self.SinginButton=Button(self.custwin, text = "Sign In", width=12, bg='Black', fg='White', font=("Arial",14),command = self.gotoRedeem) #creates sign in button using the gotoRedeem function and associated validation
        self.SinginButton.place(x=170, y=410)
        self.custwin.mainloop() # Create an event loop

    def employeePage(self): #created Employee Page
        self.emplwin=Tk()
        self.emplwin.title("Employee Page") # Set title of the window
        self.emplwin.configure(background='white')
        self.emplwin.geometry("500x250") #sets window size

        Label(self.emplwin, text = "Enter employee ID", bg='White', justify=CENTER, font=('Arial', 16)).place(x=165, y=35) #adds large text title

        #employee ID input box
        self.employeeID = StringVar()
        self.EmployeeIDEntry=Entry(self.emplwin, textvariable = self.employeeID, justify = LEFT, validate="key", validatecommand=(self.emplwin.register(self.VerificateNumber), "%S"))
        self.EmployeeIDEntry.place(x=190, y=110)

        self.LoginButton=Button(self.emplwin, text = "Log In", width=12, bg='Black', fg='White', font=("Arial",14),command = self.gotoLogRewards) #creates button using the gotoLogRewards function and validates the employee ID entry
        self.LoginButton.place(x=183, y=185)

        self.emplwin.mainloop()

    def redeemPage(self,name,PT,RP): #creates Redeem Page
        self.redewin=Tk()
        self.redewin.title("Redeem Points") # Set title of the window
        self.redewin.configure(background='white')
        self.redewin.geometry("700x300") #sets window size

        Label(self.redewin, text = ("Hello "+name+", your Reward Points total is: "+RP), bg='White', justify=CENTER, font=('Arial', 16)).place(x=80, y=35) #creates large text personalized title
        Label(self.redewin, text = "How many points would you like to spend?", bg='White', font=("Arial",12), justify=CENTER).place(x=185, y=80)
        Label(self.redewin, text = "** 1 point earned for every $10 spent. Redeem 1 point to receive $0.10 off on this purchase. **", bg='White', font=("Arial",12), justify=CENTER).place(x=20, y=185) #note on point calculation and the value of 1 point

        #creates input box
        self.ActualRP=int(RP)
        self.ActualPT=PT
        self.redeemRewardsVar = StringVar()
        self.redeemRewardsEntry=Entry(self.redewin, textvariable = self.redeemRewardsVar, justify = LEFT, validate="key", validatecommand=(self.redewin.register(self.VerificateNumber), "%S"))
        self.redeemRewardsEntry.place(x=265, y=135)

        RedeemButton=Button(self.redewin, text = "Redeem", width=12, bg='Black', fg='White', font=('Arial', 14),command = self.gotoInitialfromRedeem) #creates button using the gotoInitialfromRedeem function and updates reward account using that function
        RedeemButton.place(x=262, y=235)

        self.redewin.mainloop()

    def logRewardsPage(self,employeeName): #creates Log Rewards Page
        self.logrewin=Tk()
        self.logrewin.title("Log Rewards") # Set title of the window
        self.logrewin.configure(background='white')
        self.logrewin.geometry("500x600") #sets window size

        Label(self.logrewin, text = "Welcome "+employeeName+" to the Log Rewards Page!", bg='White', font=('Arial', 15)).place(x=17, y=30) #creates cusstomized large text title

        #other text labels for the window
        Label(self.logrewin, text = "Customer Reward number", bg='White', font=('Arial', 12)).place(x=150, y=95)
        Label(self.logrewin, text = "OR", bg='White', font=('Arial', 12)).place(x=220, y=185)
        Label(self.logrewin, text = "Customer Phone number", bg='White', font=('Arial', 12)).place(x=150, y=245)
        Label(self.logrewin, text = "AND", bg='White', font=('Arial', 12)).place(x=220, y=335)
        Label(self.logrewin, text = "Customer Purchase total", bg='White', font=('Arial', 12)).place(x=150, y=400)

        #creates input boxes for window
        self.rewardsIDVar = StringVar()
        self.rewardIDEntry=Entry(self.logrewin, textvariable = self.rewardsIDVar, justify = LEFT, validate="key", validatecommand=(self.logrewin.register(self.VerificateNumber), "%S"))
        self.rewardIDEntry.place(x=180, y=125)
        self.phoneNumberLogRVar = StringVar()
        self.PNEntry=Entry(self.logrewin, textvariable = self.phoneNumberLogRVar, justify = LEFT, validate="key", validatecommand=(self.logrewin.register(self.VerificateNumber), "%S"))
        self.PNEntry.place(x=180, y=275)
        self.purchaseTotalVar = StringVar()
        self.purchaseTotalEntry=Entry(self.logrewin, textvariable = self.purchaseTotalVar, justify = LEFT, validate="key", validatecommand=(self.logrewin.register(self.VerificateNumber), "%S"))
        self.purchaseTotalEntry.place(x=180, y=430)

        self.logRewardsButton=Button(self.logrewin, text = "Log Rewards", width=12, bg='Black', fg='White', font=("Arial", 14),command = self.gotoInitialfromlogRewards) #creates button using the gotoInitialfromlogRewards function and updates cutomer account data
        self.logRewardsButton.place(x=175, y=520)

    def signUpPage(self): #creates sign up page
        self.supwin=Tk()
        self.supwin.title("Sign Up for Rewards") # Set title of the window
        self.supwin.configure(background='white')
        self.supwin.geometry('500x800') #sets window size

        #creates input box labels for window
        Label(self.supwin, text = "Sign Up for Rewards", bg='White', font=('Arial', 19)).place(x=135, y=40)
        Label(self.supwin, text = "First name (*)", bg='White', font=('Arial', 12)).place(x=180, y=95)
        Label(self.supwin, text = "Last name (*)", bg='White', font=('Arial', 12)).place(x=180, y=150)
        Label(self.supwin, text = "Phone Number (*)", bg='White', font=('Arial', 12)).place(x=180, y=205)
        Label(self.supwin, text = "Email (*)", bg='White', font=('Arial', 12)).place(x=180, y=260)
        Label(self.supwin, text = "Street Address (*)", bg='White', font=('Arial', 12)).place(x=180, y=315)
        Label(self.supwin, text = "City (*)", bg='White', font=('Arial', 12)).place(x=180, y=370)
        Label(self.supwin, text = "State (*)", bg='White', font=('Arial', 12)).place(x=180, y=425)

        #creates options for use in state drop-down list
        self.StateVar = StringVar(self.supwin)
        choices = {'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
        'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY',
        'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'}
        choices=sorted(choices)
        self.StateMenu = OptionMenu(self.supwin,self.StateVar, *choices) #creates drop-down list
        self.StateMenu.place(x=180, y=450)

        #more input box labels
        Label(self.supwin, text = "Zip Code (*)", bg='White', font=('Arial', 12)).place(x=180, y=490)
        Label(self.supwin, text = "Birthday (*)", bg='White', font=('Arial', 12)).place(x=180, y=545)
        Label(self.supwin, text = "\n\nBy clicking Sign Up, you agree to Ampersand's Terms of Use and acknowledge\n you have read the Privacy Policy. You also consent to receive calls or SMS \nmessages, including by automated dialer, from Ampersand and its affiliates to the \nnumber you provide for informational and/or marketing purposes. Consent to \nreceive marketing messages is not a condition to use Ampersand’s services. You \nunderstand that you may opt out by texting “STOP” to 89203.", bg='White', font=('Arial', 9)).place(x=17, y=650)

        #Create data input boxes
        self.firstNameVar = StringVar()
        self.FnameEntry=Entry(self.supwin, textvariable = self.firstNameVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateText), "%S"))
        self.FnameEntry.place(x=180, y=120)
        self.lastNameVar = StringVar()
        self.LnameEntry=Entry(self.supwin, textvariable = self.lastNameVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateText), "%S"))
        self.LnameEntry.place(x=180, y=175)
        self.phoneNumberVar = StringVar()
        self.PhoneEntry=Entry(self.supwin, textvariable = self.phoneNumberVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateNumber), "%S"))
        self.PhoneEntry.place(x=180, y=230)
        self.emailVar = StringVar()
        self.EmailEntry=Entry(self.supwin, textvariable = self.emailVar, justify = LEFT)
        self.EmailEntry.place(x=180, y=285)
        self.streetAddressVar = StringVar()
        self.StreetEntry=Entry(self.supwin, textvariable = self.streetAddressVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateAlNum), "%S"))
        self.StreetEntry.place(x=180, y=340)
        self.cityVar = StringVar()
        self.CityEntry=Entry(self.supwin, textvariable = self.cityVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateText), "%S"))
        self.CityEntry.place(x=180, y=395)
        self.zipCodeVar = StringVar()
        self.ZipEntry=Entry(self.supwin, textvariable = self.zipCodeVar, justify = LEFT, validate="key", validatecommand=(self.supwin.register(self.VerificateNumber), "%S"))
        self.ZipEntry.place(x=180, y=515)
        self.birthdayVar = StringVar()
        self.BirthdayEntry=Entry(self.supwin, textvariable = self.birthdayVar, justify = LEFT)
        self.BirthdayEntry.place(x=180, y=570)

        Button(self.supwin, text = "Sign Up", width=12, bg='Black', fg='White', font=("Arial", 16),command = self.gotoConfirmation).place(x=170, y=620) #creates button using the gotoConfirmation function

        self.supwin.mainloop()

    def confirmationPage(self,client): #creates Confirmation Page
        self.confwin=Tk()
        self.confwin.title("Confirmation Page") # Set title of the window
        self.confwin.configure(background='white')
        self.confwin.geometry("500x250") #sets window size

        data=open("C:\\Customers_data.txt","r") #opens customer data file
        coincidence=True
        while(coincidence):
            randNum = round(random.uniform(10000,99999)) #creates random rewards ID number
            coincidence=False
            for line in data:
                field=line.split()
                if field[9]==str(randNum):
                    coincidence=True
        data.close()
        client=client+"   "+str(randNum)+"   000   0"
        data=open("C:\\Customers_data.txt","a")
        data.write(client)
        data.close()
        self.rewardNum = randNum #assigns a random number to reward number

        #creates text labels for window
        Label(self.confwin, text = "Congratulations, You're earning points!", bg='White', font=('Arial', 19)).place(x=25, y=25)
        Label(self.confwin, text = "Your Rewards Number", bg='White').place(x=185, y=85)
        Label(self.confwin, text = self.rewardNum, bg='White', font=('Arial', 16)).place(x=210, y=110)
        Label(self.confwin, text = "Thank you and make sure to visit on your birthday for your free treat!", bg='White').place(x=65, y=170)

        self.HomeButton=Button(self.confwin, text = "Home", width=21, bg='Black', fg='White', font=("Arial", 16),command = self.gotoInitialfromConfirmation) #creates button using the gotoInitialfromConfirmation function
        self.HomeButton.place(x=120, y=200)

        self.confwin.mainloop() # Create an event loop

syst=System()  #start GUI
