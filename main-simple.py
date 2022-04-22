user_list = []
owes_list = []
owed_by = []
money_owed = []


while True:
    command = input("Awaiting Input... ")

    if command == "post":
        print("----------------")
        name = input("Name of lender?: ")
        owes = input("Who are you borrowing money from?: ")
        amount_money = input("How much are you owing this person?: ")

        user_list.append(name)
        owes_list.append(owes)
        money_owed.append(amount_money)

        print("----------------")

    if command == "get":
        inp = input("Do you want all_users or one specific user (Name)?: ")
        if inp == "all_users":

            print("----------------")

            print(user_list)
            print(owes_list)
            print(money_owed)

            print("----------------")
        
        else:
            if inp in user_list:

                print("----------------")

                print(user_list[user_list.index(inp)])
                print(owes_list[user_list.index(inp)])
                print(money_owed[user_list.index(inp)])

                print("----------------")

            else:
                print("The person you mentioned is not in the user_list, please add something with command 'post'")

                print("----------------")

    

    if command == "x":
        break


# The Problems
# What if I borrowed money from multiple persons -> what is being displayed when I get with specific name
# user should be unique
# Answer ------> Classes + Instances





    

    


