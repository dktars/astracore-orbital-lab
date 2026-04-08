from src.body import Body
from src.constants import MAX_TRAIL_POINTS, SIMULATION_TIME_STEP
from src.physics import update_bodies

class Simulation:
    def __init__(self, bodies: list[Body]) -> None:
        self.bodies = bodies
        self.elapsed_time = 0.0

    def update(self, frame_dt: float) -> None:
        del frame_dt # reserved for future use

        update_bodies(self.bodies, SIMULATION_TIME_STEP)
        self.elapsed_time += SIMULATION_TIME_STEP

        for body in self.bodies:
            body.add_trail_point()
            if len(body.trail) > MAX_TRAIL_POINTS:
                body.trail.pop(0)

    def reset(self, bodies: list[Body]) -> None:
        self.bodies = bodies
        self_elapsed_time = 0.0
