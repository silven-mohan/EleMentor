# 🧪 EleMentor – Position of Element

**EleMentor** is a Python-based GUI tool that identifies the **period**, **group**, and **block** of a chemical element using its **atomic number**, **name**, or **abbreviation**. It includes color-coded CLI output, precise group logic, and special handling for electronic configuration exceptions (like Cr, Cu, Pd, etc.).

---

## 🚀 Features

- 🔍 Determine the **position** of any known element (Z ≤ 118)
- 🧠 Calculates:
  - **Period** (based on outermost shell)
  - **Group number** (using valence orbital logic)
  - **Block type** (s, p, d, or f)
- 📦 Built-in support for elements with **exceptional electronic configurations**
- 🖥️ GUI built with **Tkinter**

---

## 🖱️ How to Use

### ✅ Run the App

```bash
python EleMentor_Position_of_element.py
```
🧾 Input Format
* Atomic number: e.g., 26

* Element name: e.g., Iron

* Abbreviation: e.g., Fe

```bash
Iron(Fe) is a d-block element in 4th period and in 8th group.
```

## How it works
*The app uses the valence shell configuration to determine:

*Group number:

  *s1 → Group 1 (Alkali Metals)

  *s2 → Group 2 (Alkaline Earth Metals)

  *d1–d10 → Groups 3–12

  *p1–p6 → Groups 13–18

*Period from highest shell number.

*Block from the last occupied subshell.

*Exception configurations are pre-defined for elements like:

  *Chromium (Cr): 4s1 3d5

  *Copper (Cu): 4s1 3d10

  *Palladium (Pd): 4d10 (no 5s!)

  *Platinum (Pt), Gold (Au), etc.


## Author-Silven Mohan










