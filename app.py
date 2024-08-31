import random
import streamlit as st
import requests as rq

# Fetch the word list
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = rq.get(word_site)
WORDS = response.content.splitlines()
cleaned_words = [word.decode('utf-8') for word in WORDS]

# Streamlit app interface
st.header("Welcome to this random fantasy word name scramble")
st.write("------------------------------------------")

# Input for scramble factor
scrambleFactor = st.text_input("How many letter swaps per word?", "1")
scrambleFactor = int(scrambleFactor)
clicked = st.button("Generate")

# Initialize lists to store words
toScramble = []
scrambled = []

if clicked:
    # Select 10 random words
    for _ in range(10):
        selected_word = random.choice(cleaned_words)
        toScramble.append(selected_word)

    # Scramble each word based on the scramble factor
    for entry in toScramble:
        word = list(entry)  # Convert word to list of characters for swapping
        for _ in range(scrambleFactor):
            # Choose two random indices to swap
            idx1, idx2 = random.sample(range(len(word)), 2)
            # Swap the letters at the selected indices
            word[idx1], word[idx2] = word[idx2], word[idx1]
        scrambled.append(''.join(word))  # Convert list back to string

    # Display the original and scrambled words
    st.write("Original Words:")
    st.write(toScramble)
    st.write("Scrambled Words:")
    st.write(scrambled)
