# My Django Project

This repository contains a Django project named "trydjango."

## Prerequisites

- Python 3.9 installed on your system.

## Getting Started

1. Clone this repository to your local machine:

```
git clone
```

2. Create a virtual environment and activate it:

```
python -m venv myenv
source myenv/bin/activate  # On macOS and Linux
myenv\Scripts\activate    # On Windows
```
3. Install Django:
```
pip install django==2.0.7
```
4. Navigate to the project directory:
```
cd trydjango
```
5. Run the development server:
```
python manage.py runserver

```
## Other Useful Commands

6. Migrate Database:
```
python manage.py migrate

```
7. Create Superuser:
```
 python manage.py createsuperuser

```


8. Create Component
```
python manage.py startapp componentName

```

9. New App migration 
```
python manage.py makemigrations

```
## Create Model Objects Commands

10. Creating objects in shell
```
python manage.py shell 
#shell
from products.models import Product
Product.objects.all()
Product.objects.create()

```

10. New App migration 
```
python manage.py makemigrations

```

Access your project in a web browser at http://127.0.0.1:8000/.



