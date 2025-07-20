from bson import ObjectId

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "size": product.get("size")
    }

def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "product_ids": order["product_ids"]
    }
