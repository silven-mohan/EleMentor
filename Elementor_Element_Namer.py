import tkinter as tk
from tkinter import Menu
#----Main----
#Main
def main_Elementor_Element_Namer(event=None):
    atomic_number=user_input()
    element_namer(atomic_number)
    entry.delete(0, tk.END)

#----GUI SETUP----
root=tk.Tk()
root.title("EleMentor")

#Frame
frame=tk.Frame(root, bg="#343541")
frame.pack(fill=tk.BOTH, expand=True)
#Output
output=tk.Text(frame, height=20, width=60, bg="#343541", fg="white", font=("Consolas", 12), bd=0, highlightthickness=0)
output.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#Input
entry=tk.Entry(frame, bg="#444654", fg="white", font=("Consolas", 12))
entry.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
entry.focus_set()
#Menu
menu_bar=Menu(root)
#Element Namer
menu_bar.add_command(label="Element Name", command=main_Elementor_Element_Namer)

root.config(menu=menu_bar)

#----Text Colors----
output.tag_configure("orange", foreground="#FFBF00")
output.tag_configure("blue", foreground="#00BFFF")
output.tag_configure("default", foreground="white")

def CLI_print(msg, tag="default"):
    output.insert(tk.END, str(msg) + '\n', tag)
    output.see(tk.END)


#----Dictionaries----

#----Elements Over 118----
elements_over_118={
    0:{"name":"nil", "abb":"n"},
    1:{"name":"un", "abb":"u"},
    2:{"name":"bi", "abb":"b"},
    3:{"name":"tri", "abb":"t"},
    4:{"name":"quad", "abb":"q"},
    5:{"name":"pent", "abb":"p"},
    6:{"name":"hex", "abb":"h"},
    7:{"name":"sept", "abb":"s"},
    8:{"name":"oct", "abb":"o"},
    9:{"name":"enn", "abb":"e"}
}

