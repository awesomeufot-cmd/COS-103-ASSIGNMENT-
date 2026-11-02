
print("===== PHYSICS FORMULA CALCULATOR 2 =====")
print("1. Acceleration")
print("2. Momentum")
print("3. Kinetic Energy")
print("4. Potential Energy")
print("5. Power")

choice = int(input("Choose a formula (1-5): "))

if choice == 1:
    velocity = float(input("Enter final velocity (m/s): "))
    initial = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (s): "))
    acceleration = (velocity - initial) / time
    print("Acceleration =", acceleration, "m/s²")

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    momentum = mass * velocity
    print("Momentum =", momentum, "kg m/s")

elif choice == 3:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    energy = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", energy, "J")

elif choice == 4:
    mass = float(input("Enter mass (kg): "))
    gravity = float(input("Enter gravity (m/s²): "))
    height = float(input("Enter height (m): "))
    energy = mass * gravity * height
    print("Potential Energy =", energy, "J")

elif choice == 5:
    work = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    power = work / time
    print("Power =", power, "W")

else:
    print("Invalid choice! Please choose 1-5.")
