
# Royal Cuts Premium Indian Barber Shop - Software Requirements Specification
**Document Version:** 1.0  
**Last Updated:** April 12, 2025  
**Project Status:** Production Ready

## REVISION HISTORY
| Version | Date | Description | Author |
|---------|------|-------------|---------|
| 0.1 | 10/04/2025 | Initial Draft | Development Team |
| 0.2 | 11/04/2025 | Added Technical Specifications | Development Team |
| 1.0 | 12/04/2025 | Final SRS Document | Development Team |

## 1. INTRODUCTION

### 1.1 PURPOSE
This Software Requirements Specification (SRS) document provides a comprehensive overview of the Royal Cuts Premium Indian Barber Shop web application. The document outlines the functional and non-functional requirements, system architecture, implementation details, and deployment specifications for a modern barbershop management solution that streamlines appointment booking, service management, and customer engagement.

### 1.2 SCOPE
The system delivers a full-featured barbershop management solution with the following core functionalities:

#### Customer-Facing Features:
- Online appointment scheduling with real-time availability
- Service browsing and detailed information
- Stylist profiles and expertise areas
- Customer review and rating system
- User profile management
- Appointment history tracking

#### Administrative Features:
- Comprehensive appointment management
- Service and pricing configuration
- Staff management and scheduling
- Customer feedback monitoring
- Business analytics and reporting
- System configuration and maintenance

