# app.py
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import base64
# import os
# import uvicorn

# from main import process_query

# app = FastAPI()

# class QueryRequest(BaseModel):
#     query: str

# class QueryResponse(BaseModel):
#     image_base64: str
#     analysis: str
#     news: list

# @app.post("/analyze", response_model=QueryResponse)
# def analyze_query(request: QueryRequest):
#     try:
#         image_path, analysis, newsD = process_query(request.query)

#         # Convert image to base64
#         with open(image_path, "rb") as f:
#             encoded_image = base64.b64encode(f.read()).decode("utf-8")

#         return {
#             "image_base64": encoded_image,
#             "analysis": analysis,
#             "news": newsD
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# # if __name__ == "__main__":
# #     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

