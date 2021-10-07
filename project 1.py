import random

destinations = ['Yellowstone', 'Honolulu', 'Tokyo', 'Rome']
restaurants = ['Chipotle', 'Olive Garden', 'Milano']
modes_of_transportation = ['Plane', 'Train', 'Automobile']
entertainments = ['Netflix', 'Hulu', 'Hbo Max']


random_destination = random.choice(destinations)
print(random_destination)

random_restaurant = random.choice(restaurants)
print(random_restaurant)

random_mode_of_transportation = random.choice(modes_of_transportation)
print(random_mode_of_transportation)

random_entertainment = random.choice(entertainments)
print(random_entertainment)


repeat_random_destination = input('Would you like another random destination, restaurant, mode of transportation, and entertainment?') 
answer = yes
regenerate_random_scenario = True

while regenerate_random_scenario is True:
    if answer = yes:
    print(random_destination, random_restaurant, random_mode_of_transportation, random_entertainment)
    else:
        return



# confirm_daytrip = input('Are you satisfied with your daytrip details?')
# answer = yes



# print_out_daytrip = input('Would you like a printout of your daytrip?')
# answer = yes
# print_out_daytrip = True


# while print_out_daytrip is True:
#     print()

# def add_two_numbers(num_one, num_two):
#     result = num_one + num_two
#     return result
    

# sum = add_two_numbers(1,2)

# def display_sum(sum):
#     print(sum)

# display_sum(sum)