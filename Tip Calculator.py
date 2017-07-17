__author__ = 'BenDiegel'

def tipcalc():
    mealCost = float(raw_input("What was the cost of your meal?\n"))
    tipPercent = float(raw_input("Please enter the tip percentage in decimal form.\n"))

    tipAmount = mealCost * tipPercent
    mealAmount = mealCost + tipAmount
    raw_input("Press enter\n")

    print "Tip amount ="
    print tipAmount
    print "Total meal amount ="
    print mealAmount

    tipcalc()
tipcalc()