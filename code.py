import board
import terminalio
import time
from adafruit_display_text import bitmap_label
import displayio
import adafruit_scd4x
# import busio

# Initialize I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()  # Start taking measurements

display = board.DISPLAY

# Create the main display group
main_group = displayio.Group()

# Create the PPM text (large and centered)
ppm_text = bitmap_label.Label(
    terminalio.FONT,
    text="Wait...",  # Initial text while sensor warms up
    scale=3,  # Makes it larger
    color=0xFF0000,  # Red color in hex
)
# Center the PPM text
ppm_text.anchor_point = (0.5, 0.5)
ppm_text.anchored_position = (display.width // 2, display.height // 2)

# Create the clock text (smaller, bottom right)
clock_text = bitmap_label.Label(terminalio.FONT, text="00:00:00", scale=1)
# Position clock in bottom right
clock_text.x = display.width - 70
clock_text.y = display.height - 10

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

    # Read CO2 data if it's available
    if scd4x.data_ready:
        co2 = scd4x.CO2
        ppm_text.text = f"{co2} ppm"

        # Optionally change color based on CO2 levels
        if co2 < 1000:
            ppm_text.color = 0x00FF00  # Green
        elif co2 < 2000:
            ppm_text.color = 0xFFFF00  # Yellow
        else:
            ppm_text.color = 0xFF0000  # Red

    # Small delay to prevent too frequent updates
    time.sleep(1)
