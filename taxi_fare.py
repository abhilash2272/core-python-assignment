BASE_FARE = 50
PER_KM = 10


def calculate_fare(distance):
    return BASE_FARE + (PER_KM * distance)


# Example Input
trips = [5, 10, 3]

total_fare = 0

for i, d in enumerate(trips, 1):
    fare = calculate_fare(d)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print("Total Fare:", f"${total_fare}")