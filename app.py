from flask import Flask, render_template
import time
import board
import digitalio
import adafruit_max31856

app = Flask(__name__)

@app.route('/')
def index():
    curTemp = Tcup()
    return render_template('index.html', curTemp=curTemp)

def Tcup():
    spi = board.SPI()
    cs = digitalio.DigitalInOut(board.D5)
    cs.direction = digitalio.Direction.OUTPUT
    thermocouple = adafruit_max31856.MAX31856(spi, cs)
    curTemp = thermocouple.temperature
    if curTemp is not None:
        return round(curTemp,1)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

