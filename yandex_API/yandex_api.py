import requests

from config import url, token

'''
    Приложение создает папку в Яндекс.Диске с помошью API
'''

headers = {
    "Authorization": f"{token}"
}
params = {
    "path": "/folder_name"
}

def create_folder(url, headers, params):
    """
        Функция для создания папки на Яндекс.Диске с помощью API.
        Возвращает ответ от сервера.
    """
    responce = requests.put(url, headers=headers, params=params)
    return responce

def delete_folder(url, headers, params):
    """
        Функция для удаления папки на Яндекс.Диске с помощью API.
        Возвращает ответ от сервера.
    """
    responce = requests.delete(url, headers=headers, params=params)
    return responce

# if __name__ == "__main__":
#     # print(create_folder(url, headers, params))
#     # print(delete_folder(url, headers, params))