#----Elements Under 118----
elements_under_119={
    1: {"name": "Hydrogen", "abb": "H", "char": "nonmetal"},
    2: {"name": "Helium", "abb": "He", "char": "nonmetalnoblegas"},
    3: {"name": "Lithium", "abb": "Li", "char": "metal"},
    4: {"name": "Beryllium", "abb": "Be", "char": "metal"},
    5: {"name": "Boron", "abb": "B", "char": "metalloid"},
    6: {"name": "Carbon", "abb": "C", "char": "nonmetal"},
    7: {"name": "Nitrogen", "abb": "N", "char": "nonmetal"},
    8: {"name": "Oxygen", "abb": "O", "char": "nonmetal"},
    9: {"name": "Fluorine", "abb": "F", "char": "nonmetal"},
    10: {"name": "Neon", "abb": "Ne", "char": "nonmetalnoblegas"},
    11: {"name": "Sodium", "abb": "Na", "char": "metal"},
    12: {"name": "Magnesium", "abb": "Mg", "char": "metal"},
    13: {"name": "Aluminum", "abb": "Al", "char": "metal"},
    14: {"name": "Silicon", "abb": "Si", "char": "metalloid"},
    15: {"name": "Phosphorus", "abb": "P", "char": "nonmetal"},
    16: {"name": "Sulphur", "abb": "S", "char": "nonmetal"},
    17: {"name": "Chlorine", "abb": "Cl", "char": "nonmetal"},
    18: {"name": "Argon", "abb": "Ar", "char": "nonmetalnoblegas"},
    19: {"name": "Potassium", "abb": "K", "char": "metal"},
    20: {"name": "Calcium", "abb": "Ca", "char": "metal"},
    21: {"name": "Scandium", "abb": "Sc", "char": "metal"},
    22: {"name": "Titanium", "abb": "Ti", "char": "metal"},
    23: {"name": "Vanadium", "abb": "V", "char": "metal"},
    24: {"name": "Chromium", "abb": "Cr", "char": "metal"},
    25: {"name": "Manganese", "abb": "Mn", "char": "metal"},
    26: {"name": "Iron", "abb": "Fe", "char": "metal"},
    27: {"name": "Cobalt", "abb": "Co", "char": "metal"},
    28: {"name": "Nickel", "abb": "Ni", "char": "metal"},
    29: {"name": "Copper", "abb": "Cu", "char": "metal"},
    30: {"name": "Zinc", "abb": "Zn", "char": "metal"},
    31: {"name": "Gallium", "abb": "Ga", "char": "metal"},
    32: {"name": "Germanium", "abb": "Ge", "char": "metalloid"},
    33: {"name": "Arsenic", "abb": "As", "char": "metalloid"},
    34: {"name": "Selenium", "abb": "Se", "char": "nonmetal"},
    35: {"name": "Bromine", "abb": "Br", "char": "nonmetal"},
    36: {"name": "Krypton", "abb": "Kr", "char": "nonmetalnoblegas"},
    37: {"name": "Rubidium", "abb": "Rb", "char": "metal"},
    38: {"name": "Strontium", "abb": "Sr", "char": "metal"},
    39: {"name": "Yttrium", "abb": "Y", "char": "metal"},
    40: {"name": "Zirconium", "abb": "Zr", "char": "metal"},
    41: {"name": "Niobium", "abb": "Nb", "char": "metal"},
    42: {"name": "Molybdenum", "abb": "Mo", "char": "metal"},
    43: {"name": "Technetium", "abb": "Tc", "char": "metal"},
    44: {"name": "Ruthenium", "abb": "Ru", "char": "metal"},
    45: {"name": "Rhodium", "abb": "Rh", "char": "metal"},
    46: {"name": "Palladium", "abb": "Pd", "char": "metal"},
    47: {"name": "Silver", "abb": "Ag", "char": "metal"},
    48: {"name": "Cadmium", "abb": "Cd", "char": "metal"},
    49: {"name": "Indium", "abb": "In", "char": "metal"},
    50: {"name": "Tin", "abb": "Sn", "char": "metal"},
    51: {"name": "Antimony", "abb": "Sb", "char": "metalloid"},
    52: {"name": "Tellurium", "abb": "Te", "char": "metalloid"},
    53: {"name": "Iodine", "abb": "I", "char": "nonmetal"},
    54: {"name": "Xenon", "abb": "Xe", "char": "nonmetalnoblegas"},
    55: {"name": "Caesium", "abb": "Cs", "char": "metal"},
    56: {"name": "Barium", "abb": "Ba", "char": "metal"},
    57: {"name": "Lanthanum", "abb": "La", "char": "metal"},
    58: {"name": "Cerium", "abb": "Ce", "char": "metal"},
    59: {"name": "Praseodymium", "abb": "Pr", "char": "metal"},
    60: {"name": "Neodymium", "abb": "Nd", "char": "metal"},
    61: {"name": "Promethium", "abb": "Pm", "char": "metal"},
    62: {"name": "Samarium", "abb": "Sm", "char": "metal"},
    63: {"name": "Europium", "abb": "Eu", "char": "metal"},
    64: {"name": "Gadolinium", "abb": "Gd", "char": "metal"},
    65: {"name": "Terbium", "abb": "Tb", "char": "metal"},
    66: {"name": "Dysprosium", "abb": "Dy", "char": "metal"},
    67: {"name": "Holmium", "abb": "Ho", "char": "metal"},
    68: {"name": "Erbium", "abb": "Er", "char": "metal"},
    69: {"name": "Thulium", "abb": "Tm", "char": "metal"},
    70: {"name": "Ytterbium", "abb": "Yb", "char": "metal"},
    71: {"name": "Lutetium", "abb": "Lu", "char": "metal"},
    72: {"name": "Hafnium", "abb": "Hf", "char": "metal"},
    73: {"name": "Tantalum", "abb": "Ta", "char": "metal"},
    74: {"name": "Tungsten", "abb": "W", "char": "metal"},
    75: {"name": "Rhenium", "abb": "Re", "char": "metal"},
    76: {"name": "Osmium", "abb": "Os", "char": "metal"},
    77: {"name": "Iridium", "abb": "Ir", "char": "metal"},
    78: {"name": "Platinum", "abb": "Pt", "char": "metal"},
    79: {"name": "Gold", "abb": "Au", "char": "metal"},
    80: {"name": "Mercury", "abb": "Hg", "char": "metal"},
    81: {"name": "Thallium", "abb": "Tl", "char": "metal"},
    82: {"name": "Lead", "abb": "Pb", "char": "metal"},
    83: {"name": "Bismuth", "abb": "Bi", "char": "metal"},
    84: {"name": "Polonium", "abb": "Po", "char": "metal"},
    85: {"name": "Astatine", "abb": "At", "char": "metal"},
    86: {"name": "Radon", "abb": "Rn", "char": "nonmetalnoblegas"},
    87: {"name": "Francium", "abb": "Fr", "char": "metal"},
    88: {"name": "Radium", "abb": "Ra", "char": "metal"},
    89: {"name": "Actinium", "abb": "Ac", "char": "metal"},
    90: {"name": "Thorium", "abb": "Th", "char": "metal"},
    91: {"name": "Protactinium", "abb": "Pa", "char": "metal"},
    92: {"name": "Uranium", "abb": "U", "char": "metal"},
    93: {"name": "Neptunium", "abb": "Np", "char": "metal"},
    94: {"name": "Plutonium", "abb": "Pu", "char": "metal"},
    95: {"name": "Americium", "abb": "Am", "char": "metal"},
    96: {"name": "Curium", "abb": "Cm", "char": "metal"},
    97: {"name": "Berkelium", "abb": "Bk", "char": "metal"},
    98: {"name": "Californium", "abb": "Cf", "char": "metal"},
    99: {"name": "Einsteinium", "abb": "Es", "char": "metal"},
    100: {"name": "Fermium", "abb": "Fm", "char": "metal"},
    101: {"name": "Mendelevium", "abb": "Md", "char": "metal"},
    102: {"name": "Nobelium", "abb": "No", "char": "metal"},
    103: {"name": "Lawrencium", "abb": "Lr", "char": "metal"},
    104: {"name": "Rutherfordium", "abb": "Rf", "char": "metal"},
    105: {"name": "Dubnium", "abb": "Db", "char": "metal"},
    106: {"name": "Seaborgium", "abb": "Sg", "char": "metal"},
    107: {"name": "Bohrium", "abb": "Bh", "char": "metal"},
    108: {"name": "Hassium", "abb": "Hs", "char": "metal"},
    109: {"name": "Meitnerium", "abb": "Mt", "char": "metal"},
    110: {"name": "Darmstadtium", "abb": "Ds", "char": "metal"},
    111: {"name": "Roentgenium", "abb": "Rg", "char": "metal"},
    112: {"name": "Copernicium", "abb": "Cn", "char": "metal"},
    113: {"name": "Nihonium", "abb": "Nh", "char": "metal"},
    114: {"name": "Flerovium", "abb": "Fl", "char": "metal"},
    115: {"name": "Moscovium", "abb": "Mc", "char": "metal"},
    116: {"name": "Livermorium", "abb": "Lv", "char": "metal"},
    117: {"name": "Tennessine", "abb": "Ts", "char": "nonmetal"},
    118: {"name": "Oganesson", "abb": "Og", "char": "nonmetalnoblegas"}
}

