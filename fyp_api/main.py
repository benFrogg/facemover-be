
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import shutil as _shutil
import services as _services, schemas as _schemas
import os
import io
import subprocess
import time

from fastapi import UploadFile, File, Request
from typing import List, Optional
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = _fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/users")
async def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(user.email, db)

    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)

@app.post("/token")
async def generate_token(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await _services.create_token(user)

@app.get("/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User=_fastapi.Depends(_services.get_current_user)):
    return user

@app.post("/get-image")
async def get_image(file: UploadFile = File(...)):
    image = await file.read()
    _services.uploaded_image("Mover/upload_img/input/A/" + file.filename, image)
    
    return {"image_name" : file.filename}

@app.post("/get-feature")
async def get_feature(feature_id: _schemas.FeatureBase):
    os.chdir("Mover")
    subprocess.call(['python', 'switch.py', '--mode', str(feature_id.feature_id)])
    os.chdir("..")

    return {"features_id": feature_id.feature_id}

@app.get("/output-image")
async def get_output(request: Request):
    if len(os.listdir('Mover/list/output/')) != 0:
        for file in os.listdir("Mover/list/output"):
            if file.endswith("gif"):
                with open(f"Mover/list/output/{file}", "rb") as img_gif:
                    output = img_gif.read()
                output_io = io.BytesIO(output)
                output_io.seek(0)
                return StreamingResponse(content=output_io, media_type="image/gif")
            if file.endswith("mp4"):
                return _services.range_requests_response(
                    request, file_path=f"Mover/list/output/{file}", content_type="video/mp4"
                )
    return None