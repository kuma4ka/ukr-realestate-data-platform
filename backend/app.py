from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Property
import os

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route("/api/properties", methods=["GET"])
def get_properties():
    session = Session()
    properties = session.query(Property).order_by(Property.id.desc()).limit(20).all()
    session.close()
    return jsonify([
        {"id": p.id, "title": p.title, "price": str(p.price), "address": p.address, "url": p.url}
        for p in properties
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)