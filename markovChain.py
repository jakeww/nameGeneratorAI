import random

def build_markov_chain(data):
    markov_chain = {}
    for line in data:
        words = line.strip().split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if current_word in markov_chain:
                markov_chain[current_word].append(next_word)
            else:
                markov_chain[current_word] = [next_word]
    return markov_chain

def generate_text(markov_chain, length):
    current_word = random.choice(list(markov_chain.keys()))
    generated_text = current_word
    for i in range(length-1):
        if current_word in markov_chain:
            current_word = random.choice(markov_chain[current_word])
            generated_text += ' ' + current_word
    return generated_text

with open("cleanedNameData.txt", "r") as f:
    data = f.readlines()

markov_chain = build_markov_chain(data)

for i in range(3):
    generated_name = generate_text(markov_chain, length=3)
    print(generated_name)
