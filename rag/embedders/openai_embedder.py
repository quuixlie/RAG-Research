from rag.embedders.__embedder_template import EmbedderTemplate
from numpy import ndarray
from openai import OpenAI
import numpy as np
from typing import List # Import List for type hinting

class OpenAIEmbedder(EmbedderTemplate):
    """
    OpenAI embedder which uses OpenAI API to encode text fragments into embeddings.

    :param embedder_name: Name of the embedder
    :param openai_api_key: OpenAI API key
    :param openai_model: OpenAI model name (e.g., "text-embedding-ada-002")
    """

    def __init__(self, embedder_name: str, api_key: str, model_name: str, dimension: int) -> None:
        super().__init__(embedder_name)
        self.__openai_client = OpenAI(api_key=api_key)
        self.openai_model = model_name
        self.dimension = dimension 


    def encode(self, fragments: List[str], show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings using the OpenAI API.

        :param fragments: List of text fragments (strings) to encode.
        :param show_progress_bar: Whether to show a progress bar (not implemented for this client).
        :return: A 2D numpy array of embeddings (N, D) where N is the number of fragments
                 and D is the embedding dimension. If only one fragment is passed,
                 a 1D numpy array of shape (D,) is returned.
                 Returns an empty 0-D array if the input list is empty.
        """
        if not fragments:
            return np.array([]) # Return an empty array for empty input

        # Ensure all fragments are strings, as expected by the API
        string_fragments = [str(f) for f in fragments]

        try:
            # Call the OpenAI embeddings API
            response = self.__openai_client.embeddings.create(
                input=string_fragments,
                model=self.openai_model,
                dimensions=self.dimension,
            )
            
            # Extract the embedding vectors from the response
            # response.data is a list of Embedding objects
            # Each Embedding object has an 'embedding' attribute which is the list of floats
            embeddings_list = [item.embedding for item in response.data]
            
            # Convert the list of embeddings to a NumPy array
            # Specify dtype for consistency, float32 is common for embeddings
            embeddings_np = np.array(embeddings_list, dtype=np.float32)

            
            return embeddings_np

        except Exception as e:
            # Log the error or handle it as appropriate for your application
            print(f"Error during OpenAI embedding generation: {e}")
            # Re-raise the exception or return a specific error indicator
            # For now, re-raising to make the caller aware of the failure.
            raise