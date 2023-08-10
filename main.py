from  fastapi import FastAPI
from typing import Optional
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

@app.get("/blog")

def index(limit =10,published:bool=True, sort : Optional[str]= None):
    #only get 10 published blogs
    return published
    if published:

        return{'data' : f'{limit}  published blogs from the DB'}
    else:
        return{'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return{'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id =id
    return {'data': id}



@app.get('/blog/{id}/comments')

def comments(id,limit=10):
    #fetch comments of blog with id = id
    return limit
    return{'data': {'1', '2'}}