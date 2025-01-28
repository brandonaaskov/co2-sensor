import board
import terminalio
import time
from adafruit_display_text import bitmap_label
import displayio
import adafruit_scd4x
import digitalio

# Initialize I2C
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

# Initialize fan control GPIO
fan_pin = digitalio.DigitalInOut(board.D9)
fan_pin.direction = digitalio.Direction.OUTPUT
fan_pin.drive_mode = digitalio.DriveMode.PUSH_PULL
fan_pin.value = False  # Start with fan off (normal logic)

display = board.DISPLAY

# Create the main display group
main_group = displayio.Group()

# Create the PPM text (large and centered)
ppm_text = bitmap_label.Label(terminalio.FONT, text="Wait...", scale=3, color=0xFF0000)
ppm_text.anchor_point = (0.5, 0.5)
ppm_text.anchored_position = (display.width // 2, display.height // 2)

# Create the clock text (smaller, bottom right)
clock_text = bitmap_label.Label(terminalio.FONT, text="00:00:00", scale=1)
clock_text.x = display.width - 70
clock_text.y = display.height - 10

# Create fan status text (smaller, top right)
fan_text = bitmap_label.Label(terminalio.FONT, text="Fan: OFF", scale=1)
fan_text.x = display.width - 70
fan_text.y = 20

# Add all elements to the main group
main_group.append(ppm_text)
main_group.append(clock_text)
main_group.append(fan_text)

# Show it on the display
display.root_group = main_group

# Variables for fan control with hysteresis
FAN_ON_THRESHOLD = 1100

while True:
    print(fan_pin.value)
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

        # Fan control logic with hysteresis (normal logic)
        if co2 > FAN_ON_THRESHOLD:  # Check if fan is off
            fan_pin.value = True  # Turn fan on
            fan_text.text = "Fan: ON"
        else:  # Check if fan is on
            fan_pin.value = False  # Turn fan off
            fan_text.text = "Fan: OFF"

        # Color coding based on CO2 levels
        if co2 < FAN_ON_THRESHOLD:
            ppm_text.color = 0x00FF00  # Green
        elif co2 < 1500:
            ppm_text.color = 0xFFFF00  # Yellow
        else:
            ppm_text.color = 0xFF0000  # Red

    time.sleep(1)
