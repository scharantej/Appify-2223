## Problem

### Create a celebration website to celebrate Stream being able to successfully be created.

## Flask Application Design

### HTML Files 

**index.html:**

- Home page of the website
- Content:
  - Header with the website title and subtitle
  - Main section with information and images related to Stream's creation
  - Footer with copyright and contact information

**team.html:**

- Page listing the team members who contributed to creating Stream
- Content:
  - Header with the page title
  - Table or list of team members with their names, roles, and social media links
  - Footer with copyright and contact information

**contact.html:**

- Page providing contact information for the website owners
- Content:
  - Header with the page title
  - Form for visitors to send messages or inquiries
  - Email address and phone number for direct contact
  - Footer with copyright and contact information

### Routes

**app.py:**

- Python file containing Flask application code
- Imports necessary modules and initializes the Flask application
- Defines routes for the HTML pages
- Defines routes for handling form submissions (if applicable)

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```