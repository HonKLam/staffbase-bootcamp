user_list = []
owes_list = []
owed_by = []
money_owed = []

# Questions
# How do I save as many instances as I like???


class user:
    def __init__(self, name, owes, owes_money):
        self.name = name
        self.owes = owes
        self.owes_money = owes_money

    def show_user(self):
        print(self.name)
        print(self.owes)
        print(self.owes_money)


while True:
    command = input("Awaiting Input... ")

    if command == "post":
        name = input("Name of lender?: ")
        owes = input("Who are you borrowing money from?: ")
        amount_money = input("How much are you owing this person?: ")

        
        # Instead of new_user, there should be name of the person as an class instance, but how do I do it?
        new_user = user(name, owes, amount_money)
        user_list.append(new_user.name)
        owes_list.append(new_user.owes)
        money_owed.append(new_user.owes_money)

    if command == "get":
        inp = input("Do you want all_users or one specific user (Name)?: ")
        if inp == "all_users":

            #Instead of printing the lists, I could somehow call all instances and their attributes, but how do I do it?
            print(user_list)
            print(owes_list)
            print(money_owed)
        
        else:
            if inp in user_list:
                inp.show_user()

            else:
                print("The person you mentioned is not in the user_list, please add something with command 'post'")

    

    if command == "x":
        break




    

    


