#This program calculates the units per pallet, that we produce on our receive dock
#additionally the program also calculates the units lost according to the UPP.

pallet_units_receieved = float(input("Enter the number of pallet units received: "))
pallets = int(input("Enter the number of pallets received: "))
upp = pallet_units_receieved / pallets
print(f"Your UPP is {upp:.1f}")
response = input("Would you like to calculate the units lost due to UPP?(yes,no) ")
if response == "yes":
    upp_planned = float(input("Enter the planned UPP: "))
    units_lost = (upp_planned - upp) * pallets
    print(f"Units lost due to UPP is {units_lost:.1f}")
else:
    quit()