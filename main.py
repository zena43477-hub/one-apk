import pgzrun
from pygame import Rect

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

pgzrun.go()
