## My name is Merdan Garlyyev, and I am taking CS 230 class. The due date for this assignment is Oct 10, 2022.
## My program is a story scenario. It's a story of a guy, James, who wants invite the girl, Rachel, that he likes very much somewhere special for their first date, but doesn't know where yet.
## My program asks James several questions about the details of his date and suggests him where to go depending on the day of the date.

## Here I am these variables value of 0 because I will need it at the very end to transform from 6 outputs values into 3
flowers = 0
toy = 0
popcorn = 0
gift = 0

## Here is my first option of the days when to go to a date (3 way selection statement)
number = str(input("What day should I invite Rachel to a date? "))
if number == "Monday" or number == "Tuesday" or number == "Wednesday":
    print("That's a good day to go to Baja or Yamato. Please make your option")

    ## Here I ask for his decision of a restaraunt (2 way selection statement)
    option1 = input("What's your option? ")
    if option1 == "Baja":
        print("Your total cost at this restaurant will be more than $100. Also after having food you decided to buy her flowers to make her happy")

        ## Another input asking to buy a toy (1 way selection statement). The if statement and print statement of this i wrote at the very end to decrease the number of outputs to 3 as we need it according to requirements
        flowers = int(input("How many flowers did you buy? "))


    if option1 == "Yamato":
        print("Your total at this place is less than $70. After the date you decided to buy her a toy to make her day ")
        ## Another input asking to buy a toy (1 way selection statement). The if statement and print statement of this i wrote at the very end to decrease the number of outputs to 3 as we need it according to requirements
        toy = int(input("How many toys did you buy her? "))


##Here is my second option of the days when to go to a date
if number == "Thursday" or number == "Friday":
    print("That's a nice day to go to Museum or Theater. Please make your option")
    ## this is 2 way selecion statements that asks to make decision to go to Museum or Theater
    option2 = input("What did you decide? ")
    if option2 == "Museum":
        print("Your total expenses for the date is $60. After the date you decided to buy her a toy to make her day ")
        ## Another input asking to buy a toy (1 way selection statement). The if statement and print statement of this i wrote at the very end to decrease the number of outputs to 3 as we need it according to requirements
        toy = int(input("How many toys did you buy her? "))

    if option2 == "Theater":
        print("You are spending $55 for your date. After the date you decided to buy her a popcorn to make her day ")
        ## Input value that asks a question from the user (1 way selection statement). The if statement and print statement of this i wrote at the very end to decrease the number of outputs to 3 as we need it according to requirements
        popcorn = int(input("How many bags of popcorn did you buy her? "))

## Here is my final option of the days when to go to a date
if number == "Saturday" or number == "Sunday":
    print("That's a perfect day to go to a Bar or a Party. Please make your option")
    ## 2 way selection statements asking where for a place to go to a date
    option3 = input("Where do you want to go? ")
    if option3 == "Bar":
        print("You are going to spend $40. After the date you decided to buy her a popcorn to make her day ")

        ## 1 way selection statement that asks for the number of items that he bought her
        popcorn = int(input("How many bags of popcorn did you buy her? "))

    if option3 == "Party":
        print("Your expenses are $33. After the date you decided to buy her a gift to make her day ")
        ## 1 way selection statement that asks for the number of items that he bought her
        gift = int(input("How many gifts did you buy her? "))

##Here are the if statements that I was talking about before that I need for my last 3 outputs
if flowers>0:
    print(f"You gave her {flowers} flowers! She is very happy and that was a perfect date")
if toy>0 or popcorn>0:
    print(f"She is the happiest girl on the earth and the date was great!")
if gift>0:
    print(f"You bought her {gift} gifts! She is screaming from happiness and this was the best date in her life")










