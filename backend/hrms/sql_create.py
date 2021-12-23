import pymysql
import re
import time
import codecs


""" 连接数据库 """
cur = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=6666, db='humansource', charset='utf8')
cur.commit()
db = cur  # 数据库

""" 创建表需要的head字段 """
account = ["Name", "Password"]
staff = ["ID"]
department = ["Department_id", "Department_name", "Manager_id", "Affairs"]
position = ["Position_id", "Position_rank", "Position_name", "Salary", "Post_number", "Post_already"]
user_info = ['ID', 'Sex', 'Name', 'Email', 'Phone']
employee = ["Employee_id", "Department_id", "Position_id", "Hire_date", "State"]
experience = ["ID", "Work_experience", "Achievement"]

def table_exists(cur, table_name):  # 这个函数用来判断表是否存在
    cur.execute( "show tables;")
    tables = [cur.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return True  # 存在
    else:
        return False  # 不存在

# 创建表
def create_table_head(db ,table, head):
    """
    :param db:  数据库
    :param table: 表名
    :param head:  表头名
    :return:
    """
    sql = 'create table if not exists {}('.format(table)  # 创建表
    for i in range(0, len(head)):
        sql += '`{}` varchar(50)'.format(head[i])
        if i != len(head) - 1:
            sql += ','
        sql += '\n'
    sql += ');'
    try:
        cur = db.cursor()  # 创建光标
        if (table_exists(cur, table)):
            print(table,"表已经存在")
        else:
            cur.execute(sql)  # 执行命令
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table,'表创建完成')
    except Exception as e:
        print(table,'表创建失败,失败原因', e)

# 插入数据
def insert_table_info( db,table, info):
    sql = 'insert into {} values ('.format(table)
    for i in range(0, len(info)):
        sql += '"{}" '.format(info[i])
        if i != len(info) - 1:
            sql += ','
    sql += ');'
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table,'表数据插入成功')
        else:
            print(table,'表不存在')
    except Exception as e:
        print(table,'表数据插入失败,失败原因', e)

# 表需要的数据
def insert_alltable_info(db, table,filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        row = 0
        for line in f.readlines():
            data = line.split()  # 遍历文件中每一行
            row += 1
            if row == 1: continue
            rowdata = data[0].split(',')
            """ 先查询数据是否已经存在 """
            searchdata = search_table_info(db,table)
            if rowdata in searchdata:
                print(rowdata,"数据已存在")
            else:
                insert_table_info(db, table,rowdata)  # 存储单条数据

def search_table_info(db,table):
    sql = 'SELECT * FROM {}'.format(table)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            result = cur.fetchall()
            print(table, '表数据查询成功')
            searchdata = []
            for item in result:
                searchdata.append(list(item))
            print(table, "表存在", len(searchdata), "条数据")
            return searchdata
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据查询失败,失败原因', e)

def delete_table_info( db, table,table_head,head_value):
    # SQL语句删除数据
    sql = 'DELETE FROM {} WHERE {} = {}'.format(table,table_head,head_value)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中',head_value,'该条数据删除成功')
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据删除失败,失败原因', e)

def update_table_info(db, table,table_head1,head_value1,table_head2,head_value2):
    # SQL语句更新数据
    sql = 'UPDATE {} SET {}= {} WHERE {} = {}'.format(table,table_head1,head_value1,table_head2,head_value2)
    try:
        cur = db.cursor()
        if (table_exists(cur, table)):
            cur.execute(sql)
            db.commit()  # 一定要进行事务更新
            time.sleep(0.1)
            print(table, '表中',head_value2,'该条数据修改成功')
        else:
            print(table, '表不存在')
    except Exception as e:
        print(table, '表数据修改失败,失败原因', e)


if __name__ == '__main__':
    """ 删除所有的表 """
    conn = cur.cursor()  # 创建操作游标
    conn.execute("drop table account")
    conn.execute("drop table staff")
    conn.execute("drop table department")
    conn.execute("drop table position2")
    conn.execute("drop table user_info")
    conn.execute("drop table employee")
    conn.execute("drop table experience")

    """ 创建表 """
    create_table_head(db,"account", account)  # 创建表
    create_table_head(db, "staff", staff)  # 创建表
    create_table_head(db, "department", department)  # 创建表
    create_table_head(db, "position2", position)  # 创建表
    create_table_head(db, "user_info", user_info)  # 创建表
    create_table_head(db, "employee", employee)  # 创建表
    create_table_head(db, "experience", experience)  # 创建表

    """ 插入数据 """
    insert_alltable_info(db, "account","SQL_testdata//Account.txt")    # 插入数据
    insert_alltable_info(db, "staff", "SQL_testdata//Staff.txt")  # 插入数据
    insert_alltable_info(db, "department","SQL_testdata//Department.txt")    # 插入数据
    insert_alltable_info(db, "position2","SQL_testdata//Position.txt")    # 插入数据
    insert_alltable_info(db, "user_info", "SQL_testdata//user_info.txt")  # 插入数据
    insert_alltable_info(db, "employee","SQL_testdata//Employee.txt")    # 插入数据
    insert_alltable_info(db, "experience", "SQL_testdata//Experience.txt")  # 插入数据

    """ 查询数据 """
    # searchdata = search_table_info(db, "account")
    # for rowdata in searchdata:
    #     print(rowdata)


    """ 删除数据 """
    # delete_table_info(db, "department", "Department_id", 1)

    # """ 删除表 """
    # conn =  cur.cursor()  # 创建操作游标
    # conn.execute("drop table account")
    # conn.execute("drop table staff")
    # conn.execute("drop table user_info")
    # conn.execute("drop table department")
    # conn.execute("drop table employee")


    """ 更新数据 """
    update_table_info(db, "department","Manager_id",1666,"Manager_id",1124)


    """ 查询数据 """
    searchdata = search_table_info(db, "department")
    for rowdata in searchdata:
        print(rowdata)




