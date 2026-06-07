from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

df = pd.read_csv("/Users/avijitkundal/Downloads/q-fastapi.csv")

@app.get("/api")
def get_students(class_: List[str] = Query(default=None, alias="class")):
    if class_:
        filtered = df[df["class"].isin(class_)]
    else:
        filtered = df
    return {"students": filtered.to_dict(orient="records")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)