import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='shopdb',
    charset='utf8'
)

curs = conn.cursor()


# sql = "insert into product(pcode, pname, price, amount)values('p0005', '핸드폰', 800000, 5)"
# sql = "update product set price=50000 where pcode = 'p0003'"
# sql = "delete from product where pcode='p0005'"
# sql = "select * from product"
# sql = "select * from product where pcode = %s"
# max1 = 1000000
# min2 = 500000
sql = "select avg(price), sum(amount) from product where price <= %s "
curs.execute(sql,(100000))
result = curs.fetchall()
for data in result:
    print(data)
# conn.commit()
