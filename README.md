# Alunify

Alunify is a comprehensive alumni networking platform built with Django 5.0. The platform helps connect graduates, facilitates professional networking, and enables alumni to showcase their skills and experiences.

## Features

- **User Management**: Custom Alumni user model with extended profile information
- **Profile System**: Detailed alumni profiles with education, work experience, skills, and professional categorization
- **Search Functionality**: Advanced search capabilities to find alumni by various criteria
- **Responsive Design**: Mobile-friendly interface built with modern frontend techniques
- **Secure Authentication**: Robust login, registration, and password reset functionality
- **Media Support**: Profile pictures and other media uploads

## Project Structure

The application consists of the following main components:

- **user**: Custom user authentication and Alumni model
- **profiles**: Profile management, experiences, education, skills, and professions
- **search**: Alumni search and query tracking functionality

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Development Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd alunify
   ```

2. Create and activate virtual environment (optional):
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use: env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your settings.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

### Database Configuration

By default, the application uses SQLite for development. For production, it's recommended to use PostgreSQL:

1. Make sure PostgreSQL is installed and running on your server.

2. Configure the database URL in your `.env` file:
   ```
   DATABASE_URL=postgres://username:password@host:port/database_name
   ```

The application will automatically use PostgreSQL when the `DATABASE_URL` environment variable is set.

## Deployment

### Preparing for Deployment

1. Set the following environment variables:
   ```
   DEBUG=False
   SECRET_KEY=<your-secure-secret-key>
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,alunify.onrender.com
   DATABASE_URL=postgres://username:password@host:port/database_name
   ```

2. Collect static files:
   ```
   python manage.py collectstatic --no-input
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

### Deploy to Render.com

The application is configured for deployment on Render.com:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure environment variables as listed above
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `gunicorn alunify.wsgi:application`

## Development

### Adding New Features

1. Create a new branch for your feature
2. Implement and test your changes
3. Submit a pull request for review

### Testing

Run the test suite with:
```
python manage.py test
```

## Technologies Used

- **Backend**: Django 5.0+
- **Database**: SQLite (development), PostgreSQL (production)
- **Media Storage**: Local filesystem
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render.com

## License

This project is licensed under the terms of the LICENSE file included in the repository. 