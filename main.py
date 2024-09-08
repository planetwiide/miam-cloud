# MiamCloud - v3.0.1
# Author: Planetwide
# Description:
# This script sets up a Flask-based web application named "MiamCloud" for uploading, downloading, and managing files.
# The application features an ASCII UI display with animations using the Pystyle library.

# Import required modules
from flask import Flask, request, send_file, redirect
from pystyle import Colorate, Colors, System, Center, Write, Anime
from webbrowser import open_new as open_browser
from socket import gethostname, gethostbyname
from os import listdir, chdir, name as os_name
from os.path import isfile as file_exists

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
     (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          
                                        
                                        '''

# Flask application initialization
app = Flask("MiamCloud")

# Function to read the content of a file and return it
def read_file_contents(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Start the Flask application
def start_flask_app(host: str, port: int):
    return app.run(host, port)

# Main route to display index.html
@app.route('/', methods=['GET'])
def index_route():
    return read_file_contents('front/index.html')

# Function to return text and a status code
def response_with_status(text: str, status_code: int = 200) -> tuple:
    print(f"Response: {text} | Status Code: {status_code}")
    return text, status_code

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_handler():
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

# Route to retrieve a file
@app.route('/get/<filename>', methods=['GET'])
def file_retrieval_route(filename):
    file_path = f'files/{filename}'
    if file_exists(file_path):
        return send_file(file_path, as_attachment=True)
    
    for file in listdir('files'):
        if filename == ''.join(file.split('.')[:-1]):
            return send_file(f'files/{file}', as_attachment=True)
    
    return send_file('files/miamcloud.png', as_attachment=True)

# Route to retrieve an image
@app.route('/images/<image>', methods=['GET'])
def image_retrieval_route(image):
    image_path = f'front/images/{image}'
    if file_exists(image_path):
        return send_file(image_path, as_attachment=True)
    return send_file('files/miamcloud.png', as_attachment=True)

# System configuration with Pystyle
System.Clear()
System.Size(160, 50)
System.Title("MiamCloud")

# Function to display the UI
def display_ui():
    System.Clear()
    print("\n" * 2)
    print(Colorate.Diagonal(Colors.blue_to_purple, Center.XCenter(miamcloud_banner)))
    print("\n" * 5)

# Banner animation display
Anime.Fade(Center.Center(banner_image), Colors.blue_to_purple,
           Colorate.Diagonal, enter=True)

# Main function
def main():
    display_ui()

    # Retrieve hostname and local IP
    hostname, local_ip = gethostname(), gethostbyname(gethostname())
    print(" ")

    # Input for IP and port
    host = Write.Input("Input IP address (press enter to automate): ",
                       Colors.blue_to_purple, interval=0.002) or local_ip

    print(" ")

    port = Write.Input("Input port (press enter to automate): ",
                       Colors.blue_to_purple, interval=0.002) or "8080"
    
    try:
        port = int(port)
    except ValueError:
        Colorate.Error("Invalid port; port should be an integer.")
        return

    print(" ")
    Write.Input("Press enter to run the server ", Colors.blue_to_purple, interval=0.002)

    # Generate and start the URL
    url = f"http://{host}:{port}/"
    open_browser(url)
    
    display_ui()
    print(Colorate.Vertical(Colors.blue_to_purple, f"   Running on: {url}"))
    print(Colors.green, end='')

    start_flask_app(host=host, port=port)

# Entry point
if __name__ == '__main__':
    while True:
        main()
