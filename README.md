# CO2 Sensor

## Fifth AI Attempt (Claude only)

I would like to expand this code to read values from a CO2 sensor and display that value instead of the hardcoded “1500 ppm” that’s currently in there:

Here’s the current code:

```python
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
```

Here is the CO2 sensor that I have:

- Product page: https://www.adafruit.com/product/5187
- Learning guide: https://learn.adafruit.com/adafruit-scd-40-and-scd-41?view=all
- Another guide: https://learn.adafruit.com/diy-trinkey-no-solder-air-quality-monitor?view=all
- Another guide: https://learn.adafruit.com/disconnected-co2-data-logger?view=all

Can you help me update my code to read values from this sensor and display that instead?
