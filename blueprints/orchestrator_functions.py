import azure.functions as func
import azure.durable_functions as df
import logging

# Create blueprint for orchestrator function
orchestrator_bp = df.Blueprint()

@orchestrator_bp.orchestration_trigger(context_name="context")
def orchestrator(context):
    blob_info = context.get_input()
    blob_name = blob_info["name"]
    blob_size = blob_info["size"]
    
    yield context.call_activity("logBlobName", blob_name)
    yield context.call_activity("logBlobSize", str(blob_size))
