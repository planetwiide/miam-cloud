# miamcloud - v3.0.1
# author: planetwide
# description: 
# this script creates a flask-based web application called "miamcloud" that allows users to upload, download, and manage files.
# the application also includes an ascii ui display with animations using the pystyle library.

# import necessary modules
from os import listdir, chdir, name as os_name
from os.path import isfile as is_file_path
from flask import Flask, request, send_file, redirect
from pystyle import Colorate, Colors, System, Center, Write, Anime
from webbrowser import open_new as start_browser
from socket import gethostname, gethostbyname

# ascii banner with image
banner = '''
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

# ascii banner for miamcloud
miamcloud = """
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



# flask app initialization
app = Flask("miamcloud")

# start flask app
def run(host: str, port: int):
    return app.run(host, port)

# main route to display index.html
@app.route('/', methods=['GET'])
def main_route():
    return render('front/index.html')

# function to return text and a status code
def ren(text: str, status_code: int = 200) -> tuple:
    print(f"Response: {text} | Status Code: {status_code}")
    return text, status_code

# route to retrieve a file
@app.route('/get/<filename>', methods=['GET'])
def get_route(filename):
    file_path = f'files/{filename}'
    if is_file_path(file_path):
        return send_file(file_path, as_attachment=True)
    
    for file in listdir('files'):
        if filename == ''.join(file.split('.')[:-1]):
            return send_file(f'files/{file}', as_attachment=True)
    
    return send_file('files/miamcloud.png', as_attachment=True)

# function to read the contents of a file and return it
def render(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
      
# route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_route():
    try:
        name = request.args.get('filename', '').strip()
        if not name:
            return ren('error, invalid filename provided.')
        
        file = request.files.get('file')
        if file:
            file.save(f'files/{name}')
            return redirect('/')
        return ren('error, no file uploaded.')
    except Exception as e:
        return ren(f'error: {str(e)}')



# route to retrieve an image
@app.route('/images/<image>', methods=['GET'])
def image_route(image):
    image_path = f'front/images/{image}'
    if is_file_path(image_path):
        return send_file(image_path, as_attachment=True)
    return send_file('files/miamcloud.png', as_attachment=True)



# function to display the ui
def ui():
    System.Clear()
    print("\n" * 2)
    print(Colorate.Diagonal(Colors.blue_to_purple, Center.XCenter(miamcloud)))
    print("\n" * 5)
  
# system configuration with pystyle
System.Clear()
System.Size(160, 50)
System.Title("miamcloud")

# banner animation display
Anime.Fade(Center.Center(banner), Colors.blue_to_purple,
           Colorate.Diagonal, enter=True)

# main function
def main():
    ui()

    # automate hostname and IP retrieval
    hostname, local_ip = gethostname(), gethostbyname(gethostname())
    print(" ")
    # input for IP and port
    host = Write.Input("input IP address (press enter to automate): ",
                    Colors.blue_to_purple, interval=0.005) or local_ip

    print(" ")

    port = Write.Input("input port (press enter to automate): ",
                    Colors.blue_to_purple, interval=0.005) or "8080"
    
    try:
        port = int(port)
    except ValueError:
        Colorate.Error("invalid port; port should be an integer.")
        return

    print(" ")
    Write.Input("press enter to run the server ", Colors.blue_to_purple, interval=0.005)

    # generate and start the URL
    url = f"http://{host}:{port}/"
    start_browser(url)
    
    ui()
    print(Colorate.Vertical(Colors.blue_to_purple, f"   running on: {url}"))
    print(Colors.green, end='')

    run(host=host, port=port)

# entry point
if __name__ == '__main__':
    while True:
        main()
