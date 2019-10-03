#Nana Osei Asiedu Yirenkyi
#Summer 2018 
#This is a python program that will take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers.



#Standard Price for premium Shipping
prem_ground_shipping = 125

#Calculates the cost of ground shipping using weight
def ground_shipping(weight):
  flat_charge = 20
  if weight <= 2:
    cost = flat_charge + (weight * 1.5)
  elif 2 < weight <= 6:
    cost = flat_charge + (weight * 3)
  elif 6 < weight <= 10:
    cost = flat_charge + (weight * 4)
  else:
    cost = flat_charge + (weight * 4.75)
  return cost

#Calculates the cost of drone shipping using weight
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.5
  elif 2 < weight <= 6:
    cost = weight * 9
  elif 6 < weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25
  return cost

#Checking functions
print(ground_shipping(8.4))
print(drone_shipping(1.5))

#Comparing the two functions and the premium price to determine the cheapest method of shipping
def cheapest_shipping(weight):
  if ( ground_shipping(weight) < drone_shipping(weight) ) and ( ground_shipping(weight) < prem_ground_shipping):
    print('Ground Shipping is the cheapest method of shipping a '+str(weight)+ ' pound package.\nTotal cost will be $'+str(ground_shipping(weight) ) )
  elif ( drone_shipping(weight) < ground_shipping(weight) ) and ( drone_shipping(weight) < prem_ground_shipping):
    print('Drone Shipping is the cheapest method of shipping a '+str(weight)+ ' pound package.\nTotal cost will be $'+str(drone_shipping(weight)))
  else:
    print('Premium Shipping is the cheapest method of shipping a '+str(weight)+ ' pound package.\nTotal cost will be $'+str(prem_ground_shipping))
    
    
 
cheapest_shipping(4.8)
cheapest_shipping(41.5)