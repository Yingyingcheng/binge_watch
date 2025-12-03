# 📺 Binge-Watch Risk App (Django)

This is a web application built with Django that allows users to review and rate movies and TV shows based on two key metrics: **Quality Score** and **Binge Risk Score**. The app provides a personalized dashboard for users to track their review history and see overall community averages.

## ✨ Features

- **User Authentication:** Secure user login and profile management.
- **Review Submission:** Submit reviews for content with detailed score sliders.
- **Decimal Scoring:** Uses a precision scale (e.g., 4.5/5) for accurate ratings.
- **Update-or-Create:** Allows users to update an existing review for a show instead of creating duplicates.
- **Personalized Dashboard:** Displays a user's complete history of submitted reviews.
- **Community Averages:** Calculates and displays the average Quality and Risk scores across all community reviews.
- **Responsive Design:** Netflix-inspired dark theme optimized for both desktop and mobile viewing using CSS Grid and Flexbox.

## 🚀 Getting Started

Follow these steps to get the Binge-Watch Risk App running on your local machine.

### Prerequisites

You need **Python 3** and **pip** installed.

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd binge_watch_project
```

### 2. Set Up the Virtual Environment

It's best practice to use a virtual environment to manage dependencies.

```bash
# Create the environment
python -m venv venv


# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
venv\Scripts\activate
```

### 3. Install Dependencies

Install all necessary packages using the requirements.txt file we created:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

You need to initialize the database and create a superuser for administration.

```bash
# Apply migrations (creates tables based on models.py)
python manage.py migrate

# Create a superuser (for accessing /admin/)
python manage.py createsuperuser
```

### 5. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

The app will now be accessible in your browser at: http://127.0.0.1:8000/

### 6. Project Structure

The key components of the application are located here:

- **`binge_watch_app/models.py`**: Defines the `Content` and `Review` database models.
- **`binge_watch_app/forms.py`**: Contains the `ReviewForm` definition with custom widgets for the range sliders.
- **`binge_watch_app/views.py`**: Handles all application logic, including the review submission, form validation, history fetching, and average calculations.
- **`binge_watch_app/templates/binge_watch/content_list.html`**: The main dashboard template containing the review form, history, and score displays.
- **`binge_watch_app/static/binge_watch/index.css`**: All styling for the Netflix-themed dashboard.
