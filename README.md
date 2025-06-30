# 🧠 Advanced Task Manager

A clean and powerful web app to manage personal or team tasks efficiently.  
Create project boards, organize tasks in lists, set priorities, add tags, and track deadlines — all in one place.

---

## 🚀 Live Demo

👉 Try it now: [https://advanced-task-manager.onrender.com](https://advanced-task-manager.onrender.com)

---

## 📸 What You Can Do

- 🔐 Register and log in securely
- 📁 Create project boards
- 📂 Organize tasks by list: To Do, In Progress, Done
- 📝 Add task details: title, description, deadline
- ⚙️ Choose priority: low, medium, high
- 🏷️ Assign tags like "frontend", "urgent", etc.
- 🔄 Update task status easily from the interface
- 📱 Fully responsive design (Bootstrap 5)
- 🌐 Publicly accessible on Render

---

## 💻 Tech Stack

- **Backend**: Django 5.2, SQLite3
- **Frontend**: Bootstrap 5, Crispy Forms
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

# 5. Start the dev server
python manage.py runserver
Then go to http://127.0.0.1:8000

🙌 Contributing
Pull requests are welcome! Feel free to open issues for suggestions or bugs.

📄 License
This project is licensed under the MIT License.
