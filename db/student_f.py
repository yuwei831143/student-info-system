
from db.mysql_file import pool


class Stusent_info:

    # 添加学生信息

    def insert_student(self,s_name,chinese,math,english):

        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO s_student(s_name,chinese,math,english) " \
                  "VALUES(%s,%s,%s,%s)"
            cursor.execute(sql,(s_name,chinese,math,english))
            con.commit()


        except Exception as e:
            if 'con' in dir():
                con.rollback()
                print(e)

        finally:
            if 'con' in dir():
                con.close()

    # 查找学生信息,通过学号(id)

    def search_id(self,s_id):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student WHERE id=%s"
        cursor.execute(sql,[s_id])
        result = cursor.fetchall()
        return result

    def search_all_id(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id FROM s_student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    # 查找学生信息，通过姓名

    def search_name(self,s_name):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student WHERE s_name=%s"
        cursor.execute(sql, [s_name])
        result = cursor.fetchall()
        return result

    # 删除学生信息
    def delete_student(self,s_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM s_student WHERE id=%s"
            cursor.execute(sql,[s_id])
            con.commit()

        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 展示所有学生信息
    def show_student(self,page):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student " \
              "LIMIT %s,%s"
        cursor.execute(sql,((page-1)*10,10))
        result = cursor.fetchall()
        return result

    # 学生信息分页

    def count_student_page(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT CEIL(COUNT(*)/10) FROM s_student "
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        return result

    # 修改学生信息

    def update_student(self,s_name,chinese,math,english,s_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE s_student SET s_name=%s,chinese=%s,math=%s,english=%s " \
                  "WHERE id=%s"
            cursor.execute(sql,(s_name,chinese,math,english,s_id))
            con.commit()

        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
    # 语文成绩排序
    def sort_chinese(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student ORDER BY chinese DESC "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    #  数学成绩排序
    def sort_math(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student ORDER BY math DESC "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    # 英语成绩排序

    def sort_english(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,s_name,chinese,math,english FROM s_student ORDER BY english DESC "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result





