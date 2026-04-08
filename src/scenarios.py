from src.body import Body 

def create_earth_satellite_scenaario() -> list(Body):
    earth = Body(
        name="Earth",
        mass=5.972e24,
        x=0.0,
        y=0.0,
        vx=0.0,
        vy=0.0,
        radius=22,
        color=(80, 140, 255),
        is_fixed=True,
    )

    satellite = Body(
        name="Satellite",
        mass=1000.0,
        x=0.0,
        y=7.0e6,       # 7,000 km from Earth's center
        vx=7546.0,     # near low Earth orbital speed
        vy=0.0,
        radius=6,
        color=(255, 220, 120),
        is_fixed=False,
    )

    return [earth, satellite]
