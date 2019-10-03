#Nana Osei Asiedu Yirenkyi
#Summer 2018

#You are the data analyst at Carly's Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

#Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.First, let's sum up all the prices of haircuts. Create a variable total_price.

total_price = 0

#Iterate through the prices list and add each price to the variable total_price.

for price in prices:
  total_price += price

#After your loop, create a variable called average_price 
average_price = total_price / len(prices)

#Print the value of average_price
print("Average Price: "+str(average_price))

#That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

new_prices = [price-5 for price in prices]

print("New Prices: ", new_prices)

#Carly really wants to make sure that Carly's Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

total_revenue = 0


#Use a for loop to create a variable i that goes from 0 to len(hairstyles)-1.

for i in range(0,len(hairstyles)-1):
  total_revenue += (prices[i] * last_week[i])
  
print("Total Revenue: ", total_revenue)

#Find the average daily revenue
average_daily_revenue = (total_revenue/7)

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

cuts_under_30 = [hairstyles[i] for i in range(0,len(hairstyles)-1) if new_prices[i] < 30]

print("Cuts Under 30",cuts_under_30)
  