#User Input
def user_input():
    CLI_print("Enter atomic number:")
    ask_atomic_number=entry.get().strip()

    if ask_atomic_number is None:
        CLI_print("Enter a number and continue")
        return None
    atomic_number=ask_atomic_number.strip().replace(" ", "")

    if not atomic_number.isdigit():
        CLI_print("Enter a number only")
        return None
    else:
        return int(atomic_number)

#Element Naming
def element_namer(atomic_number):
    
    #Elements under 118
    if 1<=atomic_number<=118:
        element=elements_under_119[atomic_number]
        name, abb, char=element["name"], element["abb"], element["char"]
        suffix=""

        if char=="nonmetal":
            element_name=f"Element Name: {name}({abb})"
            CLI_print(element_name, tag="orange")
        elif char=="nonmetalnoblegas":
            suffix="Nobel Gas"
            element_name=f"Element Name: {name}({abb})-{suffix}"
            CLI_print(element_name, tag="orange")
        elif atomic_number==43 or atomic_number==61 or 84<=atomic_number<=118:
            suffix="☢Radioactive"
            element_name=f"Element Name: {name}({abb})-{suffix}"
            CLI_print(element_name,tag="default")
        elif char=="metalloid":
            element_name=f"Element Name: {name}({abb})"
            CLI_print(element_name,tag="blue")
        else:
            element_name=f"Element Name: {name}({abb})"
            CLI_print(element_name, tag="default")
            
    #Elements over 118
    elif atomic_number>=119 and atomic_number<1000:
        a,b,c=map(int, str(atomic_number))
        prefix, root, suffix=elements_over_118[a]["name"], elements_over_118[b]["name"], elements_over_118[c]["name"]    
        abb_a, abb_b, abb_c=elements_over_118[a]["abb"], elements_over_118[b]["abb"], elements_over_118[c]["abb"]

        name_part=f"{prefix}{root}{suffix}ium"
        name=name_part.capitalize()

        abb_part=f"{abb_a}{abb_b}{abb_c}"
        abb=abb_part.capitalize()

        element_name=f"Element Name: {name}({abb})"
        CLI_print(element_name, tag="default")
    else:
        CLI_print("Enter a number less than 1000")

entry.bind("<Return>", main_Elementor_Element_Namer)


root.mainloop()
