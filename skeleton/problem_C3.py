import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리

# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
file_path = Path('skeleton/data/books_2000.json')  # JSON 파일 경로 설정

output_path = Path('series.json')
# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일이 존재할 경우
    # rglob을 사용해 하위 폴더를 포함한 모든 JSON 파일을 재귀적으로 탐색
    

    # 3. 시리즈 정보 추출 및 병합
    series_data = {}  # 시리즈별 정보를 저장할 빈 딕셔너리
    with file_path.open('r', encoding='utf-8') as file:
            # JSON 파일을 파이썬 딕셔너리로 변환하는 코드 (json.load)
            books = json.load(file)  # JSON 파일을 파이썬 딕셔너리(리스트)로 변환

    for item in books:  # 파일 안의 도서 리스트를 순회
        series_info = item.get('seriesInfo')  # 시리즈 정보 가져오기

        if not series_info:  # 시리즈 정보가 없는 도서는 건너뛰기
            continue

        series_id = series_info.get('seriesId')  # 시리즈 ID 가져오기
        series_name = series_info.get('seriesName')  # 시리즈 이름 가져오기

        if series_id is None:  # 시리즈 ID가 없으면 건너뛰기
            continue

        series_key = str(series_id)  # JSON의 key는 문자열이어야 하므로 변환

        if series_key not in series_data:  # 처음 등장하는 시리즈면 새로 생성
            series_data[series_key] = {
                "seriesId": series_id,
                "seriesName": series_name,
                "books": []
            }

        # 요구사항에 맞는 도서 정보만 정리
        book_info = {
            "title": item.get('title'),
            "link": item.get('link'),
            "author": item.get('author'),
            "pubDate": item.get('pubDate'),
            "description": item.get('description'),
            "isbn": item.get('isbn'),
            "isbn13": item.get('isbn13')
        }

        series_data[series_key]["books"].append(book_info)  # 도서 정보를 해당 시리즈에 추가
    # 4. 새로운 JSON 파일 생성
    with output_path.open('w', encoding='utf-8') as out_file:
        json.dump(series_data, out_file, ensure_ascii=False, indent=2)  # JSON 파일로 저장

    # 5. 결과 출력
    if output_path.exists():  # 생성된 파일이 실제로 존재하는지 검증
        print("모든 시리즈 데이터가 series.json 파일로 병합되었습니다.")
    else:
        print("series.json 파일 생성에 실패했습니다.")

else:
    # 6. 디렉토리가 없을 경우 처리
    print(f"디렉토리가 존재하지 않습니다: {file_path}")