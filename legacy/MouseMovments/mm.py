import pyautogui
import time


def display_screensize():
    print(pyautogui.size())


class MouseMove:
    x = 0
    y = 0

    def __init__(self):
        pyautogui.PAUSE = 1  # set the pause equals to one
        pyautogui.FAILSAFE = True  # Sets the Fail safe to be one
        display_screensize()  # Printing the size of the display
        self.x, self.y = self.get_positions()
        print(self.x)
        print(self.y)

    def get_positions(self):
        x, y = pyautogui.position()  # this returns a tupple as in the x and the y
        return x, y

    def move_left(self):
        p_v = self.x
        self.x -= 100
        if self.x >= 0:
            pyautogui.moveTo(self.x, self.y, duration=0.25)  # Moving in the left area
            print(self.x)
        else:
            self.x = p_v  # Sets to zero

    def move_right(self):
        p_v = self.x  # Previous value
        self.x += 90  # Incrementing the value of x axis
        if self.x >= 0:
            pyautogui.moveTo(self.x, self.y, duration=0.25)  # Moving in the left area
            print(self.x)  # Debugging
        else:
            self.x = p_v  # Going back to the previous value

    # Below Function will be responsible for the Moving of the cursor dup (positive y - axis)

    def move_up(self):
        p_v = self.y
        self.y -= 90
        if self.y >= 0:
            pyautogui.moveTo(self.x, self.y, duration=0.25)
            print(self.y)  # Debugging purpose
        else:
            self.y = p_v  # setting to the previous value of the y axis

    # Below Function will be responsible for the Moving of the cursor down (negative y - axis)
    def move_down(self):
        p_v = self.y
        self.y += 90
        if self.y >= 0:
            pyautogui.moveTo(self.x, self.y, duration=0.25)
            print(self.y)  # Debugging purpose
        else:
            self.y = p_v  # setting to the previous value of the y axis

    def on_click_screen(self):
        try:
            pyautogui.click(self.x, self.y, duration=0.25)
            print("Clicked")
        except Exception as Ex:
            print("clicked")

    # The Function is responsible for the movement on the basis of the applied Text (input)
    def on_command_move(self, mouse_command=None):
        try:
            if mouse_command is not None:
                mouse_command = mouse_command.strip()  # remove the extra white spaces
                mouse_command = mouse_command.lower()  # Converts into lower Strings
                if mouse_command == "left":
                    self.move_left()  # move left function is called
                elif mouse_command == "right":
                    self.move_right()  # move right function is called
                elif mouse_command == "up":
                    self.move_up()  # move up function is called
                elif mouse_command == "down":
                    self.move_down()  # Move down function called
                elif mouse_command == "click":
                    self.on_click_screen()  # Clicks the specified location in the Screen
                else:
                    print("Invalid Command Mate!")
                    return  # Returns to the Place where the function was called
        except KeyboardInterrupt as Ex:
            print("Interrupted by the Keyboard keys :", Ex)
        except Exception as Ex:
            print("The following Error Occurred", Ex)  # this is the Printing of the exception

    def scroll_down(self):
        pyautogui.scroll(200)  # Scrolls the pyautogui
        print("SCROLLING")
        time.sleep(1)

    def scroll_up(self):
        pyautogui.scroll(-90)  #
        time.sleep(1)

    def test_check(self):
        for i in range(2):
            pyautogui.moveTo(100, 100, duration=0.25)
            pyautogui.moveTo(200, 100, duration=0.25)
            pyautogui.moveTo(200, 200, duration=0.25)
            pyautogui.moveTo(100, 200, duration=0.25)


# M_obj = MouseMove()
# M_obj.move_left()
# M_obj.move_up()
# M_obj.move_right()
# M_obj.move_down()
# M_obj.test_check() # Just for the debuggin purpose
# M_obj.on_command_move("left")
# M_obj.on_command_move("up")
# M_obj.on_command_move("right")
# M_obj.on_command_move("down")
# M_obj.on_command_move("click")
# M_obj.scroll_down()
