#okay so this time we are simulating a coffee machine with OOP
# we are gonna have a class of coffee machine
# an abstract class of coffee types with the required ingredients, the sub class being the differnt types of cofee
# a money system so that keep track of the said profit
#...and a maybe coffee shop
#so for the machine, you turn it on, you choose a coffee type, you pay coins,it checks resources, then you get your coffee
#i'm guessing the sub classes of coffee type will have the set ingredients and their cost, so that we can rack up profit later on
from abc import abstractmethod
import time
class CoffeeDrink:
    cp=0
    @abstractmethod
    def info(self):
        ...
    def name(self):
        ...
    def cost(self):
        return 0
class Espresso(CoffeeDrink):
    cp=1.5
    def cost(self):
        return 1.8
    def info(self):
        return {"water":10,"milk":0,"sugar":5,"coffee":30}#ingredients in ml
    def name(self):
        return "Espresso"
class Latte(CoffeeDrink):
    cp=1.8
    def cost(self):
        return 2.5
    def info(self):
        return {"water":30,"milk":40,"sugar":20,"coffee":30}#cost in $
    def name(self):
        return "Latte"
class Americano(CoffeeDrink):
    cp=1.0
    def cost(self):
        return 1.7
    def info(self):
        return {"water":30,"milk":0,"sugar":0,"coffee":40}
    def name(self):
        return "Americano"
class Cappuccino(CoffeeDrink):
    cp=2.0
    def cost(self):
        return 3.0
    def info(self):
        return {"water":20,"milk":30,"sugar":10,"coffee":30}
    def name(self):
        return "Cappuccino"


class CoffeeMachine:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
        self.water=700
        self.milk=500
        self.coffee=500
        self.sugar=300
        self.turned_on:bool=False
        self.profit:float=0
    def turn_on(self):
        if self.turned_on:
            print("The Machine is already on")
        else:
            self.turned_on=True
            print("🎶Lala lala🎶..The machine is on")
    def turn_off(self):
        if self.turned_on:
            self.turned_on=False
        else:
            print("This machine is not ON!!")
    def check_resources(self,coffee:CoffeeDrink):
         ingredients=coffee.info()
         if self.water>ingredients["water"] and self.milk>ingredients["milk"
            ]and self.coffee > ingredients["coffee"] and self.sugar>ingredients["sugar"]:
             return True
         else:
             return False

    def make_drinks(self,coffee: CoffeeDrink):
        print("Please wait for a few minutes while your coffee gets ready ~~~")
        ingredients=coffee.info()
        self.water -= ingredients["water"]
        self.milk -= ingredients["milk"]
        self.sugar -= ingredients["sugar"]
        self.coffee -= ingredients["coffee"]
        time.sleep(15)
        print(f"One cup of {coffee.name()} ready ☕. Enjoy (≧∇≦)ﾉ")

    def __str__(self):
        return f"Coffee Machine of {self.brand} of size{self.size}"
    def accept_payment(self,coffee:CoffeeDrink):
        profit=coffee.cost()-coffee.cp
        self.profit+=profit

    def help(self):
        print("Initializing emergency control action......managing errors....forcing temporary shutdown...")



def run_machine():
    coffe_machine_1 = CoffeeMachine("Toshiba", 5)
    coffe_machine_1.turn_on()

    coffee_instances = [Latte(), Cappuccino(), Americano(), Espresso()]
    while True:
        print("------Available Coffee Drinks-------")
        for index, drink in enumerate(coffee_instances,start=1):
            print(f"{index}: {drink.name()}: Price:${drink.cost()}")
        print("Enter 0 to turn off the machine....")
        try:
            num_drink=int(input("Enter the number associated with drink of preferred choice: "))
        except ValueError:
            print("We asked for a number silly!!")
            continue
        if num_drink!=0:
            drink=coffee_instances[num_drink-1]
            criterion=coffe_machine_1.check_resources(drink)
            if criterion:
                try:
                    payment=float(input("Please enter payment in dollars:"))

                    if payment>drink.cost():# okay so the magic that went on here was this...we accsess the coffe drink with it' index and get the cost, the number the user chooses is 1 greater than the drink,s index
                        change=payment-drink.cost()
                        coffe_machine_1.accept_payment(drink)
                        print(f"Payment made.Here is your change of ${change}.")
                    elif payment==drink.cost():
                        coffe_machine_1.accept_payment(drink)
                        print("Payment successful")
                    else:
                        print("Insufficient payment has been made.......\n"
                              "Please recheck the correct price for your order and try again")
                    if payment>=drink.cost():
                        coffe_machine_1.make_drinks(drink)
                except ValueError:
                    print("Wrong payment method!!")
                    continue
            else:
                print(f"Sorry,not enough resources to make {drink} 😞 ")
                continue
        else:
            coffe_machine_1.turn_off()
            break
if __name__=="__main__":
    run_machine()