# 📡 readioweb – Django Project

Welcome to **readioweb**, a Django-based web application. This guide will help you set up and run the project locally for development or testing purposes.

---

## 🔧 Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **pip** (Python package manager)
- **virtualenv** (optional but recommended)
- **Git**

---

## 🚀 Getting Started

Follow the steps below to get the project running on your local machine.

---

### 1. Clone the Repository


git clone https://github.com/geniustechspace/radio_web.git
cd readioweb

### 2. Create and Activate Virtual Environment

# Create a virtual environment (Linux/macOS)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate


### 3. Install Project Dependencies
pip install -r requirements.txt

### 4. Apply Database Migrations
python manage.py migrate

### 5. Create a Superuser for Admin Access
python manage.py createsuperuser


### 6. Run the Development Server
python manage.py runserver
Visit the app in your browser:

👉 http://127.0.0.1:8000/

You can also login to admin using
👉 http://127.0.0.1:8000/admin/


```bash