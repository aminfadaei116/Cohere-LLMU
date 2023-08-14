from typing import Any, BinaryIO, Dict, Iterable, List, Optional, Union


def extract_embeding(co, prompt: List[str]):
    """
    Converts a string (sentence) to an embedding representation (a list of floating points).
    :param co: Class Cohere
        The Cohere model
    :param prompt: List[str]
        A list of sentences that needs to be embedded
    :return embeds: List[str]



    """
    response = co.embed(
        model='small',
        texts=prompt,
        truncate="END"
    )

    embeds = response.embeddings

    return embeds
