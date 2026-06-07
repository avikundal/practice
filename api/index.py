from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Access-Control-Allow-Origin"],
)

DATA = [
  {"region":"apac","latency_ms":178.37,"uptime_pct":98.192},
  {"region":"apac","latency_ms":206.37,"uptime_pct":97.32},
  {"region":"apac","latency_ms":133.01,"uptime_pct":98.485},
  {"region":"apac","latency_ms":207.3,"uptime_pct":98.322},
  {"region":"apac","latency_ms":178.31,"uptime_pct":98.618},
  {"region":"apac","latency_ms":174.95,"uptime_pct":97.592},
  {"region":"apac","latency_ms":174.83,"uptime_pct":98.963},
  {"region":"apac","latency_ms":207.27,"uptime_pct":98.469},
  {"region":"apac","latency_ms":195.47,"uptime_pct":99.01},
  {"region":"apac","latency_ms":182.99,"uptime_pct":97.882},
  {"region":"apac","latency_ms":220.83,"uptime_pct":99.469},
  {"region":"apac","latency_ms":144.05,"uptime_pct":98.131},
  {"region":"emea","latency_ms":117.93,"uptime_pct":97.75},
  {"region":"emea","latency_ms":123.61,"uptime_pct":97.449},
  {"region":"emea","latency_ms":128.6,"uptime_pct":97.442},
  {"region":"emea","latency_ms":140.34,"uptime_pct":97.955},
  {"region":"emea","latency_ms":106.6,"uptime_pct":97.153},
  {"region":"emea","latency_ms":160.34,"uptime_pct":99.037},
  {"region":"emea","latency_ms":205.57,"uptime_pct":97.447},
  {"region":"emea","latency_ms":124.53,"uptime_pct":99.466},
  {"region":"emea","latency_ms":140.89,"uptime_pct":98.098},
  {"region":"emea","latency_ms":220.85,"uptime_pct":98.668},
  {"region":"emea","latency_ms":142.29,"uptime_pct":99.293},
  {"region":"emea","latency_ms":130.08,"uptime_pct":97.603},
  {"region":"amer","latency_ms":160.8,"uptime_pct":98.074},
  {"region":"amer","latency_ms":217.06,"uptime_pct":98.211},
  {"region":"amer","latency_ms":198.96,"uptime_pct":99.102},
  {"region":"amer","latency_ms":189.12,"uptime_pct":99.073},
  {"region":"amer","latency_ms":200.1,"uptime_pct":99.065},
  {"region":"amer","latency_ms":129.86,"uptime_pct":97.717},
  {"region":"amer","latency_ms":217.96,"uptime_pct":97.23},
  {"region":"amer","latency_ms":161.52,"uptime_pct":98.606},
  {"region":"amer","latency_ms":194.16,"uptime_pct":98.601},
  {"region":"amer","latency_ms":191.26,"uptime_pct":97.309},
  {"region":"amer","latency_ms":205.23,"uptime_pct":99.382},
  {"region":"amer","latency_ms":175.55,"uptime_pct":98.606},
]

class LatencyRequest(BaseModel):
    regions: List[str]
    threshold_ms: float

@app.post("/api/latency")
def latency(req: LatencyRequest):
    results = []
    for region in req.regions:
        rows = [r for r in DATA if r['region'] == region]
        if not rows:
            continue
        lats = [r['latency_ms'] for r in rows]
        ups = [r['uptime_pct'] for r in rows]
        results.append({
            "region": region,
            "avg_latency": round(sum(lats)/len(lats), 4),
            "p95_latency": round(float(np.percentile(lats, 95)), 4),
            "avg_uptime": round(sum(ups)/len(ups), 4),
            "breaches": sum(1 for l in lats if l > req.threshold_ms)
        })
    return {"results": results}
