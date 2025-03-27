# Royal Cuts Premium Indian Barber Shop

A full-featured barbershop management system with booking functionality, service management, stylist profiles, and admin dashboard built with Django and Supabase.

## Project Overview

Royal Cuts is a comprehensive web application for a premium Indian barber shop that allows users to:
- Browse services and stylists
- Book appointments based on real-time availability
- Leave reviews for stylists
- Manage their profile and appointment history

Administrators can:
- Manage all appointments, services, and stylists
- Add, edit, or delete services and stylists
- Review and approve customer reviews

## Key Features

- **User Authentication**: Secure login/signup with role-based access (user vs admin)
- **Services Management**: Browse and manage services with categories and pricing
- **Stylist Profiles**: View stylist details, experience, and services offered
- **Booking System**: Book appointments with real-time time slot availability
- **Admin Dashboard**: Comprehensive dashboard for business management
- **Responsive Design**: Mobile-friendly interface for all devices

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Django (Python web framework)
- **Database**: Supabase (PostgreSQL as a service)
- **Authentication**: Custom session-based auth with Supabase
- **Styling**: Custom CSS with Bootstrap components
- **Deployment**: Supports local development and cloud platforms

## Local Development Setup

### Prerequisites
- Python 3.10+ 
- Git
- pip (Python package manager)

### Quickstart (Easiest Method)

We've provided convenient scripts to set up and run the application automatically:

#### For Linux/macOS Users
```bash
# Clone the repository
git clone <your-repository-url>
cd royal-cuts-barbershop

# Make the script executable
chmod +x runserver.sh

# Run the setup script (which will also start the server)
./runserver.sh
```

#### For Windows Users
```bash
# Clone the repository
git clone <your-repository-url>
cd royal-cuts-barbershop

# Run the setup batch file
runserver.bat
```

These scripts will:
1. Check if Python is installed with the correct version
2. Set up a virtual environment (if needed)
3. Install all required dependencies
4. Create a default `.env` file if none exists
5. Start the development server

### Manual Setup (Alternative Method)

