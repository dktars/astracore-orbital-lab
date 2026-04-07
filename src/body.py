from dataclasses import dataclass, field

@dataclass
class Body: 
    name: str
    mass: float 
    x: float 
    y: float
    vx: float 
    vy: float
    radius: int
    color: tuple[int, int, int]
    is_fixed: bool = False
    trail: list[tuple[float, float, float]] = field(default_factory=list)

    def add trail_point(self) -> None:
        self.trail.append((self.x, self.y))
