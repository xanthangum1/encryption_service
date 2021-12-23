app = FastAPI(
    title="Encryption services",
    description="Service layer, ecryption",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url=None,
    default_response_class=ORJSONResponse,
    debug=True,
)

