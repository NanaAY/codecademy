#Nana Osei Asiedu Yirenkyi

#Summer 2018

#You work at Len's Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

# A list To keep track of the kinds of pizzas you sell
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
# A list To keep track of how much each kind of pizza slice costs
prices = [2,6,1,3,2,7,2]

#Find the length of the toppings list 
num_pizzas = len(toppings)

print("We sell "+str(num_pizzas)+" different kinds of pizza!\n")

#Combines the two lists into a list called pizzas that pairs topping with price
pizzas = list(zip(prices, toppings))

print(pizzas)

#Sorts pizzas so that the pizzas with the lowest prices are at the start of the list.
pizzas.sort()

#Store the first element of pizzas in a variable called cheapest_pizza.
cheapest_pizza = pizzas[0]

#A man in a business suit walks in and shouts "I will have your MOST EXPENSIVE pizza!" Get the last item of the pizzas list and store it in a variable called priciest_pizza.
priciest_pizza = pizzas[-1]

#Three mice walk into the store. They don't have much money (they're mice), but they do each want different pizzas. Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizzas[:3]

#Print the three_cheapest list.
print('\nThe three cheapest pizzas are:', three_cheapest)

#Your boss wants you to do some research on $2 slices.Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
num_two_dollar_slices = prices.count(2)
print('\nThe number of $2 dollar slices are:', num_two_dollar_slices)




