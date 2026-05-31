# 📝 TodoApp

A full-featured Todo & Blog REST API built with **Django** and **Django REST Framework**, containerized with Docker.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2, Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Email | django-templated-email + smtp4dev |
| Task Queue | Celery + Redis |
| Scheduler | django-celery-beat |
| API Docs | drf-yasg (Swagger) |
| Testing | pytest + pytest-django |
| Containerization | Docker + Docker Compose |

---

## 📁 Project Structure

```
todoapp/
├── accounts/        # User auth (register, login, reset password)
├── todo/            # Todo app
├── core/            # Django project settings & Celery config
├── templates/
│   └── email/       # Email templates
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

---

## ⚙️ Getting Started

### Prerequisites

- Docker & Docker Compose installed

### 1. Clone the repository

```bash
git clone https://github.com/amirmad2007/todoapp.git
cd todoapp
```

### 2. Create `.env` file

```env
SECRET_KEY=django-insecure-testkey123
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 3. Run with Docker

```bash
docker-compose up --build
```

### 4. Apply migrations

```bash
docker-compose exec backend python manage.py migrate
```

### 5. Create superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

---

## 🌐 Services & Ports

| Service | URL |
|---|---|
| Django API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/swagger/ |
| smtp4dev (Email UI) | http://localhost:3000 |

---

## 📬 API Endpoints

### Accounts
| Method | Endpoint | Description |
|---|---|---|
| POST | `/accounts/api/v1/register/` | Register new user |
| POST | `/accounts/api/v1/login/` | Login & get JWT token |
| POST | `/accounts/api/v1/token/refresh/` | Refresh JWT token |
| POST | `/accounts/api/v1/reset-password/` | Request password reset |
| GET | `/accounts/api/v1/profile/` | Get user profile |

### Tasks
| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks/api/v1/task/` | List all tasks |
| POST | `/tasks/api/v1/task/` | Create a task |
| GET | `/tasks/api/v1/task/{id}/` | Retrieve a task |
| PUT | `/tasks/api/v1/task/{id}/` | Update a task |
| DELETE | `/tasks/api/v1/task/{id}/` | Delete a task |

---

## 🧪 Running Tests

```bash
# Run all tests
docker-compose exec backend pytest

# Run specific app tests
docker-compose exec backend pytest accounts/tests/
docker-compose exec backend pytest products/tests/

# With verbose output
docker-compose exec backend pytest -v
```

---

## 🔧 Celery Workers

```bash
# Worker
docker-compose exec worker celery -A core worker --loglevel=info

# Beat Scheduler
docker-compose exec beat celery -A core beat --loglevel=info
```

---

## 📄 License

MIT License
