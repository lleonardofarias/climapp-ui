# climapp-ui

**Important Note:** Before proceeding, make sure to check out the [climapp-api](https://github.com/lleonardofarias/climapp-api) project to set up and obtain access to the required weather data API.

## Introduction

Welcome to climapp-ui! This is the user interface component that allows users to interact with weather data provided by the climapp API. In this guide, we will explain how to configure the API URL in the views and provide additional information about user registration and superuser creation.

## Prerequisites

Before you can run climapp-ui, you need to ensure that you have Django installed on your system. This UI is built using Django, a powerful Python web framework. Follow the steps below to install Django and run the application.

### Installing Django

You can install Django using `pip`, the Python package manager. If you don't have `pip` installed, you can follow [these instructions](https://pip.pypa.io/en/stable/installation/) to install it.

#### Using Python Django:

Open your terminal/command prompt and run the following command to install Django:

```bash
pip install Django
```

## Running the Application

Once you have Django installed, you can run climapp-ui as follows:

- Navigate to the project directory containing the manage.py file in your terminal/command prompt.

- Use Python or Python3 to run the development server:

- Using Python (Python 2.x):

```bash
python manage.py runserver
```
If it doesn't work, try doing it like this

```bash
python3 manage.py runserver
```

## User Authentication

climapp-ui comes with a built-in user authentication system that includes login and logout functionality. To start using the application, follow these steps:

1. Register a User:
   - Navigate to the registration page and complete the registration form.
   - After registration, you can log in with your credentials.

2. Log In:
   - Use the registered username and password to log in to the application.

### Creating an Admin or Superuser

If you need to create an admin or superuser account for administrative purposes, you can use Django's built-in management commands. Here's how:

1. Open a terminal/command prompt.

2. Navigate to the project directory containing your `manage.py` file.

3. To create a superuser, run the following command:

   ```bash
   python manage.py createsuperuser
   ```

Follow the prompts to enter a username, email (optional), and password.

You now have a superuser account that can access admin features.

### Configuring API URL in Views

To configure the API URL in the views, follow these steps:

- Open the views.py file in your climapp-ui project.

- Locate the following line of code:

  ```bash
  api_url = "Your server docker link""/api/weather/?city={city}"
   ```
- Replace "Your server docker link" with the URL of the climapp-api that you have set up.

- Save the file.

Now you you run the django server.

  ```bash
  python manage.py runserver
   ```

Now, your climapp-ui is configured to fetch weather data from the climapp-api.

### Using climapp-ui

- After logging in, you will be directed to the application's main page.

- On the main page, enter the name of the city for which you want to fetch weather data.

- Choose the metric system (e.g., metric or imperial).

- Select the desired time zone (default is America/Sao_Paulo).

- Click on the "Search Weather" button.

-You will receive weather information for the specified city based on the chosen metric system and time zone.

Enjoy using climapp-ui to access real-time weather data!
