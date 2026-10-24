# CSV Text File Analyzer 🐍

A beginner-friendly Python project that reads student records from a CSV file, analyzes the data, and saves the results in a separate text file.

## 📌 Project Overview

This project demonstrates file handling and data analysis using Python. It reads student records containing roll numbers, names, courses, and marks, then performs basic text analysis.

## ✨ Features

- Upload a CSV file using Google Colab.
- Read and count the total number of lines.
- Count words and characters in the file data.
- Search for a specific word and count its occurrences.
- Find the longest and shortest words.
- Display analysis results in the output.
- Save the results in `analysis.txt`.

## 🛠️ Technologies Used

- Python
- CSV Module
- OS Module
- Google Colab

## 📂 Project Structure

```text
csv-text-file-analyzer/
├── main.py
├── README.md
├── .gitignore
└── analysis.txt  # Generated output (not committed)
```

## ▶️ How to Run

1. Open the Python program in [Google Colab](https://colab.research.google.com/).
2. Run the code cell.
3. Upload a CSV file containing the following column headers:

   `Roll Number, Name, Course, Marks`

4. Enter the word you want to search for when prompted.
5. View the analysis results in the output.
6. Find the generated report in `analysis.txt`.

## 📊 Sample CSV Data

```csv
Roll Number,Name,Course,Marks
101,Rahul Sharma,BCA,85
102,Priya Singh,BTech,92
103,Aman Kumar,BSc,78
```

## 📄 Output

The program displays and saves the following information:

- Number of lines
- Number of words
- Number of characters
- Occurrences of the searched word
- Longest word
- Shortest word

## 🎯 Learning Objectives

- Understand Python file handling.
- Work with CSV files using the `csv` module.
- Use lists, loops, functions, and conditional statements.
- Perform basic text analysis.
- Write analysis results to a text file.

## 👨‍💻 Author

Aditya Kumar

---

⭐ If you find this project useful, feel free to star the repository!
