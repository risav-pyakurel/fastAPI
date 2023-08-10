from  fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()



@app.get("/") # / is a root path
def index():
    return {'data':{'name':'RISAV'}}

@app.get('/about')
def about():
    return {'data': 'about page loaded'}

