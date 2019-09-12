from unittest import TestCase, main
from unittest.mock import patch, mock_open
from read_file import read_file

class TestReadFile(TestCase):
    @patch("read_file.open", new_callable=mock_open, read_data="content")
    def test_read_file(self, mock_open):        
        r = read_file()
        self.assertEqual('content', r)


if __name__ == "__main__":
    main()
