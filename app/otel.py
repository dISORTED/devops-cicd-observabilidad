from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI

import os

# Variables de entorno (se deben definir en Koyeb o en tu entorno local)
GRAFANA_CLOUD_API_TOKEN = os.getenv("GRAFANA_CLOUD_API_TOKEN")
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT")
SERVICE_NAME = os.getenv("SERVICE_NAME", "cicd-demo")

# Configuración del proveedor de trazas
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configuración del exportador OTLP
otlp_exporter = OTLPSpanExporter(
    endpoint=OTEL_EXPORTER_OTLP_TRACES_ENDPOINT,
    headers={
        "Authorization": f"Bearer {GRAFANA_CLOUD_API_TOKEN}"
    }
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# Creación de la app FastAPI
app = FastAPI()

# Instrumentación automática de FastAPI
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + OpenTelemetry + Grafana!"}
