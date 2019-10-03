#Nana Osei Asiedu Yirenkyi
#Summer 2018
#This is a python project that help speed up the process of creating receipts for your customers.

#In this project, we will be storing the names and prices of a furniture store's catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.


lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00



stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylish_settee_price = 180.50



luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15



sales_tax = .088



customer_one_total = 0

customer_one_itemization = ''

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += '\n' + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax



print('Customer One Items:')

print('\n', customer_one_itemization)

print('\n' + 'Customer One Total:')

print(customer_one_total)



customer_two_total = 0

customer_two_itemization = ''

customer_two_total += stylish_settee_price

customer_two_itemization += '\n' + stylish_settee_description

customer_two_total += luxurious_lamp_price

customer_two_itemization += '\n' + luxurious_lamp_description

customer_two_tax = customer_two_total * sales_tax

customer_two_total += customer_two_tax



print('\n\nCustomer 2 Items:')

print(customer_two_itemization)

print('\nCustomer Two Total:')

print(customer_two_total)








