<h1 align="center">Migration-from-SQL-to-NoSQL</h1>

<img src="https://img.shields.io/badge/Made%20with-MySQL-1f425f.svg"/>    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"/>    <img src="https://img.shields.io/badge/Made%20with-MongoDB-1f425f.svg"/> 

</br>

<h1>Project By</h1>

| <h3>Dhairya Shah</h3> | <h3>Sameer Wadhwa</h3> |
| -------------------- | ---------------------- |
| <h3>1911119 </h3>    | <h3>1911131</h3>       |
| <h3>B4</h3>          | <h3>B4</h3>            |

</br>

<h1>Faculty</h1>

| <h3>Prof. Pradnya Bhangale</h3> | <h3>Prof. Vaibhav Vasani</h3> |
| ------------------------------- | ----------------------------- |


</br>
</br>

## Prerequisites

  -   A system running Windows 10
  -   A user account with administrator privileges (required to install software, modify file permissions, and modify system PATH)
  -   Command Prompt or Powershell

</br>
</br>

## Install MySQL Server, Python3 and MongoDB on Windows

-   Installing MySQL on Windows 10 may seem complicated to novice users, but this simple tutorial will have you up and running.
-   If you already have MySQL, Python 3 and MongoDB installed, you can skip the first two steps.

</br>
</br>

### Step 1: Install MySQL Server

-   Open Browser and navigate to https://dev.mysql.com/downloads/installer/.
-   Download the latest stable version.
-   Add it to the environment variable.

</br>
</br>

### Step 2: Install Python

-   Open Browser and navigate to https://www.python.org/downloads/.
-   Download the latest stable version.
-   Add it to the environment variable.

</br> 
</br>

### Step 3: Install MongoDB

-   Open a browser and navigate to https://www.mongodb.com/try/download/community.
-   Select the current version and MSI package and click on download.

</br>
</br>

## Running the project

</br>

-   Make sure Java, Python and Spark are installed correctly by running the following command.

    -   `mysql --version`
    -   `py --version`
    -   `mongo --version`

-   Open the terminal/command prompt.
-   Clone the repository.
    </br>
    -   `https://github.com/dhairya903/Migration-from-SQL-to-NoSQL`

### Step 1:

-   Clone https://github.com/datacharmer/test_db for the required data.
-   Open command prompt and navigate to the cloned folder.
-   Run `mysql -u root -p` and enter your password
-   To load the database run `\. employees.sql`
-   Run `show databases;` to check if the database is created.

</br>

### Step 2:

-   Open and run `mainScript.py` using a code editor.
-   You will get a data.json of the query which is inside the script.

</br>

### Step 3:

-   Open terminal and type `mongod` to run the mongo server
-   Open MongoDB Compass or terminal and create a new database
-   Create a new collection inside the database.
-   Now import the data.json file using MongoDB Compass or run the following command:

    ```cmd
    mongoimport --db ia2 --colection queryTable --file data.json --jsonArray
    ```
    
-   Now in the shell, type the following commands to check if the data is imported:

    ```cmd
    show dbs;
    use ia2;
    db.queryTable.find({});
    ```
    
</br>

### Step 4:
-   Now to compare the query times between MongoDB and MySQL open 3 terminals (powershell/cmd)
-   To run MongoDB we need to type `mongod` inside of the 1st terminal.
-   In the second terminal run mysql and use the created database and run the following query:

    ```cmd
    EXPLAIN ANALYZE SELECT e.emp_no,d.dept_no,e.first_name FROM current_dept_emp AS d JOIN employees AS e ON e.emp_no=d.emp_no WHERE d.dept_no='d003';
    ```
    
-   In the third terminal run mongo and use the created database and collection and type in the following query:

    ```cmd
    db.queryTable.find({"emp_no" : "d003"}).explain("executionStats");
    ```

-   Now compare the time in milli-seconds in both the returned analytics.

    <img src="Images\mysql.PNG">
    </br>
    <p align="center">
    <img src="Images\mongoDB.PNG">
    </p>

</br>


## Featured technologies:

-   MySQL: MySQL Database Service is a fully managed database service to deploy cloud-native applications

-   Python: Python is a programming language that lets you work more quickly and integrate your systems more effectively.

-   MongoDB: MongoDB is a NoSQL document database with the scalability and flexibility that you want with the querying and indexing that you need.

</br>
</br>
</br>

## Tools and Technologies used

</br>


<p><img height="50" src="Images\mysql-logo.svg"> &nbsp;  <img height="50" src="Images\python-logo.png">  &nbsp;  <img height="50" src="Images\mongodb-logo.svg"></p>



