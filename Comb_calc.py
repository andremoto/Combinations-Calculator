import math


""""
The Combinations Calculator will find the number of possible combinations 
that can be obtained by taking a sample of items from a larger set. 
Basically, it shows how many different possible subsets can be made from the larger set.
For this calculator, the order of the items chosen in the subset does not matter.

"""
def combination_calc(x,y): # x = number of number choices, y = selecetd sample size

    # C(x, y) = x! / (y! * (x - y)!)
    formula = int(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

    print("The odds are 1 in ", end="")
    print ('{:,}'.format(formula))

if __name__ == "__main__":
    combination_calc(45,5)
