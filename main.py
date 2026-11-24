import sys, os, traceback, textwrap

def show_error(text):
    try:
        path = os.path.join(os.environ.get("ANDROID_PRIVATE", "."), "error.txt")
        with open(path, "w") as f:
            f.write(text)
    except Exception:
        pass
    try:
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((480, 800))
        font = pygame.font.Font(None, 26)
        lines = []
        for raw in text.splitlines():
            lines += textwrap.wrap(raw, 38) or [""]
        lines = lines[-28:]
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
            screen.fill((60, 0, 0))
            for i, line in enumerate(lines):
                screen.blit(font.render(line, True, (255, 255, 255)), (8, 8 + i * 27))
            pygame.display.flip()
            clock.tick(15)
    except Exception:
        pass

try:
    import pgzrun
    from pygame import Rect
except Exception:
    show_error(traceback.format_exc())
    sys.exit()

WIDTH = 480
HEIGHT = 800
TITLE = "Button test"

button = Rect(60, 300, 360, 200)
colors = ["red", "green", "blue", "orange", "purple"]
state = {"n": 0, "touches": 0, "pos": (0, 0)}

def draw():
    screen.fill((30, 30, 40))
    screen.draw.filled_rect(button, colors[state["n"] % len(colors)])
    screen.draw.text("НАЖМИ", center=button.center, fontsize=60, color="white")
    screen.draw.text(f"Нажатий: {state['n']}", center=(WIDTH // 2, 150), fontsize=50)
    screen.draw.text(f"Касаний: {state['touches']}  {state['pos']}",
                     center=(WIDTH // 2, 650), fontsize=32, color="gray")

def on_mouse_down(pos):
    state["touches"] += 1
    state["pos"] = pos
    if button.collidepoint(pos):
        state["n"] += 1

try:
    pgzrun.go()
except Exception:
    show_error(traceback.format_exc())
