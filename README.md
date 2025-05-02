# Django Airways

The Flight Booking Management System is a full-featured web application built with Django and Django REST Framework (DRF) that allows users to search, book, and manage local flights seamlessly. Designed with a user-friendly interface and powerful backend logic, the platform supports dynamic pricing based on travel class, real-time seat availability, and session-based booking flow with API support.

### Getting Started

These instructions will guide you through setting up Django Airways on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.
- [Requests](https://pypi.org/project/requests/) - A simple and elegant HTTP library for Python, used to send HTTP/1.1 requests with methods like GET and POST. It simplifies interacting with external APIs.
- [Django REST Framework](https://www.django-rest-framework.org/) – A powerful and flexible toolkit for building Web APIs in Django. It provides features like serialization, authentication, and browsable APIs, making it easy to develop and test RESTful services.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv airways_env
    cd airways_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-airways.git
    cd django-airways

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create/Login to Paystack account, and get secret and public key, then add it to the settings.py file (see file ending)

    PAYSTACK_SECRET_KEY = ''
    PAYSTACK_PUBLIC_KEY = ''

Create a super user. This account will be used to access the admin dashboard to add travel class and flight schedules.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- Flight Search with Filtering and Pagination: Users can browse available flight schedules, filter by departure/arrival locations and dates, and view results paginated for better usability.

- Service Selection and Dynamic Pricing: Customers can select a travel class (e.g., Business or Economy) and the system automatically calculates the total cost based on class-specific fees.

- Unique Daily Booking Identifier: Each booking is assigned a unique 6-character alphanumeric code generated per day to simplify lookup and ensure uniqueness.

- Session-Based Booking Flow: After booking, the booking ID is stored in the session to enable a seamless redirection to the payment and confirmation pages.

- Customizable Travel Classes: Travel classes are defined as a separate model, allowing easy management and reuse across different flight schedules.

- Booking Summary and Confirmation Page: After submission, users see a personalized summary page displaying booking, passenger, and flight details clearly.

- Print-Friendly Confirmation: Users can easily print their booking confirmation with a built-in “Print” button that triggers the browser print dialog.

- RESTful API for Flight Schedules: A clean, DRF-powered API endpoint exposes all flight schedules in JSON format, ready for frontend, mobile, or third-party integration.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

