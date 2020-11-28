from flask import Flask, jsonify
import mysql.connector
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def Member_import():
    config = {
        'user': 'cbb107018',
        'password': 'zasd0456123',
        'host': 'web.csie.nptu.edu.tw',
        'port': '3306',
        'database': 'cbb107018_DB2020'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM INFORMATION_SCHEMA.Tables')
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
