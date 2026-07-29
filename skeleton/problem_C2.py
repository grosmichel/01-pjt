import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 카테고리 데이터를 뽑아 JSON파일로 만들기
# 아래에 생성형 AI를 활용한 코드 작성
# pathlib을 사용하여 파일 경로를 설정합니다.
current_path = Path.cwd()  # 파일 경로 설정 부분

file_path = current_path/'skeleton'/'data'/'books_2000.json'
output_path = Path('category_books.json')  # 출력 파일 경로 설정

# 2. 파일 존재 여부 확인
if file_path.exists():  # 파일 존재 여부 확인
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)  # JSON 파일을 파이썬 딕셔너리(리스트)로 변환

    # 3. 카테고리별 도서 정보 분류
    category_books = {}  # 카테고리별 도서 정보를 저장할 빈 딕셔너리
    for item in data:  # 도서 리스트를 순회
        category_id = item.get('categoryId')  # 카테고리 ID 가져오기
        category_name = item.get('categoryName')  # 카테고리 이름 가져오기

        if category_id is None:  # 카테고리 ID가 없는 경우 건너뛰기
            continue

        category_key = str(category_id)  # JSON의 key는 문자열이어야 하므로 변환

        if category_key not in category_books:  # 처음 등장하는 카테고리면 새로 생성
            category_books[category_key] = {
                "name": category_name,
                "books": []
            }

        # 요구사항에 맞는 도서 정보(제목, 저자, 출판사, 출판일, ISBN, 가격)만 정리
        book_info = {
            "title": item.get('title'),
            "author": item.get('author'),
            "publisher": item.get('publisher'),
            "pubDate": item.get('pubDate'),
            "isbn": item.get('isbn13'),
            "price": item.get('priceSales')
        }

        category_books[category_key]["books"].append(book_info)  # 도서 정보를 해당 카테고리에 추가

    # 4. 새로운 JSON 파일 생성
    with output_path.open('w', encoding='utf-8') as out_file:
        json.dump(category_books, out_file, ensure_ascii=False, indent=2)  # JSON 파일로 저장

    # 5. 결과 출력
    if output_path.exists():  # 생성된 파일이 실제로 존재하는지 검증
        print(f"JSON 파일이 생성되었습니다: {output_path}")
    else:
        print("JSON 파일 생성에 실패했습니다.")

else:
    # 6. 파일이 없을 경우 처리
    print(f"파일이 존재하지 않습니다: {file_path}")