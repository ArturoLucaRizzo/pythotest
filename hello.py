from flask import Flask, json, render_template, request, jsonify
from employee import Employee
import urllib
import names
import requests
import sys
import mysql.connector

app = Flask(__name__)

employeeList = []


@app.route("/json")
def hello():
    try:

        # Initialize a employee list
        employeeList = []

        # create a instances for filling up employee list
        for i in range(0, 5):
            employee = Employee(names.get_first_name(), names.get_last_name())

        # convert to json data
        jsonStr = json.dumps(employee.toJSON())

    except: print("error ", sys.exc_info()[0])

    return jsonStr


@app.route("/readJson")
def read():
    content = requests.get("http://localhost:5000/json")
    jsons = json.loads(content.content)
    config = {
        'user': 'root',
        'password': 'qwerty',
        'host': '127.0.0.1 ',
        'port': '3306',
        'database': 'user',
        'raise_on_warnings': True,
    }
    cnx = mysql.connector.connect(**config)
    add_employee = ("INSERT INTO user "
                    "(name, surname) "
                    "VALUES (%s, %s)")
    data_employee = (jsons['firstName'], jsons['lastName'])
    cursor = cnx.cursor()
    cursor.execute(add_employee, data_employee)
    cnx.commit()
    cursor.close()
    cnx.close()

    return jsons['firstName']


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/json.js")
def jsons():
    return render_template('json.js')


@app.route("/readj", methods=["POST"])
def javas():
    js = request.json['js']
    surname = int(js['surname'])
    name = int(js['name'])

    result = surname + name
    print(name, surname)

    return jsonify(result=result)


if __name__ == "__main__":
    app.run()