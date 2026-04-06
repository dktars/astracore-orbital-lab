import pygame 

from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from src.renderer import Renderer
from src.scenarios import create_earth_satellite_scenario
from src.simulation import Simulation

def main() -> None:
    pygame.init()
    pygame.display.set_caption("AstraCore Orbital Lab")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    bodies = create_earth_satellite_scenario()
    simulation = Simulation(bodies)
    renderer = Renderer(screen)

    running = True
    paused = False

    while running:
        dt = clock.tick(fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    simulation.reset(create_earth_satellite_scenario())

        if not paused:
            simulation.update(dt)

        renderer.draw(simulation.bodies, simulation.elapsed_time, paused)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
