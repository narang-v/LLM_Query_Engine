# Libraries import
import os
import uvicorn
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, Range
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "bb-chaabi") # Collection name "bb-chaabi"

# sentence-transformer searcher functionality class
class LLMSearcher:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        # initialize Qdrant client
        self.qdrant_client = QdrantClient("http://localhost:6333")

    # searching the text query
    def search(self, text: str):
        rnge = 0
        vector = self.model.encode(text).tolist()

        # filter according to the ratings
        query_filter = Filter(
            should=[
            FieldCondition(
                key="rating",
                range=Range(
                    gt=None,
                    gte=rnge,
                    lt=None,
                    lte=None,
                ),
            ),
        ],
        )
        
        limit = 15
        
        # search operation results
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=("fast-bge-small-en",vector),
            query_filter=None,
            limit=limit  # top 15 data entries
        )

        # returning top queries from the "search_result" according to the similarity scores
        payloads = [hit.payload for hit in search_result]
        return payloads
    

