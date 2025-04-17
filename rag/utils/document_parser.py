import pymupdf4llm
from pymupdf import Document
from multiprocessing import Pool, cpu_count


def parse_to_markdown(document: Document) -> str:
    """
    Parse the document to markdown using multiprocessing for performance.
    :param document: Document object
    :return: Parsed markdown content
    """
    num_proc = cpu_count()
    total_pages = document.page_count

    # Serialize the document into bytes
    document_bytes = document.write()  # Serialize the document
    document.close()  # Close the document after serialization

    # Divide the pages into chunks for each process
    pages_list = []
    pages = list(range(total_pages))
    chunk_size = (total_pages + num_proc - 1) // num_proc

    for i in range(0, total_pages, chunk_size):
        pages_list.append(pages[i:i + chunk_size])

    # Use multiprocessing to parse the document
    with Pool(processes=num_proc) as pool:
        results = pool.starmap(__parse_to_markdown, [(document_bytes, pages) for pages in pages_list])
        parsed_document_to_markdown = "".join(results)

    return parsed_document_to_markdown


def __parse_to_markdown(document_bytes: bytes, pages: list) -> str:
    """
    Parse given pages of the document to markdown.
    :param document_bytes: Serialized document bytes
    :param pages: List of pages to parse
    :return: Markdown content for the given pages
    """
    # Reconstruct the document from bytes
    document = Document(stream=document_bytes, filetype="pdf")
    markdown = pymupdf4llm.to_markdown(doc=document, pages=pages)
    document.close()  # Close the document after processing
    return markdown