If you prefer to set up manually, follow these steps:

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd royal-cuts-barbershop
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   
   # macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django psycopg2-binary requests python-dotenv
   ```

5. **Create a .env file**
   Create a `.env` file in the project root with the following content:
   ```
   # Supabase connection details (required)
   SUPABASE_URL=https://phuhhrqzzqdfheuhqofi.supabase.co
   SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBodWhocnF6enFkZmhldWhxb2ZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI3NTAyMjEsImV4cCI6MjA1ODMyNjIyMX0.b4KLx3W1wliVO6fgHMaJIqN6vA9F5BMiUFqdD1tmsHo
   SUPABASE_SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBodWhocnF6enFkZmhldWhxb2ZpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0Mjc1MDIyMSwiZXhwIjoyMDU4MzI2MjIxfQ.HBoktk6j1cBqXbuT1wOwUDRsCAwMTDKyXC_qxs7n474
   
   # Django settings (optional)
   DJANGO_DEBUG=True
   DJANGO_SECRET_KEY=django-insecure-q&kzhu^6j5%n#ioc!2nh+9z4!yj-0kbxf+0!0c9_3qt-v3p=j&
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
   DJANGO_CSRF_TRUSTED_ORIGINS=https://*.replit.dev,https://*.replit.app,http://localhost:8000,http://127.0.0.1:8000
   
   # Server settings (optional)
   PORT=8000
   ```

6. **Start the development server**
   ```bash
   # Navigate to the barbershop directory where manage.py is located
   cd barbershop
   
   # Run the server
   python manage.py runserver 0.0.0.0:8000
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:8000`
   
### Using a Custom Port

By default, the application runs on port 8000. You can change this by:

1. **Using the scripts with a port parameter:**
   ```bash
   # Linux/macOS
   ./runserver.sh 5000
   
   # Windows
   runserver.bat 5000
   ```

2. **Editing the .env file:**
   ```
   PORT=5000
   ```

3. **Manually specifying the port:**
   ```bash
   cd barbershop
   python manage.py runserver 0.0.0.0:5000
   ```

## User Accounts

### Admin Account
- **Username**: admin
- **Password**: admin123
- Has full access to the admin dashboard

### Test User Account
- **Username**: testuser
- **Password**: password123
- Regular user with booking privileges

## Project Structure Explanation

```
/                               # Project root
├── barbershop/                 # Django project directory
│   ├── barbershop/             # Project settings
│   │   ├── __init__.py
│   │   ├── asgi.py             # ASGI config for async servers
│   │   ├── settings.py         # Django settings (routing, middleware, etc.)
│   │   ├── urls.py             # Main URL routing
│   │   └── wsgi.py             # WSGI config for sync servers
│   │
│   ├── main/                   # Main application
│   │   ├── __init__.py
│   │   ├── admin.py            # Django admin config
│   │   ├── apps.py             # App config
│   │   ├── db_init.py          # Database initialization logic
│   │   ├── forms.py            # Form definitions (booking, login, etc.)
│   │   ├── middleware.py       # Custom middleware for user access control
│   │   ├── models.py           # Data models for Supabase tables
│   │   ├── supabase.py         # Supabase API client/wrapper
│   │   ├── urls.py             # App-specific URL routing
│   │   ├── utils.py            # Utility functions (auth, time slots, etc.)
│   │   ├── views.py            # View functions (request handlers)
│   │   │
│   │   ├── static/             # Static assets
│   │   │   ├── css/            # CSS styles
│   │   │   ├── images/         # Images
│   │   │   └── js/             # JavaScript files
│   │   │
│   │   └── templates/          # HTML templates
│   │       └── main/           # Template files
│   │           ├── base.html   # Base template with navigation
│   │           ├── index.html  # Home page
│   │           ├── login.html  # Login page
│   │           ├── dashboard.html  # Admin dashboard
│   │           └── ...         # Other templates
│   │
│   └── manage.py               # Django command-line utility
│
├── .env                        # Environment variables
├── .env.example                # Example environment variable file
├── pyproject.toml              # Python project dependencies
├── runserver.sh                # Linux/macOS setup and run script
├── runserver.bat               # Windows setup and run script
└── README.md                   # This documentation file
```

## Database Structure

The application uses Supabase (PostgreSQL as a service) as the database backend. Below is a detailed breakdown of each table and its purpose:

### Core Tables

| Table | Description | Key Fields |
|-------|-------------|------------|
| **users** | User accounts including admins, customers, and linked stylist accounts | `id`, `username`, `password`, `email`, `phone_number`, `role` |
| **service_categories** | Categories of services (e.g., Haircuts, Beard Grooming, etc.) | `id`, `name`, `description` |
| **services** | Specific service offerings with pricing and details | `id`, `name`, `description`, `category_id`, `price`, `duration`, `is_active` |
| **stylists** | Barber/stylist profiles with experience and availability | `id`, `name`, `bio`, `profile_image`, `experience_years`, `is_active`, `user_id` |

### Relationship and Operational Tables

| Table | Description | Key Fields |
|-------|-------------|------------|
| **stylist_services** | Many-to-many mapping between stylists and the services they offer | `id`, `stylist_id`, `service_id` |
| **appointments** | Customer bookings with date, time, and service details | `id`, `user_id`, `customer_name`, `customer_phone`, `service_id`, `stylist_id`, `date`, `time`, `status`, `special_requests` |
| **reviews** | Customer feedback for stylists and services | `id`, `user_id`, `service_id`, `stylist_id`, `appointment_id`, `rating`, `comment`, `is_approved` |
| **business_hours** | Shop operating hours for each day of the week | `id`, `day_of_week`, `opening_time`, `closing_time`, `is_closed` |

### Database Schema

The database follows a relational schema with appropriate foreign key relationships:

```
users (1) -----< appointments (N)
services (1) ----< appointments (N)
stylists (1) ----< appointments (N)
services (M) <---- stylist_services (N) ----> stylists (M)
service_categories (1) ----< services (N)
```

### For Beginners: Understanding Database Tables

- **Primary Keys**: Each table has an `id` field as the primary key, which uniquely identifies each record
- **Foreign Keys**: Fields ending with `_id` reference records in other tables (e.g., `category_id` in the services table references a specific category)
- **Relationships**:
  - One-to-Many: For example, one stylist can have many appointments
  - Many-to-Many: For example, stylists offer multiple services, and services are offered by multiple stylists (using the `stylist_services` junction table)

### Supabase Integration

Supabase is used as a PostgreSQL database service. The application connects to Supabase using:

1. The custom `SupabaseClient` class in `supabase.py`
2. REST API calls for CRUD operations
3. Environment variables for connection credentials (`SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_SECRET_KEY`)

This approach gives the application cloud database capabilities without requiring complex server setup.

## Key Concepts for Beginners

### 1. Django MVT Architecture

Django follows the Model-View-Template (MVT) pattern, which is similar to MVC (Model-View-Controller):

- **Model** (`models.py`): Defines the data structure and database representation
  - In this project, we have custom model classes that represent Supabase tables
  - Example: `User`, `Service`, `Stylist`, `Appointment` classes

- **View** (`views.py`): Contains the logic to process user requests and prepare data
  - Functions that handle URLs and return responses
  - Example: `login_view()`, `booking_view()`, `dashboard_services_view()`

- **Template** (HTML files in `templates/`): Displays data to users with dynamic content
  - HTML files with Django template language (variables, filters, tags)
  - Example: `{% if user.is_authenticated %}`, `{{ service.name }}`

### 2. Supabase Integration

- **Custom Client** (`supabase.py`): A wrapper for the Supabase REST API
  - Handles authentication, database operations, and error handling
  - Methods include `select()`, `insert()`, `update()`, `delete()`

- **Connection Setup**:
  ```python
  # From supabase.py
  def __init__(self, url=None, key=None, secret_key=None):
      self.url = url or os.environ.get('SUPABASE_URL')
      self.key = key or os.environ.get('SUPABASE_KEY')
      self.secret_key = secret_key or os.environ.get('SUPABASE_SECRET_KEY')
  ```

- **Data Operations Example**:
  ```python
  # Example usage for fetching services
  services = supabase.select('services', filter_column='is_active', filter_value=True)
  ```

### 3. User Authentication

- **Session-Based Authentication**:
  - User credentials stored in Django session
  - No tokens or JWT handling needed for client-side

- **Login Process**:
  1. User submits username/password
  2. Password is verified against hashed version in database
  3. User details stored in session if valid
  4. Redirected based on role (admin → dashboard, user → home)

- **Role-Based Access**:
  - User roles: 'user', 'admin', 'stylist'
  - Different views and permissions based on role
  - Admin users have exclusive access to dashboard features

### 4. Middleware

- **AdminMiddleware** (`middleware.py`):
  - Intercepts requests to determine if the user is an admin
  - Restricts admin users to dashboard pages only
  - Redirects non-admins attempting to access admin pages

- **Implementation**:
  ```python
  # Process view to check user permissions
  def process_view(self, request, view_func, view_args, view_kwargs):
      # Check if user is logged in and is an admin
      if request.session.get('user') and request.session['user'].get('role') == 'admin':
          # If admin trying to access non-admin page, redirect to dashboard
          if not any(pattern in request.path for pattern in self.admin_urls):
              return redirect('dashboard')
      # If non-admin trying to access admin page, redirect to home
      elif any(pattern in request.path for pattern in self.admin_urls):
          return redirect('home')
  ```

### 5. Form Handling

- **Django Forms** (`forms.py`):
  - Declarative way to define HTML forms
  - Built-in validation and error handling
  - Automatic rendering of form fields

- **Form Types**:
  - **LoginForm**: Username and password fields
  - **SignupForm**: Registration with validation
  - **BookingForm**: Appointment scheduling with dynamic choices
  - **ServiceForm**: Admin form for managing services
  - **StylistForm**: Admin form for managing stylists

- **Form Processing Example**:
  ```python
  # In a view function
  if request.method == 'POST':
      form = BookingForm(request.POST)
      if form.is_valid():
          # Process valid form data
          appointment = Appointment(...)
          supabase.insert('appointments', appointment.__dict__)
      else:
          # Handle validation errors
  else:
      # Display empty form
      form = BookingForm()
  ```

### 6. Booking System Logic

- **Time Slot Management**:
  - Available slots based on business hours, stylist availability, and service duration
  - AJAX calls to update available times when date/stylist/service changes

- **Appointment Validation**:
  - Checks for double-booking
  - Ensures dates are in the future
  - Verifies stylist offers the selected service

### 7. Frontend Interaction

- **JavaScript Features** (`main.js`):
  - Dynamic forms that update as selections change
  - AJAX calls for time slot availability
  - Interactive dashboard elements for admin users

## Development Workflow

1. Make changes to the code
2. Test locally
3. Deploy to your hosting platform
4. Monitor for issues

## Troubleshooting

### Common Issues and Solutions

| Issue | Possible Causes | Solutions |
|-------|----------------|-----------|
| **Database Connection Errors** | Incorrect Supabase credentials | - Verify the `SUPABASE_URL`, `SUPABASE_KEY`, and `SUPABASE_SECRET_KEY` in your `.env` file<br>- Ensure Supabase service is running<br>- Check if IP address is allowed in Supabase dashboard |
| **Template Rendering Problems** | Path errors, missing context variables | - Check the template path in the view function<br>- Ensure all variables used in templates are passed in the context<br>- Look for typos in template variable names |
| **CSS Styling Issues** | Static files not loading | - Ensure static files are properly collected (`python manage.py collectstatic`)<br>- Check browser console for 404 errors on CSS files<br>- Verify static file settings in `settings.py` |
| **Form Validation Failures** | Missing required fields, invalid data | - Check form submission in browser inspector<br>- Look for validation errors in the form object<br>- Add proper error handling in the view |
| **Admin Access Problems** | Middleware redirect loops | - Clear your browser cookies/session<br>- Check the `AdminMiddleware` configuration<br>- Verify user role in the database |

### Debugging Tips

1. **Enable Django Debug Mode**:
   - Set `DJANGO_DEBUG=True` in your `.env` file to see detailed error pages

2. **Check Server Logs**:
   - Look for error messages in the terminal where the server is running

3. **Inspect Database Queries**:
   - Use Supabase dashboard to monitor API requests
   - Look for unsuccessful HTTP status codes (4xx, 5xx)

4. **Test User Authentication**:
   - Try logging in with the test accounts provided
   - Check if session data is being stored correctly

5. **Verify JavaScript Console**:
   - Open browser developer tools (F12) and check for JavaScript errors
   - Test AJAX functionality in the browser console

## Contributing

Contributions to Royal Cuts Barber Shop are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the repository**:
   - Create your own copy of the project on GitHub

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
   - Add or modify code
   - Update documentation as needed
   - Add tests if possible

4. **Test your changes locally**:
   - Run the application using the provided scripts
   - Ensure all features still work as expected

5. **Commit your changes**:
   ```bash
   git commit -m "Add your meaningful commit message here"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**:
   - Submit a PR from your fork to the main repository
   - Describe your changes in detail

### Contribution Guidelines

- Follow the existing code style and organization
- Keep changes focused on a single purpose
- Test thoroughly before submitting
- Update documentation for any new features
- Be respectful in communications

### Development Areas for Contribution

- **Frontend Enhancements**: Improve UI/UX of the booking system or dashboard
- **Backend Optimization**: Make database queries more efficient
- **New Features**: Add functionality like SMS notifications, online payment, etc.
- **Testing**: Add automated tests for critical functionality
- **Documentation**: Improve or expand existing documentation

Thank you for considering contributing to Royal Cuts Barber Shop!