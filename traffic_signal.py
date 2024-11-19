import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

def draw_traffic_light(state):
    """
    Draws the traffic light based on the current state ('red', 'yellow', 'green').
    """
    fig, ax = plt.subplots(figsize=(4, 10))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_facecolor('lightgrey')
    
    # Draw the traffic light frame
    frame = patches.Rectangle((-1.2, 0), 2.4, 7, edgecolor='black', facecolor='black', linewidth=2)
    ax.add_patch(frame)
    
    # Draw the light circles
    colors = {'red': 'gray', 'yellow': 'gray', 'green': 'gray'}
    colors[state] = state  # Activate the current light
    
    # Red light
    ax.add_patch(plt.Circle((0, 6), 0.8, color=colors['red']))
    ax.text(0, 6, 'STOP', color='white', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Yellow light
    ax.add_patch(plt.Circle((0, 4), 0.8, color=colors['yellow']))
    ax.text(0, 4, 'READY', color='black', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Green light
    ax.add_patch(plt.Circle((0, 2), 0.8, color=colors['green']))
    ax.text(0, 2, 'GO', color='white', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Add labels
    ax.text(0, -0.5, "Traffic Light Simulation", ha='center', fontsize=12, fontweight='bold', color='darkblue')
    
    # Turn off axes
    plt.axis('off')
    plt.show()

# Traffic light sequence
def traffic_light_simulation():
    for _ in range(3):  # Repeat the sequence 3 times
        draw_traffic_light('red')    # Red light
        time.sleep(2)  # Simulate delay
        draw_traffic_light('yellow') # Yellow light
        time.sleep(1)  # Simulate delay
        draw_traffic_light('green')  # Green light
        time.sleep(2)  # Simulate delay

# Run the simulation
traffic_light_simulation()
