from fastapi import FASTAPI, File, UploadFile
from fastapi.middleware.cors import CORSmiddleware
from utils.ai_hair_replace import replace_hair
import shutil
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads/"
RESULT_DIR = "results/"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result_path = replace_hair(file_path)
    return {"result_url": f"http://localhost:8000/{result_path}"}