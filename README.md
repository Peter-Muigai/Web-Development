# 📝 Django Blog Project

A full-featured blog web application built using Django.
This project allows users to create, edit, and manage blog posts, with user authentication and a clean interface.

---

## 🚀 Features

* User registration and authentication
* Create, edit, and delete blog posts
* Comment and delete comments on posts
* Responsive design using Bootstrap
* Admin panel for content management
* Database-backed content storage

---

## 🛠️ Technologies Used

* Python
* Django
* HTML, CSS, Bootstrap
* SQLite (development)
* PostgreSQL (production)
* Gunicorn (deployment)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Peter-Muigai/Web-Development.git
cd Web-Development
```

---

### 2. Create virtual environment

```bash
python -m venv ll_env
source ll_env/bin/activate  # Linux/Mac
ll_env\Scripts\activate     # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run migrations

```bash
python manage.py migrate
```

---

### 5. Start development server

```bash
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000/
```

---

## Environment Variables

Create a `.env` file or set environment variables:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

---

##  Deployment

This project is configured for deployment on Render.

Key steps:

* Add environment variables in the Render dashboard
* Configure PostgreSQL database
* Use Gunicorn as the web server

---

##  Future Improvements

* Add likes and reactions
* Improve UI/UX design
* Add REST API for mobile integration

---

##  Author

**Peter Muigai**
Electrical & Electronics Engineering Student
Passionate about AI, IoT, and Software Development

---

## 📄 License

This project is open-source and available under the MIT License.
