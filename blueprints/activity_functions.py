import azure.functions as func
import azure.durable_functions as df
import logging

# Create blueprint for activity functions
activity_bp = df.Blueprint()

@activity_bp.activity_trigger(input_name="blobName")
def logBlobName(blobName: str):
    logging.info("Blob name: " + blobName)

@activity_bp.activity_trigger(input_name="blobSize")
def logBlobSize(blobSize: str):
    logging.info("Blob size: " + blobSize)
