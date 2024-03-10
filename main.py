def love(name):
    print("I love " + name)



def person_1(name):
    print(f"{name}: hello how can I help you")

def person_2(food, drinks, dessert, name):
    name = input("What is your name: ")
    food = input("What do you want to eat: ")
    drinks = input("What do you want to drink: ")
    dessert = input("What dessert do you want: ")
    print(f"{name}: I would like {food} I want to drink {drinks} I want {dessert} as a dessert.")

def person_1_2(name):
    print(f"{name}: Thank you for comming........")

person_1("Chef")
person_2("food", "drinks", "dessert","name")