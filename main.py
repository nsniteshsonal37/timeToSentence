from dataclasses import InitVar
from fastapi import FastAPI, Form
import uvicorn
from pydantic import BaseModel
from runner import *
from fastapi.middleware.cors import CORSMiddleware
import re

app=FastAPI() 
regex= '^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
x="01:60"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Time(BaseModel):
    time: str

global initVar
initVar=1
@app.post("/post")
def postF(time: str=Form()):
    global inputTime, var
    global initVar
    initVar=0
    inputTime=time
    var=re.match(regex,inputTime)
    print(initVar)
    if(var):
        return{"Status":"Received"}
    else:
        return{"Status":"Regex Fail"}
@app.get("/")
def root():
    print(initVar)
    if(initVar==1):
        return{"Status": "API Launched"}
    if(var):
        return{"time": out(inputTime)}
    else:
        return{"Status":"Regex Fail"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=5000, log_level="info", reload=True)