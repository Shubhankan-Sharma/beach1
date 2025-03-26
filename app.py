from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(_name_)

# Function to generate timestamps at 30-minute intervals# Sample data for beach locations
beach_data = {
    "beach1": {
        "location": "Beach 1",
        "data": {
            "timestamp": datetime.now().isoformat(),
            "temperature": random.uniform(20.0, 30.0),
            "currentspeed": random.uniform(0.5, 3.0),
            "ph": round(random.uniform(6.5, 7.5), 2),
            "tidelength": random.uniform(1.0, 2.0) 
        }
    },
    # Add more beaches as needed
}

@app.route('/api/beach/<beach_id>', methods=['GET'])
def get_beach_data(beach_id):
    if beach_id in beach_data:
        return jsonify(beach_data[beach_id])
    else:
        return jsonify({"error": "Beach not found"}), 404

if _name_ == '_main_':
    app.run(debug=True)
