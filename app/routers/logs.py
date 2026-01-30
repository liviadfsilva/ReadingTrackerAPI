from datetime import datetime
from app.database.models import Tracker
from app.database.schemas import all_data
from fastapi import FastAPI, APIRouter, HTTPException
from app.database.mongo import collection
from bson.objectid import ObjectId

app = FastAPI()
router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)

@router.get("/")
async def get_all_logs():
    data = collection.find()
    return all_data(data)

@router.post("/")
async def create_log(new_log: Tracker):
    try:
        response = collection.insert_one(dict(new_log))
        return {"status_code":200, "id":str(response.inserted_id)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured: {e}")
    
@router.patch("/{task_id}")
async def update_log(task_id: str, updated_log: Tracker):
    try:
        try:
            obj_id = ObjectId(task_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid task ID.")
        

        existing_doc = collection.find_one({"_id": obj_id})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="This log does not exist.")
        
        updated_log.updated_at = int(datetime.now().timestamp())
        collection.update_one({"_id": obj_id}, {"$set": updated_log.model_dump()})
        
        return {"status_code": 200, "message": "Log updated successfully."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")
    
@router.delete("/{task_id}")
async def delete_log(task_id: str):
    try:
        try:
            obj_id = ObjectId(task_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid task ID.")
        
        result = collection.delete_one({"_id": obj_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Log not found.")
        
        return {"status_code": 200, "message": "Log deleted successfully/"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")