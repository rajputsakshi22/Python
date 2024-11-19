import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Add the Sun at the center
sun = plt.Circle((0, 0), radius=0.5, color='yellow', label="Sun")
ax.add_artist(sun)

# Define planet properties (distance from the sun, radius, color, name)
planets = [
    {"distance": 1, "radius": 0.1, "color": 'gray', "name": "Mercury"},
    {"distance": 1.5, "radius": 0.15, "color": 'orange', "name": "Venus"},
    {"distance": 2, "radius": 0.2, "color": 'blue', "name": "Earth"},
    {"distance": 3, "radius": 0.18, "color": 'red', "name": "Mars"},
    {"distance": 5, "radius": 0.3, "color": 'brown', "name": "Jupiter"},
    {"distance": 7, "radius": 0.25, "color": 'yellowgreen', "name": "Saturn"},
]

# Add planets and their orbits
for planet in planets:
    # Draw orbit as a circle
    orbit = plt.Circle((0, 0), planet["distance"], color='white', fill=False, linestyle='dotted', linewidth=1.2)
    ax.add_artist(orbit)
    
    # Calculate planet's position
    angle = np.random.uniform(0, 2 * np.pi)  # Random position in the orbit
    x = planet["distance"] * np.cos(angle)
    y = planet["distance"] * np.sin(angle)
    
    # Draw planet
    planet_body = plt.Circle((x, y), planet["radius"], color=planet["color"], label=planet["name"])
    ax.add_artist(planet_body)
    
    # Add planet label
    ax.text(x + 0.3, y + 0.3, planet["name"], fontsize=8, color='white')

# Set plot limits to show the entire solar system
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')

# Add background color to represent space
ax.set_facecolor("black")

# Remove axes for a cleaner look
plt.axis('off')

# Add legend for planets
handles = [patches.Patch(color=p["color"], label=p["name"]) for p in planets]
plt.legend(handles=handles, loc='lower right', frameon=False, fontsize=8)

# Display the plot
plt.title("Solar System Simulation", color='white')
plt.show()
