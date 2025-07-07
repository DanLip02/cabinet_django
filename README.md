## 🚀 Quickstart

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-org/internal-dashboard.git
   cd internal-dashboard

2. **Create virtual environment and install dependencies:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

3. **Create a .env file at the root with the following content:**

       DEBUG=True
       SECRET_KEY=your-secret-key
       ALLOWED_HOSTS=127.0.0.1,localhost

4.  **Service credentials**
    ```
    METABASE_URL=https://metabase.com
    METABASE_USER=user
    METABASE_PASS=password
    
    Or other services can be added
    ```
4. **Apply migrations and create superuser:**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    Run the development server:

5. **Apply migrations and create superuser:**
    ```bash
    python manage.py runserver
   
⚙️ Features
✅ Service Monitoring (/monitoring/)
Periodically checks internal services using HTTP GET/HEAD.

Auth support for Metabase and BasicAuth-based services.

Parses HTML responses (e.g., Streamlit, GitHub) using BeautifulSoup to determine actual status.

Verifies login/auth APIs (e.g., Metabase /api/session) and downstream APIs (/api/user/current).

📚 Internal Services Registry
Declaratively define service endpoints, types (basic, metabase, streamlit) and authentication in settings.SERVICES.

# Example:

    SERVICES = {
        "Github": {
            "url": "https://github.com",
            "auth": None
        },
        "Metabase": {
            "url": os.getenv("METABASE_URL"),
            "auth": (os.getenv("METABASE_USER"), os.getenv("METABASE_PASS")),
            "type": "metabase"
        },
        "Default-table": {
            "url": os.getenv("DEFAULT_TABLE_URL"),
            "auth": (os.getenv("DEFAULT_TABLE_LOGIN"), os.getenv("DEFAULT_TABLE_PASSWORD")),
            "type": "basic"
        },
    }
# Output example in monitoring UI:

    Github: 🟢
    Metabase: 🟢
    Default-table: 🟢

# 💬 Chat System
Real-time WebSocket chat with Django Channels and Redis.

Rooms, user tracking, and admin access control.

Only available to logged-in users.

Message log and online presence support.

Admins can view users via /admin/ and assign permissions or groups.

