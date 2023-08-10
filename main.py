from  fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

'''
# decorator
@app.get("/") # / is a root path
def index(): 
    return {'data':{'name':'RISAV'}} #path operation function

@app.get('/about')
def about():
    return {'data': 'about page loaded'}

'''

@app.get("/")

def index():
    return{'data' : 'blog list'}
    
@app.get('/blog/unpublished')
def unpublished():
    return{'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id =id
    return {'data': id}



@app.get('/blog/{id}/comments')

def comments(id):
    #fetch comments of blog with id = id
    return{'data': {'1', '2'}}