import unittest
from services.criptografa_senha import *

class TestCriptografaSenha(unittest.TestCase):
    def test_sha356_default(self):
        self.assertEqual(
            hash_sha256('a51g7sj*7h$'),
            '30b36ef39adafb4e2ac8b80fc6069dc15bd1987679d21d57c89ca6f8789bbfa4'
        )

    def test_md5_default(self):
        self.assertEqual(
            hash_md5('a51g7sj*7h$'),
            'c31681978342cdec786cde3d038f9a25'
        )

    def test_sha256_empty(self):
        self.assertEqual(
            hash_sha256(''),
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        )

    def test_md5_empty(self):
        self.assertEqual(
            hash_md5(''),
            'd41d8cd98f00b204e9800998ecf8427e'
        )

if __name__ == '__main__':
    unittest.main()