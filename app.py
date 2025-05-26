import os
from flask import Flask, render_template, request, redirect, url_for
import urllib.parse # Used for URL encoding for mailto links

app = Flask(__name__)

# --- Static value for Site ID ---
# This will now be a fixed value, not from a database or dropdown
FIXED_SITE_ID = "Jackson Memorial Hospital"

# --- Simulate a database for Installed Products ---
# This list will populate the Installed Product dropdown
INSTALLED_PRODUCTS = [
    "MX40", # Default selected
    "MMX",
    "X3",
    "MX450",
    "MX550"
]

# --- Customer Contact, Phone, and Email Data ---
# This dictionary will populate the Customer Contact dropdown and provide phone numbers and emails
CUSTOMER_CONTACTS = {
    "Michael Brown": {"phone": "954-949-0025", "email": "mbrown8@jhsmiami.org"},
    "John Burfeindt": {"phone": "954-309-2449", "email": "JBurfeindt@JHSmiami.org"},
    "Lloyd Isaac": {"phone": "954-243-9742", "email": "lisaac@jhsmiami.org"},
    "Osee Desir": {"phone": "786-832-1410", "email": "osee.desir@jhsmiami.org"}
}

# --- Default Assign To value ---
DEFAULT_ASSIGN_TO = "Petr Pasek"


@app.route('/')
def index():
    """
    Renders the main form page, passing the fixed site ID, installed products,
    customer contacts, and default assign to value to the template.
    """
    return render_template('form.html', 
                           fixed_site_id=FIXED_SITE_ID, 
                           installed_products=INSTALLED_PRODUCTS,
                           customer_contacts=CUSTOMER_CONTACTS,
                           default_assign_to=DEFAULT_ASSIGN_TO)

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handles the form submission, processes the data, and prepares it for an email client.
    """
    if request.method == 'POST':
        # Site ID is now a fixed value, not from form input
        site_id = FIXED_SITE_ID
        
        # Retrieve other data from the form
        serial_num = request.form.get('serialNum')
        installed_product = request.form.get('installedProduct') # Changed from 'ip'
        customer_contact = request.form.get('customerContact') # Value from dropdown
        email = request.form.get('email') # This will be the populated email
        phone = request.form.get('phone') # This will be the populated phone number
        problem = request.form.get('problem')
        priority = request.form.get('priority') # Now 1-4
        hours_needed = request.form.get('hoursNeeded')
        assign_for = request.form.get('assignFor')
        assign_to = request.form.get('assignTo') # Defaulted to Petr Pasek

        # Construct the email subject
        problem_text = problem if problem is not None else ''
        email_subject = f"WO Request: {site_id} - {problem_text[:50]}{'...' if len(problem_text) > 50 else ''}"

        # Construct the email body
        email_body = f"""
New WO Request:

Site ID: {site_id or 'N/A'}
Serial #: {serial_num or 'N/A'}
Installed Product: {installed_product or 'N/A'}
Customer Contact: {customer_contact or 'N/A'}
E-mail: {email or 'N/A'}
Phone: {phone or 'N/A'}
Problem: {problem or 'N/A'}
Priority: {priority or 'N/A'}
Hours Needed: {hours_needed or 'N/A'}
Assign For: {assign_for or 'N/A'}
Assign To: {assign_to or 'N/A'}
        """.strip() 

        # Encode the subject and body for a mailto link
        encoded_subject = urllib.parse.quote(email_subject)
        encoded_body = urllib.parse.quote(email_body)

        mailto_link = f"mailto:pmccdispatch@philips.com?subject={encoded_subject}&body={encoded_body}"
        return render_template('confirmation.html', mailto_link=mailto_link, email_body=email_body)

if __name__ == '__main__':
    app.run(debug=True)
