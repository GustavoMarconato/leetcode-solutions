import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from constants import DT
from physics import velocity_verlet, schwarzschild_radius




num_particles = 200
trail_length = 30

positions = []
velocities = []



for i in range(num_particles):

    r = np.random.uniform(4, 10)
    theta = np.random.uniform(0, 2*np.pi)

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    pos = np.array([x,y])

    v = np.sqrt(100/r)

    vx = -v*np.sin(theta)
    vy = v*np.cos(theta)

    vel = np.array([vx,vy])

    positions.append(pos)
    velocities.append(vel)

positions = np.array(positions)
velocities = np.array(velocities)



trails = [[] for _ in range(num_particles)]



r_s = schwarzschild_radius()



fig, ax = plt.subplots()


speeds = np.linalg.norm(velocities, axis=1)

particles = ax.scatter(
    positions[:,0],
    positions[:,1],
    c=speeds,
    cmap="plasma",
    s=6
)

# horizonte de eventos
blackhole = plt.Circle((0,0), r_s, color="black")
ax.add_artist(blackhole)

# trilhas
trail_lines = []

for _ in range(num_particles):
    line, = ax.plot([], [], linewidth=1, alpha=0.25)
    trail_lines.append(line)

ax.set_xlim(-12,12)
ax.set_ylim(-12,12)
ax.set_aspect("equal")


def update(frame):

    global positions, velocities

    for i in range(num_particles):

        positions[i], velocities[i] = velocity_verlet(
            positions[i], velocities[i], DT
        )

        # partículas caem no buraco negro
        if np.linalg.norm(positions[i]) < r_s:
            positions[i] = np.array([np.nan, np.nan])

        # guardar trilha
        trails[i].append(positions[i].copy())

        if len(trails[i]) > trail_length:
            trails[i].pop(0)

    # velocidades
    speeds = np.linalg.norm(velocities, axis=1)

    

    depth = positions[:,1]   # usa eixo Y como profundidade
    size = 4 + 8*(depth - depth.min())/(depth.max()-depth.min()+1e-5)

    particles.set_sizes(size)

  

    particles.set_offsets(positions)
    particles.set_array(speeds)

    # atualizar trilhas
    for i in range(num_particles):

        if len(trails[i]) > 1:
            trail = np.array(trails[i])
            trail_lines[i].set_data(trail[:,0], trail[:,1])

    return particles, *trail_lines

anim = FuncAnimation(fig, update, frames=1000, interval=20)

plt.title("Black Hole Accretion Disk Simulation")

plt.show()