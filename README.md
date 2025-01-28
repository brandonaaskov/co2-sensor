# CO2 Sensor

## Final working prototype

This uses a [PN2222A transistor](https://cdn-shop.adafruit.com/datasheets/PN2222A.pdf).

Wiring “diagram”:

```
5V Power Supply -----> Fan (+) wire
                      Fan (-) wire -----> Collector (right pin)
                                        Emitter (left pin) -----> System Ground
                                        Base (middle pin) -----> 1kΩ -----> GPIO (3.3V when ON)
```
