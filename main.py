
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Home page of the website.

    Contains the website title, subtitle, and information and images related to Stream's creation.
    """
    return render_template('index.html')

@app.route('/team')
def team():
    """Page listing the team members who contributed to creating Stream.

    Includes a table or list of team members with their names, roles, and social media links.
    """
    team_members = [
        {'name': 'Alice', 'role': 'Developer', 'github': 'https://github.com/alice'},
        {'name': 'Bob', 'role': 'Designer', 'twitter': 'https://twitter.com/bob'},
        {'name': 'Carol', 'role': 'Tester', 'linkedin': 'https://www.linkedin.com/in/carol'},
    ]
    return render_template('team.html', team_members=team_members)

@app.route('/contact')
def contact():
    """Page providing contact information for the website owners.

    Includes a form for visitors to send messages or inquiries, an email address, and a phone number for direct contact.
    """
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
