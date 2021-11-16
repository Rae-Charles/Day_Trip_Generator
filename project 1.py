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

random_element = random.choice(destinations + restaurants + modes_of_transportation + entertainments)
print(random_element)



# generate random element from all lists, assignment from JJ
repeat_random_destination = input("Would you like another random destination, restaurant, mode of transportation, and entertainment? \n") 
while repeat_random_destination != "yes" and != "no":
    
        
        print("I think this is going to be a great daytrip, glad you're satisfied")

    else: 
        repeat_random_destination == "yes":
        print(random_destination, random_restaurant, random_mode_of_transportation, random_entertainment)
   




# ask user if they want a random element from individual lists, seperated
generate_single_element = input('Would you like a random element from all lists mentioned?')
while generate_random_element is True:

    if generate_single_element == "yes":
        print(random_element)
    else:
        generate_random_element = False
        print("Glad that you are satisfied with your daytrip so far!")    

print("Moving on to the next question!")























# satisfaction_with_trip = input('Are you satisfied with your daytrip details?')
# while satisfaction_with_trip is True:    
#     if satisfaction_with_trip == "yes":
#         print("I'm glad that you are satisfied with your daytrip!")
#     else:
#         satisfaction = False
#         return "repeat_random_scenario"


# print("Let's continue!")


# daytrip_satisfaction = input('Would you like a printout of your daytrip?')
# while daytrip_satisfaction is True:
#     if daytrip_satisfaction == "yes":
#     print("I'm glad that you are satisfied with your daytrip!! Here is a printout of your details: {}".format(trip details here))
    
#     else:
#         daytrip_satisfaction == False
#         return (repeat_random_scenario)




# def add_two_numbers(num_one, num_two):
#     result = num_one + num_two
#     return result
    
# sum = add_two_numbers(1,2)

# def display_sum(sum):
#     print(sum)

# display_sum(sum)



print ("Thank you, i hope you have a great time on your daytrip!")







# 1. What was the biggest challenge you faced on the project? How did you overcome it?

# Figuring out hope to end the while loops and I'm still having issues with the return function. I overcame
# some of this by using my resources from class, w3schools, google, and then asking instructors for assistance.

# 2. What was your favorite part of the project?
# My favorite part of the project was getting better at loops. I'm sure this is a feature among many companies that
# will come in handy with a developer career. I have and will continue to improve upon this, I'm sure, with
# the multiple of projects and practice that we will be getting during this program. 