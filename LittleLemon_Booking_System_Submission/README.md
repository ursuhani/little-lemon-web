# Little Lemon Booking System

Django booking website for the peer-graded Little Lemon reservation assignment.

## Project layout
- Django project: `littlelemon`
- Django app: `restaurant`
- Booking form: `/book/`
- Reservations page: `/reservations/`
- JSON endpoint: `/bookings/` (optional date filter: `/bookings/?date=YYYY-MM-DD`)
- Admin: `/admin/`

## Setup with Pipenv
Use Python 3.11 or 3.12. From this directory:

```bash
pip install pipenv
pipenv shell
pipenv install
```

### Configure MySQL
Create a database in MySQL:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Set environment variables to match your local MySQL setup before running Django. In PowerShell, for example:

```powershell
$env:MYSQL_DATABASE="littlelemon"
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="YOUR_MYSQL_PASSWORD"
$env:MYSQL_HOST="127.0.0.1"
$env:MYSQL_PORT="3306"
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

### Quick test without MySQL
If MySQL is not installed/configured, PowerShell:

```powershell
$env:DB_ENGINE="sqlite"
python manage.py migrate
python manage.py runserver
```

The assignment asks for MySQL, so use the MySQL configuration for final review/submission. The SQLite option is only for a quick smoke test.

## Booking behavior
- Date defaults to today and cannot be earlier than today.
- Slots from 10:00 through 20:00.
- Existing reservations for the selected date are shown as unavailable.
- The form checks availability server-side and the database has a unique constraint on date + slot to prevent duplicate reservations.
- `/reservations/` renders all reservations as JSON data.
- `/bookings/` returns JSON and accepts a `date` query parameter.
