import unittest
from unittest.mock import patch
from io import StringIO
import os
import tempfile

from main import (
    open_files, close_files, kitap_ekle, kitap_listele, kitap_guncelle,
    kitap_sil, kitap_ara, kullanici_ekle, kullanici_listele, kullanici_guncelle,
    kullanici_sil, kitap_odunc_alindi_mi, odunc_al, kitap_geri_getir, odunc_listele,
    kullanici_bilgisi_getir, kitap_bilgisi_getir
)

class TestYourCode(unittest.TestCase):

    def setUp(self):
        # Create temporary test files 
        self.kitaplar_test_fd, self.kitaplar_test_path = tempfile.mkstemp()
        self.kullanicilar_test_fd, self.kullanicilar_test_path = tempfile.mkstemp()
        self.odunc_test_fd, self.odunc_test_path = tempfile.mkstemp()

        with open(self.kitaplar_test_path, "w") as kitap_dosyasi:
            kitap_dosyasi.write("1 Book1 Author1 100\n")
            kitap_dosyasi.write("2 Book2 Author2 150\n")

        with open(self.kullanicilar_test_path, "w") as kullanici_dosyasi:
            kullanici_dosyasi.write("1 User1 Surname1 01.01.1990\n")
            kullanici_dosyasi.write("2 User2 Surname2 02.02.1995\n")

        with open(self.odunc_test_path, "w") as odunc_dosyasi:
            odunc_dosyasi.write("1 1 01.01.2022 15.01.2022\n")

    def tearDown(self):
        # Remove temporary test files
        os.remove(self.kitaplar_test_path)
        os.remove(self.kullanicilar_test_path)
        os.remove(self.odunc_test_path)

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_open_files(self):
        with patch('builtins.input', side_effect=[self.kitaplar_test_path, self.kullanicilar_test_path, self.odunc_test_path]):
            open_files()

        # Check if files are opened successfully
        self.assertIsNotNone(open(self.kitaplar_test_path, "r"))
        self.assertIsNotNone(open(self.kullanicilar_test_path, "r"))
        self.assertIsNotNone(open(self.odunc_test_path, "r"))

    def test_close_files(self):
        # Open files before closing them
        open(self.kitaplar_test_path, "r")
        open(self.kullanicilar_test_path, "r")
        open(self.odunc_test_path, "r")

        with patch('builtins.input', side_effect=[self.kitaplar_test_path, self.kullanicilar_test_path, self.odunc_test_path]):
            close_files()

        # Check if files are closed successfully
        with self.assertRaises(FileNotFoundError):
            open(self.kitaplar_test_path, "r")
        with self.assertRaises(FileNotFoundError):
            open(self.kullanicilar_test_path, "r")
        with self.assertRaises(FileNotFoundError):
            open(self.odunc_test_path, "r")

    def test_kitap_ekle(self):
        with patch('builtins.input', side_effect=['Book3', 'Author3', '200']):
            kitap_ekle()

        # Check if the added book is present in the file
        with open(self.kitaplar_test_path, "r") as kitap_dosyasi:
            content = kitap_dosyasi.read()
            self.assertIn("Book3 Author3 200\n", content)

    def test_kitap_listele(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            kitap_listele()
        expected_output = "1 Book1 Author1 100\n2 Book2 Author2 150"
        self.assert_stdout(expected_output, mock_stdout)


class TestBookFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file_name = "test_kitaplar.txt"
        self.temp_test_file_name = "temp_test_kitaplar.txt"
        self.create_test_file()

    def tearDown(self):
        # Remove the temporary test file after each test
        if os.path.exists(self.temp_test_file_name):
            os.remove(self.temp_test_file_name)

    def create_test_file(self):
        # Create a test file with some initial data
        with open(self.test_file_name, "w") as test_file:
            test_file.write("1234 Book1 Author1 200\n")
            test_file.write("5678 Book2 Author2 300\n")

    def test_kitap_ekle(self):
        # Test adding a new book
        with patch("builtins.input", side_effect=["TestBook", "TestAuthor", "150"]):
            kitap_ekle()

        # Check if the test book is added to the temporary file
        with open(self.temp_test_file_name, "r") as test_file:
            lines = test_file.readlines()
            self.assertIn("TestBook TestAuthor 150\n", lines)

    def test_kitap_listele(self):
        # Test listing books
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            kitap_listele()

        # Check if the output contains the existing books
        output = mock_stdout.getvalue()
        self.assertIn("1234 Book1 Author1 200\n", output)
        self.assertIn("5678 Book2 Author2 300\n", output)

    def test_kitap_guncelle(self):
        # Test updating an existing book
        with patch("builtins.input", side_effect=["1234", "UpdatedBook", "UpdatedAuthor", "250"]):
            kitap_guncelle()

        # Check if the test book is updated in the temporary file
        with open(self.temp_test_file_name, "r") as test_file:
            lines = test_file.readlines()
            self.assertIn("1234 UpdatedBook UpdatedAuthor 250\n", lines)
            self.assertNotIn("1234 Book1 Author1 200\n", lines)

    def test_kitap_sil(self):
        # Test deleting an existing book
        with patch("builtins.input", side_effect=["1234"]):
            kitap_sil()

        # Check if the test book is deleted from the temporary file
        with open(self.temp_test_file_name, "r") as test_file:
            lines = test_file.readlines()
            self.assertNotIn("1234 UpdatedBook UpdatedAuthor 250\n", lines)

    def test_kitap_ara(self):
        # Test searching for a book
        with patch("builtins.input", return_value="Book2"):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                kitap_ara()

        # Check if the output contains the searched book
        output = mock_stdout.getvalue()
        self.assertIn("5678 Book2 Author2 300\n", output)
        self.assertNotIn("1234 Book1 Author1 200\n", output)

    def test_kullanici_ekle(self):
        with patch('builtins.input', side_effect=['User3', 'Surname3', '03.03.2000']):
            kullanici_ekle()

        with open("kullanicilar_test.txt", "r") as kullanici_dosyasi:
            lines = kullanici_dosyasi.readlines()
            self.assertEqual(len(lines), 3)

    def test_kullanici_listele(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            kullanici_listele()
        expected_output = "1 User1 Surname1 01.01.1990\n2 User2 Surname2 02.02.1995"
        self.assert_stdout(expected_output, mock_stdout)

    def test_kullanici_guncelle(self):
        with patch('builtins.input', side_effect=['1', 'UpdatedUser', 'UpdatedSurname', '04.04.1995']):
            kullanici_guncelle()

        with open("kullanicilar_test.txt", "r") as kullanici_dosyasi:
            lines = kullanici_dosyasi.readlines()
            self.assertIn("1 UpdatedUser UpdatedSurname 04.04.1995\n", lines)
            self.assertNotIn("1 User1 Surname1 01.01.1990\n", lines)

    def test_kullanici_sil(self):
        with patch('builtins.input', side_effect=['1']):
            kullanici_sil()

        with open("kullanicilar_test.txt", "r") as kullanici_dosyasi:
            lines = kullanici_dosyasi.readlines()
            self.assertNotIn("1 UpdatedUser UpdatedSurname 04.04.1995\n", lines)

    def test_kitap_odunc_alindi_mi(self):
        result = kitap_odunc_alindi_mi("1", "1")
        self.assertTrue(result)

    def test_odunc_al(self):
        with patch('builtins.input', side_effect=['1', '1', '20.02.2022']):
            odunc_al()

        with open("odunc_test.txt", "r") as odunc_dosyasi:
            lines = odunc_dosyasi.readlines()
            self.assertEqual(len(lines), 2)

    def test_kitap_geri_getir(self):
        with patch('builtins.input', side_effect=['1']):
            kitap_geri_getir()

        with open("odunc_test.txt", "r") as odunc_dosyasi:
            lines = odunc_dosyasi.readlines()
            self.assertNotIn("1 1 01.01.2022 15.01.2022\n", lines)

    def test_odunc_listele(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            odunc_listele()
        expected_output = "1 1 01.01.2022 15.01.2022"
        self.assert_stdout(expected_output, mock_stdout)

    def test_kullanici_bilgisi_getir(self):
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                kullanici_bilgisi_getir()
        expected_output = "1 User1 Surname1 01.01.1990"
        self.assert_stdout(expected_output, mock_stdout)

    def test_kitap_bilgisi_getir(self):
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                kitap_bilgisi_getir()
        expected_output = "1 Book1 Author1 100"
        self.assert_stdout(expected_output, mock_stdout)

if __name__ == '__main__':
    unittest.main()