# CO2 Sensor

## Initial AI Prompt
I have some parts from Adafruit so that I can build my own CO2 sensor. When the sensor detects the amount of CO2 in the air to be too high, I want to turn on a computer fan.

Here are details on the specific parts:

**CO2 Sensor**

- Product page: https://www.adafruit.com/product/5187
- Learning guide: https://learn.adafruit.com/adafruit-scd-40-and-scd-41?view=all
- Another guide: https://learn.adafruit.com/diy-trinkey-no-solder-air-quality-monitor?view=all
- Another guide: https://learn.adafruit.com/disconnected-co2-data-logger?view=all

**Microcontroller**

- Product page: https://www.adafruit.com/product/5691
- Learning guide: https://learn.adafruit.com/esp32-s3-reverse-tft-feather
- Another guide: https://learn.adafruit.com/esp32-s2-tft-digital-clock-display-featuring-blanka-chan
- Another guide: https://learn.adafruit.com/circuitpython-day-2024-countdown-clock
- Another guide: https://learn.adafruit.com/circuitpython-elgato-wifi-light-controller

**Stemma QT Breakout Board**

- Product page: https://www.adafruit.com/product/5961
- Github repo with PCB files: https://github.com/adafruit/Adafruit-Qwiic-Stemma-QT-Breakout-Board-PCB

**Computer Fan**

- 5V, 0.9A for power input
- I have many power supplies, so please suggest one that can power the microcontroller, sensor, and fan together

**N-Channel MOSFET**

- Product page: https://www.adafruit.com/product/355
- Datasheet: https://cdn-shop.adafruit.com/datasheets/irlb8721pbf.pdf

I would prefer to write this with Python as opposed to C. I also have Stemma QT connectors and cables to make connections a little easier. Please guide me, and supply the basic code I need, so that I can:

- Display the CO2 value as parts per million on the OLED display (e.g. 1200ppm)
- Update that CO2 value once per second
- Show a tiny timestamp in the corner of the OLED screen with the last time the value was read (so I can verify it’s actually updating)
- Start the computer fan when the ppm hits a certain threshold, written as a constant in the code (default to 1500ppm for now)

I may not need the breakout board. If I can just plug the sensor directly into the microcontroller with a Stemma QT cable, I’d prefer to do that for a clean install. For now, I’ll power the microcontroller via USB-C.
