# CO2 Sensor

_Note: Prompted Claude this time (and going forward until the working prototype) as it was the most succinct and successful as compared to Perplexity and ChatGPT. I didn't give DeepSeek R1 a fair shot because it's running on my Windows machine in a Docker container at the moment and isn't as usable as it needs to be._

## Fourth AI Attempt

I have a microcontroller from Adafruit, and I want to display some stuff on this OLED screen.

**Microcontroller**

- Product page: https://www.adafruit.com/product/5691
- Learning guide: https://learn.adafruit.com/esp32-s3-reverse-tft-feather?view=all
- Another guide: https://learn.adafruit.com/esp32-s2-tft-digital-clock-display-featuring-blanka-chan?view=all
- Another guide: https://learn.adafruit.com/circuitpython-day-2024-countdown-clock?view=all
- Another guide: https://learn.adafruit.com/circuitpython-elgato-wifi-light-controller?view=all

In the bottom right of the screen I would like to display the current time as (HH:MM:SS) using military time. It should update every second. That font size can be small. I would also like to display the text “1500 ppm” in large bold text in the middle of the screen. I would also like that text to be red.

I already have CircuitPython installed on the microcontroller. I just need the code to get it operational. Can you help with that?
