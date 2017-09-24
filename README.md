# Auto-Pilot-Demo
This is the project about Auto-Pilot. We are going to build a demo car based on Lego EV3DEV platform. 

# NOTICE
By **5 Oct**, I hope all the team members can really understand how the hardware(ev3dev) works and be able to write a simple program(simple sensor and actuator loop). 

# Introduction
- [X] 2017.09.22

Eventhrough there are some certain reference documentations for the platform EV3dev or Python language, they are always constructed seperately. It means that taking all of those knowledge together for a specific project(Like our project) can be a very difficult thing for a beginner. So to let us better understand how the hardware works, I am going to update some 'Tutorial' here. Follow it and feel free to ask questions.

# What is the LEGO EV3 Controller?
- [X] 2017.09.22

As we all know, Logo EV3 is one of the most powerful hardware controller used to connect those LEGO peripheral electronic devices, which is a thing we can program by its software(Or we can call it IDE) and then download and execute it. Normally whitout any add-on stuffs(Like sd card or usb devices), this controller only works with its own IDE called 'EV3 PROGRAMMER' which is a graphic interface based programming language(like Scrath). GUI programming language usually is designed for kids or young child who are not able to learn coding. Instrad of various key words and syntax, it use some picture(Or we can say it's a Tag) things which can connect with each other following some logical order, just like a puzzle game. And on those pictures, certain feature parameters can be set. When all the tags have been connected, programing is finished. Definitely we have to say this is a very smart and creative way to do programming, but the shortage is it's not flexable and miss the abality to change some more complicate projects. 

# How can LEGO EV3 work with a OS?
- [X] 2017.09.22

Like I mentioned in the previous section, EV3 is not the only controller produced by LEGO. There are indeed some other controllers, for example NXT. But the powerful feature which only appears on EV3 is that it makes possibility to run some other OS except its own! By having an operating system, surely we can do more things. 

There are several different systems which are designed for LEGO controller. Here because of the hardware we already have, we only compare 2 different systems for EV3. They are:

> * [leJOS EV3](http://www.lejos.org/)
> * [EV3Dev](http://www.ev3dev.org/)

leJOS EV3 is actually a Java Virtual Machine(JVM) planted to fit EV3, which has full EV3 API and a java run time system. There is only one thing you have to know about this OS, Java language is the one and the only one language it supports. 

EV3Dev is a Debian Linux-based operating system that runs on several LEGO compatible platforms including the LEGO EV3 and Raspberry Pi-powered BrickPi. It means that when we have the EV3Dev on EV3, the way we use it is more close to the way we operate an RasPi or Beaglebone etc. It can support various different languages including C, Java, Python etc. 

As we know that, the only we can access hardware under linux is via file system. In other word, writting or reading files is the way linux manage its hardwares. So as long as a language can run on Linux OS and has a library to access file system, it can interact with connected hardwares. **This is one of the most important reason why we decide to choose EV3Dev system.**

To complete this project, there will be plenty of calculation and algorithm to use. **So this is another consideration why we choose Python language.** Because it has vast libraries which can help. This is also the benefits which java does not have. 

# Turtrial
- [X] 2017.09.24

## How to install EV3Dev?

To have EV3Dev on your LEGO EV3, the only thing you need is a micro SD card. Download the latest system image file from ev3dev.org. And then you have to find a software which can flash this image file onto your card. (Notice: An image file can be considered as a image of a disk. So when you flash it onto the card, it actually changes the formattiong of the card. **This is not the same concept with COPY, that's why it is called FLASH.**)

The flash tools depending on different platform are alertnative. I have done this on my Mac OS by using 'dd' command under terminal. If you are using Windown, the software and steps ![here](http://www.ev3dev.org/docs/getting-started/) you can follow. 

When the flashing is finished, simplely insert this card to EV3. Switch on your EV3 like usual, EV3Dev os will be booted automaticly. 

## How to access EV3Dev OS?

Now we have a Linux OS on the EV3, the thing is how can we access it. Answers are simple, you can do it by three different ways, Network, USB-Cable and Bluetooth.

### Network
If you check EV3 carefully, you will find that there are two usb connectors on that, one is regular port and one is mini port. The difference is, when you connected devices onto regualr port, it's usually considered as a slave as EV3. It's the same concept with the usb port of your computer. For the mini port, it's more used to connected EV3 to a PC. So in this case, EV3 is considered as a slave, like you connected your phone to your PC. 

So in this condition, we consider EV3 as a indenpent devive. Connecte a usb WiFi card will give EV3 the ability to access WiFi network. Then EV3 can be seen as a device in the network. We can use SSH to access it. This is also the way I chosed. 


`
What is SSH?

SSH stands for Secure Shell, a protocol for operating network services securely over an unsecured network. The best known example application is for remote login to computer systems by users.

`

### USB-Cable
Instead of using wireless network, this way could be more useful if you do not have a wireless card or public WiFi has a LogIn page like ISEP's. 

If you choose this way, find the details ![here](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/) with all the steps and nice picture illustration.

### Bluetooth

## How to make a simple sensor loop?

## How to write program locally and run promotely?

## How to study more operations?

# Conclusion(My experience)
