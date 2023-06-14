from fastapi import FastAPI, Request
import socket
import dataBaseMaria
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

mariadb = dataBaseMaria.DatabaseMaria('localhost', 3306, 'jang', 'jang','Launchmenu','utf8')

origins = [
    'http://211.230.166.113:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/del-menu/{num}")
def delMenu(num : int):
    mariadb.delMenu(num)
    result = mariadb.getMenuList()
    return result


@app.get("/menu_list")
def getMenuList():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    result = mariadb.getMenuList()
    return result

@app.post("/menu-add")
async def menuAdd(request : Request):
    result = await request.json()
    send_menu = result['menu']
    response = mariadb.menuAdd(send_menu)
    result1 = mariadb.getMenuList()
    return result1