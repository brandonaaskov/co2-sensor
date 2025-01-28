# CO2 Sensor

## Crappy Wiring Diagram
![Wiring Diagram](https://github.com/brandonaaskov/co2-sensor/blob/main/wiring-diagram.png?raw=true)

## Parts List

This uses a [PN2222A transistor](https://cdn-shop.adafruit.com/datasheets/PN2222A.pdf).

- [Microcontroller: Adafruit ESP32-S3 Reverse TFT Feather](https://www.adafruit.com/product/5691)
- [Adafruit CO2 Sensor](https://www.adafruit.com/product/5187)
- [PN2222A Transistor](https://www.adafruit.com/product/756)
- 1KΩ resistor
- Computer Fan: 5V 90mA
  - _does not need variable control_
  - _5V is required, low current draw allows the board to power it all_
  - _if total current draw from fans exceeds 500mA, a separate power supply is required_
