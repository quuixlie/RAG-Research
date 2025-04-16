"""
This module contains utility functions to manage the vector database.
In this case, it is assumed that the vector database is running in a Docker container.
We manage the vector database using milvus bash script.


Installation instructions for Milvus can be found here:
(https://milvus.io/docs/install_standalone-docker.md)

Installation steps
curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o milvus.sh
"""
import docker
import subprocess


def is_vector_database_running(image_name: str) -> bool:
    """
    This function checks if the vector database container is running, based on the image name.
    It assumes that vector database is running in a Docker container.

    :param image_name: Name of the Docker image for the vector database
    :return: True if the container is running, False otherwise
    """

    client = docker.from_env()

    try:
        containers = client.containers.list()

        for container in containers:
            if image_name in container.image.tags:
                return True
    except docker.errors.APIError as e:
        print(f"Error checking Docker containers: {e}")
        return False

    return False


def start_vector_database() -> None:
    """
    This function starts the vector database container using milvus bash script.

    :return: None
    """

    subprocess.run(["bash", "milvus.sh", "start"], capture_output=True, check=True)


def stop_vector_database() -> None:
    """
    This function stops the vector database container using milvus bash script.

    :return: None
    """

    subprocess.run(["bash", "milvus.sh", "stop"], capture_output=True, check=True)