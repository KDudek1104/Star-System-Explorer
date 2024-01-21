# Star System Explorer

Star System Explorer is a Django web application for exploring and managing information about star systems and stars.

## Features

### 1. Star System and Star Management

- **View Star Systems and Stars:**
  - Explore a list of existing star systems and stars.
  - Access detailed information about each star system and star.

- **Add, Edit, and Delete Operations:**
  - Add new star systems and stars through user-friendly forms.
  - Edit existing star system and star details.
  - Delete unnecessary star systems and stars.

### 2. Data Upload and Download

- **Upload Star Data:**
  - Use the "Load Data" feature to upload star data in JSON format.
  - Create or update star systems and stars based on the uploaded data.

- **Download Star Data:**
  - Utilize the "Download Data" feature to get a JSON file containing star information.
  - Convenient for backing up data or sharing information.

### 3. Search Functionality

- **Search by Star Name:**
  - Search for stars by their names using the search form.
  - Quickly locate specific stars in the system.

### 4. User-Friendly Interface

- **Responsive Design:**
  - Enjoy a user-friendly and responsive interface for easy navigation.
  - Accessible on various devices.

### 5. User Authentication and Authorization

Implement a robust user authentication and authorization system to enhance the security and personalize user experiences within the Star System Explorer application. Users should be able to register, log in, and log out. Additionally, different levels of access permissions should be established to control user interactions, ensuring that only authorized users can perform specific actions, such as adding, modifying, or deleting star system data.

#### Key Points:
- **User Registration:** Allow users to create accounts by providing necessary details like username, email, and password.
- **User Login/Logout:** Enable users to log in securely with their credentials and log out when they are done using the application.
- **Access Control:** Implement role-based access control to distinguish between regular users and administrators. Define specific permissions for each role.
- **Profile Management:** Provide users with the ability to manage their profiles, including updating personal information and changing passwords.
- **Secure Password Handling:** Implement secure password storage using hashing techniques to protect user account information.

By incorporating user authentication and authorization, you enhance the overall security of the application and tailor the user experience based on individual user roles and permissions.


## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- JavaScript

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/StarSystemExplorer.git
   cd StarSystemExplorer
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Open your browser and go to http://127.0.0.1:8000/admin/ to log in as the superuser and manage the data.**

8. **Explore the main application at http://127.0.0.1:8000/explorer/.**
