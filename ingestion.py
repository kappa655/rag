import pymupdf4llm
import os

with open('cat-facts.txt', 'r') as file:
    cat_facts = file.readlines()
    print(f"Loaded {len(cat_facts)} cat facts from 'cat-facts.txt'.")





def cosine_similarity(a, b):

    dot_product = 0
    for x, y in zip(a, b):
        dot_product = dot_product + (x * y)

    norm_a = sum([x ** 2 for x in a]) ** 0.5
    norm_b = sum([y ** 2 for y in b]) ** 0.5

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)

