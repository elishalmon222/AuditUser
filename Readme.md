# User Audit


### How to launch the project:
To run the project: Clone the repository and open it in the command line:
```
git clone https://github.com/elishalmon222/AuditUser.git
cd UserAudit
```
Create and activate a virtual environment:
```
python -m venv venv
source venv/Scripts/activate (for Windows) or source venv/bin/activate (for Linux and MacOs)
```
Install the dependencies from the *requirements.txt* file:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
cd UserAudit
```

Run migrations:
```
python manage.py migrate
```
Create superuser for Django admin:
```
python manage.py createsuperuser
```
Launch the project:
```
python manage.py runserver
```
Starting development server at http://127.0.0.1:8000/


### A Postman collection is attached to the main folder of this Repository

### Valid User Actions:
    'deleted'
    'restarted_computer'
    'went_running'
    'baked_cake' 
