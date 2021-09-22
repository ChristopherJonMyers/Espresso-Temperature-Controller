import time
import board
import digitalio
import adafruit_max31856

# Adjust the desired brew temperatur by changing the value of theis variable.
brewTemp = 94.0

# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()

# allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(board.D5)
cs.direction = digitalio.Direction.OUTPUT

# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# allocate solid state relay GPIO pin
SSR = digitalio.DigitalInOut(board.D7)

# set solid state relay direction f
SSR.direction = digitalio.Direction.OUTPUT

# This is the logic control of the SSR:
# Infinite loop that runs while the pi is on. This is done in the etc/rc.local
while True:
    # Turn on relay if thermocuple reads below desired brew temp
    if brewTemp > thermocouple.temperature:
        SSR.value = True
    # Turn off relay if thermocouple reads above desired brew temp
    elif brewTemp < thermocouple.temperature:
        SSR.value = False
    # The sleep timer determines how often the loop repeats right now  it is set up to check the temperature 10 times second.
    time.sleep(0.1)
    

