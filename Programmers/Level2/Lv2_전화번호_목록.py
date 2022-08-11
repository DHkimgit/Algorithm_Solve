def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: x, reverse=True) # 사전 순 내림차순 정렬
    idx = len(phone_book) - 1 # phone_book의 마지막 요소부터 검사
    while idx > 0:
        key = phone_book[idx] # 비교 대상
        if phone_book[idx-1][:len(key)] == key: return False # 바로 앞 숫자와 비교
        idx -= 1
    return True
