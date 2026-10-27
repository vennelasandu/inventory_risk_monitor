# inventory_risk_monitor
#Project Description
A Python based application to monitor inventory levels and identify stock risks.

#Features worked in this project
-Show all products with quantity, reorder threshold, and stock status.
-Add a product with an ID, name, quantity, and threshold.
-Update stock by adding a quantity to an existing product.
-Record a sale and reduce stock when enough units are available.
-Rank inventory risk using each product’s quantity-to-threshold ratio.
-Exit the application.

#Risk levels
The ranking compares a product’s quantity with its threshold:
- High risk: quantity is below the threshold.
- Medium risk: quantity equals the threshold.
- Low risk: quantity is above the threshold.

# Project files are
-Algorithm
-README.md
-inventory_risk_monitor.py
# Technologies used 
Python

#Installation 
Python 

#Run the program
python inventory_risk_monitor.py
