#  Digital Change Management Dashboard  

#  Overview  
The **Digital Change Management Dashboard** is a data-driven web application designed to track and manage digital transformation initiatives within an organization.  
It helps teams monitor **adoption rates, readiness scores, feedback sentiment**, and other key performance indicators essential for effective change management.  

Built using **Python (Flask)** for backend APIs, **SQL database** for structured data storage, and **HTML/CSS/JS** for a clean, interactive interface.

---

#  Features  
-  **Real-time Analytics Dashboard** – Visualize change metrics like adoption and engagement.  
-  **Change Readiness Assessment** – Evaluate organizational readiness for transformation.  
-  **Feedback & Sentiment Tracking** – Monitor feedback trends for informed decision-making.  
-  **Database Integration** – SQLite-powered backend for storing project and user data.  
-  **Web-Based UI** – Lightweight and responsive interface for easy access and updates.

---

# Tech Stack  

| Layer | Technology Used |
|-------|------------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask Framework) |
| **Database** | SQLite (`change_management.db`) |
| **Visualization** | Power BI / Custom JS Charts (optional extension) |

---

# Project Structure  
```
📁 Digital-Change-Management/
│
├── app.py                # Main Flask application
├── database.py           # Handles database connections and CRUD operations
├── change_management.db  # SQLite database file
├── index.html            # Frontend homepage/dashboard
├── style.css             # Styling for web interface
├── app.js                # Optional frontend interactivity scripts
└── README.md             # Project documentation
```

---

# Installation & Setup  

1. **Clone this repository**
   ```bash
   git clone https://github.com/suhasgowdams14-lang/Digital-Change-Management.git
   cd Digital-Change-Management
   ```

2. **Create & activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate  # For Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Access the dashboard**
   Open your browser and visit → `http://127.0.0.1:5000/`

---

# Example Use Case  
- **Scenario:** A digital transformation team wants to assess readiness and adoption of a new software rollout.  
- **Action:** Data (feedback, readiness, adoption score) is stored in `change_management.db`.  
- **Result:** The dashboard displays live insights on adoption progress and engagement, helping leaders make timely decisions.  

---

# Future Enhancements  
- Integrate **Power BI** for advanced data visualization  
- Add **role-based authentication**  
- Enable **automated email reports**  
- Implement **AI-based sentiment analysis** on feedback  

---

## Author  
**Suhas Gowda M S**  
Digital Transformation & Engagement Enthusiast  
📧 [suhasgowdams14@gmail.com]  
🌐 [GitHub Profile](https://github.com/suhasgowdams14-lang)
