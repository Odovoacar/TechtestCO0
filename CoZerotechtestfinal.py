import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import string

     # Define Transport Types and Year
EMISSION_INTENSITIES = {
    'Boat': {'2022': 25, '2023': 23},
    'Airplane': {'2022': 600, '2023': 605},
    'Truck': {'2022': 135, '2023': 130},
    'Train': {'2022': 20, '2023': 20}
}
     # Define Packages
packages = {}

def log_package(date, mode, weight, distance):
    year = date.split('-')[0]
    emission_intensity = EMISSION_INTENSITIES[mode][year]
    emissions = weight * distance * emission_intensity / 1000
    package_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    packages[package_id] = {'date': date, 'mode': mode, 'emissions': emissions}
    return package_id, emissions

def get_package_emissions(package_id):
    if package_id in packages:
        package = packages[package_id]
        return package_id, package['emissions'], package['mode']
    else:
        return None, None, None

def display_all_entries():
    entries_text = ""
    for package_id, package in packages.items():
        entries_text += f"Package ID: {package_id}, Date: {package['date']}, Mode: {package['mode']}\n"
    messagebox.showinfo("All Entries", entries_text)
        # Class Carbon Tracker
class CarbonEmissionTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Carbon Emission Tracker")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Date Entry
        ttk.Label(self, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Mode Dropdown
        ttk.Label(self, text="Mode of Transport:").grid(row=1, column=0, padx=5, pady=5)
        self.mode_var = tk.StringVar(self) 
        self.mode_dropdown = ttk.Combobox(self, textvariable=self.mode_var, values=list(EMISSION_INTENSITIES.keys()))
        self.mode_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Weight Entry
        ttk.Label(self, text="Weight (kg):").grid(row=2, column=0, padx=5, pady=5)
        self.weight_entry = ttk.Entry(self)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        # Distance Entry
        ttk.Label(self, text="Distance (km):").grid(row=3, column=0, padx=5, pady=5)
        self.distance_entry = ttk.Entry(self)
        self.distance_entry.grid(row=3, column=1, padx=5, pady=5)

        # Log Package Button
        self.log_button = ttk.Button(self, text="Log Package", command=self.log_package_gui)
        self.log_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Get Emissions Button
        self.get_emissions_button = ttk.Button(self, text="Get Package Emissions", command=self.get_package_emissions_gui)
        self.get_emissions_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Display All Entries Button
        self.display_entries_button = ttk.Button(self, text="Display All Entries", command=display_all_entries)
        self.display_entries_button.grid(row=6, column=0, columnspan=2, pady=10)
        # Define Package and Errors
    def log_package_gui(self):
        date = self.date_entry.get()
        mode = self.mode_var.get()
        weight = float(self.weight_entry.get())
        distance = float(self.distance_entry.get())

        try:
            package_id, emissions = log_package(date, mode, weight, distance)
            messagebox.showinfo("Package Logged", f"Package ID: {package_id}\nEmissions: {emissions:.2f} kg CO2")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_package_emissions_gui(self):
        package_id = simpledialog.askstring("Input", "Enter Package ID:")
        if package_id:
            id, emissions, mode = get_package_emissions(package_id)
            if id:
                messagebox.showinfo("Package Emissions", f"Package ID: {id}\nMode: {mode}\nEmissions: {emissions:.2f} kg CO2")
            else:
                messagebox.showerror("Error", "Package not found")
           # Start The GUI
if __name__ == "__main__":
    app = CarbonEmissionTracker()
    app.mainloop()
