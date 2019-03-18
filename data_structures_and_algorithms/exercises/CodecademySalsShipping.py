def cost_of_ground_shipping(weight):
    if weight<= 2.0:
      return weight * 1.5 + 20
    elif weight> 2.0 and weight<=6.0:
      return weight * 3.0+ 20
    elif weight> 6.0 and weight<=9.0:
      return weight * 4.0+ 20
    else:
      return weight * 4.75+ 20

print(cost_of_ground_shipping(8.4))

cost_premium_ground_shipping=125

def cost_of_drone_shipping(weight):
    if weight<= 2.0:
      return weight * 4.5
    elif weight> 2.0 and weight<=6.0:
      return weight * 9.0
    elif weight> 6.0 and weight<=9.0:
      return weight * 12.0
    else:
      return weight * 14.25
    
print(cost_of_drone_shipping(1.5))

def shipping_method(weight):
  cost_ground_shipping = cost_of_ground_shipping(weight)
  cost_drone_shipping = cost_of_drone_shipping(weight)
  if cost_ground_shipping<cost_drone_shipping and cost_ground_shipping<cost_premium_ground_shipping:
    print("Ground shipping is cheapest. It would cost you " + str(cost_ground_shipping))
  elif cost_ground_shipping>cost_drone_shipping and cost_drone_shipping<cost_premium_ground_shipping:
    print("Drone shipping is cheapest. It would cost you " + str(cost_drone_shipping))
  else:
    print("Premium ground shipping is cheapest. It would cost you " + str(cost_premium_ground_shipping))
    
shipping_method(15)    
shipping_method(20)
shipping_method(30)  
shipping_method(35)  
shipping_method(60)  
  