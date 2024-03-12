 Remind-me-later Project Documentation

## Clone the Project

```bash
git clone https://github.com/rohandass58/remind_me_later.git
cd remind_me_later
```
# Activate the Virtual Environment
## For Unix/Linux
```bash
source venv/bin/activate
```
## For Windows
```bash
.\venv\Scripts\activate
```

# Install Dependencies
```bash
pip install -r requirements.txt
```

# Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

# Run the Development Server
```bash
python manage.py runserver
```
