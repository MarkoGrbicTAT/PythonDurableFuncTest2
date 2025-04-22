import azure.functions as func
import azure.durable_functions as df
import logging

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@myApp.blob_trigger(arg_name="myblob", 
                   path="competitor-pdfs",
                   connection="") 
@myApp.durable_client_input(client_name="client")
async def blob_trigger(myblob: func.InputStream, client):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}")
    
    blob_info = {
        "name": myblob.name,
        "size": myblob.length 
    }
    
    await client.start_new("orchestrator", client_input=blob_info)
    
@myApp.orchestration_trigger(context_name="context")
def orchestrator(context):
    blob_info = context.get_input()
    blob_name = blob_info["name"]
    blob_size = blob_info["size"]
    
    yield context.call_activity("logBlobName", blob_name)
    yield context.call_activity("logBlobSize", str(blob_size))

@myApp.activity_trigger(input_name="blobName")
def logBlobName(blobName: str):
    logging.info("Blob name: " + blobName)

@myApp.activity_trigger(input_name="blobSize")
def logBlobSize(blobSize: str):
    logging.info("Blob size: " + blobSize)