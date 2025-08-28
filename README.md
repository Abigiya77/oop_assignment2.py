# Assignment 1: Object-Oriented Programming in Python 

## Overview
This repository contains solutions for **Assignment 1**, demonstrating core **Object-Oriented Programming (OOP)** concepts in Python, including **classes, inheritance, constructors, methods, and polymorphism**.

---

## Activity 1: Design Your Own Class
- **Objective:** Create a class representing anything you like (here, a Smartphone).  
- **Features Implemented:**
  - Attributes: brand, model, storage, battery, and extra attributes for inherited classes.
  - Methods: `make_call()`, `take_photo()`, `battery_status()`.
  - Inheritance: `GamingPhone` class extends `Smartphone` with `play_game()`.
- **Purpose:** Demonstrates **encapsulation** and **inheritance** with unique object values.

---

## Activity 2: Polymorphism Challenge
- **Objective:** Demonstrate polymorphism with different classes implementing the same action differently.
- **Classes Implemented:**  
  - `Vehicle` (base class)  
  - `Car`, `Plane`, `Boat` (subclasses overriding `move()`)
- **Behavior:** Each subclass defines `move()` differently:
  - `Car.move()` → "Driving on the road 🚗"  
  - `Plane.move()` → "Flying in the sky ✈️"  
  - `Boat.move()` → "Sailing on water 🚤"
- **Purpose:** Shows how **polymorphism** allows objects of different classes to be used interchangeably while maintaining unique behavior.

---

## How to Run
1. Make sure Python is installed on your system.  
2. Clone this repository:  
   ```bash
   git clone <your-github-repo-link>
