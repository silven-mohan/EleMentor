import re
import tkinter as tk
from tkinter import Menu, simpledialog

#----Main----
#Main
def main_Elementor_Position_of_element(event=None):
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
menu_bar.add_command(label="Position of Element", command=main_Elementor_Position_of_element)

root.config(menu=menu_bar)

#----Text Colors----
output.tag_configure("orange", foreground="#FFBF00")
output.tag_configure("blue", foreground="#00BFFF")
output.tag_configure("default", foreground="white")

def CLI_print(msg, tag="default"):
    output.insert(tk.END, str(msg) + '\n', tag)
    output.see(tk.END)



#----Elements Under 119----
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
exception_configurations = {
    24: "1s2 2s2 2p6 3s2 3p6 4s1 3d5",
    29: "1s2 2s2 2p6 3s2 3p6 4s1 3d10",
    41: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4",
    42: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5",
    44: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7",
    45: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8",
    46: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10",
    47: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10",
    57: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1",
    58: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f1",
    64: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1",
    78: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9",
    79: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10",
    89: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 6p6 7s2 6d1",
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
        E_configuration=[]
        
        for orbital in subshells:
            shell= orbital[:-1]
            n= orbital[-1]
            cap= capacities[n]

            if electrons<=0:
                break
        
            electrons_in_this_orbital = min(electrons, cap)
            E_configuration.append(f"{orbital}{electrons_in_this_orbital}")
            electrons -= electrons_in_this_orbital

        configuration=' '.join(E_configuration)
        shells = [int(re.match(r'(\d+)', part).group(1)) for part in configuration.split() if re.match(r'(\d+)', part)]
        period = max(shells) if shells else 1
        
    
    else:
        elements=elements_exception[electrons]
        ename, eabb = elements["name"], elements["abb"]
        
        configuration = exception_configurations.get(electrons, "")
        shells = [int(re.match(r'(\d+)', part).group(1)) for part in configuration.split() if re.match(r'(\d+)', part)]
        period = max(shells) if shells else 1
        
        
    #Block Type
    if 21<=atomic_number<=30 or 39<=atomic_number<=48 or 72<=atomic_number<=80 or 104<=atomic_number<=112 or atomic_number==57 or atomic_number==89:
        block_type="d"
    elif 58<=atomic_number<=71 or 90<=atomic_number<=103:
        block_type="f"
    elif 5<=atomic_number<=10 or 13<=atomic_number<=18 or 31<=atomic_number<=36 or 49<=atomic_number<=54 or 81<=atomic_number<=86 or 113<=atomic_number<=118 or atomic_number==2:
        block_type="p"
    else:
        block_type="s"

    #Period Number
    if period==1:
        np=f"{period}st"
    elif period==2:
        np=f"{period}nd"
    elif period==3:
        np=f"{period}rd"
    else:
        np=f"{period}th"   

    #Group Number
    if not 58<=atomic_number<=71 and not 90<=atomic_number<=103 and not atomic_number==57 and not atomic_number==89 and not atomic_number==41 and not atomic_number==24 and not atomic_number==42 and not atomic_number==44 and not atomic_number==45 and not atomic_number==78 and not atomic_number==29 and not atomic_number==46 and not atomic_number==47 and not atomic_number==79:
        if configuration.endswith("s1"):
            group_number=1
            group_name="Alkali Metals"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}st group.\nGroup Name={group_name}"
        elif configuration.endswith("s2") and not atomic_number==2:
            group_number=2
            group_name="Alkaline Earth Metals"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}nd group.\nGroup Name={group_name}"
        elif configuration.endswith("d1") and not atomic_number==57 and not atomic_number==89:
            group_number=3
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}rd group."
        elif configuration.endswith("d2"):
            group_number=4
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d3"):
            group_number=5
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d4") and not atomic_number==41:
            group_number=6
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d5") and not atomic_number==24 and not atomic_number==42:
            group_number=7
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d6"):
            group_number=8
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d7") and not atomic_number==44:
            group_number=9
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d8") and not atomic_number==45:
            group_number=10
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d9") and not atomic_number==78:
            group_number=11
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("d10") and not atomic_number==29 and not atomic_number==46 and not atomic_number==47 and not atomic_number==79:
            group_number=12
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
        elif configuration.endswith("p1"):
            group_number=13
            group_name="Boron Family"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif configuration.endswith("p2"):
            group_number=14
            group_name="Carbon Family"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif configuration.endswith("p3"):
            group_number=15
            group_name="Nitrogen Family/Pnicogens"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif configuration.endswith("p4"):
            group_number=16
            group_name="Oxygen Family/Chalcogens"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif configuration.endswith("p5"):
            group_number=17
            group_name="Fluorine Family/Halogen Family"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif configuration.endswith("p6"):
            group_number=18
            group_name="Noble Gases/Inert Gases/Zero Group Elements"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        elif atomic_number==2:
            group_number=18
            group_name="Noble Gases/Inert Gases/Zero Group Elements"
            output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group.\nGroup Name={group_name}"
        
    elif 58<=atomic_number<=71:
        group_number=3
        group_name="Lanthanides"
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}rd group.\nSeries ={group_name}"
    elif 90<=atomic_number<=103:
        group_number=3
        group_name="Actinides"
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}rd group.\nSeries ={group_name}"
    elif atomic_number==57 or atomic_number==89:
        group_number=3
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}rd group."
    elif atomic_number==24 or atomic_number==42:
        group_number=6
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
    elif atomic_number==29 or atomic_number==47 or atomic_number==79:
        group_number=11
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
    elif atomic_number==46 or atomic_number==78:
        group_number=10
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
    elif atomic_number==41:
        group_number=5
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
    elif atomic_number==44:
        group_number=8
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."
    else:
        group_number=9
        output_msg=f"{ename}({eabb}) is a {block_type}-block element in {np} period and in {group_number}th group."

    #Output
    CLI_print(output_msg)
root.mainloop()
