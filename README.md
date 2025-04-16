# RAG-Research
Research project on Retrieval Augmented Generation. In addition to RAG, this repository also contains useful tools such as pipelines and validation metrics that are needed for research.

# Running

### Add the user to the docker group
This is needed to run the docker commands without sudo. This is only needed once, and you need to log out and back in for the changes to take effect.
Otherwise, you will need to run main.py with sudo.
```bash
sudo usermod -aG docker $USER
```