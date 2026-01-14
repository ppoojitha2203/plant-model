import random
import matplotlib.pyplot as plt

# -------------------------------
# Fake Sensor Data Generator
# -------------------------------
def get_fake_sensor_data():
    """
    Generates simulated sensor values
    Light: 0–100 %
    Soil moisture: 0–1
    """
    light = random.uniform(20, 80)        # %
    moisture = random.uniform(0.3, 0.8)   # normalized
    return light, moisture


# -------------------------------
# Growth Logic
# -------------------------------
def calculate_growth_rate(light, moisture):
    growth_rate = 0.0

    # Light condition
    if 40 <= light <= 70:
        growth_rate += 1.0
    elif light < 30:
        growth_rate -= 0.5
    else:
        growth_rate -= 0.3

    # Moisture condition
    if moisture < 0.35:
        return 0.0       # growth stops
    elif 0.45 <= moisture <= 0.65:
        growth_rate += 1.0
    elif moisture > 0.8:
        growth_rate -= 0.4

    return max(growth_rate, 0)


# -------------------------------
# Growth Simulation
# -------------------------------
days = 30
plant_size = 1.0
max_size = 100.0

sizes = []

for day in range(days):
    light, moisture = get_fake_sensor_data()
    growth = calculate_growth_rate(light, moisture)

    # Saturation effect
    plant_size += growth * (1 - plant_size / max_size)
    sizes.append(plant_size)

    print(
        f"Day {day+1}: "
        f"Light={light:.1f}% | "
        f"Moisture={moisture:.2f} | "
        f"Plant Size={plant_size:.2f}"
    )

# -------------------------------
# Plot Result
# -------------------------------
plt.plot(range(1, days + 1), sizes)
plt.xlabel("Days")
plt.ylabel("Plant Size")
plt.title("Pea Plant Growth Simulation")
plt.grid(True)
plt.show()
