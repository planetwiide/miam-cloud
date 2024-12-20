![BannerMiamCloud](https://github.com/user-attachments/assets/7851eee4-c9a4-4e8c-95cb-741f72b13d1b)

![⭐](https://img.shields.io/github/stars/planetwiide/miam-cloud?style=social)
![🍴](https://img.shields.io/github/forks/planetwiide/miam-cloud?style=social)
![🐞](https://img.shields.io/github/issues/planetwiide/miam-cloud)
![⚡](https://img.shields.io/github/commit-activity/m/planetwiide/miam-cloud)
![🆙](https://img.shields.io/github/last-commit/planetwiide/miam-cloud)
![📚](https://img.shields.io/github/license/planetwiide/miam-cloud)


# 🌩️ miamcloud - v4.0.1

_author: [planetwide](https://github.com/planetwiide)_

---

## ✨ description

**miamcloud** is a flask-based web app designed to make file management simple and accessible through a sleek web interface. easily upload, download, and manage files or images directly from your server. the app also integrates with **pystyle** for a visually appealing experience, including interactive ascii banners and a clean terminal display.

_**UPDATE: added a login page for security and logs via webhook (discord)**_

---

## 🌟 features

- 🚀 **file uploading**: upload files effortlessly via the web interface.
- 🎯 **file downloading**: securely retrieve files through a custom download link.
- 🛠️ **flask-based**: works on any flask-supported platform, making deployment a breeze.
- 🌐 **dynamic ip & port**: automatically detects ip and port, or set them manually if preferred.
- 🧩 **clean code**: modular and easy-to-follow structure, perfect for customization.

---

## 📜 table of contents

- [📥 installation](#-installation)
- [📖 usage](#-usage)
- [🗂️ file routes](#-file-routes)
- [🔐 authentication](#-user-authentication)
- [🌐 webhook logging](#-webhook-logging)
- [🤝 contributing](#-contributing)
- [🐞 issues](#-issues)
- [📝 license](#-license)
- [📗 credits](#-credits)
- [🖼️ preview](#-preview)

---

## 📥 installation

### prerequisites

before starting, make sure you have:

- python 3.6+
- depandancies (pip install Flask pystyle PyYAML requests)

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

### 🔐 user authentication
- Login system with credentials stored in `users.yml`.
- Session management via Flask's session handling.
- Webhook logs for successful and failed login attempts.

---

### 🌐 webhook logging
- Discord webhook integration to log key events, including:
  - **Login Success**/Failure.
  - **File Uploads**.
  - **File Downloads**.
  - **App Start**/Quit.

---

## 🔧 usage

1. start the app:
   
```bash
   python main.py
```

2. input the ip and port when prompted, or hit enter to auto-configure.

3. open your browser and visit the displayed url (e.g., http://127.0.0.1:8080) to access the app.

---

## 🗂️ file routes

- **get /**: returns the index.html page from front/.
- **post /upload**: handles file uploads.
  - **params**:
    - file: file to be uploaded.
    - filename: custom name for the uploaded file.
- **get /get/<filename>**: retrieves a file by its filename. returns a default image if the file isn't found.
- **get /images/<image>**: fetches an image from front/images/. if the image doesn't exist, returns a default image.

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

## 📗 credits

this project was inspired by the ♉ [zodiac](https://github.com/billythegoat356/Zodiac) project by 🐐 [billythegoat365](https://github.com/billythegoat356/). while i drew inspiration from his work, i want to clarify that i did not copy it directly. all code has been rewritten from scratch, and i have implemented my own ideas and features. i plan to continue developing and maintaining this project, with new features on the way soon. thanks to billy for the initial inspiration!

---

## 📝 license

this project is licensed under the [mit license](https://opensource.org/licenses/MIT).

---

## 🖼️ preview

![image0](https://github.com/user-attachments/assets/dbe24a15-5f71-4a30-acf0-290ef29171c7)
![image1](https://github.com/user-attachments/assets/04c3c4b2-f23f-447d-b93a-78a8ec43a83e)
![image2](https://github.com/user-attachments/assets/7a54da41-e08e-48af-8345-b56a25bce391)
![image3](https://github.com/user-attachments/assets/a85356b1-de97-427c-9e9d-6f772b47094c)
![image4](https://github.com/user-attachments/assets/74ccdf36-1b3c-429d-bda5-bf75b5d7999b)
