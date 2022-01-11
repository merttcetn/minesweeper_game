from tkinter import *
from cell import Cell
import settings
import utilities


root = Tk()

# Main frame configurations
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Mayın Tarlası")
root.resizable(False, False)


# Top frame configurations
top_frame = Frame(
    root,
    bg='black',  # To be changed to black later
    width=1080,
    height=utilities.height_percentage(25)
)
top_frame.place(x='0', y='0')  # Placing top frame to the main frame(root)

# Left frame configurations
left_frame = Frame(
    root,
    bg='black',  # To be changed to black later
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=135)

# Center frame configurations
center_frame = Frame(
    root,
    bg='black',  # To be changed black later
    width=utilities.width_percentage(75),
    height=utilities.height_percentage(75)
)
center_frame.place(x=utilities.width_percentage(25), y=utilities.height_percentage(25))

# Title configurations
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    height=4,
    width=24,
    font=("", 36),
    text="Minesweeper Game"
)
# Placing title
game_title.place(
    x=utilities.width_percentage(25),
    y=-50
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_object(center_frame)  # Locating the button object to the center frame object
        c.cell_button_object.grid(
            column=x,
            row=y
        )

Cell.randomize_mines()

# Call the label object from class level
Cell.create_cell_count_label(left_frame)  # Locate it on the left frame

Cell.cell_count_label_object.place(  # Positioning the label
    x=0,
    y=0
)

# To run the window
root.mainloop()

