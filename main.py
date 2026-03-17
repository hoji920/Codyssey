import os

def main():
    # 설치 확인 출력
    print("Hello Mars")
    
    file_path = 'mission_computer_main.log'
    
    # 파일 존재 여부 확인 및 예외 처리
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} 파일을 찾을 수 없습니다.")

        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"\n--- {file_path} 내용 출력 ---")
            content = file.read()
            print(content)

        # 역순 출력
        with open(file_path, 'r', encoding='utf-8') as revFile:
            lines = revFile.readlines()
            for line in reversed(lines):  # 역순으로 하나씩 꺼냄
                print(line.strip())
            
    except FileNotFoundError as e:
        print(f"오류: {e}")
    except PermissionError:
        print("오류: 파일에 접근할 권한이 없습니다.")
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")

if __name__ == "__main__":
    main()