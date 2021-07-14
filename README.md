# my-library
An application for administrating my personal library.

## Installation

Requirements:
- Git
- Python3
- virtualenv


Clone this repository. Inside its directory run:

```bash
virtualenv env
```

This will create a Python environment. Now you need to active it. The following solution works on Linux based systems:

```bash
source env/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

In order to create and prepare a local database run:

```bash
python manage.py makemigrations
python manage.py migrate
```

You are able to run the application with:

```bash
python manage.py runserver
```