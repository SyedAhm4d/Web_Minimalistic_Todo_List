# Web Minimalistic Todo List

A minimalistic web-based Todo list application written using Python and HTML templates.  
Designed for simplicity, ease of use, and quick setup.

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Technologies & Dependencies](#technologies–dependencies)  
- [Requirements](#requirements)  
- [Installation & Setup](#installation-and-setup)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Configuration](#configuration)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## About

This project is a lightweight Todo list web application that allows you to add, view, update and delete tasks via a simple web interface. The goal is to keep the user interface and codebase minimal, making it ideal as a starter project, a learning tool, or a quick deployable component.

## Features

- Simple, clean UI for managing todos (add / edit / delete).  
- Minimal dependencies and minimal external overhead.  
- Written in Python (backend) + HTML (templates) – easy to understand and extend.  
- Clear project structure for templates and main app logic.  
- Quick setup & local deployment.

## Technologies & Dependencies

- Python (version 3.x)  
- A web framework 'Flask'  
- HTML templates (in `templates/` directory)  
- Standard libraries and minimal third-party packages to keep it simple.  

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.x (e.g., 3.7, 3.8, 3.9 or newer)  
- `pip` (Python package installer)  
- (Optional) virtual environment tool (`venv`, `virtualenv`) to isolate the project  
- A modern web browser  

## Installation & Setup

Follow these steps to get the application up and running:

```bash
# 1. Clone this repository
git clone https://github.com/SyedAhm4d/Web_Minimalistic_Todo_List.git
cd Web_Minimalistic_Todo_List

# 2. (Optional) Create and activate a virtual environment
python3 -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
# If you don’t have a requirements file, install manually (example):
pip install flask

# 4. Run the app
python main.py
