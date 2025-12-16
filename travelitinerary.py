destinations = []

print("Please enter your 5 travel destinations:")
for i in range(5):
    place = input(f"Destination {i + 1}: ")
    destinations.append(place)

print("\nOriginal travel itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")

print("\nLet's update your second and fifth destination.")
destinations[1] = input("Enter a new destination for position 2: ")
destinations[4] = input("Enter a new destination for position 5: ")

print("\nUpdated travel itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")
