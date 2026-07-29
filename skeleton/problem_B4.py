from datetime import datetime  # 날짜와 시간 처리를 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 1. 파일 경로 설정 (books_500.json 사용)
current_path = Path.cwd()  # 파일 경로 설정 부분

file_path = current_path/'skeleton'/'data'/'books_500.json'
# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    with file_path.open('r', encoding='utf-8') as books:  # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)
        books = json.load(books)

    # 3. 출판일을 기준으로 최신 도서 10개 추출 (hint: sorted 함수 key 속성)
      # 최신 도서 10개를 추출하는 코드
        latest_books = sorted(books, key=lambda x : datetime.strptime(x["pubDate"],"%Y-%m-%d"), reverse=True)
    # 4. 결과 출력
    print("최신 도서 10개:")
    for book in latest_books[0:10]:  # 선택된 도서를 순회하며 출력
        print(book["title"], '-', book["pubDate"])  # 도서 제목과 출판일을 출력하는 코드

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
