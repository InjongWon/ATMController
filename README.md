# ATMController
 A simple ATM controller

This project can be cloned by entering:
git clone https://github.com/The-Shwin/ATMController.git

in to your terminal.

The file was written and tested in Python 3.7.2.
The program will exit if you try to run it in a version older than 3.7.2. 

 ### Code Details
This repo only has a controller.py file.

controller.py has three main sections:
* Bank Class
  * Has the Bank constructor, which generates the bank
  * Card_nums and pins can be added to bank with add_entry method
  * add_account only works for existing card_nums, program will do nothing if it doesn't exist
  * check_pin takes card_num and pin to verify, this ensures Controller doesn't receive pin from Bank
  * update_account is used by Controller to change balances
* Controller Class
  * Constructor takes in a Bank obj and cash_bin
  * swipe methods takes in card_num and pin to check if valid. 
  * A proper user interface would call this method after invoking user input for pin. 
  * Account_select lets user select their account if valid pin was entered
  * Account actions method is the way balance/withdraw/deposit are implemented. 
  * __call__ function is the very basic driver of the Controller. 
    * It is a driver of Controller, that runs through a list of actions and returns messages
    * This is useful for testing
    * A user interface would behave similarly logic-wise (only entering actions after valid pin, etc), but would await user input
    * Another engineer can see from this function how to go about using swipe, account_selection, and account_actions
* Main
  * Main has test cases built-in to it.
  * Running the program from the command-line will run the test cases.
  * If more tests are desired they can be added into main.
  * Different Controllers or Banks can be created by invoking their constructor. 
  * Lists of actions can be created to run on those objects. 
  * Controller has a __call__ function that be invoked with () around the object name.
  * Actions in a list should be in tuple format ("action", amt). Amt can be 0 if it is irrelevant to action. 
  
 ### Running the Program
 This program can be executed by simply running:
 
 python3 controller.py 
 
 in the command line
 
 If someone else wants to extend this to an actual interface they would have to import controller.py and use the classes/functions.
 The main will only run, if the execution is run with controller.py as main file.