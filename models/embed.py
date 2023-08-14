

def extract_embeding(co, prompt: str):
    output = co.embed(
        model='large',
        texts=prompt)
    embeds = output.embeddings

    print('Number of articles:', len(embeds))