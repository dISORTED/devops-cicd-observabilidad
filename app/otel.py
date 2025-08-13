
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor

import os

# Variables desde Koyeb
grafana_token = os.getenv("GRAFANA_CLOUD_API_TOKEN")
otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT")
service_name = os.getenv("SERVICE_NAME", "cicd-demo")

# Configuración de recursos
resource = Resource.create({
    "service.name": service_name
})

# Proveedor de trazas
trace.set_tracer_provider(TracerProvider(resource=resource))

# Exportador OTLP (HTTP/protobuf)
otlp_exporter = OTLPSpanExporter(
    endpoint=otlp_endpoint,
    headers={
        "Authorization": f"Bearer {grafana_token}"
    }
)

# Procesador de spans
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)
