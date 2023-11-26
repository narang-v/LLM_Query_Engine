# This file uploads the generated embeddings present in the bb-chaabi.npy file to the collection
# The collection is given name "bb-chaabi".
# The queries are responded using this collection in the "search_main.py" file.
# Libraries import
import os.path
import numpy as np
import pandas as pd
from qdrant_client import QdrantClient, models
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import os

# Qdrant Details
QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY", "")

# Defining Collection Name
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "bb-chaabi")

VECTOR_FIELD_NAME = "fast-bge-small-en"
TEXT_FIELD_NAME = "index"

# Function to upload our generated vector embeddings to our collection
def upload_embeddings():
    # Qdrant Client 
    client = QdrantClient(
        url=QDRANT_URL
    )

    # Dataset read    
    df=pd.read_csv('bigBasketProducts.csv') # set path to dataset file here
    
    # Dataset Preprocessing
    df.fillna({"rating":0}, inplace= True)
    df.fillna("NA", inplace=True)
    payload = df.to_dict('records')

    # Already Generated vectors
    vectors = np.load('bb_chaabi_vectors.npy') #set path to the vector file here
    
    # making our collection from the vectors
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            VECTOR_FIELD_NAME: models.VectorParams(
                size=vectors.shape[1],
                distance=models.Distance.COSINE
            )
        },
        quantization_config=models.ScalarQuantization(
            scalar=models.ScalarQuantizationConfig(
                type=models.ScalarType.INT8,
                quantile=0.99,
                always_ram=True
            )
        )
    )

    # uploading our collection with the name "bb-chaabi"
    client.upload_collection(
        collection_name=COLLECTION_NAME,
        vectors={
            VECTOR_FIELD_NAME: vectors
        },
        payload=payload,
        ids=None,  
        batch_size=256
    )


if __name__ == '__main__':
    upload_embeddings()
