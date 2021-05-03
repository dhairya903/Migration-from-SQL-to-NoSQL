import pymysql
import json

try:
    db = pymysql.connect(host="127.0.0.1", user="root",
                         password="qazwsxedc", db="employees")

except:
    print("error unable to connect to the database")

cursor = db.cursor()
# query = "SELECT e.emp_no,d.dept_no,e.first_name from current_dept_emp as d join employees as e on e.emp_no=d.emp_no where d.dept_no='d003';"
query = "SELECT e.emp_no,d.dept_no,e.first_name from current_dept_emp as d join employees as e on e.emp_no=d.emp_no;"
try:
    dataSetArr = []
    dataSetDict = {}
    final = {}
    cursor.execute(query)
    output = cursor.fetchall()
    for item in output:
        emp_no = item[0]
        dept_no = item[1]
        first_name = item[2]
        dataSetDict["emp_no"] = emp_no
        dataSetDict["dept_no"] = dept_no
        dataSetDict["first_name"] = first_name
        # print(dataSetDict)

        dataSetArr.append(dataSetDict)
        dataSetDict = {}

    y = json.dumps(dataSetArr)
    # print(y)
    json_object = json.loads(y)
    print(type(json_object))
    with open("data.json", "w") as f:
        f.write(y)
except:
    print("problem fetching")
