import pygame 

from src.body import Body
from src.constants import (
    BACKGROUND_COLOR,
    PIXELS_PER_METER,
    TEXT_COLOR,
    TRAIL_COLOR_DIM_FACTOR,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen 
        self.font = pygame.font.SysFont("Arial", 20)
        self.title_font = pygame.font.SysFont("Arial", 28, bold=True)

    def world_to_screen(self, x: float, y: float) -> tuple[init, init]:
        screen_x = int(WINDOW_WIDTH / 2 + x * PIXELS_PER_METER)
        screen_y = int)WINDOW_HEIGHT /2 - y * PIXELS_PER_METER)
        return screen_x, screen_y
    
    def _draw(self, bodies: list[Body], elapsed_time:
        self.screen.fill(BACKGROUND_COLOR)

        self._draw_trails(bodies)
        self._draw_bodies(bodies)
        self._draw_hud(elapsed_time, paused)

    def _draw_trails(self, bodies: list[Body]) -> None:
        for body in bodies:
            if len(body.trail) < 2:
                continue
                
            points = [self.world_to_screen(x, y) for x, y in body.trail]
            dimmed_color = tuple(int(c * TRAIL_COLOR_DIM_FACTOR) for c in body.color)
            pygame.draw.circle(self.screen, dimmed_color, False, points, 2)

    def _draw_bodies(self, bodies: list[Body]) -> None:
        for body in bodies:
            sx, sy = self.world_to_screen(body.x, body.y)
            pygame.draw.circle(self.screen, body.color, (sx, sy), body.radius)

            label = self.font.render(body.name, True, TEXT_COLOR)
            self.screen.blit(label, (sx + body.radius + 8, sy - body.radius -8))

    def _draw_hud(self, elapsed_time: float, paused: bool) -> None:
        title = self.title_font.render("AstraCore Orbital Lab", True, TEXT_COLOR)
        self.screen.blit(title, (20, 20))

        status_text = "Paused" if paused else "Running"
        hours = elapsed_time / 3600.0

        hud_lines = [
            f"Status: {status_text}",
            f"Simulated Time: {hours:.2f} hours",
            "Controls: SPACE pause/resume | R reset | ESC quit",
        ]

        y = 65 
        for line in hud_lines:
            text = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(text, (20, y))
            y += 28
