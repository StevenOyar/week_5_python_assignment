# week_5_python_assignment


## 📱 Assignment 1: Object-Oriented Programming in Python

This project demonstrates the use of **OOP concepts** in Python, including **Inheritance, Encapsulation, and Polymorphism**.  
The program models a generic `Device` and a specialized `Smartphone` that extends its behavior.

## 📌 Features
- **Inheritance**:  
  `Smartphone` inherits common attributes and methods (`brand`, `model`, `power_on`, `power_off`) from `Device`.

- **Encapsulation**:  
  The `Smartphone` class uses a private attribute `__storage_space` with a getter method to protect data.  

- **Polymorphism**:  
  The `Smartphone` overrides the `power_on()` method from `Device` with a custom startup message.

- **App Management**:  
  Install and delete apps, with automatic updates to storage space.

## 🖥️ Example Output
Oppo A74 Powering on...
Please enter your password:_____

My phone
Oppo A74 is turning on.....Welcome to OS

Storage before app installation: 128GB
Installed WhatsApp successfully. Storage left: 126GB.

Installed Telegram successfully. Storage left: 101GB.

Successfully deleted Safaricom app.
Freed up space is 20GB.
Storage available: 121GB



# Polymorphism Challenge in acitivity assignment.py

This project demonstrates **polymorphism** in Python using a `Vehicle` base class and several subclasses (`Car`, `Plane`, `Boat`, `Bike`).  
Each subclass overrides the `move()` method to show different behaviors, while sharing the same method name.

## 📌 How It Works
- `Vehicle` defines a default `move()` method.
- Subclasses (`Car`, `Plane`, `Boat`, `Bike`) each implement their own version of `move()`.
- When called, the same method name produces **different outputs** depending on the object.

## 🖥️ Example Output
Each vehicle moves in its own unique way:
🚗 Driving on the road__...
✈️ Flying in the sky...
🚤 Sailing on the water...
🚴 Pedaling on the path...