Support Request Generator
This is a simple web application built with Flask that allows users to submit support requests by filling out a form. The application then generates a pre-filled email (via a mailto: link) and provides the email body for easy copying.

Features
Fixed Site ID: Automatically sets "Jackson Memorial Hospital" as the Site ID.

Installed Product Dropdown: Select from common installed products (MX40, MMX, X3, MX450, MX550), with "MX40" as the default.

Dynamic Customer Contact: Choose a customer contact from a dropdown, and their associated phone number and email address will automatically populate the respective fields.

Default Problem Description: The "Problem" field defaults to "Device won't boot up".

Priority Selection: Select priority from 1 to 4, with "2" as the default.

Default Hours Needed: The "Hours Needed" field defaults to "2".

Date Picker for "Assign For": Use a native calendar input to select a date for assignment.

Default "Assign To": The "Assign To" field defaults to "Petr Pasek".

Email Generation: Creates a mailto: link to open your default email client with the subject and body pre-filled.

Copy to Clipboard: Provides an option to copy the generated email body to the clipboard.

Responsive Design: Styled with Tailwind CSS for a clean and mobile-friendly interface.

Setup Instructions
To run this application locally, follow these steps:

Prerequisites
Python 3.x installed on your system.

pip (Python package installer).

Installation
Clone the repository (or download the files):
If you're using Git:

git clone <your-repository-url>
cd <your-repository-name>

If you downloaded the files, navigate to the project directory.

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows (Command Prompt):

venv\Scripts\activate.bat

On Windows (PowerShell):

.\venv\Scripts\Activate.ps1

Install Flask:

pip install Flask

Project Structure
Ensure your project directory has the following structure:

your_project_name/
├── app.py
└── templates/
    ├── form.html
    └── confirmation.html

Usage
Run the Flask application:
With your virtual environment activated, navigate to the root of your project directory (where app.py is located) and run:

python app.py

You should see output similar to this:

 * Serving Flask app "app"
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Access the application in your browser:
Open your web browser and navigate to:

http://127.0.0.1:5000/

Fill out the form:

The "Site ID" will be pre-filled.

Select an "Installed Product" from the dropdown.

Choose a "Customer Contact" to automatically populate the "E-mail" and "Phone" fields.

The "Problem" field will have a default message.

Select a "Priority" (defaulting to 2).

The "Hours Needed" field will default to 2.

Click on "Assign For" to open a calendar and select a date.

The "Assign To" field will default to "Petr Pasek".

Generate Email:
Click the "Generate Email & Copy" button. This will redirect you to a confirmation page.

Send Email or Copy:
On the confirmation page, you can:

Click "Click to Open Email Client" to open your default email application with the subject and body pre-filled.

Copy the "Email Body Preview" text to your clipboard for manual pasting.

Customization
app.py:

Modify FIXED_SITE_ID, INSTALLED_PRODUCTS, CUSTOMER_CONTACTS, DEFAULT_PROBLEM, DEFAULT_PRIORITY, DEFAULT_HOURS_NEEDED, and DEFAULT_ASSIGN_TO to change default values and dropdown options.

Change the mailto: recipient email address on line mailto_link = f"mailto:pmccdispatch@philips.com?subject={encoded_subject}&body={encoded_body}" to your desired recipient.

templates/form.html:

Adjust the form layout and styling using Tailwind CSS classes.

Add or remove input fields as needed.

templates/confirmation.html:

Customize the confirmation message and layout.
