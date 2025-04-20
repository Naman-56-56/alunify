# Alunify

Alumni networking platform built with Django.

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
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgres://username:password@host:port/database_name
   ```

2. Collect static files:
   ```
   python manage.py collectstatic
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

### Deploy to a Hosting Platform

Follow the specific instructions for your hosting platform (Heroku, AWS, etc.) for deploying Django applications.

## License

This project is licensed under the terms of the LICENSE file included in the repository. 