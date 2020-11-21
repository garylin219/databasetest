from flask import Flask, jsonify
import mysql.connector
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def Member_import():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'memberData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM memberList')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

class Member(Resource):
    def get(self):
        return jsonify(Member_import())


api.add_resource(Member, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
