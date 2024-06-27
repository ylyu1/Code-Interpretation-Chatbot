
# Get pinecone serverless API keys from environment
import os
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Initialize client connection
from pinecone import Pinecone
pc = Pinecone()

# Create serverless indexes
# Make sure the index name is unique each time you create a new index.
from pinecone import ServerlessSpec
pc.create_index(
    name="lightyear",
    dimension=1536, # dimensionality of text-embedding-ada-002
    metric='cosine',
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-west-2'
    ) 
) 

# Verify our indexes were created
print(pc.list_indexes())

# Need to connect to an existing index in order to ingest data
index_name = "lightyear" # Specify the name of your Pinecone index
index = pc.Index(index_name) 
stats = index.describe_index_stats() # Get index statistics
print(stats) # Print the stats
