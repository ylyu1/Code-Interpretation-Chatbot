import os
# Access API keys from environment variables
pinecone_api_key = os.getenv("PINECONE_API_KEY")

from pinecone import Pinecone
# Initialize client connection
pc = Pinecone(api_key=pinecone_api_key)

# Create a serverless index
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

# Connect to an existing index
index_name = "lightyear" # Specify the name of your Pinecone index
index = pc.Index(index_name) 
stats = index.describe_index_stats() # Get index statistics
print(stats) # Print the stats
