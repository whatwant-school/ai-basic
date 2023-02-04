from datetime import datetime

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]

    for i in range(10):
        try:
            print(i, 10 // i)
            print(a[i])
        except ZeroDivisionError as err:
            print(err)
            print(f"{datetime.now()} - Not divided by zero")
        except IndexError as e:
            print(e)
            print(f"{datetime.now()} - Index out of range exception")
        except Exception as e:
            print(e)
            print(f"{datetime.now()} - Other exception")
        finally:
            print(f"{datetime.now()} - Finally")  # Always executed
    
    while True:
        value = input("변환할 정수 값을 입력해주세요 : ")
        for digit in value:
            if digit not in "0123456789":
                raise ValueError("숫자값을 입력하지 않으셨습니다")
        print(f"정수값으로 변환된 숫자 - {int(value)}")
