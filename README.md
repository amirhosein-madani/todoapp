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
SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST=smtp4dev
EMAIL_PORT=25
EMAIL_USE_TLS=False
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
| Redis | localhost:6379 |

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

### Blog / Posts
| Method | Endpoint | Description |
|---|---|---|
| GET | `/blog/api/v1/post/` | List all posts |
| POST | `/blog/api/v1/post/` | Create a post |
| GET | `/blog/api/v1/post/{id}/` | Retrieve a post |
| PUT | `/blog/api/v1/post/{id}/` | Update a post |
| DELETE | `/blog/api/v1/post/{id}/` | Delete a post |

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
