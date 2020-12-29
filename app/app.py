from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def favorite_emps() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'employees'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM employees')
    results = [{name: eid} for (name, eid) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_employees': favorite_emps()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
