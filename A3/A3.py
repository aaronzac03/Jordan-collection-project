#Programming Project
#Student name: Aaron Zacharia Mathew


def start():#First function to startup the collection
    print('--------------------------------------------------------------------------------')
    print('-------------Welcome to the limited edition JORDAN COLLECTION!!!!!!-------------')
    print('--------------------------------------------------------------------------------')

    retrieve() #Continues to the next function called retrieve


def retrieve():#Second function used to retrieve the data from the text file
    f = open("Stock.txt", 'r')#opens up and reads the text file
    line = f.readline()
    items = line.split()
    global shoes_dict #creates a dictionary called shoes_dictionary and makes it a global variable
    global Overall_Stock_Value #creates a global variable called Overall Stock Value
    Overall_Stock_Value = 0
    items_display = list()
    keys = []

    print('\n')
    print('--------------------------------------------------------------------------------')
    print('----------------------------Retrieving Initial Data-----------------------------')
    print('--------------------------------------------------------------------------------')
    print('Loading data from file: Stock.txt')
    print("Columns, in order, are:", items[0], items[1], items[2], items[3], 'and', items[4])
    print('Items loaded: ', end="")

    for line in f: #for loop to allow for the total prices to be added and count towards Overall Stock Value
        items = line.split(",")
        print(items[0] + ",", end=" ")
        Overall_Stock_Value = Overall_Stock_Value + float(items[1])
        items_display.append(line)
        keys.append(items[0])
    shoes_dict = {}
    for items in range(len(keys)):
        shoes_dict[keys[items]] = items_display[items]

    display()#Continues to the next function called display


def display():#Function that displays the starting stock text file
    print('\n')
    print('--------------------------------------------------------------------------------')
    print('----------------------------Displaying Initial Data-----------------------------')
    print('--------------------------------------------------------------------------------')
    print('\n')
    print('Showing all shoes information (by alphabetical order of their name):')
    print('')
    for keys in sorted(shoes_dict.keys()):#Sorts the data from the text file alphabetically
        print(shoes_dict[keys], end="")
    print("\nOverall Stock Value is: ", Overall_Stock_Value)
    print("\n")
    main_menu()#Continues to main menu



def main_menu():#Function that displays the main menu
    print('--------------------------------------------------------------------------------')
    print('--------------------------------Main Menu---------------------------------------')
    print('--------------------------------------------------------------------------------')

    print('Path 1 - Show the information for a shoe')
    print('Path 2 - Show the information for all stock')
    print('Path 3 - Add a shoe')
    print('Path 4 - Update a shoe')
    print('Path 5 - Remove a shoe')
    print('Path 6 - Save data and exit')
    print('Path 7 - Exit without saving')


    response = int(input("Which path would you like to do: \n"))#takes users input to decide which subsection of the collection to visit
    if response == 1:#if the users response is 1 it takes them to the function items_info
        print("Showing information for one shoe")
        shoe_info()
    elif response == 2:#if the users response is 2 it takes them to the function stock_info
        print("Showing information for all stock")
        stock_info()
    elif response == 3:#if the users response is 3 it takes them to the function item_add
        print("Adding an shoe")
        shoe_add()
    elif response == 4:#if the users response is 4 it takes them to the function item_update
        print("Updating an shoe")
        shoe_update()
    elif response == 5:#if the users response is 5 it takes them to the function item_remove
        print("Removing an shoe")
        shoe_remove()
    elif response == 6:#if the users response is 6 it takes them to the function datasave_exit
        print("Saving data and exiting")
        datasave_exit()
    elif response == 7:#if the users response is 7 it takes them to the function nosave_exit
        print("Exiting without saving")
        nosave_exit()
    else:
        print("Please choose a path 1,2,3,4,5,6 or 7!!!!")
        main_menu()#if the user inputs something other than an integer from 1-7 it should print an error message and bring them back to the main menu function


def shoe_info():#Function for users to get information of one item
    print("Here are the current available shoes")
    for key in sorted(shoes_dict.keys()):
        print(key)
    try:
        shoe = input("\nWhat shoe would you like the information for? ")

        if shoe in shoes_dict.keys():
            print("displaying information for", shoe)
            print(shoes_dict[shoe], end="")
            main_menu()
        else:
            print( "The", shoe, " can not be found!")
            print("You will now be returned to the main menu")
            main_menu()#if the user input is not in the list it will return back to main menu function
    except:
        print("Your input is not a real shoe try again")
        shoe_info()#triggers the function again if the user did not enter a shoe name



def stock_info():#Function used to display all the stock information
    print('Showing all shoes information:')
    print('')
    for keys in sorted(shoes_dict.keys()):#sorts the shoes alphabetically
        print(shoes_dict[keys])
    main_menu()#returns the user back to the main menu




