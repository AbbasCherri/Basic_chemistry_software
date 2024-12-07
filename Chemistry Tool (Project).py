import customtkinter as ctk
from Blancing_algo import equation_balancer
from MolarMassCalc import molar_mass_calc
from significant_figures import sig_fig
from PIL import Image
from dilution import c1, c2, v1, v2
from concentration_convertor import concen_converter, guardian
from unit_conversion import volume_convert, weight_convert, dist_convert 
from tkinter import messagebox

# Initialize the application window
app = ctk.CTk()
app.title("Chemistry Tools - Beta")    
app.geometry("400x600")

def open_chemical_balancer():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create a label and input field for the chemical balancer
    label = ctk.CTkLabel(app, text="Enter Chemical Equation to Balance:", font=("Arial", 16))
    label.pack(pady=10)

    input_box = ctk.CTkEntry(app, placeholder_text="E.g., H2 + O2 -> H2O", width=300)
    input_box.pack(pady=10)

    result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    # Define the submit action
    def submit_action():
        equation = input_box.get()
        result_label.configure(text=f"Balanced: {equation_balancer(equation)}")  # Display the result

    submit_button = ctk.CTkButton(app, text="Submit", command=submit_action)
    submit_button.pack(pady=10)

    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

def open_molar_mass_calculator():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create labels and input fields
    label = ctk.CTkLabel(app, text="Molar Mass Calculator", font=("Arial", 16))
    label.pack(pady=10)

    mass_label = ctk.CTkLabel(app, text="Enter the mass of the substance (g):", font=("Arial", 14))
    mass_label.pack(pady=5)

    mass_input = ctk.CTkEntry(app, placeholder_text="E.g., 18", width=300)
    mass_input.pack(pady=5)

    element_input = ctk.CTkEntry(app, placeholder_text="E.g., O", width=300)
    element_input.pack(pady=5)

    element_mass_label = ctk.CTkLabel(app, text="Enter the mass of the element (g):", font=("Arial", 14))
    element_mass_label.pack(pady=5)

    result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    # Define the submit action
    def calculate_moles():
        try:
            substance_mass = float(mass_input.get())
            element = element_input.get()
            answer = molar_mass_calc(substance_mass, element)
            result_label.configure(
                text=(
                    f"Molar Mass of {element}: {answer:.3f} g/mol\n"
                )
            )

        except ValueError:
            result_label.configure(text="Invalid input. Please enter numeric values.")

    calculate_button = ctk.CTkButton(app, text="Calculate Moles", command=calculate_moles)
    calculate_button.pack(pady=10)

    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

