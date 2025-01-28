import board
import terminalio
import time
from adafruit_display_text import bitmap_label
import displayio

display = board.DISPLAY

# Create the main display group
main_group = displayio.Group()

# Create the PPM text (large and centered)
ppm_text = bitmap_label.Label(
    terminalio.FONT,
    text="1500 ppm",
    scale=3,  # Makes it larger
    color=0xFF0000,  # Red color in hex
)
# Center the PPM text
ppm_text.anchor_point = (0.5, 0.5)
ppm_text.anchored_position = (display.width // 2, display.height // 2)

# Create the clock text (smaller, bottom right)
clock_text = bitmap_label.Label(terminalio.FONT, text="00:00:00", scale=1)
# Position clock in bottom right
clock_text.x = display.width - 70  # Adjust this value if needed
clock_text.y = display.height - 10  # Adjust this value if needed

# Add both text elements to the main group
main_group.append(ppm_text)
main_group.append(clock_text)

# Show it on the display
display.root_group = main_group

# Main loop
while True:
    # Update the time
    current_time = time.localtime()
    time_str = "{:02d}:{:02d}:{:02d}".format(
        current_time.tm_hour, current_time.tm_min, current_time.tm_sec
    )
    clock_text.text = time_str

    # Small delay to prevent too frequent updates
    time.sleep(1)
