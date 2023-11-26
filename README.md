# LLM_Query_Engine by Vatan Narang

# Requirements and Dependencies
1. Python 3.X
2. Numpy
3. Pandas
4. Requests
5. Flask
6. Sentence Transformers
7. Qdrant Client
8. Scikit Learn
9. [Qdrant](https://qdrant.tech/)
10. [Docker](https://docs.docker.com/get-docker/)

   Install using requirements.txt
   ```
    pip3 install -r requirements.txt
   ```

# Setup
1. Download the Qdrant image from Docker
   ```
   docker pull qdrant/qdrant
   ```
2. Run the qdrant service
   ```
   docker run -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage:z qdrant/qdrant
   ```
3. A qdrant_storage folder is created at the specified location and the data will be stored there.
   Qdrant is now accessible, API:localhost:6333

# Generate Embeddings
1. Run the "generate_embeddings.py" file to generate the embeddings from the bigBasketProducts.csv file. This will create a "bb_chaabi_vectors.npy" vectors file.
   ```
   python generate_embeddings.py
   ```

# Upload Embeddings
1. Run the "upload_embeddings.py" file. This file will upload all your embeddings in the collection and make a collection of name "bb-chaabi".
   ```
   python upload_embeddings.py
   ```

# Frontend Interface
1. The Frontend interface is made using Flask (supported by Python).
2. The app.py is the file that loads the flask app, with its frontend dependencies available in 'static' and 'templates' folder.
3. The "app.py" imports its 'llm_searcher' from the "search_main.py" file which contains the function to generate the results of a sample query based on the best similarity scores achieved.
   ```
   python app.py
   ```
4. This creates a local host on the computer with the address http://127.0.0.1:5000/
5. This address displays the frontend page where the query search engine works.

# Video Tutorial
This video tutorial shows the qdrant setup as well as the running of the frontend application with the collection "bb-chaabi".

https://github.com/narang-v/LLM_Query_Engine/assets/84620915/4f6d7ccd-f5d0-4467-9249-2644d8e6cb9e

# Sample Test Results
1. Query given - Oil & Masala

![Welcome to the Query Engine - Google Chrome 26-11-2023 13_23_21](https://github.com/narang-v/LLM_Query_Engine/assets/84620915/081e974d-5dae-4eca-91ca-96ac08beabd9)
   
![Welcome to the Query Engine - Google Chrome 26-11-2023 13_23_56](https://github.com/narang-v/LLM_Query_Engine/assets/84620915/72a64d46-6260-43dc-9896-bc6481153091)

2. Query given - green fresh vegetables that are good for health

![Welcome to the Query Engine - Google Chrome 26-11-2023 13_25_54](https://github.com/narang-v/LLM_Query_Engine/assets/84620915/adf1108e-925c-4a58-8c33-dd5fb26908de)

![Welcome to the Query Engine - Google Chrome 26-11-2023 13_26_22](https://github.com/narang-v/LLM_Query_Engine/assets/84620915/9a57d5b2-faff-4be9-90f7-59dcf6bf4ca6)

