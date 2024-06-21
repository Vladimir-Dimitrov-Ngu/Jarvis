import re

from rank_bm25 import BM25Okapi

print("rag activated")
with open("./data/prices_rag.txt") as file:
    text = file.readlines()

tokenized_corpus = [doc.split(" ") for doc in text]
bm25 = BM25Okapi(tokenized_corpus)
calc_regex = re.compile(r"(цен| стоимо| стоит)", re.IGNORECASE)

print("rag active")


def get_top_n(query, n=1):
    tokenized_query = query.split(" ")
    top_n = bm25.get_top_n(tokenized_query, text, n=n)
    return top_n


def rag_activation(query):
    if calc_regex.search(query):
        return get_top_n(query, n=1)
    else:
        return False


if __name__ == "__main__":
    print(rag_activation("Сколько стоит Наука-Связь?"))
