import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

resource = Resource.create({"service.name": os.getenv("SERVICE_NAME", "nublibar-demo")})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

exporter = OTLPSpanExporter(
    endpoint=os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"),
    headers={"Authorization": f"Bearer {os.getenv('GRAFANA_CLOUD_API_TOKEN', '')}"}
)
provider.add_span_processor(BatchSpanProcessor(exporter))
