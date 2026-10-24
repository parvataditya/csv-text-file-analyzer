#Write a Python program to read a text file and perform the following
import csv

import os
from google.colab import files

uploaded = files.upload()


FILENAME = "/content/" + list(uploaded.keys())[0]
OUTPUT_FILE = "analysis.txt"

def analyze_file():
    """Read and analyze student records from CSV file."""

    if not os.path.exists(FILENAME):
        print("students.csv file not found.")
        return

    # Read the entire file as raw text first (for line counting)
    with open(FILENAME, "r") as f:
        raw_lines = f.readlines()

    if len(raw_lines) == 0:
        print("File is empty.")
        return

    # Number of lines = total lines in the file, including header
    number_of_lines = len(raw_lines)

    # Read records using DictReader for field-based analysis
    with open(FILENAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        records = list(reader)
        headers = reader.fieldnames

    if len(records) == 0:
        print("No student records found (only header present).")
        return

    # Build a list of actual WORDS (not CSV fields) by splitting on whitespace
    # Includes header row so the whole file is genuinely analyzed
    words = []
    words.extend(headers)  # header words, e.g. "Roll", "Number" if split by space

    for record in records:
        for field in [record["Roll Number"], record["Name"], record["Course"], record["Marks"]]:
            words.extend(field.split())  # splits multi-word names like "Rahul Sharma" properly

    # Count words
    number_of_words = len(words)

    # Count characters (sum of all word characters, no spaces/commas)
    number_of_characters = sum(len(word) for word in words)

    # Search for a particular word
    search_word = input("Enter the word to search: ").strip()

    occurrence = sum(1 for word in words if word.lower() == search_word.lower())

    # Find longest and shortest words
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    # Display results
    print("\n===== Student CSV Analysis =====")
    print("Number of lines:", number_of_lines)
    print("Number of words:", number_of_words)
    print("Number of characters:", number_of_characters)
    print(f"Occurrence of '{search_word}':", occurrence)
    print("Longest word:", longest_word)
    print("Shortest word:", shortest_word)

    # Store results in a separate TEXT file
    with open(OUTPUT_FILE, "w") as f:
        f.write("===== Student CSV Analysis =====\n")
        f.write(f"Number of lines: {number_of_lines}\n")
        f.write(f"Number of words: {number_of_words}\n")
        f.write(f"Number of characters: {number_of_characters}\n")
        f.write(f"Occurrence of '{search_word}': {occurrence}\n")
        f.write(f"Longest word: {longest_word}\n")
        f.write(f"Shortest word: {shortest_word}\n")

    print(f"\nAnalysis results saved in {OUTPUT_FILE}")


# Call the function
analyze_file()
