from typing import Literal,Optional
import langchain_huggingface
from langchain_core.embeddings.embeddings import Embeddings
from pydantic import BaseModel

HuggingFaceEmbedderName = Literal["sentence-transformers/all-mpnet-base-v2"]
EmbedderName = HuggingFaceEmbedderName

class EmbedderKwargs(BaseModel):
    api_key: Optional[str] = None
    model_kwargs: dict = {'device':'cuda'}
    encode_kwargs: dict = {'normalize_embeddings':False}

langchain_huggingface.HuggingFaceEmbeddings

def embedder_factory(name: EmbedderName, args: EmbedderKwargs) -> Embeddings:

    # TODO :: Add some way of projecting the embeddings to different sizes


    match name:
        case "sentence-transformers/all-mpnet-base-v2":
            return langchain_huggingface.HuggingFaceEmbeddings(
                model_name=name,
                model_kwargs=args.model_kwargs,
                encode_kwargs=args.encode_kwargs
            )

    raise Exception("Invalid embedder name: {}".format(name))

if __name__ == "__main__":

    text = "Hello I am under the water please help me"
    text2 = "Indian guy recording himself"

    embedder = embedder_factory("sentence-transformers/all-mpnet-base-v2",EmbedderKwargs())

    print(embedder.embed_query(text))
    print(embedder.embed_query(text2))

