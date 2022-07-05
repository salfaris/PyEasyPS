# 📄 PyEasyPS

[EasyPS](https://github.com/salfaris/EasyPS) is a simple and easy-to-use personal statement LaTeX framework. This solves the problem of messy and duplicated tex files when writing personal statements for multiple universities.

PyEasyPS then provide a high-level Python API to use EasyPS.

![Screenshot](https://github.com/salfaris/EasyPS/blob/main/docs/example.png)

## Installation
```sh
git clone https://github.com/salfaris/PyEasyPS
cd ./PyEasyPS
```
Requirements:
- Python 3.9+
- pylatex 1.4.1

## Running
1. Write your personal statement in `./content`;
2. Link your personal statements using `PyEasyPS.University` objects in `main.py`;
Then compile to PDF using:
```sh
python3 main.py
```
