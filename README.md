# 🌟 Blood Donor Finding System using Django & PostgreSQL 🌟

🚀 **Excited to share my latest project** - a simple yet impactful Blood Donor Finding System built using Django and PostgreSQL! 🩸

## 🔍 Key Features

- 🚀 **Add and manage donor information**: Easily add, update, and manage donor details, including blood group, age, and contact information.
- 🚀 **Search and filter donors**: Quickly find the right blood match by searching and filtering donors by blood group.
- 🚀 **Secure data storage**: Robust and scalable data management with PostgreSQL.
- 🚀 **User-friendly interface**: Clean and responsive design for seamless user access across devices.

## 💡 Tech Stack

- ⚙️ **Backend**: Django
- 📱 **Frontend**: HTML, CSS, Bootstrap
- 📦 **Database**: PostgreSQL

## 🎯 Why This Project?

Blood donation is a life-saving act, and this system aims to simplify the process of finding suitable blood donors in times of need. Whether for emergencies or routine requirements, this tool helps connect willing donors with those in need.

## 🚀 Live Demo

Check out the live demo: [Blood Donor Finding System](https://blood-donation-shdt.onrender.com)

## 🌐 Project Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Django

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Md-Merazul-Islam/blood_donation.git
    cd blood_donation
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:
    - Create a new PostgreSQL database.
    - Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000`.

## 📂 Project Structure

- `donor`: Contains the main application for donor management.
- `templates`: HTML templates for rendering views.
- `static`: Static files (CSS, JS).
- `settings.py`: Django settings, including database configuration.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements.

## 📝 License

This project is open-source and available under the [MIT License](https://mdmerazulislam.netlify.app/contact).
