# Espresso Temperature Controler
Add temperature control functionality to the Rancilio Silvia and live temperature readout via Flask web app.
_(sowftware should work for other machines, but hardware setup might be different.)_

![image](https://user-images.githubusercontent.com/36175788/134394088-dbea1d38-03b6-492e-822c-ecdd7ad84595.png)

## What You Will Need

### Hardware 

* [Raspberry Pi Zero Kit W](https://www.amazon.com/gp/product/B0748MPQT4/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* [24-380V SSR Single Phase Solid State Relay](https://www.amazon.com/gp/product/B094VS4HQC/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1)
* [Adafruit Universal Thermocouple Amplifier MAX31856 Breakout](https://www.amazon.com/gp/product/B01LZBBI7D/ref=ppx_yo_dt_b_asin_title_o00_s02?ie=UTF8&psc=1)
* [K Type Thermocouple](https://www.amazon.com/gp/product/B00OLNZ6XI/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* [Jumper Wires](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* [14 gauge wire](https://www.amazon.com/gp/product/B078YYLT5T/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* Tools (Optional ish)
  * Flat and Philips screwdriver
  * Wirecutters/wire strippers
  * Electrical tape
  * Soldering Iron

### Software

* [Raspbery PI OS](https://www.raspberrypi.org/software/)
* [Python 3](https://projects.raspberrypi.org/en/projects/generic-python-install-python3)

## Hardware install

(Optional)
  Solder pins to the Pi and the MAX31655 like so.
  * [Pi](https://user-images.githubusercontent.com/36175788/134370773-940226f7-7d8e-46b8-ad97-4825b6295f77.png)
  * [MAX31856](https://user-images.githubusercontent.com/36175788/134371076-ff976a91-8eec-4232-9aa9-6d8ed39b2fb7.png)

Start by wiring the parts separately before connecting to the Pi and the machine.

  Solid State Relay (SSR)

   ![0922211122_HDR](https://user-images.githubusercontent.com/36175788/134373583-a2e1c237-97be-47ce-a087-7968363057cc.jpg)

  Thermocouple

   ![image](https://user-images.githubusercontent.com/36175788/134373933-0d860447-2abb-4747-8e4e-979007b17308.png)
   
Next install parts into the machine. 

I have placed the SSR and the PI behind the front plate above the drip tray. I ran the power cable and the jumpers for the thermocouple through the cutout behind the safety overpressure valve. I also ran the two red wires from the SSR up to the boiler chamber.

  ![0922211138_HDR](https://user-images.githubusercontent.com/36175788/134377188-b90efa48-52ad-47a4-9d1a-b6bd83ebe7fe.jpg)

For the thermocuple, I placed it between the pump and the center plate with the jumpers going through the cutout and the thermocouple wire going up to the boiler.

  ![0922211144_HDR](https://user-images.githubusercontent.com/36175788/134377822-fda81ca4-20c2-422b-ae09-c0332f16bd48.jpg)
  
Next we need to connect the SSR. What we are effectively doing is replaceing the thermocouple for the brew temperature with our won digital one. There are two thermocouple at the top of the boiler, one controls the temperature  for steaming (labled 140c) and the other for brewing(labeled 100c). We now need to disconnect the brew thermocouple.

![image](https://user-images.githubusercontent.com/36175788/134380624-7c30d268-4f01-4557-bf8c-0fd950811360.png)

Now that we have disconected the Brew(100c) thermostat we need to bridge the two wire we disconnected. We do this by conneting a wire from teh SSR to each of the wire we just pulled off the stock thermostat.

![image](https://user-images.githubusercontent.com/36175788/134381109-77dd9eeb-437b-4549-9d3c-60b5a3adaa57.png)

Next we need to attach our thermocouple to the boiler body. I have done this by placing it unter the stock Brew Thermostat. (Be carful when tightening the stock thermostat back down. It should be snug so it wont fall out, but no tighter.

![image](https://user-images.githubusercontent.com/36175788/134381982-b5c0ec8a-4cb6-4d06-8732-d72e537ce9af.png)

## Jumper Layout

Using this image as a refference I did the following: 
* SSR 
  * SSR Positive (white) to GPIO 7
  * SSr Negative (black) to Ground directly across from GPIO 7
* MAX31856 sensor
  * Pi 3V to sensor VIN
  * Pi GND to sensor GND
  * Pi SCK (SPI 0) to sensor SCK
  * Pi MISO (SPI 0) to sensor SDO
  * Pi MOSI (SPI 0) to sensor SDI
  * Pi GPIO 5 to sensor CS (or any other free digital I/O pin)

![image](https://user-images.githubusercontent.com/36175788/134382274-c73abe2b-6a66-4213-8021-6028e3000ce0.png)

### Now your Silvia harware is set up!!!


## Software Instalation

First clone this repository to your project directory. 
```
sudo git clone https://github.com/ChristopherJonMyers/Espresso-Temperature-Controler.git
```

You are going to need to install the prerequisits for the Adafruit Universal Thermocouple Amplifier MAX31856.

[Install CircuitPython onto your machine](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

Update to python3
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
```

Install CircuitPython 
```
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```

Install CircuitPython drivers for [adafruit max31856 thermocouple amplifier](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier/python-circuitpython)
```
sudo pip3 install adafruit-circuitpython-max31856
```

[Install and set up Flask](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
```
pip install flask
export FLASK_APP=app
export FLASK_ENV=development
```

Set up Flask and Brewtemp Controller to run on Boot of Raspberrt Pi.

This is done by adding the scripts into the rc.local in the etc folder. 
Start by opening a new terminal and put in these comands to open the file

```
sudo su
cd ../../etc/
nano rc.local
```
Now you need to add the scripts BrewTempControler.py and app.py as shown below. 
(you will need to provide the correct path to where you cloned this repository) 
![image](https://user-images.githubusercontent.com/36175788/134390644-02e19c27-206d-462b-bddd-e1ee54ca68b3.png)

Save this file and reboot.
```
sudo reboot
```

### Now your Raspberry Pi is set up! Time to brew! 




