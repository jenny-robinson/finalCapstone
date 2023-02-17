# Shoe Inventory

## Table of contents
1. [Introduction](#introduction) 
1. [Installation](#installation) 
1. [Usage](#usage) 

--------

<a name="introduction"/>

## Introduction
A program that stores informtation for a shoe shop manager to perform stock take. 
The program tracks the  following information for each shoe:
- country of manufacture
- product code
- product name
- product cost
- quantity in stock
- value (cost * stock)

Program allows users to:
- search products by code
- determine product with lowest quantity for restock
- determine product with highest quantity for sale
- calculate total value of each stock item

<a name="installation"/>

## Installation
- clone this repository
- ensure tabulate is installed by entering:
```
pip3 install tabulate
```

<a name="usage"/>

## Usage
Run the program with:
```
python3 inventory.py
```

and select an item from the menu:
```
Select one of the following Options below:
    r - 	Read shoes data
    a - 	Add new shoe data
    v - 	View shoe data
    l - 	Restock the show with the lowest quantity
    s - 	Search for shoe
    c - 	Calculate shoe value
    h - 	Search for shoe with the highest quantity
    e - 	Exit
    : v
Country        Code      Product                Cost    Quantity
-------------  --------  -------------------  ------  ----------
South Africa   SKU44386  Air Max 90             2300          20
China          SKU90000  Jordan 1               3200          50
Vietnam        SKU63221  Blazer                 1700          19
United States  SKU29077  Cortez                  970          60
Russia         SKU89999  Air Force 1            2000          43
Australia      SKU57443  Waffle Racer           2700           4
Canada         SKU68677  Air Max 97             3600          13
Egypt          SKU19888  Dunk SB                1500          26
Britain        SKU76000  Kobe 4                 3400          32
France         SKU84500  Pegasus                2490          28
Zimbabwe       SKU20207  Air Presto             2999           7
Morocco        SKU77744  Challenge Court        1450          11
Israel         SKU29888  Air Zoom Generation    2680           6
Uganda         SKU33000  Flyknit Racer          4900           9
Pakistan       SKU77999  Air Yeezy 2            4389          67
Brazil         SKU44600  Air Jordan 11          3870          24
Columbia       SKU87500  Air Huarache           2683           8
India          SKU38773  Air Max 1              1900          29
Vietnam        SKU95000  Air Mag                2000          14
Israel         SKU79084  Air Foamposite         2430           4
China          SKU93222  Air Stab               1630          10
South Korea    SKU66734  Hyperdunk              1899           7
Australia      SKU71827  Zoom Hyperfuse         1400          15
France         SKU20394  Eric Koston 1          2322          17
```

