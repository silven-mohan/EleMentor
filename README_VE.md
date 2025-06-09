# 🧪 EleMentor – Valence Electron Identifier

**EleMentor** is a GUI-based Python tool that determines the **valence electrons** of any element with atomic number **1 through 118**. It intelligently handles:
- s-, p-, d-, and f-block elements,
- exceptions in electronic configuration (e.g., Cr, Cu, Pt, Au),
- and  CLI-like output in a user-friendly Tkinter GUI.

---

## 🚀 Features

- ✅ **Valence electron calculator** for all elements Z ≤ 118
- 🧠 Supports:
  - **s-, p-, d-, and f-block** valence logic
  - **Exception configurations** (Chromium, Palladium, Gadolinium, etc.)
- 🧪 Electron configuration is determined programmatically or via hardcoded exceptions
- 🖥️ **Simple GUI** using Python's built-in `Tkinter`

---

## 🖥 GUI Interface

The app uses a minimal but functional GUI:
- A `Text` widget for output
- A `Menu` item titled `Valence Electrons`
- Prompts the user via `simpledialog` for:
  - Atomic number (e.g., `26`)
  - Element name (e.g., `Iron`)
  - Symbol (e.g., `Fe`)

---

## 🧠 Valence Electron Logic

### 🔹 For s- and p-block (Groups 1–2 and 13–18):
Valence = number of outermost **s and p electrons**.

### 🔹 For d-block (Groups 3–12):
Valence = Group number.

### 🔹 For f-block (Lanthanides and Actinides):
Valence = sum of:
- outermost **s electrons**
- \( (n-1)d \) electrons
- \( (n-2)f \) electrons  
This is extracted by parsing the electron configuration string.

---

## 📦 Configuration Exceptions

Certain elements (like Cr, Cu, Mo, Pd, Au) **do not follow the Aufbau principle**. These are handled with a hardcoded dictionary for accurate electron configuration assignment.

### Example:
```text
Input: 29 (Copper)
Actual config: [Ar] 4s1 3d10 → Valence = 1 (s) + 10 (d)
```

## 🧪 Sample Use Case
Open the app

Click Valence Electrons in the top menu

Enter input like:

"Fe" → Iron

"64" → Gadolinium

"Xenon" → Nonmetal

## 📤 Output Example
```text
Valence Electrons of Gadolinium(Gd) is/are: 10
```

## Author: Silven Mohan
