# Function getInx() : No Argument
# Purpose: Ask user for the choice and error handle
contacts = {}

def getInx():
    # choice
    order = ["Look up an entry ", "Set an entry", "Delete an entry",  "List all entries", "Quit"]
    
    # print out choice and prompt input
    print ("Electronic Phone Book\n=====================")
    for i in range(len(order)):
        print ("{num}. {oda}".format(num=i+1, oda=order[i]))
    
    ans = 'err'
    while ans == 'err':
    # Error Handling Start---
    # Prompt user for input
        try:                    
            ans = int(input("What do you want to do? (1-5)"))
        # String Error
        except ValueError: 
            print ("Invalid Input. ")
    
        # number out of range error
        if ans not in range(0, len(order)+1): 
            print("Type in number between 1 and 5")
            ans = "err"
        elif ans == 5:
            print ("Bye. Come Back soon.")
            return False
        # No records stored errror
        elif ans != 2 and len(contacts) <= 0:
            print ("No record stored in your contacts. Please select 2.")
            ans = "err"    
        # anycase, return ans 
        else:
            return ans
# process depending on answer
def phonebook():
    # ==== main 

    ans = getInx()

    while ans > 0:
        if ans == 4:
            for keys, values in contacts.items():
                print ("Found entry for \"{name}\": {phone}".format(name=keys, phone=values))
        else:
            name = input("Name?: ")
            # Check records exists.
            if name in contacts:
                # Check user on what they wants to do
                if ans == 2:
                    try:  
                        yn = input("Record exists. Update phone number? (y/n): ").lower()
                    # error handling for user input something else
                    except:
                        print ("Invalid Entry. Bye")
                        break
                    # updating record
                    if yn == 'y':
                        phone = input("Phone number?(xxx-xxx-xxxx): ")
                        contacts[name] = phone
                        print ("name: {0}, phone: {1} stored.".format(name, contacts[name]))
                    # NOT updating record => break out
                    else:
                        print ("Bye. Come back soon")
                        break
                # delete when record exists
                elif ans == 3:
                    del contacts[name]    
                    print ("Delete entry for \"{name}\"".format(name=name))
                # for 1 : show 1 record
                else: 
                    print ("Found entry for \"{name}\": {phone}".format(name=name, phone=contacts[name]))
            # when name not in contacts
            else: 
                # register new record
                if ans == 2:
                    phone = input("Phone number?(xxx-xxx-xxxx): ")
                    contacts[name] = phone
                    print ("name: {0}, phone: {1} stored.".format(name, contacts[name]))
                # for 
                else: 
                    print ("\"{name}\" is not in your contacts.".format(name=name))

        # Repeat
        if (input("Try again? (y/n): ")).lower() == 'y':
            ans = getInx()
        else:
            print ("Bye. Come back soon!")
            break