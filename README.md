# 🧠 Advanced Task Manager

A modern, Trello-inspired task management web app built with Django.  
Manage projects, create task lists, assign priorities, tag tasks, and track progress — all in a clean and responsive UI.

---

## 🚀 Live Demo

👉 Try it now: [https://advanced-task-manager.onrender.com](https://advanced-task-manager.onrender.com)

---

## 📸 Features

- 🔐 **User Authentication** (signup, login, logout)
- 📁 **Project Boards** – one per user
- 📂 **Task Lists** – To Do, In Progress, Done (customizable)
- ✅ **Tasks** – with title, description, deadline, and priority
- 🏷️ **Tags** – like "frontend", "urgent", "research", etc.
- 📊 **Status Updates** – move tasks through lists easily
- 🖥️ **Responsive Design** – built with Bootstrap 5
- 🌐 **Deployed on Render** – publicly accessible

---

## 💻 Tech Stack

- **Backend**: Django 5.2, SQLite3
- **Frontend**: HTML, Bootstrap 5, Crispy Forms
- **Auth**: Django AllAuth
- **Deploy**: Render (Free Tier)

---

## 🔧 Local Setup

> Requirements: Python 3.12, pip, virtualenv (or conda)

```bash
# 1. Clone the repo
git clone https://github.com/GermanHernandez2902/advanced-task-manager.git
cd advanced-task-manager

# 2. Create and activate virtual env
python -m venv env
source env/bin/activate  # on Windows use: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Run the dev server
python manage.py runserver
Then go to http://127.0.0.1:8000

🙌 Contributing
Pull requests are welcome! Feel free to open issues for suggestions or bugs.

📄 License
This project is licensed under the MIT License.
