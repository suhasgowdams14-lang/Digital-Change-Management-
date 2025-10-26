import sqlite3
from flask import Flask, jsonify, render_template
from flask_cors import CORS # Needed for the webpage to talk to the backend

app = Flask(__name__)
CORS(app) # Allows cross-origin requests

DATABASE = 'change_management.db'

def get_db_connection():
    """Helper function to connect to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Allows accessing columns by name
    return conn

# --- Main Webpage Route ---

@app.route('/')
def dashboard():
    """Serves the main HTML dashboard webpage."""
    return render_template('index.html')

# --- API Routes (for Power BI or our webpage) ---

@app.route('/api/metrics/latest')
def get_latest_metrics():
    """API endpoint to get the most recent adoption and readiness scores."""
    try:
        conn = get_db_connection()
        # Get the single most recent entry for initiative 1
        metrics = conn.execute(
            'SELECT adoption_rate, readiness_score FROM metrics WHERE initiative_id = 1 ORDER BY metric_date DESC LIMIT 1'
        ).fetchone()
        conn.close()

        if metrics:
            return jsonify({
                'adoption_rate': metrics['adoption_rate'],
                'readiness_score': metrics['readiness_score']
            })
        else:
            return jsonify({'error': 'No metrics found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sentiment')
def get_sentiment():
    """API endpoint to calculate sentiment distribution."""
    try:
        conn = get_db_connection()
        # Simple categorization of sentiment
        feedback = conn.execute(
            '''
            SELECT
                SUM(CASE WHEN sentiment_score > 0.3 THEN 1 ELSE 0 END) AS positive,
                SUM(CASE WHEN sentiment_score BETWEEN -0.3 AND 0.3 THEN 1 ELSE 0 END) AS neutral,
                SUM(CASE WHEN sentiment_score < -0.3 THEN 1 ELSE 0 END) AS negative
            FROM feedback
            WHERE initiative_id = 1
            '''
        ).fetchone()
        conn.close()

        if feedback:
            return jsonify(dict(feedback))
        else:
            return jsonify({'positive': 0, 'neutral': 0, 'negative': 0})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/adoption/history')
def get_adoption_history():
    """API endpoint to get time-series data for adoption."""
    try:
        conn = get_db_connection()
        history = conn.execute(
            "SELECT metric_date, adoption_rate FROM metrics WHERE initiative_id = 1 ORDER BY metric_date ASC"
        ).fetchall()
        conn.close()
        
        # Format data for Chart.js
        data = {
            'labels': [row['metric_date'] for row in history],
            'data': [row['adoption_rate'] * 100 for row in history] # As percentage
        }
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

from waitress import serve

if __name__ == '__main__':
    print("Starting production server on http://127.0.0.1:5000")
    serve(app, host='127.0.0.1', port=5000)