import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='shopdb',
    charset='utf8'
)

curs = conn.cursor()

def good_all():
    try:
        sql = "select * from product"
        curs.execute(sql)
        result = curs.fetchall()
        for data in result:
            print(data)
    except Exception as e:
        print(f"에러 발생: {e}")

def good_search():
    try:
        user_search = input("제품번호 입력 : ")
        sql = "select * from product where pcode = %s"
        curs.execute(sql, user_search)
        result = curs.fetchone()
        if result:
            print(result)
        else:
            print("해당 제품을 찾을 수 없습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

def good_add():
    try:
        good_number = input("제품번호 입력 : ")
        good_name = input("제품명 입력 : ")
        good_price = int(input("제품가격 입력 : "))
        good_quantity = int(input("제품수량 입력 : "))
        
        sql = "insert into product (pCode, pName, price, amount) values (%s,%s,%s,%s)"
        curs.execute(sql, (good_number, good_name, good_price, good_quantity))
        conn.commit()
        print(f"{good_number}이 입력 되었습니다")
    except ValueError:
        print("가격과 수량은 숫자로 입력해야 합니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

def good_update():
    try:
        user_update = input("수정할 제품번호 입력 : ")
        sql_1 = "select * from product where pcode = %s"
        curs.execute(sql_1, user_update)
        result = curs.fetchone()
        if not result:
            print("해당 제품을 찾을 수 없습니다.")
            return
        print(result)
        
        user_update_number = input("수정 제품번호 입력 : ")
        user_update_name = input("수정 제품명 입력 : ")
        user_update_price = int(input("수정 제품가격 입력 : "))
        user_update_quantity = int(input("수정 제품수량 입력 : "))
        
        sql = "update product set pcode=%s, pname=%s, price=%s, amount=%s where pcode = %s"
        curs.execute(sql, (user_update_number, user_update_name, user_update_price, user_update_quantity, user_update))
        conn.commit()
        print("수정이 완료 되었습니다")
    except ValueError:
        print("가격과 수량은 숫자로 입력해야 합니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

def good_delete():
    try:
        user_delete = input("삭제할 제품번호 입력 : ")
        sql = "delete from product where pcode = %s"
        curs.execute(sql, user_delete)
        conn.commit()
        print(f"{user_delete}가/이 삭제되었습니다")
    except Exception as e:
        print(f"에러 발생: {e}")

def main():
    while True:
        try:
            print("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆")
            print()
            print("            제품 관리 프로그램         ")
            print()
            print("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆")
            print("메뉴를 선택하세요")
            print("전체제품보기(1)")
            print("제품   검색(2)")
            print("제품   추가(3)")
            print("제품   수정(4)")
            print("제품   삭제(5)")
            print("종       료(6)")
            user_choice = input("번호 입력 : ")
            if user_choice == '1':
                good_all()
            elif user_choice == '2':
                good_search()
            elif user_choice == '3':
                good_add()
            elif user_choice == '4':
                good_update()
            elif user_choice == '5':
                good_delete()
            elif user_choice == '6':
                print("프로그램을 종료합니다")
                break
            else:
                print("잘못된 번호입니다")
        except Exception as e:
            print(f"에러 발생: {e}")

main()
