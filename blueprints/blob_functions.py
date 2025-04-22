import azure.functions as func
import azure.durable_functions as df
import logging

# Create blueprint for blob trigger function
blob_bp = df.Blueprint()

@blob_bp.blob_trigger(arg_name="myblob", 
                   path="competitor-pdfs",
                   connection="") 
@blob_bp.durable_client_input(client_name="client")
async def blob_trigger(myblob: func.InputStream, client):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}")
    
    blob_info = {
        "name": myblob.name,
        "size": myblob.length 
    }
    
    await client.start_new("orchestrator", client_input=blob_info)
