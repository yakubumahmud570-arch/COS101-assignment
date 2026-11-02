
# COS 101 Assignment
# Five Physics Formulas

# 1. Speed = Distance / Time
def speed(distance, time):
    return distance / time


# 2. Force = Mass × Acceleration
def force(mass, acceleration):
    return mass * acceleration


# 3. Density = Mass / Volume
def density(mass, volume):
    return mass / volume


# 4. Work Done = Force × Distance
def work_done(force, distance):
    return force * distance


# 5. Kinetic Energy = 1/2 × Mass × Velocity²
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


# Display results
print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Density:", density(20, 4), "kg/m³")
print("Work Done:", work_done(50, 10), "J")
print("Kinetic Energy:", kinetic_energy(2, 10), "J")
