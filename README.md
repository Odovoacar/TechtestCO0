# TechtestCO0
Project for a Techtest
My App for the tech test creates a simple carbon emission tracker application using the Tkinter library for the graphical user interface. Here's a breakdown of its functionality:
1.
Importing Libraries:
2.
import tkinter as tk: Imports the Tkinter library and assigns it the alias tk for easier use.
from tkinter import ttk, messagebox, simpledialog: Imports specific components from Tkinter for creating widgets, displaying messages, and getting user input.
import random: Imports the random module to generate random package IDs.
import string: Imports the string module for generating random strings.
3.
Defining Emission Intensities:
4.
EMISSION_INTENSITIES: A dictionary that stores emission intensities for different modes of transport (Boat, Airplane, Truck, Train) for the years 2022 and 2023.
5.
Defining Packages:
6.
packages: An empty dictionary that will be used to store information about the logged packages.
7.
log_package Function:
8.
Takes the date, mode of transport, weight, and distance as input.
Calculates the emissions based on the emission intensity of the selected mode of transport for the specified year.
Generates a unique 8-character random package ID.
Stores the package details (date, mode, emissions) in the packages dictionary using the package ID as the key.
Returns the package ID and emissions.
9.
get_package_emissions Function:
10.
Takes a package ID as input.
Retrieves the package details from the packages dictionary if the package ID exists.
Returns the package ID, emissions, and mode of transport if the package is found; otherwise, returns None for all values.
11.
display_all_entries Function:
12.
Iterates through the packages dictionary and creates a string containing all the logged package details.
Displays the string in a message box using messagebox.showinfo.
13.
CarbonEmissionTracker Class:
14.
Inherits from the tk.Tk class, which is the base class for Tkinter windows.
Initializes the main window of the application with the title "Carbon Emission Tracker" and sets its geometry.
Calls the create_widgets method to create the GUI elements.
15.
create_widgets Method:
16.
Creates various GUI widgets (labels, entry fields, dropdown, buttons) and arranges them using the grid layout manager.
Creates an entry field for the date, a dropdown for selecting the mode of transport, and entry fields for weight and distance.
Creates buttons for "Log Package", "Get Package Emissions", and "Display All Entries".
Defines the command attribute of each button to call the respective functions when clicked.
17.
log_package_gui Method:
18.
Called when the "Log Package" button is clicked.
Retrieves values from the input fields for date, mode, weight, and distance.
Calls the log_package function to calculate emissions and store package details.
Displays a message box with the package ID and emissions.
Handles ValueError exceptions if the user enters invalid input.
19.
get_package_emissions_gui Method:
20.
Called when the "Get Package Emissions" button is clicked.
Prompts the user to enter a package ID using a simple dialog box.
Calls the get_package_emissions function to retrieve package details.
Displays a message box with the package details if the package is found; otherwise, shows an error message.
1.Starting the GUI:
The if __name__ == "__main__": block ensures that the code inside it is executed only when the script is run directly.
Creates an instance of the CarbonEmissionTracker class, which starts the Tkinter event loop, making the application interactive.
In summary, main.py creates a user-friendly GUI application that allows users to log packages, calculate their carbon emissions, and view all logged entries. It leverages Tkinter for the GUI, calculates emissions based on predefined emission intensities, and manages package information efficiently.
