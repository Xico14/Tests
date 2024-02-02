documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    """
        Добавляет новый документ в базу данных.
        Принимает тип документа, номер документа, имя владельца и номер полки.
    """
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
    return "Документ не найден"

def get_directory(doc_number):
    """
        Возвращает имя владельца документа по его номеру.
        Принимает номер документа.
    """
    for dir in directories:
        if doc_number in directories[dir]:
            return dir
    return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
    """
        Возвращает номер полки, на которой находится документ.
        Принимает номер документа.
    """
    documents.append({"type": document_type, "number": number, "name": name})
    directories[shelf_number].append(number)
    return documents


# if __name__ == '__main__':
#     print(get_name("10006"))
#     print(get_name("311 020203"))
#     print(get_name("101"))
#     print(get_directory("11-2"))
#     print(get_directory("311 020203"))
#     print(get_directory("311 020204"))
#     print(add('international passport', '311 020203', 'Александр Пушкин', '3'))