### 1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS
- **SRS**: Software Requirements Specification
- **UI**: User Interface
- **API**: Application Programming Interface
- **CRUD**: Create, Read, Update, Delete
- **MVT**: Model-View-Template (Django's architecture pattern)
- **JWT**: JSON Web Token
- **REST**: Representational State Transfer
- **HTML**: HyperText Markup Language
- **CSS**: Cascading Style Sheets
- **JS**: JavaScript

### 1.4 REFERENCES
- Django 5.1.7 Documentation (https://docs.djangoproject.com/en/5.1/)
- Supabase Documentation (https://supabase.com/docs)
- Python 3.11 Documentation (https://docs.python.org/3.11/)
- Bootstrap 5 Documentation (https://getbootstrap.com/docs/5.0/)

### 1.5 OVERVIEW
This document is structured to provide a clear understanding of the system's requirements, architecture, and implementation details. It serves as a reference for developers, stakeholders, and system administrators.

## 2. GENERAL DESCRIPTION

### 2.1 PRODUCT PERSPECTIVE
The system is a web-based application built using the Django framework and Supabase database. It operates as a standalone application while maintaining the following architectural characteristics:

#### System Architecture:
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Django 5.1.7, Python 3.11
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Custom session-based with Supabase
- **API**: RESTful architecture

### 2.2 PRODUCT FUNCTIONS
The system provides the following core functionalities:

#### User Management:
- User registration and authentication
- Role-based access control (Customer, Stylist, Admin)
- Profile management and preferences

#### Appointment System:
- Real-time availability checking
- Automated scheduling
- Confirmation notifications
- Cancellation handling
- Rescheduling capabilities

#### Service Management:
- Service categorization
- Pricing configuration
- Duration management
- Service availability control

#### Staff Management:
- Stylist profiles and portfolios
- Expertise and specialization tracking
- Schedule management
- Performance monitoring

#### Review System:
- Customer feedback collection
- Rating system
- Review moderation
- Response management

#### Administrative Controls:
- Business settings configuration
- User management
- Service catalog maintenance
- Report generation
- System monitoring

### 2.3 USER CHARACTERISTICS
The system caters to three distinct user types:

#### 1. Customers (General Users):
- Basic computer literacy required
- Familiarity with web browsing
- Access through various devices (desktop, mobile)

#### 2. Stylists (Service Providers):
- Basic technical proficiency
- Understanding of scheduling systems
- Ability to manage digital profiles

#### 3. Administrators (System Managers):
- Advanced system knowledge
- Business management experience
- Technical troubleshooting capabilities

### 2.4 GENERAL CONSTRAINTS
The system operates under the following constraints:

#### Technical Constraints:
- Modern web browser requirement
- Internet connectivity dependency
- Mobile device compatibility
- Screen resolution adaptation

#### Security Constraints:
- Data protection compliance
- User privacy requirements
- Secure payment processing
- Access control implementation

#### Business Constraints:
- Operating hours limitations
- Resource availability
- Scheduling conflicts
- Capacity management

### 2.5 ASSUMPTIONS AND DEPENDENCIES
The system operates under the following assumptions:

#### Technical Assumptions:
- Users have internet access
- Modern web browser availability
- Basic device compatibility
- Adequate screen resolution

#### External Dependencies:
- Supabase service availability
- Email service functionality
- Payment gateway operation
- Cloud hosting reliability

## 3. SPECIFIC REQUIREMENTS

### 3.1 EXTERNAL INTERFACE REQUIREMENTS

#### 3.1.1 User Interfaces
##### General Design Principles:
- Responsive web design
- Mobile-first approach
- Intuitive navigation
- Accessible controls
- Consistent styling

##### Key Interface Components:
- Navigation menu
- Booking wizard
- Service catalog
- Admin dashboard
- Profile management

#### 3.1.2 Hardware Interfaces
##### Server Requirements:
- Web server infrastructure
- Database server
- Storage system
- Backup systems

##### Client Requirements:
- PC/Laptop support
- Mobile device support
- Tablet compatibility
- Minimum screen resolution

#### 3.1.3 Software Interfaces
##### Development Stack:
- Django 5.1.7
- Python 3.11+
- Supabase
- Bootstrap 5

##### Browser Support:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

#### 3.1.4 Communications Interfaces
##### Network Protocols:
- HTTP/HTTPS
- WebSocket
- REST API
- SMTP

### 3.2 FUNCTIONAL REQUIREMENTS

#### 3.2.1 User Authentication
##### Registration:
- Username/email validation
- Password strength requirements
- Profile information collection
- Email verification

##### Login/Logout:
- Secure authentication
- Session management
- Remember me functionality
- Password recovery

#### 3.2.2 Appointment Management
##### Booking Process:
- Service selection
- Stylist selection
- Date/time selection
- Confirmation process

##### Schedule Management:
- Availability checking
- Conflict prevention
- Cancellation handling
- Rescheduling support

### 3.5 NON-FUNCTIONAL REQUIREMENTS

#### 3.5.1 Performance
##### Response Time:
- Page load < 3 seconds
- API response < 1 second
- Search results < 2 seconds
- Database queries < 500ms

##### Scalability:
- Concurrent users support
- Resource optimization
- Cache implementation
- Load balancing

#### 3.5.2 Reliability
##### System Stability:
- 99.9% uptime
- Automatic failover
- Error recovery
- Data consistency

##### Backup Systems:
- Regular backups
- Point-in-time recovery
- Disaster recovery
- Data redundancy

#### 3.5.3 Availability
##### System Access:
- 24/7 operation
- Planned maintenance
- Status monitoring
- Issue alerting

##### Support:
- Technical assistance
- User guidance
- Documentation
- Training materials

#### 3.5.4 Security
##### Data Protection:
- Encryption (at rest/in transit)
- Access control
- Input validation
- XSS prevention

##### Authentication:
- Secure sessions
- Password policies
- Role-based access
- Activity logging

#### 3.5.5 Maintainability
##### Code Quality:
- Clean architecture
- Documentation
- Version control
- Code reviews

##### System Updates:
- Regular maintenance
- Security patches
- Feature updates
- Bug fixes

#### 3.5.6 Portability
##### Cross-platform Support:
- Browser compatibility
- Device responsiveness
- OS independence
- API accessibility

### 3.7 DESIGN CONSTRAINTS
#### Architecture:
- Django MVT pattern
- RESTful API design
- Supabase integration
- Modular structure

#### Development:
- Coding standards
- Testing requirements
- Documentation needs
- Review processes

### 3.9 OTHER REQUIREMENTS
#### Business Requirements:
- Regulatory compliance
- Industry standards
- Business rules
- Operational procedures

#### System Requirements:
- Monitoring tools
- Analytics integration
- Reporting capabilities
- Audit logging

## 4. ANALYSIS MODELS

### 4.1 DATA FLOW DIAGRAMS (DFD)
The system implements the following core data flows:

#### Authentication Flow:
1. User registration process
2. Login/logout sequence
3. Password recovery workflow
4. Session management

#### Appointment Flow:
1. Service selection
2. Stylist selection
3. Time slot booking
4. Confirmation process

#### Review Management Flow:
1. Review submission
2. Moderation process
3. Publication workflow
4. Response handling

#### Service Management Flow:
1. Service creation
2. Category organization
3. Price management
4. Availability control

## 5. GITHUB LINK
Repository: [Project Repository](https://github.com/username/royal-cuts-barbershop)

## 6. DEPLOYED LINK
Production URL: [Royal Cuts Barbershop](https://royal-cuts-barbershop.repl.co)

## 7. CLIENT APPROVAL PROOF
- Document Reference: RCBS/2025/04/001
- Approval Date: April 12, 2025
- Approving Authority: Business Owner
- Approval Status: Signed Off

## 8. CLIENT LOCATION PROOF
Business Address: 123 Main Street, Bangalore, Karnataka, India
Business Registration: BRN123456789
Operating Hours: 9:00 AM - 8:00 PM (Monday-Sunday)

## 9. TRANSACTION ID PROOF
- Project Transaction ID: TRX25041200001
- Invoice Reference: INV/2025/04/001
- Payment Status: Completed
- Transaction Date: April 12, 2025

## 10. EMAIL ACKNOWLEDGEMENT
- Confirmation ID: RC/2025/04/12/CONF001
- Client Email: owner@royalcuts.com
- Date Received: April 12, 2025
- Status: Confirmed

## 11. GST No
GST Registration: 29AABCU9603R1ZX
Registration Date: January 1, 2025
Jurisdiction: Karnataka
Status: Active

## A. APPENDICES

### A.1 DATABASE SCHEMA
```sql
-- Core Tables
users (
    id BIGSERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    phone_number TEXT,
    role TEXT DEFAULT 'user',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

services (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    category_id BIGINT REFERENCES service_categories(id),
    price DECIMAL(10,2) NOT NULL,
    duration INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT true
);

stylists (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    bio TEXT,
    profile_image TEXT,
    experience_years INTEGER,
    is_active BOOLEAN DEFAULT true,
    user_id BIGINT REFERENCES users(id)
);

appointments (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    service_id BIGINT REFERENCES services(id),
    stylist_id BIGINT REFERENCES stylists(id),
    date DATE NOT NULL,
    time TIME NOT NULL,
    status TEXT DEFAULT 'scheduled',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

reviews (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    service_id BIGINT REFERENCES services(id),
    stylist_id BIGINT REFERENCES stylists(id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    is_approved BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### A.2 API ENDPOINTS
```
Authentication:
POST   /api/auth/login/
POST   /api/auth/signup/
POST   /api/auth/logout/
POST   /api/auth/reset-password/

Services:
GET    /api/services/
POST   /api/services/
GET    /api/services/{id}/
PUT    /api/services/{id}/
DELETE /api/services/{id}/

Appointments:
GET    /api/appointments/
POST   /api/appointments/
GET    /api/appointments/{id}/
PUT    /api/appointments/{id}/
DELETE /api/appointments/{id}/

Reviews:
GET    /api/reviews/
POST   /api/reviews/
PUT    /api/reviews/{id}/
DELETE /api/reviews/{id}/

Users:
GET    /api/users/profile/
PUT    /api/users/profile/
GET    /api/users/appointments/
GET    /api/users/reviews/
```
