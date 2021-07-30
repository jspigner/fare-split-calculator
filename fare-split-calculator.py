# Create a calculator for ride-sharing
# Common for use in ride sharing apps such as Uber and Lyft

# Define
def split_fare(fare, passengers, feature_cost):

    share = fare/passengers
    print(f"Splitting the ${fare_cost} fare between {passengers} passengers...")

    shared_cost = share + feature_cost
    print(f"Adding a ${feature_cost} feature cost...")
    return shared_cost

# Store values in variables
fare_cost = 100
passengers = 4
feature_cost = 0.5

shared_cost = split_fare(fare_cost, passengers, feature_cost)

print(f"Each pays: ${shared_cost}")