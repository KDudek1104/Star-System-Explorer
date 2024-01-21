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
