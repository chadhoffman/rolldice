
"""Simple pynecone module dice."""
import random
import pynecone as pc
from .state import State


class DiceState(State):
    size: int = 20
    current: int = 0
    history: list[int] = []
    history_string: str = "No Rolls Yet"

    def roll(self):
        h: str = "Past Rolls: " 
        self.current = random.randint(1, self.size)
        self.history.append(self.current)
        if len(self.history) > 10:
            self.history.pop(0)
            h += "... "
        for i in self.history:
            h += str(i) + ", "
        self.history_string = h.removesuffix(", ")

def die_render():
    die_heading = pc.heading(DiceState.size+" Sided Die", size="md")
#   die_heading = pc.heading(f"{DiceState.size} Sided Die", size="md")
    def roll_button():
        return pc.square(
            pc.button(
                "Roll",
                color_scheme="blue",
                size="lg",
                on_click=DiceState.roll,
            ),
            align_items="center",
            h="100%"
        )
    die_result = pc.square(pc.heading(DiceState.current, font_size="2em"))
    roll_history = pc.text(DiceState.history_string, color="grey", font_size="0.25em", text_align="center")
    
    return pc.center(
        pc.grid(
            pc.grid_item(die_heading, col_span=2, bg="white", text_align="center"),
            pc.grid_item(roll_button(), bg="white"),
            pc.grid_item(die_result, bg="white"),
            pc.grid_item(roll_history, col_span=2, bg="white"),
            template_rows="20px 1fr 15px",
            template_columns="repeat(2, 1fr)",
            gap=1,
            width="225px",
            hieght="250px",
        ),
        border_radius="15px",
        border_width="thick",
        padding=1    
    )