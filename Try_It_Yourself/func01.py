# "Main" Program
def place_to_go(place, *destinations):
    print("\nWhere to go?: " + str(place))

    for destination in destinations:
        print("There: " + destination)
