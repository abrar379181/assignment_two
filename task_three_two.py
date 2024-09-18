from transformers import AutoTokenizer
from collections import Counter


def count_unique_tokens(text_file, model_name='bert-base-uncased', chunk_size=5000, max_length=512):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    token_count = Counter()

    with open(text_file, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            tokens = tokenizer.tokenize(chunk, truncation=True, max_length=max_length, clean_up_tokenization_spaces=True)
            token_count.update(tokens)

    return token_count.most_common(30)
