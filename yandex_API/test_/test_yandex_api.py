import unittest
from unittest import TestCase

from yandex_api import create_folder, url, headers, params  # импорт функции для тестирования

class Testyandex_api(TestCase):

    def test_create_folder(self):
        """
        Тест создания папки на Яндекс.Диске.
        Проверяет, что статус код равен 201 (Создано).
        """
        self.assertEqual(create_folder(url, headers, params).status_code, 201)
    
    def test_err_create_folder(self):
        """
        Тест создания папки на Яндекс.Диске с тем же именем, что и существующая папка.
        Проверяет, что статус код равен 409 (Конфликт).
        """
        self.assertEqual(create_folder(url, headers, params).status_code, 409)

    def test_not_auth(self):
        """
        Тест создания папки на Яндекс.Диске без правильной авторизации.
        Проверяет, что статус код равен 401 (Несанкционировано).
        """
        headers1 = {
                "Authorization": ""
        }
        self.assertEqual(create_folder(url, headers1, params).status_code, 401)

if __name__ == '__main__':
    unittest.main()