def shoe_add():#function used to allow for users to add shoes
    print("Enter your shoe you would like to add")
    shoe_addition = input("Enter your shoe name")
    if shoe_addition in shoes_dict:#if statement that checks wether the users input is already in the collection
        print('Sorry', shoe_addition, 'already exists in the collection')
        print('Please choose another Shoe')
        shoe_add()#redirects the user back to the shoe_add function
    else:#else statement that allows the user to input the details for the new shoes
        print('--------Shoe is getting ready to be added--------')
        print('Please enter more details about your shoe')
        shoe_name = shoe_addition
        shoe_price = input('What is the price of your shoe?')
        shoe_release_date = input('What is the release date of your shoe?')
        shoe_colourways = input("How many different colourways does your shoe have?")
        shoe_quality = input('What is the quality of your shoe?')
        shoes_dict[shoe_name] = shoe_name + ", " + shoe_price + ", " + shoe_release_date + ", " + shoe_colourways + ", " + shoe_quality + '\n'
    print(shoes_dict)#prints out the new dictionary containing the new shoes
    main_menu()#returns the user back to the main menu




def shoe_update():#function used to allow for users to update shoes
    print("Update")
    print("Here are the current available shoes")
    for key in sorted(shoes_dict.keys()):#sorts te shoes alphabetically
        print(key)
    shoe_select = input("Please enter the shoe you would like to update")#defines input as shoe select
    if shoe_select in shoes_dict.keys():
        print("displaying information for", shoe_select)
        print(shoes_dict[shoe_select], end="")
        del shoes_dict[shoe_select]#if shoe_select is located in the dictionary then all the information for it will be deleted and then the user can input the new information
        upd_name = input("What is the new shoe name?")
        upd_price = input("What is the new shoe price?")
        upd_release_date = input("What is the new shoe release date?")
        upd_colourways = input("What is the new number of colourways?")
        upd_quality = input("What is the new quality of the shoes")
        shoes_dict[upd_name] = upd_name + ", " + upd_price + ", " + upd_release_date + ", " + upd_colourways + ", " + upd_quality + '\n'
        print(shoes_dict)#prints out the updated dictionary containing the updated shoes
        main_menu()#returns the user back to the main menu
    else:#if the shoe_select was not found in the dictionary the user will be shown an error message
        print("The", shoe_select, " can not be found!")
        print("You will now be returned to the main menu")
        main_menu()#returns the user to the main menu





def shoe_remove():#function used to allow for users to remove shoes
    print("Loading up shoe removal")
    print("Here are the current available shoes")
    for key in sorted(shoes_dict.keys()):#sorts the shoes alphabetically
        print(key)
    removed_shoe = input("Enter which shoe you would like to remove")
    if removed_shoe in shoes_dict:#if the removed_shoe is present in the dictionary it then gets deleted
        del shoes_dict[removed_shoe]
        print("This shoe has been successfully removed")
        main_menu()#returns the user to the main menu
    else:
        print("This shoe is not currently in the collection")
        print("Returning to main menu")
        main_menu()#returns the user to the main menu



def datasave_exit():
    infile = open("Stock.txt", 'r')#reads Stock.txt file
    outfile = open('updated_Stock.txt', 'w') #writes to a new file called updated_Stock.txt

    for keys in sorted(shoes_dict.keys()):#sorts the shoes alphabetically
        outfile.write(shoes_dict[keys])

    print('Showing all shoes information (by alphabetical order of their name):')
    print('')
    for keys in sorted(shoes_dict.keys()):#sorts the shoes alphabetically
        print(shoes_dict[keys])
    print("Exiting process now")

    infile.close()
    outfile.close()
    end()#takes user to the end function



def nosave_exit():#function to allow for users to exit without saving
    decision = input('Are you sure you would like to exit?(Yes or No)')
    if decision == 'Yes':
        print("This program is closing, goodbye!!!!")
        end()#if the decision is yes it takes user to end function
    elif decision == 'No':
        main_menu()#if the decision is no returns user to the main menu
    else:
        print('Please enter Yes or No!')
        nosave_exit()#if the user enters a response other than yes or no, an error message is displayed and the user is returned to the nosave_exit function



def end():#function to end the program
    print("-----------------------------------------------------------------------------------------")
    print("----------Remember to hop back in if you would like to make further adjustments----------")
    print("-----------------------------------------------------------------------------------------")
    print("\n")
    print("-----------------------------------------------------------------------------------------")
    print("-------------Thank you for using THE LIMITED EDITION JORDAN COLLECTION!!!!!--------------")
    print("-----------------------------------------------------------------------------------------")


start()