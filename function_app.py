import azure.functions as func
import azure.durable_functions as df
import logging

# Import blueprints
from blueprints.blob_functions import blob_bp
from blueprints.orchestrator_functions import orchestrator_bp
from blueprints.activity_functions import activity_bp

# Create the main function app
app = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Register blueprints
app.register_blueprint(blob_bp)
app.register_blueprint(orchestrator_bp)
app.register_blueprint(activity_bp)
