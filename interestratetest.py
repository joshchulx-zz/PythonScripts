money_invested = input("Enter money to be invested")
interest_rate = input("What is the interest rate")
interest_rate = float(interest_rate) * .01
money_invested = float(money_invested)


for i in range(10):
    money_invested = money_invested + (money_invested * interest_rate)
    print(money_invested)
    print("investment after 1 more year : {:.2f}".format(money_invested))



5