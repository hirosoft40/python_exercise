##==== Object Exercise ====

## 1. Basic
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetCount = 0
        self.greetedFriends= []
    
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    # def __repr__(self):
    #     return ('{}'.format(self.friends))

    def greet(self, other_person):
        self.greetCount += 1
        if other_person in self.greetedFriends:
            pass
        else:
            self.greetedFriends.append(other_person)

        print (f'Hello {other_person.name}, I am {self.name}!')

    def print_contact_info(self):
        print (f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friend(self):
        print (f"{self.name} has {len(self.friends)} friends.")

    def num_greetings(self):
        print (f"Greet Count is:{self.greetCount}")

    def num_unique_people_greeted(self):
        print (f'{self.name} has greeted {len(self.greetedFriends)} friends.')

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948') # No.1
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456') # No.2
tommy = Person('Tommy', 'tommy@yahoo.com', '123-456-7890')

## -- greetig 
sonny.greet(jordan) # No.3
jordan.greet(sonny) # No.4 

## -- printing contacts
print (f'{sonny.name}\'s email is: {sonny.email} and his phone is: {sonny.phone}')
print (f'{jordan.name}\'s email is: {jordan.email} and his phone is: {jordan.phone}')
sonny.print_contact_info() # Add a method 2

## -- add friends
sonny.friends.append(jordan) 
jordan.friends.append(sonny)
# 
## -- add freinds by method   
jordan.add_friend(sonny)
print ('Jordan has {} friends'.format(len(jordan.friends))) # Add a add_friend_method
jordan.num_friend()          # Add a num_friend method
jordan.add_friend(tommy) 

## --- count No of greetings
jordan.num_greetings()      # Count No of greetings

## --- show contact info of the person
print (jordan.__str__())  # __str__

## --- No of unique person greeted
jordan.greet(tommy)
sonny.greet(tommy)
sonny.greet(tommy)
tommy.greet(sonny)
tommy.greet(jordan)
jordan.num_unique_people_greeted()
sonny.num_unique_people_greeted()
tommy.num_unique_people_greeted()
#print (len(jordan.greetedFriends))

sonny.greetedFriends[0].name

## 2. Make your own class
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):  # Add a method
        print (self.year, self.make, self.model)

car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()  # No.2
