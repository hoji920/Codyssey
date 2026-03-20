import csv

file_path = 'Mars_Base_Inventory_List.csv'

with open(file_path,'r',encoding='utf-8') as file:

    # Mars_Base_Inventory_List 출력
    print(f"\n----- {file_path} 출력 -----")
    for files in file:
        print(files.strip())

    # 파일 포인터를 다시 맨 처음(0)으로 이동
    file.seek(0)

    # 리스트로 변환 및 배열 할당
    reader = csv.reader(file)
    list =[]
    for readers in reader:
        # print(readers)
        list.append(readers)

    # 인화성이 높은 순으로 정렬
    list.sort(key=lambda x: x[4],reverse=True)
    print(f"\n----- {file_path} 내림차순 정렬 -----")
    for sortList in list:
        print(sortList)

    # 인화성 지수 0.7이상 출력
    high_value_items = []
    print(f"\n----- {file_path} 인화성 지수가 0.7 이상 출력 -----")
    for row in list:
        try:
            if float(row[4]) >= 0.7:
                high_value_items.append(row)
        except ValueError:
            pass
    
    for highList in high_value_items:
        print(highList)
