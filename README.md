to run this app

1. create virtual envirotment with python, make sure python version is 3.6 or higer (recomended 3.6)

2. install requirement in requirement.txt

3. create database then setup database config in .env.example with filename is ".env"

4. in root folder, execute 'python3 app db init', folder migration will be created

5. in root folder, execute 'python3 app db migrate',

6. to run application run bash file 'run.sh', make sure that file have execution permision

===================== documentation ======================

host = gttp://0.0.0.0:5000

[get] {{host}}/siswa/:id
example : {{host}}/siswa/1
response example :
{
    "id": 1,
    "name": "sholeh",
    "gender": "L",
    "age": 25,
    "date_birth": "1995-11-01 00:00:00",
    "grade": "XI"
}

[post] {{host}}/siswa
require json body request : nama, gender, umur, date_birth, grade
example json body :
{
    "nama" : "derby",
    "gender" : "L",
    "umur" : "18",
    "date_birth" : "01-11-1995",
    "grade" : "XII"
}

example response :
{
    "id": 3,
    "name": "derby",
    "gender": "L",
    "age": 18,
    "date_birth": "1995-11-01 00:00:00",
    "grade": "XII"
}

[put] {{host}}/siswa/:id
example endpoint {{host}}/siswa/1
json body optional : nama, gender, umur, date_birth, grade
example request body :
{   
    "nama" : "ariff"
}
example response :
{
    "id": 1,
    "name": "ariff",
    "gender": "L",
    "age": 25,
    "date_birth": "1995-11-01 00:00:00",
    "grade": "XI"
}


[delete] {{host}}/siswa/:id
example endpoint {{host}}/siswa/1
response :
{
    "status": "DELETED"
}