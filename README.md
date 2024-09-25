# 🌩️ MiamCloud v4.0.1

MiamCloud is a Flask-based web application that allows users to upload, download, and manage files. It features an animated ASCII user interface (UI) built using the **Pystyle** library, with logging capabilities via Discord webhooks. This project is designed to be lightweight and customizable, making it a flexible solution for personal or small-scale cloud storage needs.

![Repo Stars](https://img.shields.io/github/stars/planetwiide/miam-cloud?style=flat-square)
![Repo Forks](https://img.shields.io/github/forks/planetwiide/miam-cloud?style=flat-square)
![Contributors](https://img.shields.io/github/contributors/planetwiide/miam-cloud?style=flat-square)
![License](https://img.shields.io/github/license/planetwiide/miam-cloud?style=flat-square)
![Commits](https://img.shields.io/github/commit-activity/m/planetwiide/miam-cloud?style=flat-square)

## ⚡ Features

### 🔐 User Authentication
- Login system with credentials stored in `users.yml`.
- Session management via Flask's session handling.
- Webhook logs for successful and failed login attempts.

### 📁 File Management
- **File Uploads**: Upload files via `/upload` route, with file management stored in the `files` directory.
- **File Downloads**: Download files via `/get/<filename>`, or retrieve the default `miamcloud.png` if a file is not found.
- **Image Retrieval**: Serve images via `/images/<image>` route.

### 💻 ASCII User Interface (UI)
- Animated terminal-based UI using **Pystyle**, with banners and transitions.
- Interactive prompts for IP and port configuration, with default values for quick setup.

### 🌐 Webhook Logging (Discord)
- Discord webhook integration to log key events, including:
  - **Login Success**/Failure.
  - **File Uploads**.
  - **File Downloads**.
  - **App Start**/Quit.

> Note: Set `webhook_url` to `"none"` if you don't want webhook logging.

### 🛠️ Easy Setup
- Automatic detection of local IP address and default port (8080).
- Customizable host and port settings through interactive terminal prompts.

## 🌩️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/planetwiide/miam-cloud.git
   cd miam-cloud
