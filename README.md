# 🏨 Hotel Management System (HMS)

A **console-based Hotel Management System** built with **Python** 🐍.  
This project manages **Bookings** (Rooms, Halls, Tables) and **Food Orders** 🍛🥤🍨 for both hotel guests and independent food customers.

---

## ✨ Features

### 🛎️ Booking System
- 👤 **New / Existing Users**  
- 🛏️ **Room Booking**  
  - Single Seater (₹1200/day)  
  - Double Seater (₹2000/day)  
  - Mini Suite (₹3500/day)  
  - Suite (₹5000/day)  
- 🎉 **Hall Booking**  
  - For 80–120 people (₹12,000 flat)  
- 🍽️ **Table Booking**  
  - 2-Seater (₹2500)  
  - 4-Seater (₹4500)  
  - 6-Seater (₹6500)

### 🍴 Food Ordering System
- Works for both **booking customers** and **independent customers**.
- 🥗 **Veg Menu** → Dal Makhani (₹300), Shahi Paneer (₹500)  
- 🍗 **Non-Veg Menu** → Chicken Curry (₹350), Fish Fry (₹400)  
- 🥤 **Drinks** → Coke (₹50), Cold Coffee (₹120)  
- 🍨 **Desserts** → Ice Cream (₹80), Gulab Jamun (₹100)  
- ➕ Add multiple items until you choose to **exit**.

### 💾 Data Storage
- `existing_customers` → Stores booking details, bills, and customer info.  
- `X` → Stores food order details.  
- 📊 Bills are auto-updated after each booking or food order.

---

## ⚙️ How It Works
1. Launch the program ➡️ `python hotel_management.py`  
2. Choose between:  
   - **Bookings** 🏨  
   - **Food Orders** 🍽️  
3. Follow the menu options and enter details.  
4. ✅ System generates **Booking ID / Order ID** and maintains records.  
5. Final bill is displayed at the end.  

---

## 🛠️ Tech Stack
- **Language**: Python 🐍  
- **Modules Used**:  
  - `random` 🎲 → For generating Booking & Order IDs  

---

## 🚀 Future Improvements
- 🔄 Replace recursive input handling with `while` loops (to prevent stack overflow).  
- 🆔 Avoid ID collisions by assigning unique ranges for bookings & food orders.  
- 💾 Add file/database support for **data persistence** (currently, data resets after exit).  
- 📊 Improve bill summary with itemized receipts.  

---

## 🎯 Skills Demonstrated
- 📚 Python Functions & Modular Programming  
- 📂 Dictionaries & Nested Data Structures  
- 🔁 Loops, Conditionals, and Recursion  
- 🧮 Bill Calculation & Data Management  
- 🖥️ Console-Based User Interaction  

---

## 📸 Demo (Console Flow)
<img width="1283" height="870" alt="image" src="https://github.com/user-attachments/assets/671ee8ba-c46f-43ed-ae76-493d26f9f63a" />
<img width="300" height="430" alt="image" src="https://github.com/user-attachments/assets/9b3c3aa4-32dc-4c3a-8e5b-2098f99f6174" />


