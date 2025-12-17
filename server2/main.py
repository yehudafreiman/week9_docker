from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import json
from pathlib import Path


app = FastAPI(title="Items API", version="1.0.0")


# נתיב למסד הנתונים
DB_PATH = Path("db/shopping_list.json")


# מודל
class Item(BaseModel):
    name: str
    quantity: int


# בדיקת קיום מסד נתונים
def check_database_exists() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database file not found: {DB_PATH}")


# פונקציות עזר
def load_database() -> Dict:
    """קריאת מסד הנתונים"""
    with open(DB_PATH, "r") as f:
            return json.load(f)


def save_database(data: Dict) -> None:
    """כתיבת מסד הנתונים"""
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

# on_event
@app.on_event("startup")
async def startup_event():
    check_database_exists()

# GET
@app.get("/items")
async def list_items():
    """רשימת כל הפריטים"""
    items = load_database()
    return items

# POST
@app.post("/items/")
async def create_item(item: Item):
    """הוספת פריט חדש"""
    items = load_database()
    new_id = str(len(items) + 1)
    items[new_id] = item.dict()
    save_database(items)
    return {
        "message": "Item created successfully",
        "item_id": new_id,
        "item": items[new_id]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
