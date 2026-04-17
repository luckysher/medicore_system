from endpoints.users_endpoints import *


@app.get("/")
def home():
    return "Welcome to medicore system API"