def open_significant_figure_calculator():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create a label and input field for the significant figure calculator
    label = ctk.CTkLabel(app, text="Significant Figure Calculator", font=("Arial", 16))
    label.pack(pady=10)

    instruction_label = ctk.CTkLabel(app, text="Enter a number to determine its significant figures:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    input_box = ctk.CTkEntry(app, placeholder_text="E.g., 0.00456 or 123.45", width=300)
    input_box.pack(pady=10)

    result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    # Define the submit action
    def calculate_significant_figures():
        try:
            number = input_box.get()

            sig_figs = sig_fig(number)
            result_label.configure(text=f"Significant Figures: {sig_figs}")

        except Exception as e:
            result_label.configure(text="Invalid input. Please try again.")

    submit_button = ctk.CTkButton(app, text="Submit", command=calculate_significant_figures)
    submit_button.pack(pady=10)

    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

def open_dilution_calculator():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create the Dilution Calculator label
    label = ctk.CTkLabel(app, text="Dilution Calculator", font=("Arial", 16))
    label.pack(pady=10)

    # Dropdown to select the variable to calculate
    selection_label = ctk.CTkLabel(app, text="Select Variable to Calculate:", font=("Arial", 14))
    selection_label.pack(pady=10)

    variable_dropdown = ctk.CTkOptionMenu(app, values=("C1", "C2", "V1", "V2"))
    variable_dropdown.set("C1")  # Default selection
    variable_dropdown.pack(pady=10)

    # Frame to dynamically add input fields
    input_frame = ctk.CTkFrame(app)
    input_frame.pack(pady=10)

    # Labels and Entry widgets for dynamic input fields
    input_boxes = {}

    def update_input_fields(selected_variable):
        # Clear previous input fields
        for widget in input_frame.winfo_children():
            widget.destroy()

        # Define other variables to input based on the selected variable
        variables = ["C1", "C2", "V1", "V2"]
        variables.remove(selected_variable)

        # Create input fields for the remaining variables
        for var in variables:
            input_label = ctk.CTkLabel(input_frame, text=f"Enter {var}:", font=("Arial", 14))
            input_label.pack(pady=5)

            input_boxes[var] = ctk.CTkEntry(input_frame, placeholder_text=f"Enter {var} value", width=300)
            input_boxes[var].pack(pady=5)

    # Initial setup of input fields
    update_input_fields(variable_dropdown.get())

    # Update input fields when the dropdown value changes
    variable_dropdown.configure(command=update_input_fields)

    # Result label
    result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    # Submit button to perform the calculation
    def calculate_dilution():
        selected_variable = variable_dropdown.get()
        try:
            # Retrieve inputs and convert to float
            inputs = {var: float(input_boxes[var].get()) for var in input_boxes}

            # Call the corresponding function based on the selected variable
            if selected_variable == "C1":
                result = c1(inputs["V1"], inputs["C2"], inputs["V2"])
            elif selected_variable == "C2":
                result = c2(inputs["C1"], inputs["V1"], inputs["V2"])
            elif selected_variable == "V1":
                result = v1(inputs["C1"], inputs["C2"], inputs["V2"])
            elif selected_variable == "V2":
                result = v2(inputs["C1"], inputs["V1"], inputs["C2"])

            # Display the result
            result_label.configure(text=f"Calculated {selected_variable}: {result:.2f}")

        except ValueError:
            result_label.configure(text="Invalid input. Please enter numeric values.")

    submit_button = ctk.CTkButton(app, text="Submit", command=calculate_dilution)
    submit_button.pack(pady=10)

    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

def open_concentration_converter():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create the Concentration Converter label
    label = ctk.CTkLabel(app, text="Concentration Converter", font=("Arial", 16))
    label.pack(pady=10)

    # Dropdown to select the unit to convert from
    input_unit_label = ctk.CTkLabel(app, text="Select the unit to convert from:", font=("Arial", 14))
    input_unit_label.pack(pady=10)

    input_unit = ctk.StringVar(value="Select Unit")
    input_unit_dropdown = ctk.CTkOptionMenu(
        app, 
        variable=input_unit, 
        values=["Eq", "ppm", "Mass Percent"],
        command=lambda value: update_output_unit_dropdown(value)  # Pass the selected value
    )
    input_unit_dropdown.pack(pady=10)

    # Dropdown to select the unit to convert to
    output_unit_label = ctk.CTkLabel(app, text="Select the unit to convert to:", font=("Arial", 14))
    output_unit_label.pack(pady=10)

    output_unit = ctk.StringVar(value="Select Conversion")
    output_unit_dropdown = ctk.CTkOptionMenu(
        app, 
        variable=output_unit, 
        values=[],
        command=lambda value: show_inputs(value)  # Pass the selected value
    )
    output_unit_dropdown.pack(pady=10)

    # Dictionary for possible output units based on input unit selection
    output_unit_options = {
        "Eq": ["ppm", "Mass Percent", "Volume Percent"],
        "ppm": ["Eq/L", "Mass Percent", "Volume Percent"],
        "Mass Percent": ["Eq/L", "Volume Percent", "ppm"]
    }

    # Function to update the output dropdown options based on input unit
    def update_output_unit_dropdown(input_unit_value):
        output_unit_dropdown.configure(values=output_unit_options.get(input_unit_value, []))
        output_unit.set("Select Conversion")  # Reset output unit to default

    # Dynamic input fields
    input_fields = {}

    def show_inputs(output_unit_value):
        """Display input fields based on the selected conversion."""
        # Clear previous input fields
        for widget in app.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.destroy()

        input_fields.clear()

        # Define the fields for the selected conversion
        fields = []
        if input_unit.get() == "Eq" and output_unit_value in ["ppm", "Mass Percent", "Volume Percent"]:
            fields = [
                ("Valence", "valence"),
                ("Molar Mass (g/mol)", "molar_mass"),
            ]
            if output_unit_value == "ppm" or output_unit_value == "Mass Percent":
                fields.append(("Solution Mass (kg)", "solution_mass"))
            if output_unit_value == "Volume Percent":
                fields.append(("Solution Volume (L)", "solution_volume"))

        elif input_unit.get() == "ppm" and output_unit_value in ["Eq/L", "Mass Percent", "Volume Percent"]:
            fields = [
                ("Solution Volume (L)", "solution_volume"),
            ]
            if output_unit_value == "Eq/L":
                fields.append(("Concentration (mol/L)", "concentration"))
            if output_unit_value == "Mass Percent":
                fields.append(("Molar Mass (g/mol)", "molar_mass"))
            if output_unit_value == "Volume Percent":
                fields.append(("Solution Volume (L)", "solution_volume"))

        elif input_unit.get() == "Mass Percent" and output_unit_value in ["Eq/L", "Volume Percent", "ppm"]:
            fields = [
                ("Solution Mass (kg)", "solution_mass"),
            ]
            if output_unit_value == "Eq/L":
                fields.append(("Concentration (mol/L)", "concentration"))
            if output_unit_value == "Volume Percent":
                fields.append(("Solution Volume (L)", "solution_volume"))
            if output_unit_value == "ppm":
                fields.append(("Molar Mass (g/mol)", "molar_mass"))

        # Create input fields based on selected options
        for field_label, field_key in fields:
            label = ctk.CTkLabel(app, text=field_label, font=("Arial", 14))
            label.pack(pady=5)
            input_box = ctk.CTkEntry(app, placeholder_text=f"Enter {field_label}", width=300)
            input_box.pack(pady=5)
            input_fields[field_key] = input_box

        # Add a submit button to calculate
        submit_button = ctk.CTkButton(app, text="Convert", command=perform_conversion)
        submit_button.pack(pady=10)

        # Global reference for the result label
    

    def perform_conversion():
        result_label = None  # Declare the global variable for result_label

        try:
            # Get the input values
            input_values = {key: float(field.get()) if field.get() != '' else 0 for key, field in input_fields.items()}

            # Determine the selected unit type (1 = Eq, 2 = PPM, 3 = Mass Percent)
            if input_unit.get() == "Eq":
                unit = 1  # Eq
            elif input_unit.get() == "ppm":
                unit = 2  # PPM
            elif input_unit.get() == "Mass Percent":
                unit = 3  # Mass Percent
            else:
                raise ValueError("Invalid unit selected.")

            # Perform the conversion based on selected input and output units
            conversion_results = concen_converter(input_values.get("valence", 1), unit, **input_values)

            # Example of handling results and displaying them
            result_label_text = f"Converted values:\n"
            for key, result in conversion_results.items():
                result_label_text += f"{key}: {result}\n"

            if result_label is None:
                # Create the result label if it doesn't exist
                result_label = ctk.CTkLabel(app, text=result_label_text, font=("Arial", 14))
                result_label.pack(pady=10)
            else:
                # Update the text of the existing label
                result_label.config(text=result_label_text)

        except ValueError as e:
            if result_label is None:
                # Create the error label if it doesn't exist
                result_label = ctk.CTkLabel(app, text=f"Error: {str(e)}", font=("Arial", 14))
                result_label.pack(pady=10)
            else:
                # Update the text of the existing label
                result_label.config(text=f"Error: {str(e)}")


    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

def periodic_table():
    root = ctk.CTk()
    root.title("Periodic Table Explorer")
    root.geometry("1200x700")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Periodic table data
    elements =(
        {"symbol": "H",  "name": "Hydrogen",     "atomic_number": 1,   "group": 1,  "period": 1},
        {"symbol": "He", "name": "Helium",       "atomic_number": 2,   "group": 18, "period": 1},
        {"symbol": "Li", "name": "Lithium",      "atomic_number": 3,   "group": 1,  "period": 2},
        {"symbol": "Be", "name": "Beryllium",    "atomic_number": 4,   "group": 2,  "period": 2},
        {"symbol": "B",  "name": "Boron",        "atomic_number": 5,   "group": 13, "period": 2},
        {"symbol": "C",  "name": "Carbon",       "atomic_number": 6,   "group": 14, "period": 2},
        {"symbol": "N",  "name": "Nitrogen",     "atomic_number": 7,   "group": 15, "period": 2},
        {"symbol": "O",  "name": "Oxygen",       "atomic_number": 8,   "group": 16, "period": 2},
        {"symbol": "F",  "name": "Fluorine",     "atomic_number": 9,   "group": 17, "period": 2},
        {"symbol": "Ne", "name": "Neon",         "atomic_number": 10,  "group": 18, "period": 2},
        {"symbol": "Na", "name": "Sodium",       "atomic_number": 11,  "group": 1,  "period": 3},
        {"symbol": "Mg", "name": "Magnesium",    "atomic_number": 12,  "group": 2,  "period": 3},
        {"symbol": "Al", "name": "Aluminium",    "atomic_number": 13,  "group": 13, "period": 3},
        {"symbol": "Si", "name": "Silicon",      "atomic_number": 14,  "group": 14, "period": 3},
        {"symbol": "P",  "name": "Phosphorus",   "atomic_number": 15,  "group": 15, "period": 3},
        {"symbol": "S",  "name": "Sulfur",       "atomic_number": 16,  "group": 16, "period": 3},
        {"symbol": "Cl", "name": "Chlorine",     "atomic_number": 17,  "group": 17, "period": 3},
        {"symbol": "Ar", "name": "Argon",        "atomic_number": 18,  "group": 18, "period": 3},
        {"symbol": "K",  "name": "Potassium",    "atomic_number": 19,  "group": 1,  "period": 4},
        {"symbol": "Ca", "name": "Calcium",      "atomic_number": 20,  "group": 2,  "period": 4},
        {"symbol": "Sc", "name": "Scandium",     "atomic_number": 21,  "group": 3,  "period": 4},
        {"symbol": "Ti", "name": "Titanium",     "atomic_number": 22,  "group": 4,  "period": 4},
        {"symbol": "V",  "name": "Vanadium",     "atomic_number": 23,  "group": 5,  "period": 4},
        {"symbol": "Cr", "name": "Chromium",     "atomic_number": 24,  "group": 6,  "period": 4},
        {"symbol": "Mn", "name": "Manganese",    "atomic_number": 25,  "group": 7,  "period": 4},
        {"symbol": "Fe", "name": "Iron",         "atomic_number": 26,  "group": 8,  "period": 4},
        {"symbol": "Co", "name": "Cobalt",       "atomic_number": 27,  "group": 9,  "period": 4},
        {"symbol": "Ni", "name": "Nickel",       "atomic_number": 28,  "group": 10, "period": 4},
        {"symbol": "Cu", "name": "Copper",       "atomic_number": 29,  "group": 11, "period": 4},
        {"symbol": "Zn", "name": "Zinc",         "atomic_number": 30,  "group": 12, "period": 4},
        {"symbol": "Ga", "name": "Gallium",      "atomic_number": 31,  "group": 13, "period": 4},
        {"symbol": "Ge", "name": "Germanium",    "atomic_number": 32,  "group": 14, "period": 4},
        {"symbol": "As", "name": "Arsenic",      "atomic_number": 33,  "group": 15, "period": 4},
        {"symbol": "Se", "name": "Selenium",     "atomic_number": 34,  "group": 16, "period": 4},
        {"symbol": "Br", "name": "Bromine",      "atomic_number": 35,  "group": 17, "period": 4},
        {"symbol": "Kr", "name": "Krypton",      "atomic_number": 36,  "group": 18, "period": 4},
        {"symbol": "Rb", "name": "Rubidium",     "atomic_number": 37,  "group": 1,  "period": 5},
        {"symbol": "Sr", "name": "Strontium",    "atomic_number": 38,  "group": 2,  "period": 5},
        {"symbol": "Y",  "name": "Yttrium",      "atomic_number": 39,  "group": 3,  "period": 5},
        {"symbol": "Zr", "name": "Zirconium",    "atomic_number": 40,  "group": 4,  "period": 5},
        {"symbol": "Nb", "name": "Niobium",      "atomic_number": 41,  "group": 5,  "period": 5},
        {"symbol": "Mo", "name": "Molybdenum",   "atomic_number": 42,  "group": 6,  "period": 5},
        {"symbol": "Tc", "name": "Technetium",   "atomic_number": 43,  "group": 7,  "period": 5},
        {"symbol": "Ru", "name": "Ruthenium",    "atomic_number": 44,  "group": 8,  "period": 5},
        {"symbol": "Rh", "name": "Rhodium",      "atomic_number": 45,  "group": 9,  "period": 5},
        {"symbol": "Pd", "name": "Palladium",    "atomic_number": 46,  "group": 10, "period": 5},
        {"symbol": "Ag", "name": "Silver",       "atomic_number": 47,  "group": 11, "period": 5},
        {"symbol": "Cd", "name": "Cadmium",      "atomic_number": 48,  "group": 12, "period": 5},
        {"symbol": "In", "name": "Indium",       "atomic_number": 49,  "group": 13, "period": 5},
        {"symbol": "Sn", "name": "Tin",          "atomic_number": 50,  "group": 14, "period": 5},
        {"symbol": "Sb", "name": "Antimony",     "atomic_number": 51,  "group": 15, "period": 5},
        {"symbol": "Te", "name": "Tellurium",    "atomic_number": 52,  "group": 16, "period": 5},
        {"symbol": "I",  "name": "Iodine",       "atomic_number": 53,  "group": 17, "period": 5},
        {"symbol": "Xe", "name": "Xenon",        "atomic_number": 54,  "group": 18, "period": 5},
        {"symbol": "Cs", "name": "Cesium",       "atomic_number": 55,  "group": 1,  "period": 6},
        {"symbol": "Ba", "name": "Barium",       "atomic_number": 56,  "group": 2,  "period": 6},
        {"symbol": "La", "name": "Lanthanum",    "atomic_number": 57,  "group": 3,  "period": 6},
        {"symbol": "Hf", "name": "Hafnium",      "atomic_number": 72,  "group": 4,  "period": 6},
        {"symbol": "Ta", "name": "Tantalum",     "atomic_number": 73,  "group": 5,  "period": 6},
        {"symbol": "W",  "name": "Tungsten",     "atomic_number": 74,  "group": 6,  "period": 6},
        {"symbol": "Re", "name": "Rhenium",      "atomic_number": 75,  "group": 7,  "period": 6},
        {"symbol": "Os", "name": "Osmium",       "atomic_number": 76,  "group": 8,  "period": 6},
        {"symbol": "Ir", "name": "Iridium",      "atomic_number": 77,  "group": 9,  "period": 6},
        {"symbol": "Pt", "name": "Platinum",     "atomic_number": 78,  "group": 10, "period": 6},
        {"symbol": "Au", "name": "Gold",         "atomic_number": 79,  "group": 11, "period": 6},
        {"symbol": "Hg", "name": "Mercury",      "atomic_number": 80,  "group": 12, "period": 6},
        {"symbol": "Tl", "name": "Thallium",     "atomic_number": 81,  "group": 13, "period": 6},
        {"symbol": "Pb", "name": "Lead",         "atomic_number": 82,  "group": 14, "period": 6},
        {"symbol": "Bi", "name": "Bismuth",      "atomic_number": 83,  "group": 15, "period": 6},
        {"symbol": "Po", "name": "Polonium",     "atomic_number": 84,  "group": 16, "period": 6},
        {"symbol": "At", "name": "Astatine",     "atomic_number": 85,  "group": 17, "period": 6},
        {"symbol": "Rn", "name": "Radon",        "atomic_number": 86,  "group": 18, "period": 6},
        {"symbol": "Fr", "name": "Francium",     "atomic_number": 87,  "group": 1,  "period": 7},
        {"symbol": "Ra", "name": "Radium",       "atomic_number": 88,  "group": 2,  "period": 7},
        {"symbol": "Ac", "name": "Actinium",     "atomic_number": 89,  "group": 3,  "period": 7},
        {"symbol": "Rf", "name": "Rutherfordium", "atomic_number": 104, "group": 4, "period": 7},
        {"symbol": "Db", "name": "Dubnium",      "atomic_number": 105, "group": 5, "period": 7},
        {"symbol": "Sg", "name": "Seaborgium",   "atomic_number": 106, "group": 6, "period": 7},
        {"symbol": "Bh", "name": "Bohrium",      "atomic_number": 107, "group": 7, "period": 7},
        {"symbol": "Hs", "name": "Hassium",      "atomic_number": 108, "group": 8, "period": 7},
        {"symbol": "Mt", "name": "Meitnerium",   "atomic_number": 109, "group": 9, "period": 7},
        {"symbol": "Ds", "name": "Darmstadtium", "atomic_number": 110, "group": 10, "period": 7},
        {"symbol": "Rg", "name": "Roentgenium",  "atomic_number": 111, "group": 11, "period": 7},
        {"symbol": "Cn", "name": "Copernicium",  "atomic_number": 112, "group": 12, "period": 7},
        {"symbol": "Nh", "name": "Nihonium",     "atomic_number": 113, "group": 13, "period": 7},
        {"symbol": "Fl", "name": "Flerovium",    "atomic_number": 114, "group": 14, "period": 7},
        {"symbol": "Mc", "name": "Moscovium",    "atomic_number": 115, "group": 15, "period": 7},
        {"symbol": "Lv", "name": "Livermorium",  "atomic_number": 116, "group": 16, "period": 7},
        {"symbol": "Ts", "name": "Tennessine",   "atomic_number": 117, "group": 17, "period": 7},
        {"symbol": "Og", "name": "Oganesson",    "atomic_number": 118, "group": 18, "period": 7}
    )
    # Create a frame for the periodic table
    table_frame = ctk.CTkFrame(root, width=1000, height=500)
    table_frame.pack(pady=20)

    # Create buttons for each element
    def show_element_details(element):
        elem_image =ctk.CTkImage(dark_image=Image.open(f"lems\\{element['name']}.jpg"),size=(200,200))
        if element['group']!=None:
            details_label.configure(
                text=(
                    f"Name: {element['name']}\n"
                    f"Symbol: {element['symbol']}\n"
                    f"Atomic Number: {element['atomic_number']}\n"
                    f"Group: {element['group']}\n"
                    f"Period: {element['period']}"
                )
            )
        else:
            details_label.configure(
                text=(
                    f"Name: {element['name']}\n"
                    f"Symbol: {element['symbol']}\n"
                    f"Atomic Number: {element['atomic_number']}\n"
                    f"Period: {element['period']}"
                )
            )
        image_label.configure(
            image = elem_image
        )

    for element in elements:
        btn = ctk.CTkButton(
            table_frame,
            text=element["symbol"],
            width=50,
            height=50,
            command=lambda: show_element_details(element),
        )
        btn.grid(row=element["period"], column=element["group"], padx=5, pady=5)
    elements2 =(
        {"symbol": "Ce", "name": "Cerium",         "atomic_number": 58,  "group": None, "column":1, "period": 6},
        {"symbol": "Pr", "name": "Praseodymium",   "atomic_number": 59,  "group": None, "column":2, "period": 6},
        {"symbol": "Nd", "name": "Neodymium",      "atomic_number": 60,  "group": None, "column":3, "period": 6},
        {"symbol": "Pm", "name": "Promethium",     "atomic_number": 61,  "group": None, "column":4, "period": 6},
        {"symbol": "Sm", "name": "Samarium",       "atomic_number": 62,  "group": None, "column":5, "period": 6},
        {"symbol": "Eu", "name": "Europium",       "atomic_number": 63,  "group": None, "column":6, "period": 6},
        {"symbol": "Gd", "name": "Gadolinium",     "atomic_number": 64,  "group": None, "column":7, "period": 6},
        {"symbol": "Tb", "name": "Terbium",        "atomic_number": 65,  "group": None, "column":8, "period": 6},
        {"symbol": "Dy", "name": "Dysprosium",     "atomic_number": 66,  "group": None, "column":9, "period": 6},
        {"symbol": "Ho", "name": "Holmium",        "atomic_number": 67,  "group": None,"column":10, "period": 6},
        {"symbol": "Er", "name": "Erbium",         "atomic_number": 68,  "group": None,"column":11, "period": 6},
        {"symbol": "Tm", "name": "Thulium",        "atomic_number": 69,  "group": None,"column":12, "period": 6},
        {"symbol": "Yb", "name": "Ytterbium",      "atomic_number": 70,  "group": None,"column":13, "period": 6},
        {"symbol": "Lu", "name": "Lutetium",       "atomic_number": 71,  "group": None,"column":14, "period": 6},
        {"symbol": "Th", "name": "Thorium",        "atomic_number": 90,  "group": None, "column":1, "period": 7},
        {"symbol": "Pa", "name": "Protactinium",   "atomic_number": 91,  "group": None, "column":2, "period": 7},
        {"symbol": "U",  "name": "Uranium",        "atomic_number": 92,  "group": None, "column":3, "period": 7},
        {"symbol": "Np", "name": "Neptunium",      "atomic_number": 93,  "group": None, "column":4, "period": 7},
        {"symbol": "Pu", "name": "Plutonium",      "atomic_number": 94,  "group": None, "column":5, "period": 7},
        {"symbol": "Am", "name": "Americium",      "atomic_number": 95,  "group": None, "column":6, "period": 7},
        {"symbol": "Cm", "name": "Curium",         "atomic_number": 96,  "group": None, "column":7, "period": 7},
        {"symbol": "Bk", "name": "Berkelium",      "atomic_number": 97,  "group": None, "column":8, "period": 7},
        {"symbol": "Cf", "name": "Californium",    "atomic_number": 98,  "group": None, "column":9, "period": 7},
        {"symbol": "Es", "name": "Einsteinium",    "atomic_number": 99,  "group": None,"column":10, "period": 7},
        {"symbol": "Fm", "name": "Fermium",        "atomic_number": 100, "group": None,"column":11, "period": 7},
        {"symbol": "Md", "name": "Mendelevium",    "atomic_number": 101, "group": None,"column":12, "period": 7},
        {"symbol": "No", "name": "Nobelium",       "atomic_number": 102, "group": None,"column":13, "period": 7},
        {"symbol": "Lr", "name": "Lawrencium",     "atomic_number": 103, "group": None,"column":14, "period": 7},
        )

    table_frame2 = ctk.CTkFrame(root, width=800, height=100)
    table_frame2.pack(pady=0)

    for elem in elements2:
        column =0
        btn = ctk.CTkButton(
            table_frame2,
            text=elem["symbol"],
            width=50,
            height=50,
            command=lambda el=elem: show_element_details(el),
        )
        btn.grid(row=elem["period"],column=elem["column"], padx=5, pady=5)

    details_label = ctk.CTkLabel(root, text="Select an element to see details", font=("Arial", 16))
    details_label.pack(pady=10)

    all_elements = elements + elements2

    def get_elem(element_name, elements=all_elements):
        for i in range(len(elements)):
            if element_name in elements[i].values():
                return elements[i]


    search_bar = ctk.CTkEntry(root, placeholder_text="Search for element")
    search_bar.pack(pady=20, padx=20)
    button = ctk.CTkButton(root, text="Submit",command=lambda: show_element_details(get_elem(search_bar.get())))
    button.pack(pady=0)


    image_label = ctk.CTkLabel(root,text="")
    image_label.pack(pady=0)

    # Run the app
    root.mainloop()

def open_unit_conversion():
    """
    Opens a unit conversion window with options to convert between Volume, Weight, and Distance.
    Clears the old window and displays the relevant input fields.
    """

    # Clear the previous window content
    for widget in app.winfo_children():
        widget.destroy()

    # Dropdown menu for selecting unit type
    ctk.CTkLabel(app, text="Choose conversion type:").pack(pady=10)
    unit_type_menu = ctk.CTkComboBox(app, values=["Volume", "Weight", "Distance"])
    unit_type_menu.pack(pady=10)
    unit_type_menu.set("Select")

    # Label for displaying messages (errors or results)
    message_label = ctk.CTkLabel(app, text="", text_color="red")
    message_label.pack(pady=10)

    def show_conversion_input():
        """
        Displays the input fields and unit dropdown based on the selected conversion type.
        """

        # Get the selected unit type
        unit_type = unit_type_menu.get()

        if unit_type == "Select":
            message_label.configure(text="Please select a conversion type.", text_color="red")
            return

        # Clear previous widgets
        for widget in app.winfo_children():
            widget.destroy()

        # Input field for the number to convert
        ctk.CTkLabel(app, text=f"Enter the value to convert:").pack(pady=10)
        num_entry = ctk.CTkEntry(app)
        num_entry.pack(pady=10)

        # Dropdown menu for selecting units based on type
        if unit_type == "Volume":
            unit_menu = ctk.CTkComboBox(app, values=["ml", "cl", "dal", "dl", "hl", "kl", "Ml", "Gl"])
        elif unit_type == "Weight":
            unit_menu = ctk.CTkComboBox(app, values=["mg", "cg", "dag", "dg", "hg", "kg", "Mg", "Gg"])
        elif unit_type == "Distance":
            unit_menu = ctk.CTkComboBox(app, values=["mm", "cm", "dm", "dam", "hm", "km", "Mm", "Gm"])

        unit_menu.pack(pady=10)
        unit_menu.set(f"Select {unit_type.lower()} unit")

        # Label for displaying messages (results or errors)
        result_label = ctk.CTkLabel(app, text="", text_color="blue")
        result_label.pack(pady=10)

        # Submit button for processing the input
        def convert_units():
            """
            Converts the input based on the selected unit type and displays the result.
            """
            try:
                # Get user inputs
                num = float(num_entry.get())
                unit = unit_menu.get()

                # Perform the conversion (use placeholder functions as required)
                if unit_type == "Volume":
                    result = volume_convert(num, unit)
                elif unit_type == "Weight":
                    result = weight_convert(num, unit)
                elif unit_type == "Distance":
                    result = dist_convert(num, unit)
                else:
                    result = "Invalid conversion type."

                # Display the result
                result_label.configure(text=f"{num} {unit} is {result}", text_color="blue")

            except ValueError:
                result_label.configure(text="Please enter a valid number for conversion.", text_color="red")

        ctk.CTkButton(app, text="Submit", command=convert_units).pack(pady=20)

        # Back button to return to the main menu
        ctk.CTkButton(app, text="Back", command=main_menu).pack(pady=10)

    # Button to proceed to input fields after selecting the conversion type
    ctk.CTkButton(app, text="Next", command=show_conversion_input).pack(pady=20)

    # Back button to return to the main menu
    ctk.CTkButton(app, text="Back", command=main_menu).pack(pady=10)

def smooth_transition(to_function):
    """Smoothly transitions between windows with fade-out and fade-in."""
    def fade_out(alpha=1.0):
        if alpha > 0:
            app.attributes("-alpha", alpha)
            app.after(10, lambda: fade_out(alpha - 0.5))  # Decrease alpha gradually
        else:
            to_function()  # Call the target function after fade-out
            fade_in()  # Start fade-in

    def fade_in(alpha=0.0):
        if alpha < 1:
            app.attributes("-alpha", alpha)
            app.after(10, lambda: fade_in(alpha + 0.06))  # Increase alpha gradually

    fade_out()  # Start fade-out

def main_menu():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create and place the buttons
    buttons = (
        ("Chemical Equation Balancer", lambda: smooth_transition(open_chemical_balancer)),
        ("Molar Mass Calculator", lambda: smooth_transition(open_molar_mass_calculator)),
        ("Significant Figure Calculator", lambda: smooth_transition(open_significant_figure_calculator)),
        ("Dilution Calculator", lambda: smooth_transition(open_dilution_calculator)),  
        ("Unit Conversion Tool", lambda: open_unit_conversion()),
        ("Concentration Converter", lambda: smooth_transition(open_concentration_converter)),
        ("Interactive Periodic Table", lambda: periodic_table()),
    )

    for name, action in buttons:
        button = ctk.CTkButton(
            master=app,
            text=name,
            command=action
        )
        button.pack(pady=10)

    # Load the settings icon
    settings_icon = ctk.CTkImage(
        light_image=Image.open("settings_icon.png"),  # Replace with your light mode icon path
        dark_image=Image.open("settings_icon_dark.png"),  # Replace with your dark mode icon path
        size=(24, 24)  # Adjust size as needed
    )

    # Add Settings button in the bottom right with an icon
    settings_button = ctk.CTkButton(
        master=app,
        text="",  # Remove text
        image=settings_icon,
        command=lambda: smooth_transition(open_settings_menu),
        width=40,
        height=40
    )
    settings_button.place(relx=0.95, rely=0.95, anchor="se")  # Bottom-right corner

def open_settings_menu():
    # Clear the current window
    for widget in app.winfo_children():
        widget.destroy()

    # Create the Settings menu
    label = ctk.CTkLabel(app, text="Settings Menu", font=("Arial", 16))
    label.pack(pady=10)

    # Theme Dropdown
    theme_label = ctk.CTkLabel(app, text="Select Theme:", font=("Arial", 14))
    theme_label.pack(pady=10)

    theme_dropdown = ctk.CTkOptionMenu(
        app,
        values=("System", "Light", "Dark"),
        command=lambda theme: ctk.set_appearance_mode(theme.lower())
    )
    theme_dropdown.set(ctk.get_appearance_mode().capitalize())  # Set initial value
    theme_dropdown.pack(pady=10)

    # Accent Color Dropdown
    color_label = ctk.CTkLabel(app, text="Select Accent Color:", font=("Arial", 14))
    color_label.pack(pady=10)

    # Predefined colors supported by customtkinter
    predefined_colors = ("blue", "green")

    color_dropdown = ctk.CTkOptionMenu(
        app,
        values=predefined_colors,
        command=lambda color: set_accent_color(color)
    )
    color_dropdown.set("blue")  # Default accent color
    color_dropdown.pack(pady=10)

    # Back button to return to the main menu
    back_button = ctk.CTkButton(app, text="Back", command=lambda: smooth_transition(main_menu))
    back_button.pack(pady=20)

# Helper function to set accent colors
def set_accent_color(color):
    try:
        # Dynamically reload the default color theme
        ctk.set_default_color_theme(color)
    except Exception as e:
        print(f"Error setting color theme: {e}")


# Start with the main menu
main_menu()

# Run the application
app.mainloop()
