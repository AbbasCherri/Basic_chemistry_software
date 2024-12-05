import customtkinter as ctk
import PIL as pl
# Initialize the app
app = ctk.CTk()
app.title("Periodic Table Explorer")
app.geometry("1200x700")
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
table_frame = ctk.CTkFrame(app, width=1000, height=500)
table_frame.pack(pady=20)

# Create buttons for each element
def show_element_details(element):
    elem_image =ctk.CTkImage(dark_image=pl.Image.open(f"Elem\\{element['name']}.jpg"),size=(200,200))
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
        command=lambda el=element: show_element_details(el),
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

table_frame2 = ctk.CTkFrame(app, width=800, height=100)
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

details_label = ctk.CTkLabel(app, text="Select an element to see details", font=("Arial", 16))
details_label.pack(pady=10)

all_elements = elements + elements2

def get_elem(element_name, elements=all_elements):
    for i in range(len(elements)):
        if element_name in elements[i].values():
            return elements[i]


search_bar = ctk.CTkEntry(app, placeholder_text="Search for element")
search_bar.pack(pady=20, padx=20)
button = ctk.CTkButton(app, text="Submit",command=lambda: show_element_details(get_elem(search_bar.get())))
button.pack(pady=0)


image_label = ctk.CTkLabel(app,text="")
image_label.pack(pady=0)

# Run the app
app.mainloop()