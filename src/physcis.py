import math 

from src.body import Body

G = 6.67430e-11

def compute_gravitational_acceleration(target: Body, source: Body) -> tuple[float, float]:
    dx = source.x - target.x
    dy = source.y - target.y

    distance_squared = dx * dx + dy * dy
    if distance_squared == 0:
        return 0.0, 0.0
    
    distance = math.sqrt(distance_squared)
    acceleration_magnitude = G * source.mass / distance_squared

    ax = acceleration_magnitude * dx / distance
    ay = acceleration_magnitude * dy / distance
    return ax, ay 

def update_bodies(bodies: list[Body], dt_seconds: float) -> None: 
    acceleration: list[tuple[float, float]] 

    for target in bodies:
        if target.is_fixed:
            acceleration.append((0.0, 0.0))
            continue
        total_ax = 0.0
        total_ay = 0.0

        for source in bodies:
            if source is target:
                continue

            ax, ay = compute_gravitational_acceleration(target, source)
            total_ax += ax 
            total_ay += ay

        acceleration.append((total_ax, total_ay))

    for body, (ax, ay) in zip(bodies, accelerations):
        if body.is_fixed:
            continue

        body.vx += ax * dt_seconds
        body.vy += ay * dt_seconds
        body.x += body.vx * dt_seconds
        body.y += body.vy * dt_seconds
