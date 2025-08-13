from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
import app.otel  # inicializa OpenTelemetry

app = FastAPI()

# Instrumentación automática de FastAPI
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + OpenTelemetry + Grafana!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/work")
def work():
    return {"task": "processing"}
