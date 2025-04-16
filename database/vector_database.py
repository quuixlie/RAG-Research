from pymilvus import MilvusClient, DataType, CollectionSchema


class VectorDatabase:
    def __init__(self):
        self.client = MilvusClient(
            uri="http://localhost:19530",
            token="root:Milvus"
        )


    def create_collection(self, conversation_d: int, dimension: int) -> None:
        """
        This function creates a collection in the vector database. If the collection already exists, it removes it first.

        :param conversation_d: ID of the conversation
        :param dimension: Dimension of the embedding
        :return: None
        """

        collection_name = self.__get_collection_name_by_id(conversation_d)

        # Remove the collection if it already exists
        if self.client.has_collection(collection_name):
            self.remove_collection(conversation_d)

        self.client.create_collection(collection_name, dimension, schema=self.__create_schema(dimension))
        self.client.create_index(collection_name, index_params=self.__create_index())


    def __get_collection_name_by_id(self, conversation_id: int) -> str:
        """
        This function generates a collection name based on the conversation ID.

        :param conversation_id: ID of the conversation
        :return: Collection name
        """

        return f"conversation_{conversation_id}"


    def __create_schema(self, dimension: int) -> CollectionSchema:
        """
        This function creates a schema for the collection.

        :param dimension: Dimension of the embedding
        :return: Collection schema
        """

        schema = MilvusClient.create_schema()

        # Add fields to the schema
        schema.add_field("id", datatype=DataType.INT64, is_primary=True, auto_id=True)
        schema.add_field("embedding", datatype=DataType.FLOAT_VECTOR, dim=dimension)
        schema.add_field("text", datatype=DataType.VARCHAR, max_length=65535)

        return schema


    def __create_index(self):
        """
        This function creates an index for the embedding field in the collection.

        :return: Index parameters for the embedding field
        """

        # Create an index for the embedding field
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="embedding",
            index_type="FLAT",  # or "HNSW"
            metric_type="COSINE",
        )

        return index_params


    def remove_collection(self, conversation_id: int) -> None:
        """
        This function removes a collection from the vector database.

        :param conversation_id: ID of the conversation
        :return: None
        """

        collection_name = self.__get_collection_name_by_id(conversation_id)

        if self.client.has_collection(collection_name):
            self.client.drop_collection(collection_name)
        else:
            return


    def has_collection(self, conversation_id: int) -> bool:
        """
        This function checks if a collection exists in the vector database.

        :param conversation_id: ID of the conversation
        :return: True if the collection exists, False otherwise
        """

        collection_name = self.__get_collection_name_by_id(conversation_id)
        return self.client.has_collection(collection_name)


    def insert_data(self, conversation_id: int, data: list):
        """
        This function inserts data into the vector database.

        :param conversation_id: ID of the conversation
        :param data: Data to be inserted
        """

        collection_name = self.__get_collection_name_by_id(conversation_id)
        self.client.insert(collection_name, data=data)


    def search(self, conversation_id: int, query_embedding: list):
        """
        This function searches for similar data in the vector database.

        :param conversation_id: ID of the conversation
        :param query_embedding: Query embedding to search for
        :return: Search results
        """

        collection_name = self.__get_collection_name_by_id(conversation_id)
        self.client.load_collection(collection_name)
        search_params = {
            "metric_type": "COSINE",
        }

        try:
            results = self.client.search(collection_name, anns_field="embedding", data=query_embedding,
                                         search_params=search_params,
                                         limit=5, output_fields=["text"])
        finally:
            self.client.release_collection(collection_name)

        return results

