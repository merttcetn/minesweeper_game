from tkinter import Button, Label, messagebox
import settings
import random
import sys  # To exit game when losing

class Cell:
    all = []  # Creating a list to store 'all' instances

    cell_count_number = settings.CELL_COUNT  # Giving it the initial value

    cell_count_label_object = None  # Creating a label object to assign later

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine  # To decide whether the cell is mine
        self.is_opened = False  # To decide whether the cell is opened or not
        self.is_mine_candidate = False  # Stating that the cell is right clicked
        self.x = x
        self.y = y
        self.cell_button_object = None

        Cell.all.append(self)  # Appending all instances to a list that consists of the instances

    def create_button_object(self, location):
        button = Button(
            location,  # In our case the location will be center_frame
            width=9,
            height=3
        )

        button.bind('<Button-1>', self.left_click_actions)  # Left click
        button.bind('<Button-3>', self.right_click_actions)  # Right click

        self.cell_button_object = button

    @staticmethod  # Since label is not belong to cells we need to call it from the class level
    def create_cell_count_label(location):
        label = Label(
            location,
            bg='black',
            fg='white',
            height=4,
            width=12,
            font=("", 28),
            text=f"Cells Left: {Cell.cell_count_number}"
        )

        Cell.cell_count_label_object = label  # Making it equal to the 'label' we have created

    def left_click_actions(self, event):  # Adding the 'event' variable because that's how Python works
        if not self.is_mine_candidate:
            if self.is_mine:
                self.show_mine()
            else:
                if self.surrounding_mines_counter == 0:  # If we have left clicked on a '0' cell
                    for cell_obj in self.surrounding_cells:  # every cell surrounding it
                        cell_obj.show_cell()  # will be opened as well
                self.show_cell()

        # Cancel the Left click actions if the cell is opened
        self.cell_button_object.unbind('<Button-1>')

    def get_cell_by_axis(self, x, y):  # Return a cell object based on its x and y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.cell_button_object.configure(bg='red')  # Set the cell color to red if it is a mine
        messagebox.showerror("Game Over!", "You clicked on a mine.")
        sys.exit()  # To exit game

    @property  # Making the function a property to make it a read-only attribute
    def surrounding_cells(self):  # Gathering the surrounding cells by using get_cell_axis method
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        # Filtering out the 'None' cells in the surrounding cells list by list comprehension

        return cells

    def show_cell(self):
        if not self.is_opened:  # If it is not opened do these;

            Cell.cell_count_number -= 1  # Decreasing it by 1, every time we click on a cell

            # Checking whether if we have won;
            if Cell.cell_count_number == settings.WIN_COUNT:
                Cell.cell_count_label_object.configure(text="YOU WON!")
                messagebox.showinfo("YOU WON!", "You have won the game.")
                sys.exit()

            # Writing the surrounding mines to the cell after clicking
            self.cell_button_object.configure(text=f"{self.surrounding_mines_counter}")

            # Rewrite on the cell_count_label_object in this function
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left: {Cell.cell_count_number}")

        # Mark the cell as opened if it is not (Use it as the last line)
        self.is_opened = True

    @property  # Making the function a property to make it a read-only attribute
    def surrounding_mines_counter(self):
        count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count += 1

        return count  # Returning the count to reach it from other methods

    def right_click_actions(self, event):
        if not self.is_opened:
            if not self.is_mine_candidate:
                self.cell_button_object.configure(
                    bg='orange',
                    text="Mine"
                )
                self.is_mine_candidate = True

            else:
                self.cell_button_object.configure(
                    bg='SystemButtonFace',
                    text=""
                )
                self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(  # Randomly picking cells to make them mines
            Cell.all,
            settings.MINES_COUNT
        )

        for picked_cell in picked_cells:  # Turning picked cells into mines
            picked_cell.is_mine = True

    def __repr__(self):  # Overriding the __repr__ method to make it more user friendly
        return f"Cell({self.x}, {self.y})"
