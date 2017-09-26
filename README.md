# Auto-Pilot-Demo
This is the project about Auto-Pilot. We are going to build a demo car based on Lego EV3DEV platform. 

# NOTICE
By **5 Oct**, I hope all the team members can really understand how the hardware(ev3dev) works and be able to write a simple program(simple sensor and actuator loop). 

# Table of Contents

* [Introduction](https://github.com/CoorFun/Auto-Pilot-Demo#Introduction)
* [What is the LEGO EV3 Controller?](https://github.com/CoorFun/Auto-Pilot-Demo#what-is-the-lego-ev3-controller)
* [How can LEGO EV3 work with a OS?](https://github.com/CoorFun/Auto-Pilot-Demo#how-can-lego-ev3-work-with-a-os)
* [Tutorial](https://github.com/CoorFun/Auto-Pilot-Demo#tutorial)
  * [How to install EV3Dev?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-install-ev3dev)
  * [How to access EV3Dev OS?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-access-ev3dev-os)
    * [Network](https://github.com/CoorFun/Auto-Pilot-Demo#network)
    * [USB-Cable](https://github.com/CoorFun/Auto-Pilot-Demo#usb-cable)
    * [Bluetooth](https://github.com/CoorFun/Auto-Pilot-Demo#bluetooth)
  * [How to understand the way linux manage hardware?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-understand-the-way-linux-manage-hardware)
  * [How to make a simple sensor loop?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-make-a-simple-sensor-loop)
  * [How to write program locally and run promotely?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-write-program-locally-and-run-promotely)
  * [How to study more operations?](https://github.com/CoorFun/Auto-Pilot-Demo#how-to-study-more-operations)
* [Conclusion(My experience)](https://github.com/CoorFun/Auto-Pilot-Demo#conclusionmy-experience)

# Introduction
- [X] 2017.09.22

Even through there are some certain reference documentations for the platform EV3dev or Python language, they are always constructed separately. It means that taking all of those knowledge together for a specific project(Like our project) can be a very difficult thing for a beginner. So to let us better understand how the hardware works, I am going to update some 'Tutorial' here. Follow it and feel free to ask questions.

# What is the LEGO EV3 Controller?
- [X] 2017.09.22

As we all know, Logo EV3 is one of the most powerful hardware controller used to connect those LEGO peripheral electronic devices, which is a thing we can program by its software(Or we can call it IDE) and then download and execute it. Normally, without any add-on stuffs(Like SD card or USB devices), this controller only works with its own IDE called 'EV3 PROGRAMMER' which is a graphic interface based programming language(like Scrath). GUI programming language is usually designed for kids or young child who are not able to learn coding. Instead of various key words and syntax, it uses some picture(Or we can say it's a Tag) things which can connect with each other following some logical order, just like a puzzle game. And on those pictures, certain feature parameters can be set. When all the tags have been connected, programing is finished. Definitely we have to say this is a very smart and creative way to do programming, but the shortage is it's not flexable and miss the abality to change some more complicate projects. 

# How can LEGO EV3 work with a OS?
- [X] 2017.09.22

Like I mentioned in the previous section, EV3 is not the only controller produced by LEGO. There are indeed some other controllers, for example NXT. But the powerful feature which only appears on EV3 is that it makes possibility to run some other OS except its own! By having an operating system, surely we can do more things. 

There are several different systems which are designed for LEGO controller. Here because of the hardware we already have, we only compare 2 different systems for EV3. They are:

> * [leJOS EV3](http://www.lejos.org/)
> * [EV3Dev](http://www.ev3dev.org/)

leJOS EV3 is actually a Java Virtual Machine(JVM) planted to fit EV3, which has full EV3 API and a java run time system. There is only one thing you have to know about this OS, the Java language is the one and the only one language it supports. 

EV3Dev is a Debian Linux-based operating system that runs on several LEGO compatible platforms including the LEGO EV3 and Raspberry Pi-powered BrickPi. It means that when we have the EV3Dev on EV3, the way we use it is closer to the way we operate an RasPi or Beaglebone etc. It can support various different languages including C, Java, Python etc. 

As we know that, the only we can access hardware under Linux is via the file system. In other word, writing or reading files are the way Linux manages its hardwares. So as long as a language can run on Linux OS and has a library to access file system, it can interact with connected hardwares. **This is one of the most important reasons why we decide to choose EV3Dev system.**

To complete this project, there will be plenty of calculation and algorithm to use. **So this is another consideration why we choose Python language.** Because it has vast libraries which can help. This is also the benefits which java does not have. 

# Tutorial
- [X] 2017.09.24

## How to install EV3Dev?

To have EV3Dev on your LEGO EV3, the only thing you need is a micro SD card. Download the latest system image file from ev3dev.org. And then you have to find a software which can flash this image file onto your card. (Notice: An image file can be considered as an image of a disk. So when you flash it onto the card, it actually changes the formatting of the card. **This is not the same concept with COPY, that's why it is called FLASH.**)

The flash tools depending on different platform are alternatives. I have done this on my Mac OS by using 'dd' command under the terminal. If you are using Windown, the software and steps [here](http://www.ev3dev.org/docs/getting-started/) you can follow. 

When the flashing is finished, simply insert this card to EV3. Switch on your EV3 like usual, EV3Dev os will be booted automaticaly. 

## How to access EV3Dev OS?

Now we have a Linux OS on the EV3, the thing is how can we access it. The answers are simple, you can do it by three different ways, Network, USB-Cable and Bluetooth.

### Network
If you check EV3 carefully, you will find that there are two usb connectors on that, one is conventional port and one is mini port. The difference is, when you connected devices onto conventional port, it's usually considered as a slave as EV3. It's the same concept with the usb port of your computer. For the mini port, it's more used to connect EV3 to a PC. So in this case, EV3 is considered as a slave, like you connected your phone to your PC. 

So in this condition, we consider EV3 as an independent device. Connect a usb WiFi card will give EV3 the ability to access WiFi networks. Then EV3 can be seen as a device in the network. We can use SSH to access it. This is also the way I chose. 

> ### What is SSH?
> SSH stands for Secure Shell, a protocol for operating network services securely over an unsecured network. The best known example application is for remote login to computer systems by its IP address.
> 
> SHH connection can be done in the terminal if you are using a Linux system. If you are using a Windows system, putty is always best choice. Find the tutroial [here](http://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/).

### USB-Cable
Instead of using wireless network, this way could be more useful if you do not have a wireless card or public WiFi has a LogIn page like ISEP's. 

If you choose this way, find the details [here](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/) with all the steps and nice picture illustration.

### Bluetooth

Bluetooth is also an option for connecting EV3, but the configuration is more complicated. So I do not recommend this way. If you want more information, check out [here](http://www.ev3dev.org/docs/tutorials/using-bluetooth-tethering/).

## How to understand the way linux manage hardware?

As I wrote in the previous instruction, writing or reading files is the way linux manage its hardwares. Now I can propose you a basic test by light on/off a LED to let you understand it :)

Debian linux system saves all the interactable hardware class under directory 'sys/class'. So the first ting is to go into this location.

> $ cd /sys/class

You can now list all the contains under this location by

> $ ls -al

All the leds on the EV3 are considered as a device under class LEDs, so we can go into this dir.

> $ cd leds
>
> $ ls -al

We can see there are 4 leds shown whit its property. Each of these name is a directory.

>ev3:left:green:ev3dev
>
>ev3:left:red:ev3dev
>
>ev3:right:green:ev3dev
>
>ev3:right:red:ev3dev

For example we want to test if the left red led works, we can check its dir:

> $ cd ev3:left:red:ev3dev
> 
> $ ls
> 
> $ more brightness

We just checked the brightness value of this led. If the result shows 255, it means this led is on. If the result shows 0, led is off. So to tune this led, we can write either 255 or 0 to switch it ON or OFF. We can use 'echo' command to change the value:

> $ echo 255 > brightness

Now can should see the left red led is ON!

> $ echo 0 > brightness

And this command should turn this led OFF.

Now you are really able to have a perceptual understanding of how linux manage its hardwares. 

## How to make a simple sensor loop?
- [X] 2017.09.25

In this section, we will try to use one sensor and one actuator to make a simple logic loop. The purpose here is to understand how to use Python library and have a global view form software to hardware, they are TOGETHER. 

EV3Dev OS already has the Python libraries for all the LEGO EV3 APIs integrated. So to make sure we always have the latest version of the libraries and system, we can run 'apt-get update' before start programming. This step may take some time, but be patient. (Be sure to use 'sudo' to execute as a super user. Password is the same with login, 'maker')

> $ sudo apt-get update

When you run this command, there are someting shown in the terminal like this:

```
robot@ev3dev:~$ sudo apt-get update
[sudo] password for robot:
Get:1 http://security.debian.org jessie/updates InRelease [63.1 kB]
Hit http://archive.ev3dev.org jessie InRelease
Ign http://httpredir.debian.org jessie InRelease
Hit http://httpredir.debian.org jessie Release.gpg
Hit http://httpredir.debian.org jessie Release
Get:2 http://security.debian.org jessie/updates/main armel Packages [537 kB]
Get:3 http://archive.ev3dev.org jessie/main armel Packages [48.5 kB]
Get:4 http://security.debian.org jessie/updates/contrib armel Packages [994 B]
Get:5 http://security.debian.org jessie/updates/non-free armel Packages [20 B]
Get:6 http://httpredir.debian.org jessie/main armel Packages [8868 kB]
Get:7 http://httpredir.debian.org jessie/contrib armel Packages [42.9 kB]
Get:8 http://httpredir.debian.org jessie/non-free armel Packages [71.1 kB]
Fetched 9631 kB in 1min 38s (97.3 kB/s)
Reading package lists... Done
```

Now we are ready to start coding. 

The sensor I used a ultrasonic and medium motor as actuator. I will write a program which acquires distance as a input and then use this value to regulate the speed of motor. 

```Python 
#!/usr/bin/env python3
#Author: Coor

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

# This is the function I made for remapping values. 
# You can just skip this function and look it later.
def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaledThrust = float(value - minInput) / float(inputSpan)

	return minOutput + (scaledThrust * outputSpan)

# Create ultrasonic sensor entity, 
# 'in1' is the port sensor is connected.

s = ev3.UltrasonicSensor('in1')

# Configure sensor mode
# 'US-DIST-CM' means that Continuous measurement in centimeters.

s.mode = 'US-DIST-CM'

# Create motor entity
# 'outA' is the port Medium motor is connected.

m = ev3.MediumMotor('outA')

# All the configurations are done so far
try:
	# Make a infinite loop
	while True:
		# Measure distance
		distance = s.value()
		# Because the speed range is from 0 - 1500
		# Here convert distance to speed
		# Suppose the valid distance range is from 5cm to 50cm
		if distance < 50:
			distance = 50
		if distance > 500:
			distance = 500

		# Call reMap function
		speed = reMap(distance, 500, 50, 1500, 0)
		# Start the motor to run at the given speed
		m.run_forever(speed_sp = speed)
		
		print('Current speed is %d'%speed)
		print('Current distance is %d'%distance)
#		time.sleep(1)

except KeyboardInterrupt:
	m.stop()

```

Here is another example of using the speaker. Modify the following code, try out the thing you want the robot say.

```Python
#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

ev3.Sound.speak('Welcome Group 5!').wait()
time.sleep(3)
ev3.Sound.speak('How are you?').wait()
``` 

I have already cloned this repository onto EV3 including testing code. These code is in the 'Auto-Pilot-Demo/Test_Program' directory. If you want to modify, you can use whichever editor under linux, nano or vim. To run these program, you can execute it directly. Like this:

> $ ./demo.py

You can also use python3 to run it:

> $ sudo python3 demo.py

For more information about library classes and functions, refer to [here](http://python-ev3dev.readthedocs.io/en/stable/index.html).

## How to write program locally and run promotely?
- [X] 2017.09.26

Using terminal to program on EV3 is always an avaliable way. However, the terminal itself and the editor under linux is not designed for making big programs. You only see several lines without syntax highlighting, this could be the worest programming experience I can image. 

Well, for basic test which only content no more than 10 lines is fine with terminals. But the program we are going to make is not such thing. So write your program locally is a better choice. 

To easy test your program once you are done, we can simply use Git. We have set a repostory on Github already, so you can clone it onto your computer. Write your program, save it to the project directory. Commit and push it onto Github. Finally do the same clone procedure on the EV3. The lastest code will be loaded there, then you can test. With this working way, your code version can be easily tracked as well. 

So here I want to mention 3 basic Git command. 

To clone a repostory onto your computer(For instance our repostory):

> $ git clone https://github.com/CoorFun/Auto-Pilot-Demo.git

When you changed the contents, add them first(Parameter -A stands for add all):

> $ git add -A

Then commit the reasons why you have changed or updated:

(During this procedure, you may be asked to input who you are)

> $ git commit -m "The reasons"

Finally, upload to respostory:

(During this procedure, you may be asked to input your github username and password)

> $ git push

Then you are done! You can use 'pull' request to keep local content same with repostory's. This is also the way to make these updates on EV3 when you update your code:

> $ git pull

## How to study more operations?

The offical EV3dev API document can be found [here](). For each different sensor and actuator, it has a specific class. Find out these class, you will see different class methods and attributes inside. All the usage and function are addressed. 

For example, in the section 'Medium EV3 Motor', we can see how to operate this motor:

![doc1](https://github.com/CoorFun/Auto-Pilot-Demo/raw/master/Tutorial/Pics/doc1.png)

You may ask why there are only a few lines of instruction. That's because 'MediumMotor' is actually the sub-class of 'Motor' class. So let's check out what is under 'Motor' class:

![doc2](https://github.com/CoorFun/Auto-Pilot-Demo/raw/master/Tutorial/Pics/doc2.png)

These are the method you can apply:

![doc3](https://github.com/CoorFun/Auto-Pilot-Demo/raw/master/Tutorial/Pics/doc3.png)

These are the attributes you can set or check:

![doc4](https://github.com/CoorFun/Auto-Pilot-Demo/raw/master/Tutorial/Pics/doc4.png)

The sensors are working in the same way. Try out by yourself :)

# Conclusion(My experience)
