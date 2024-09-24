# MiamCloud - v4.0.0
# Author: Planetwide
# Description:
# This script sets up a Flask-based web application named "MiamCloud" for 
# uploading, downloading, and managing files. It features an ASCII UI display 
# with animations using the Pystyle library.

# Import required modules
from flask import Flask, request, send_file, redirect, url_for, session
from pystyle import Colorate, Colors, System, Center, Write, Anime
from webbrowser import open_new as open_browser
from socket import gethostname, gethostbyname
import os
import yaml
from os import listdir, chdir, name as os_name
from os.path import isfile as file_exists
import secrets

# ASCII banner for MiamCloud
miamcloud_banner = """
              d8b                       
              Y8P                       

88888b.d88b.  888  8888b.  88888b.d88b. 
888 "888 "88b 888     "88b 888 "888 "88b
888  888  888 888 .d888888 888  888  888
888  888  888 888 888  888 888  888  888
888  888  888 888 "Y888888 888  888  888                                    

         888                        888 
         888                        888 
         888                        888 
 .d8888b 888  .d88b.  888  888  .d88888 
d88P"    888 d88""88b 888  888 d88" 888 
888      888 888  888 888  888 888  888 
Y88b.    888 Y88..88P Y88b 888 Y88b 888 
 "Y8888P 888  "Y88P"   "Y88888  "Y88888 
       v3.0.3 - @planetwide
"""

# ASCII banner with image
banner_image = '''
                _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
            _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
        ((    (..__.:'-'   .+(   )   ` _`  ) )                 
       `(       ) )       (   .  )     (   )  ._   
         ` __.:'   )     (   (   ))     `-'.-(`  ) 
      ( )       --'       `- __.'         :(      )) 
     (_.'          .')                    `(    )  )))
                  (_  )                     ` __.:'          

'''

# Flask application initialization with a dynamically generated secret key for session management
app = Flask("MiamCloud")
app.secret_key = secrets.token_urlsafe(16)

# Function to read the content of a file and return it
def read_file_contents(filename: str):
    """Read the contents of a file and return it as a string."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Function for authenticating a user by checking username and password in users.yml
def auth(username, pwd):
    """Authenticate a user by verifying credentials in users.yml."""
    with open('users.yml', 'r') as file:
        users = yaml.safe_load(file)
    
    for user in users['users']:
        if user['username'] == username and user['password'] == pwd:
            print("Authenticated:", username)
            return True
            
    print("Failed to Authenticate:", username)
    return False

# Route for login page and authentication handling
@app.route('/login', methods=['GET', 'POST'])
def login_route():
    """Handle user login and authentication."""
    next_url = request.args.get('next', '/')  # Set default next URL to root
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # If user is authenticated, store the session and redirect to next URL
        if auth(username, password):
            session['authenticated'] = True
            session.modified = True  # Mark session as changed
            return redirect(next_url)
        
        # Redirect back to the login page if authentication fails
        return redirect(url_for('login_route'))
    
    # Display the login HTML page
    return read_file_contents('front/login.html')

# Main index route
@app.route('/', methods=['GET'])
def index_route():
    """Serve the index page if the user is authenticated."""
    if 'authenticated' not in session or not session['authenticated']:
        return redirect(url_for('login_route'))
    
    return read_file_contents('front/index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_handler():
    """Handle file uploads from the user."""
    try:
        filename = request.args.get('filename', '').strip()
        if not filename:
            return response_with_status('error, invalid filename provided.')
        
        uploaded_file = request.files.get('file')
        if uploaded_file:
            uploaded_file.save(f'files/{filename}')
            return redirect('/')
        
        return response_with_status('error, no file uploaded.')
        
    except Exception as error:
        return response_with_status(f'error: {str(error)}')

# Route to retrieve a file by filename
@app.route('/get/<filename>', methods=['GET'])
def file_retrieval_route(filename):
    """Retrieve a file by its filename, or return a default image if not found."""
    file_path = f'files/{filename}'
    
    if file_exists(file_path):
        return send_file(file_path, as_attachment=True)
    
    # Attempt to match filename without extension
    for file in listdir('files'):
        if filename == ''.join(file.split('.')[:-1]):
            return send_file(f'files/{file}', as_attachment=True)
    
    return send_file('files/miamcloud.png', as_attachment=True)

# Route to retrieve images from the 'front/images' folder
@app.route('/images/<image>', methods=['GET'])
def image_retrieval_route(image):
    """Retrieve images from the front/images folder."""
    image_path = f'front/images/{image}'
    
    if file_exists(image_path):
        return send_file(image_path, as_attachment=True)
    
    return send_file('files/miamcloud.png', as_attachment=True)

# Function to return a response with a status code
def response_with_status(text: str, status_code: int = 200) -> tuple:
    """Return a response text with a specified status code."""
    print(f"Response: {text} | Status Code: {status_code}")
    return text, status_code

# System configuration with Pystyle
System.Clear()
System.Size(160, 50)
System.Title("🌩️ miamcloud 🌩️")
login = os.getlogin()

# Function to display the UI
def display_ui():
    """Display the MiamCloud user interface."""
    System.Clear()
    print("\n" * 2)
    print(Colorate.Diagonal(Colors.blue_to_purple, Center.XCenter(miamcloud_banner)))
    print(" ")
    print(Colorate.Diagonal(Colors.blue_to_purple, Center.XCenter("v3.0.3 - https://github.com/planetwiide/miam-cloud")))
    print("\n" * 5)

# Banner animation display
Anime.Fade(Center.Center(banner_image), Colors.blue_to_purple,
           Colorate.Diagonal, enter=True)

# Start the Flask application
def start_flask_app(host: str, port: int):
    """Start the Flask application on the specified host and port."""
    return app.run(host, port)

# Main function to initialize the server
def main():
    """Main function to initialize and run the MiamCloud server."""
    display_ui()

    # Retrieve hostname and local IP address
    hostname, local_ip = gethostname(), gethostbyname(gethostname())
    print(" ")

    # Get user input for IP address and port, with default values
    host = Write.Input(login + " ┃ input IP address (0.0.0.0 for all devices, press enter to automate): ",
                       Colors.blue_to_purple, interval=0.003) or local_ip
    print(" ")
    port = Write.Input(login + " ┃ input port (press enter to automate 8080): ",
                       Colors.blue_to_purple, interval=0.003) or "8080"
    
    try:
        port = int(port)
    except ValueError:
        Colorate.Error(login + " ┃ invalid port; port should be an integer.")
        return

    print(" ")
    Write.Input(login + " ┃ press enter to run the server ", Colors.blue_to_purple, interval=0.003)

    # Generate the URL and start the Flask server
    url = f"http://{host}:{port}/"
    
    display_ui()
    print(Colorate.Vertical(Colors.blue_to_purple, f"{login} ┃ running on: {url}"))
    print(Colors.green, end='')

    start_flask_app(host=host, port=port)

# Entry point to run the application
if __name__ == '__main__':
    while True:
        main()
