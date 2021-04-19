from tkinter import * # Import tkinter; do not need to install it
from random import random

class RewardSystem:
     def __init__(self):
          window = Toplevel()
          window.title("Sign Up for Rewards") # Set title of the window
          window.configure(background='white')
         
         
         #put the image in a label to display it in the window
          photo = PhotoImage(file=r'C:\Users\htcam\iCloudDrive\Documents\TCU\BIS Systems Development\APPLICATION\Ampersand.png')
          Label(window, image=photo).grid(row = 1, column = 1, columnspan=2, sticky = W) #put the image in a label to display it in the window

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
          Label(window, text = "\n\n\n").grid(row = 27, column = 1, sticky = W)
          Label(window, text = "By clicking Sign Up, you agree to Ampersand's Terms of Use and acknowledge\n you have read the Privacy Policy. You also consent to receive calls or SMS \nmessages, including by automated dialer, from Ampersand and its affiliates to the \nnumber you provide for informational and/or marketing purposes. Consent to \nreceive marketing messages is not a condition to use Ampersand’s services. You \nunderstand that you may opt out by texting “STOP” to 89203.").grid(row = 30, column = 1, sticky = W)

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
          self.stateVar = StringVar()
          Entry(window, textvariable = self.stateVar, justify = LEFT).grid(row = 18, column = 1)
          self.zipCodeVar = StringVar()
          Entry(window, textvariable = self.zipCodeVar, justify = LEFT).grid(row = 20, column = 1)
          self.birthdayVar = StringVar()
          Entry(window, textvariable = self.birthdayVar, justify = LEFT).grid(row = 22, column = 1)

         #Create a Sign Up button to proceed to next page
          Button(window, text = "SIGN UP", width=12, bg='White', fg='Black', command = self.confirmationPage).place(x=155, y=650)


          window.mainloop() # Create an event loop

    
     def confirmationPage(self):
          window = Tk() # Create a window instance
          window.title("Congratulations, You're earning points!") # Set title of the window
         
          randNum = random()
          self.rewardID = randNum #assigns a random number to reward number
         
          photo = PhotoImage(file=r'C:\Users\htcam\iCloudDrive\Documents\TCU\BIS Systems Development\APPLICATION\Ampersand.png')
          Label(window, image=photo).grid(row = 1, column = 1, columnspan=2, sticky = W) #put the image in a label to display it in the window#put the image in a label to display it in the window

          Label(window, text = "                          Congratulations, You're earning points!").grid(row = 2, column = 3, sticky = W)
          Label(window, text = "                                        Your Rewards Number").grid(row = 3, column = 3, sticky = W)
          self.rewardVar = StringVar()
          Entry(window, textvariable = self.rewardVar, justify = LEFT).grid(row = 4, column = 3)

          Label(window, text = "        Thank you and make sure to visit on you birthday for your free treat!").grid(row = 5, column = 3, sticky = W)
        #Create a Sign Up button to proceed to next page
          Button(window, text = "Back to Sign Up Page", width=21, bg='white', fg='black', command = self.__init__).place(x=120, y=110)
         
        
          window.mainloop() # Create an event loop
        

RewardSystem()  # Create GUI 