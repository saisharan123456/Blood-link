# Blood Link 🩸

Blood Link is a Python-based application that connects blood donors, hospitals, and patients by managing blood group availability through a MySQL database.  
The project aims to simplify blood availability tracking and donor information management.

---

## 📌 Features
- Store and manage donor details
- Maintain blood group availability
- Hospital blood stock tracking
- MySQL database integration
- Console-based user interaction

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Database:** MySQL  
- **Library:** mysql-connector-python  

---

## 📂 Project Structure
blood-link/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore

---

## ⚙️ Setup Instructions

 1️⃣ Clone the Repository
```bash
git clone https://github.com/USERNAME/blood-link.git
cd blood-link

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Database
Create a MySQL database
Create required tables manually (schema not included)
Set your database password as an environment variable
Mac / Linux
export DB_PASSWORD=yourpassword
Windows (PowerShell)
setx DB_PASSWORD yourpassword

4️⃣ Run the Project
python main.py
📌 Notes
Database tables must exist before running the program
This is a console-based academic project
Passwords and credentials are not hardcoded for security reasons

🚀 Future Improvements

Input validation
Modular code structure
GUI or web interface
Authentication system
Proper database schema documentation

👤 Author
Sai Sharan
CSE (Artificial Intelligence), Manipal Institute of Technology, Bangalore
