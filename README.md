# Library Management System in Python
#### Video Demo:  https://youtu.be/uOSw8hl7F3Y?si=T9gjqhp20guU2G40

## Description:
This repository contains a simple Library Management System implemented in Python. The system is designed to manage information about books, users, and book loans. It includes both the main code (`main.py`) and a comprehensive suite of unit tests (`test_main.py`) to ensure the correctness of the implemented functions.

## Main Code (`main.py`)

### File Operations

The code provides functions for handling file operations, including opening and closing files related to books, users, and book loans. The standard Python `open` function is used for file manipulation.

### Book Management

The system allows various operations related to book management:
- `kitap_ekle`: Add a new book to the system.
- `kitap_listele`: List all available books.
- `kitap_guncelle`: Update information about an existing book.
- `kitap_sil`: Delete a book from the system.

### User Management

Similar to book management, the system includes functions for managing user information:
- `kullanici_ekle`: Add a new user to the system.
- `kullanici_listele`: List all registered users.
- `kullanici_guncelle`: Update information about an existing user.
- `kullanici_sil`: Delete a user from the system.

### Book Loan Management

The system supports tracking book loans:
- `odunc_al`: Record when a book is borrowed.
- `kitap_geri_getir`: Mark a book as returned.

### Information Retrieval

Functions like `kitap_bilgisi_getir` and `kullanici_bilgisi_getir` allow retrieving detailed information about a specific book or user based on user input.

## Unit Tests (`test_main.py`)

### Test Environment Setup

The unit tests are implemented using the `unittest` framework, and `unittest.mock` is utilized for patching and mocking. Temporary files are created using the `tempfile` module to isolate tests and prevent interference.

### Test Cases

Each function in the main code has a corresponding test case in `test_main.py`. For example, `test_kitap_ekle` tests the `kitap_ekle` function. The test cases cover various scenarios, including adding books, updating information, listing items, and handling loans.

### Assertions

The test cases include assertions to validate the expected behavior of the functions. Mocking is used to simulate user input during tests.

### File Operations Tests

Tests like `test_open_files` and `test_close_files` ensure that the file-related functions are working correctly, opening and closing files as intended.

## Usage

To use the Library Management System, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Run the main code: `python main.py`

Feel free to explore and modify the code to suit your needs. Contributions and improvements are welcome!
