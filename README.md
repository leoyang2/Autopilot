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

# How can LEGO EV3 work with a Unix OS?
- [X] 2017.09.22

Like I mentioned in the previous section, EV3 is not the only controller produced by LEGO. There are indeed some other controllers, for example NXT. But the powerful feature which only appears on EV3 is that it makes possibility to run some other OS except its own! By having an operating system, surely we can do more things. 

There are several different system is designed for LEGO controller. Here because of the hardware we already have, we only compare 2 different systems for EV3. They are:

* leJOS EV3
* EV3Dev

leJOS EV3 is actually a Java Virtual Machine(JVM) planted to fit EV3, which has full EV3 API and a java run time system. There is only one thing you have to know about this OS, Java language is the one and the only one language it supports. 

EV3Dev is a Linux based system. 


# Turtrial

## Difficulties
