import re
import tkinter as tk
from tkinter import Menu, simpledialog

#----Main----
#Main
def main_Elementor_Element_Electronic_Configuration(event=None):
    entry_input=simpledialog.askstring("EleMentor", "Enter the Atomic Number or Name of the Element:").strip()
    if entry_input == "":
        CLI_print("Enter Atomic number/Name of the Element/Abbreviation")
        return
    user_input(entry_input)
    
#----GUI SETUP----
root=tk.Tk()
root.title("EleMentor")

#Frame
frame=tk.Frame(root, bg="#343541")
frame.pack(fill=tk.BOTH, expand=True)
#Output
output=tk.Text(frame, height=20, width=60, bg="#343541", fg="white", font=("Consolas", 12), bd=0, highlightthickness=0)
output.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Menu
menu_bar=Menu(root)
#Element Namer
menu_bar.add_command(label="Electronic Configuration", command=main_Elementor_Element_Electronic_Configuration)

root.config(menu=menu_bar)

#----Text Colors----
output.tag_configure("orange", foreground="#FFBF00")
output.tag_configure("blue", foreground="#00BFFF")
output.tag_configure("default", foreground="white")

superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def CLI_print(msg, tag="default"):
    output.insert(tk.END, str(msg) + '\n', tag)
    output.see(tk.END)



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

#----Elements with exceptions in electronic configuartion--

elements_exception={
    24: {"name": "Chromium", "abb": "Cr", "char": "metal"},
    29: {"name": "Copper", "abb": "Cu", "char": "metal"},
    41: {"name": "Niobium", "abb": "Nb", "char": "metal"},
    42: {"name": "Molybdenum", "abb": "Mo", "char": "metal"},
    44: {"name": "Ruthenium", "abb": "Ru", "char": "metal"},
    45: {"name": "Rhodium", "abb": "Rh", "char": "metal"},
    46: {"name": "Palladium", "abb": "Pd", "char": "metal"},
    47: {"name": "Silver", "abb": "Ag", "char": "metal"},
    57: {"name": "Lanthanum", "abb": "La", "char": "metal"},
    58: {"name": "Cerium", "abb": "Ce", "char": "metal"},
    64: {"name": "Gadolinium", "abb": "Gd", "char": "metal"},
    78: {"name": "Platinum", "abb": "Pt", "char": "metal"},
    79: {"name": "Gold", "abb": "Au", "char": "metal"},
    89: {"name": "Actinium", "abb": "Ac", "char": "metal"}
}

def user_input(entry_input):
    new_user_input=entry_input.strip().replace(" ", "")
    
    if new_user_input.isdigit():
        atomic_number=int(new_user_input)
        if atomic_number<=118 and atomic_number>0:
            elements=elements_under_119[atomic_number]
            ename=elements["name"]
            eabb=elements["abb"]
            char=elements["char"]
            electrons=atomic_number
        elif atomic_number>118:
            CLI_print("Enter atomic number less than 119 for Electronic Configuration:")
            return
        else:
            CLI_print(f"An element with atomic number={new_user_input} does not exist")
            return
    elif not new_user_input.isdigit() and not new_user_input=="":
        element_string=new_user_input.strip().replace(" ", "")
        element_name=element_string.capitalize()
        found=False
        
        for atomic_number, data in elements_under_119.items():
            if element_name==data["name"]:
                electrons=int(atomic_number)
                elements=elements_under_119[electrons]
                char=elements["char"]
                ename=elements["name"]
                eabb=elements["abb"]
                found=True
                break
            elif element_name==data["abb"]:
                electrons=int(atomic_number)
                elements=elements_under_119[electrons]
                char=elements["char"]
                ename=elements["name"]
                eabb=elements["abb"]
                found=True
                break
        if not found:
            CLI_print("Enter a valid name of the element or it's abbrevation")
            
    #----Orbitals----
    subshells= [
        "1s", "2s", "2p", "3s", "3p", "4s",
        "3d", "4p", "5s", "4d", "5p", "6s",
        "4f", "5d", "6p", "7s", "5f", "6d", "7p"
    ]

    #----Capacities of Orbitals----
    capacities={
        "s": 2,
        "p": 6,
        "d": 10,
        "f": 14
    }

    if electrons not in elements_exception:
        configuration=[]

        for orbital in subshells:
            shell= orbital[:-1]
            n= orbital[-1]
            cap= capacities[n]

            if electrons<=0:
                break
        
            electrons_in_this_orbital = min(electrons, cap)
            superscript_electrons = str(electrons_in_this_orbital).translate(superscript_map)
            configuration.append(f"{orbital}{superscript_electrons}")
            electrons -= electrons_in_this_orbital

            if char == "nonmetal":
                CLI_print(f"Electronic Configuration of {ename}({eabb}) is: {' '.join(configuration)}", tag="orange")
            elif char == "nonmetalnoblegas":
                CLI_print(f"Electronic Configuration of {ename}({eabb}) is: {' '.join(configuration)} - Stable Configuration", tag="orange")
            elif char == "metalloid":
                CLI_print(f"Electronic Configuration of {ename}({eabb}) is: {' '.join(configuration)}", tag="blue")
            else:
                CLI_print(f"Electronic Configuration of {ename}({eabb}) is: {' '.join(configuration)}")
    
    else:
        elements=elements_exception[electrons]
        ename, eabb = elements["name"], elements["abb"]
        
        if electrons==24:
            configuration="1s2 2s2 2p6 3s2 3p6 4s1 3d5"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==29:
            configuration="1s2 2s2 2p6 3s2 3p6 4s1 3d10"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==41:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d4 5s1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==42:
            configuration="1s1 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d5 5s1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==44:
            configuration="1s1 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d7 5s1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==45:
            configuration="1s1 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d8 5s1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==46:
            configuration="1s1 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==47:
            configuration="1s1 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10 5s1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==57:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==58:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==64:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==78:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==79:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")
        elif electrons==89:
            configuration="1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1"
            E_configuration = re.sub(r'([spdf])(\d)', lambda m: m.group(1) + m.group(2).translate(superscript_map), configuration)
            CLI_print(f"Electronic Configuration of {ename}({eabb})* is:{E_configuration}")


root.mainloop()
