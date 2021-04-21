from tkinter import * # Import tkinter; do not need to install it
from random import random

class RewardSystem:
    def __init__(self):
         window = Toplevel()
         window.title("Home Page") # Set title of the window
         window.configure(background='white')
         window.geometry("500x400")

         photo = PhotoImage(file=r'C:\Users\htcam\iCloudDrive\Documents\TCU\BIS Systems Development\APPLICATION\Ampersand.png')
         Label(window, image=photo, bg='White').place(x=130,y=10) #put the image in a label to display it in the window
         
         Label(window, text = "Welcome to Ampersand Reward System\n", justify=CENTER, bg='White', font=("Arial", 18)).place(x=33, y=250)
         
         Button(window, text = "Customer", width=12, bg='Black', fg='White', font=("Arial", 14), command = self.customerPage).place(x=60, y=320)
         Button(window, text = "Employee", width=12, bg='Black', fg='White', font=("Arial", 14), command = self.employeePage).place(x=290, y=320)

         window.mainloop() # Create an event loop
        
    def customerPage(self):
         window = Tk()
         window.title("Customer Page") # Set title of the window
         window.configure(background='white')

         
         Label(window, text = "Welcome to the reward system Customer Page!\n\n").grid(row = 2, column = 1, sticky = W)

         Button(window, text = "Sign Up", width=12, bg='White', fg='Black', command = self.signUpPage).grid(row = 3, column = 1, sticky = W)
         Label(window, text = "\n\nAlready have an account?\n").grid(row = 4, column = 1, sticky = W)
         Label(window, text = "Reward number").grid(row = 5, column = 1, sticky = W)
         Label(window, text = "\n\nOR\n\n").grid(row = 7, column = 1, sticky = W)
         Label(window, text = "Phone number").grid(row = 8, column = 1, sticky = W)
         Label(window, text = "\n\n").grid(row = 10, column = 1, sticky = W)
         self.rewardID = StringVar()
         Entry(window, textvariable = self.rewardID, justify = LEFT).grid(row = 6, column = 1)
         self.phoneNumberVar = StringVar()
         Entry(window, textvariable = self.phoneNumberVar, justify = LEFT).grid(row = 9, column = 1)

         Button(window, text = "Sign In", width=12, bg='White', fg='Black', command = self.redeemPage).grid(row = 11, column = 1, sticky = W)
         window.mainloop() # Create an event loop

    def redeemPage(self):
         window = Tk()
         window.title("Redeem Points") # Set title of the window
         window.configure(background='white')

         Label(window, text = "Total Rewards\n").grid(row = 1, column = 1, sticky = W)
         Label(window, text = "\nHow many points would you like to spend?\n").grid(row = 3, column = 1, sticky = W)
         
         Label(window, text = "\n\n\n** 1 point earned for every $10 spent. Redeem 1 point to receive $0.10 off on this purchase. **\n\n").grid(row = 8, column = 1, sticky = W)

         self.totalRewards = StringVar()
         Entry(window, textvariable = self.totalRewards, justify = LEFT).grid(row = 2, column = 1)
         self.redeemRewards = StringVar()
         Entry(window, textvariable = self.redeemRewards, justify = LEFT).grid(row = 4, column = 1)

         Button(window, text = "Redeem", width=12, bg='White', fg='Black', command = self.__init__).grid(row = 10, column = 1, sticky = W)
         window.mainloop() # Create an event loop

    def employeePage(self):
         window = Tk()
         window.title("Employee Page") # Set title of the window
         window.configure(background='white')
         
         Label(window, text = "Enter employee ID\n").grid(row = 1, column = 1, sticky = W)
         Label(window, text = "\n").grid(row = 3, column = 1, sticky = W)

         self.employeeID = StringVar()
         Entry(window, textvariable = self.employeeID, justify = LEFT).grid(row = 2, column = 1)

         Button(window, text = "Log In", width=12, bg='White', fg='Black', command = self.logRewardsPage).grid(row = 4, column = 1, sticky = W)
         window.mainloop() # Create an event loop

    def logRewardsPage(self):
         window = Tk()
         window.title("Log Rewards") # Set title of the window
         window.configure(background='white')

         Label(window, text = "Welcome to the Log Rewards Page!\n").grid(row = 1, column = 1, sticky = W)

         Label(window, text = "Customer Reward number").grid(row = 2, column = 1, sticky = W)
         Label(window, text = "\n\nOR\n\n").grid(row = 4, column = 1, sticky = W)
         Label(window, text = "Customer Phone number").grid(row = 5, column = 1, sticky = W)
         Label(window, text = "\n\nAND\n\n").grid(row = 7, column = 1, sticky = W)
         Label(window, text = "Customer Purchase total").grid(row = 8, column = 1, sticky = W)
         Label(window, text = "\n\n").grid(row = 10, column = 1, sticky = W)
         
         self.rewardID = StringVar()
         Entry(window, textvariable = self.rewardID, justify = LEFT).grid(row = 3, column = 1)
         self.phoneNumberVar = StringVar()
         Entry(window, textvariable = self.phoneNumberVar, justify = LEFT).grid(row = 6, column = 1)
         self.purchaseTotal = StringVar()
         Entry(window, textvariable = self.purchaseTotal, justify = LEFT).grid(row = 9, column = 1)

         Button(window, text = "Log Rewards", width=12, bg='White', fg='Black', command = self.__init__).grid(row = 11, column = 1, sticky = W)
         window.mainloop() # Create an event loop
    
    def signUpPage(self):
         window = Tk()
         window.title("Sign Up for Rewards") # Set title of the window
         window.configure(background='white')
         
         
         #put the image in a label to display it in the window


         # First, create labels in the window for each input and output value. Note they are put into a grid with rows and columns
         Label(window, text = "                             Sign Up for Rewards").grid(row = 2, column = 1, sticky = W)
         Label(window, text = "\n").grid(row = 2, column = 1, sticky = W)
         Label(window, text = "First name (*)").grid(row = 5, column = 1, sticky = W)
         Label(window, text = "Last name (*)").grid(row = 7, column = 1, sticky = W)
         Label(window, text = "Phone Number (*)").grid(row = 9, column = 1, sticky = W)
         Label(window, text = "Email (*)").grid(row = 11, column = 1, sticky = W)
         Label(window, text = "Street Address (*)").grid(row = 13, column = 1, sticky = W)
         Label(window, text = "City (*)").grid(row = 15, column = 1, sticky = W)
         Label(window, text = "State (*)").grid(row = 17, column = 1, sticky = W)
         Label(window, text = "Zip Code (*)").grid(row = 19, column = 1, sticky = W)
         Label(window, text = "Birthday (optional)").grid(row = 21, column = 1, sticky = W)
         Label(window, text = "\n\n\n\nBy clicking Sign Up, you agree to Ampersand's Terms of Use and acknowledge\n you have read the Privacy Policy. You also consent to receive calls or SMS \nmessages, including by automated dialer, from Ampersand and its affiliates to the \nnumber you provide for informational and/or marketing purposes. Consent to \nreceive marketing messages is not a condition to use Ampersand’s services. You \nunderstand that you may opt out by texting “STOP” to 89203.").grid(row = 25, column = 1, sticky = W)

         #drop down boxes
         tkvar = StringVar(window)

         choices = {'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'}
         tkvar.set('Select')

         popupMenu = OptionMenu(window,tkvar, *choices)
         popupMenu.grid(row=18, column = 1, sticky = W)

         #Create data input boxes
         self.firstNameVar = StringVar()
         Entry(window, textvariable = self.firstNameVar, justify = LEFT).grid(row = 6, column = 1)
         self.lastNameVar = StringVar()
         Entry(window, textvariable = self.lastNameVar, justify = LEFT).grid(row = 8, column = 1)
         self.phoneNumberVar = StringVar()
         Entry(window, textvariable = self.phoneNumberVar, justify = LEFT).grid(row = 10, column = 1)
         self.emailVar = StringVar()
         Entry(window, textvariable = self.emailVar, justify = LEFT).grid(row = 12, column = 1)
         self.streetAddressVar = StringVar()
         Entry(window, textvariable = self.streetAddressVar, justify = LEFT).grid(row = 14, column = 1)
         self.cityVar = StringVar()
         Entry(window, textvariable = self.cityVar, justify = LEFT).grid(row = 16, column = 1)
         self.zipCodeVar = StringVar()
         Entry(window, textvariable = self.zipCodeVar, justify = LEFT).grid(row = 20, column = 1)
         self.birthdayVar = StringVar()
         Entry(window, textvariable = self.birthdayVar, justify = LEFT).grid(row = 22, column = 1)

         #Create a Sign Up button to proceed to next page
         Button(window, text = "SIGN UP", width=12, bg='White', fg='Black', command = self.confirmationPage).place(x=155, y=420)


         window.mainloop() # Create an event loop

    
    def confirmationPage(self):
         window = Tk() # Create a window instance
         window.title("Congratulations, You're earning points!") # Set title of the window


         #put the image in a label to display it in the window

         Label(window, text = "                          Congratulations, You're earning points!\n\n").grid(row = 2, column = 2, sticky = W)
         Label(window, text = "                                        Your Rewards Number").grid(row = 3, column = 2, sticky = W)
         Label(window, text = self.rewardID).grid(row = 4, column = 2, sticky = W)

         Label(window, text = "        \n\nThank you and make sure to visit on you birthday for your free treat!").grid(row = 5, column = 2, sticky = W)
        #Create a Sign Up button to proceed to next page
         Button(window, text = "Home", width=21, bg='white', fg='black', command = self.__init__).grid(row = 7, column = 2, sticky = W)


         window.mainloop() # Create an event loop
        

RewardSystem()  # Create GUI 