# Royal Cuts Premium Indian Barber Shop

A full-featured barbershop management system with booking functionality, service management, stylist profiles, and admin dashboard.

## Features

- User and admin login/registration
- Services browsing with categories
- Stylist profiles and reviews
- Online booking system with time slot availability
- Admin dashboard for managing appointments, services, and stylists

## Installation Instructions

### Prerequisites
- Python 3.10+ 
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```
   git clone <your-repository-url>
   cd barbershop
   ```

2. **Create a virtual environment (optional but recommended)**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables**

   Create a `.env` file in the project root with the following:
   ```
   SUPABASE_URL=https://phuhhrqzzqdfheuhqofi.supabase.co
   SUPABASE_KEY=your-supabase-api-key
   SUPABASE_SECRET_KEY=your-supabase-secret-key
   ```

6. **Run migrations (if needed)**
   ```
   python manage.py migrate
   ```

7. **Run the development server**
   ```
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## Admin Login
- Username: admin
- Password: admin123

## Default User Login
- Username: testuser
- Password: password123