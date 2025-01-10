from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    print(request_data)
    items = request_data["items"] if "items" in request_data else []
    new_store = {"name": request_data["name"], "items": items}
    stores.append(new_store)

    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            store["items"].append(request_data)
            return store, 201

    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store

    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}

    return {"message": "Store not found"}, 404
