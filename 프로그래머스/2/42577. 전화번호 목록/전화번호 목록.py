def solution(phone_book:list):
    phone_book.sort()
    for i, j in zip(range(len(phone_book)), range(1, len(phone_book))):
        if phone_book[j].startswith(phone_book[i]):
            return False
    return True