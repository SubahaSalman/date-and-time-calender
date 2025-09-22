def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "los Angeles" == city:
        return 475
    
def rental_car_costs(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
    
def trip_cost(city, days, spending_money):
    return rental_car_costs(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of the rental car:", rental_car_costs(5))
print("Cost of plane ride:", plane_ride_cost("los Angeles"))
print("Cost of hotel room", hotel_cost(7))
print("Total cost of the trip:", trip_cost("los Angeles", 7, 500))
print(trip_cost("tampa",6,500))