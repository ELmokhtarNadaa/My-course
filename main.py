from typing import Optional
from fastapi import FastAPI , Request
import mysql.connector
import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
#origine angular
origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add")
async def add(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "my-courses")
    body = json.loads(await request.body())
    mycursor.execute(f"INSERT INTO `{body['contenu']}`  VALUES ( '{body['contenu']}', '{body['img']}');")
    mydb.commit()
    return {"done"}

@app.get("/signup")
def gets():
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM utilisateur")
    
    row_headers=[x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/choosesubject")
def gets():
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM matiere , level , langage ")
    row_headers=[x[0] for x in mycursor.description] 
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
