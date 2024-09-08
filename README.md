![miamcloud](https://github.com/user-attachments/assets/8a6895a6-044b-40c2-b494-e700a61f1215)

![⭐](https://img.shields.io/github/stars/planetwiide/miam-cloud?style=social)
![🍴](https://img.shields.io/github/forks/planetwiide/miam-cloud?style=social)
![🐞](https://img.shields.io/github/issues/planetwiide/miam-cloud)
![⚡](https://img.shields.io/github/commit-activity/m/planetwiide/miam-cloud)
![🆙](https://img.shields.io/github/last-commit/planetwiide/miam-cloud)
![📚](https://img.shields.io/github/license/planetwiide/miam-cloud)


# 🌩️ miamcloud - v3.0.1

_author: [planetwide](https://github.com/planetwiide)_

---

## ✨ description

**miamcloud** is a flask-based web app designed to make file management simple and accessible through a sleek web interface. easily upload, download, and manage files or images directly from your server. the app also integrates with **pystyle** for a visually appealing experience, including interactive ascii banners and a clean terminal display.

---

## 🌟 features

- 🚀 **file uploading**: upload files effortlessly via the web interface.
- 🎯 **file downloading**: securely retrieve files through a custom download link.
- 🛠️ **flask-based**: works on any flask-supported platform, making deployment a breeze.
- 🌐 **dynamic ip & port**: automatically detects ip and port, or set them manually if preferred.
- 🧩 **clean code**: modular and easy-to-follow structure, perfect for customization.

---

## 📜 table of contents

- [📥 installation](#installation)
- [📖 usage](#usage)
- [🗂️ file routes](#file-routes)
- [🤝 contributing](#contributing)
- [🐞 issues](#issues)
- [📝 license](#license)
- [🖼️ preview](#preview)

---

## 📥 installation

### prerequisites

before starting, make sure you have:

- python 3.6+
- flask
- pystyle (`pip install pystyle`)

### steps

1. clone the repo or download the project files:
   ```bash
   git clone https://github.com/planetwiide/miam-cloud.git
   cd miam-cloud
   ```

2. install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 usage

1. start the app:
   ```bash
   python main.py
   ```

2. input the ip and port when prompted, or hit enter to auto-configure.

3. open your browser and visit the displayed url (e.g., `http://127.0.0.1:8080`) to access the app.

---

## 🗂️ file routes

- **get /**: returns the `index.html` page from `front/`.
- **post /upload**: handles file uploads.
  - **params**:
    - `file`: file to be uploaded.
    - `filename`: custom name for the uploaded file.
- **get /get/<filename>**: retrieves a file by its filename. returns a default image if the file isn't found.
- **get /images/<image>**: fetches an image from `front/images/`. if the image doesn't exist, returns a default image.

---

## 🤝 contributing

want to contribute? awesome! follow the steps below to get started:

1. fork the repo.
2. create a new branch for your feature/bug fix.
3. commit your changes.
4. push the changes to your fork.
5. open a pull request.

---

## 🐞 issues

found a bug or have a feature request? feel free to [open an issue](https://github.com/planetwiide/miam-cloud/issues). we'll address it as soon as we can!

---

## 📝 license

this project is licensed under the [mit license](https://opensource.org/licenses/MIT).

## 🖼️ preview
![image](https://github.com/user-attachments/assets/0c1f3a17-bf03-4151-9dfc-5b8081c6230c)
![image](https://github.com/user-attachments/assets/50123a17-c79e-4ec5-8c14-ad13c343d1c0)
![image](https://github.com/user-attachments/assets/b23206f1-9bd3-4c80-bac8-075c5299a0e8)
![image](https://github.com/user-attachments/assets/cc5fa67d-9b9b-4fea-b742-62627ee26548)
![image](https://github.com/user-attachments/assets/280074c9-4132-42e0-b893-99c0a40ea087)



