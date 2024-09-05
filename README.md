# Miamcloud - v3.0.1

Author: planetwide

## Description

**Miamcloud** is a Flask-based web application designed to facilitate easy file management through a web interface. Users can upload, download, and retrieve files, as well as images, from their server. The application integrates with **pystyle** to provide an interactive, animated user interface with ASCII banners and a clean UI display. 

## Features

- **File Uploading**: Upload files directly through the web interface.
- **File Downloading**: Retrieve uploaded files through a secure download link.
- **Flask-based Web App**: Easy to deploy on any Flask-supported platform.
- **Dynamic IP and Port Handling**: Allows users to specify their host IP and port dynamically or use automatic defaults.
- **Simple and Clear Code Structure**: Modular functions for easy understanding and customization.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Routes](#file-routes)
- [System Configuration](#system-configuration)
- [UI & Animations](#ui--animations)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Prerequisites

Before you start, ensure you have the following:

- Python 3.6 or higher
- Flask
- pystyle (`pip install pystyle`)

### Steps

1. Clone the repository or download the project files:
   ```bash
   git clone https://github.com/planetwide/miamcloud.git
   cd miamcloud
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the `miamcloud` script:
   ```bash
   python miamcloud.py
   ```

2. The app will prompt you for an IP address and port. You can either press enter for automatic setup or specify your own values.

3. Once the server starts, visit the displayed URL (e.g., `http://127.0.0.1:8080`) in your browser to access the web interface.

---

## File Routes

- **GET /**: Returns the `index.html` page located in `front/`.
- **POST /upload**: Handles file uploads.
    - **Parameters**:
      - `file`: The file to upload.
      - `filename`: The name to save the file as.
- **GET /get/<filename>**: Retrieves a file by its filename. If the file does not exist, it returns a default image.
- **GET /images/<image>**: Retrieves an image from the `front/images/` folder. If the image does not exist, it returns a default image.

---

## System Configuration

The `pystyle` library is used to customize the terminal interface. It configures the following:

- **Terminal Size**: The terminal window is set to 160x50.
- **Terminal Title**: Sets the window title to "miamcloud".
- **Clearing the Screen**: Clears the terminal window before displaying the interface.

---

## UI & Animations

The script includes two ASCII banners (`miamcloud` and `banner`) which are displayed in the terminal. The `pystyle.Anime.Fade()` function creates a fade-in effect for the banner, giving it a smooth and animated display.

---

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

### Steps for Contribution:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes.
4. Push the changes to your fork.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License.