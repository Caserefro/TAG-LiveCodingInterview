# Coding Challenge 1 - Vehicle Rental System

## Description

A rental company manages different types of vehicles such as cars, trucks, and motorcycles.
Each vehicle type has a unique way of calculating the total rental cost depending on its characteristics.

Your task is to use Object-Oriented Programming (OOP) concepts — particularly Inheritance, Polymorphism, and Encapsulation — to design a program that calculates rental costs for different vehicle types.

## Requirements
Create a base class to represent common properties and behaviors of all vehicles.

**1. Base Class** `Vehicle`

  Attributes:
  - `brand`
  - `model`
  - `rentalRatePerDay`

  Methods:
  - `calculateRentalCost(days)`
  - `getDescription()`

**2. Derived Classes**

   `Car`
  - Attribute: `seats`
  - Formula: `totalCost = rentalRatePerDay * days`
  
  `Truck`
  - Attribute: `cargoWeight` (Tons)
  - Formula: `totalCost = (rentalRatePerDay * days) + (cargoWeight * 50)`
  
  `Motorcycle`
  - Attribute: `helmetIncluded` (bool)
  - Formula:
      ```
      totalCost = rentalRatePerDay * days
      if helmetIncluded:
        totalCost += 10
      ```

## Input
You may assume the following vehicles are created inside `main()`:
| Vehicle Type | Brand  | Model   | Rate/Day | Extra Info            | Days |
| ------------ | ------ | ------- | -------- | --------------------- | ---- |
| Car          | Toyota | Corolla | 40       | seats = 5             | 3    |
| Truck        | Volvo  | FH16    | 80       | cargoWeight = 2       | 2    |
| Motorcycle   | Yamaha | R15     | 30       | helmetIncluded = true | 1    |

## Output
```
Toyota Corolla (Car) - Total Cost: $120
Volvo FH16 (Truck) - Total Cost: $210
Yamaha R15 (Motorcycle) - Total Cost: $40
```

## Constrains
- The `Vehicle` class should be abstract and should not be instantiated directly.
- `Car`, `Truck` and `Motorcycle` must override `calculateRentalCost(days)`.
