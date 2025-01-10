import uuid

from flask import Flask, request
from flask_smorest import abort

from db import items, stores

app = Flask(__name__)


##### Store #####
# GET All Stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


# GET Store By Id
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")


# Create New Store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request, Ensure 'name' is in the JSON payload")

    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists.")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store

    return new_store, 201


# Delete Store
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found.")


##### Items #####
# GET All Items
@app.get("/item")
def get_items():
    return {"items": list(items.values())}


# GET Item By Id
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Store not found.")


# Create New Item
@app.post("/item")
def create_item_in_store():
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request, Ensure 'price', store_id', and 'name' are in the JSON payload",
        )

    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="Item already exists in the store.")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item

    return new_item, 201


# Update Item
@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request, Ensure 'price', and 'name' are in the JSON payload",
        )

    try:
        item = items[item_id]
        item |= item_data

        return item
    except KeyError:
        abort(404, message="Store not found.")


# Delete Item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Store not found.")
