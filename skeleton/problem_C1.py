from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 월별 책 정보 모아보고 평균 가격 계산하기
# 아래에 전체 코드 작성
# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
current_path = Path.cwd()  # 파일 경로 설정 부분

file_path = current_path/'skeleton'/'data'/'books_2000.json'

# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일 존재 여부 확인
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        # JSON 파일을 파이썬 딕셔너리(리스트)로 변환하는 코드 (json.load)
        data = json.load(file)

    # 3. 월별 가격 정보 취합
    # 각 도서의 'pubDate'에서 '연-월'을 추출하고, 'priceSales'를 월별로 묶습니다.
    monthly_prices = {}  # 월별 가격을 저장할 빈 딕셔너리
    for item in data:  # 도서 리스트를 순회
        pub_date = item.get('pubDate')  # 출간일 가져오기
        price = item.get('priceSales')  # 판매가 가져오기

        if not pub_date or price is None:  # 값이 없는 경우 건너뛰기
            continue

        month = datetime.strptime(pub_date, '%Y-%m-%d').month  # '월'만 정수로 추출

        if month not in monthly_prices:  # 처음 등장하는 월이면 리스트 생성
            monthly_prices[month] = []

        monthly_prices[month].append(price)  # 가격을 월별 리스트에 추가하는 코드 (monthly_prices[year_month].append)

    # 4. 월별 평균 가격 계산
    # 월별로 모인 가격 리스트의 평균을 계산합니다.
    monthly_avg_price = {}  # 월별 평균 가격을 저장할 빈 딕셔너리
    monthly_book_count = {}  # 월별 도서 수를 저장할 빈 딕셔너리

    for month, prices in monthly_prices.items():  # 월별로 순회
        monthly_avg_price[month] = sum(prices) / len(prices)  # 평균 계산 코드 (sum(prices) / len(prices))
        monthly_book_count[month] = len(prices)  # 도서 수 계산

    # 5. 결과 출력
    # 월별 평균 가격을 연-월 순서로 정렬하여 출력합니다.
    print("월별 평균 가격 및 도서 수:")
    for month in sorted(monthly_avg_price):  # 연-월 순서로 정렬
        avg_price = monthly_avg_price[month]
        book_count = monthly_book_count[month]
        print(f"{month}월: 평균 가격 {avg_price:.2f}원 (총 {book_count}권)") # 월별 평균 가격을 출력하는 코드 (print)

else:
    # 6. 파일이 없을 경우 처리
    # 파일이 존재하지 않으면 오류 메시지를 출력합니다.
    print(f"파일이 존재하지 않습니다: {file_path}")
    # 파일이 존재하지 않을 때의 처리 코드 (print(f"파일이 존재하지 않습니다: {file_path}"))