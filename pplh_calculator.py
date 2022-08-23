#Simple program that calculates pallets per labor hour (PPLH) and the units lost due to PPLH for 
#bridging purposes.



#Takes in the number of hours in receive dock
receive_dock_hours = float(input("Enter receive dock hours: "))
#Takes in the number of hours in pallet receive
pallet_receive_hours = float(input("Enter pallet receive hours: "))
#Takes in the current number of pallets produced
pallets = float(input("Enter number of pallets produced: "))
#Takes in the number of pallet units received
pallet_units_received = float(input("Enter the number of pallet units received: "))
#Calculates the current PPLH
pplh = pallets / (receive_dock_hours + pallet_receive_hours)
#Calculates the current UPP
upp = pallet_units_received / pallets
#This is the desired target pplh
desired_pplh = float(5.5)
#prints the PPLH
print(f"Your PPLH is: {pplh:.1f}")
#Asks the user to input whether they would like to calculate units lost or not
response = input("Would you like to calculate the units lost due to PPLH?(yes/no) ")
#If yes is selected units lost is then calculated otherwise the program exits
if response == "yes":
    pallets_lost = (desired_pplh - pplh) * (receive_dock_hours + pallet_receive_hours)  
    units_lost = pallets_lost * upp
    print(f"Units lost: {units_lost:,.2f}")
else:
    quit()

