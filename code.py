import board
import terminalio
from adafruit_display_text import bitmap_label
import displayio

display = board.DISPLAY
print(display)
# Update this to change the text displayed.
text = "Hello, World!"
# Update this to change the size of the text displayed. Must be a whole number.
scale = 1

text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale)
text_area.x = 10
text_area.y = 10

text_group = displayio.Group()
main_group = displayio.Group()

my_display_group = displayio.Group()
my_display_group.append(text_group)
my_display_group.append(text_area)
display.root_group = my_display_group

while True:
    pass
