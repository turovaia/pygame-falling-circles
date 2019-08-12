import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
baked_screen = pygame.Surface(screen.get_size())


circle_color = (0, 0, 255)
active_circles_positions = set()


def draw_active_circles():
    for pos in active_circles_positions:
        pygame.draw.circle(screen, circle_color, pos, 10)


def process_circles_positions():
    global active_circles_positions
    active_circles_positions = set(map(lambda p: (p[0], p[1] + 1), active_circles_positions))

    for pos in active_circles_positions:
        if pos[1] >= height:
            pygame.draw.circle(baked_screen, circle_color, pos, 10)

    active_circles_positions = set(filter(lambda p: p[1] < height, active_circles_positions))


is_running = True
while is_running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("button pressed", event.pos)
            active_circles_positions.add(event.pos)

    screen.blit(baked_screen, (0, 0))
    draw_active_circles()
    process_circles_positions()

    pygame.display.flip()

pygame.quit()
