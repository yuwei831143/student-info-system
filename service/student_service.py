
from db.student_f import Stusent_info

class Student_service:
    __student_service = Stusent_info()


    # 添加学生信息
    def insert_student(self,s_name,chinese,math,english):
        self.__student_service.insert_student(s_name,chinese,math,english)


    # 查找学生信息，通过id

    def search_id(self,s_id):
        result = self.__student_service.search_id(s_id)
        return result

    def search_all_id(self):
        result = self.__student_service.search_all_id()
        return result


    # 查找学生信息，通过姓名

    def search_name(self,s_name):
        result = self.__student_service.search_name(s_name)
        return result
    # 删除学生信息
    def delete_student(self,s_id):
        self.__student_service.delete_student(s_id)

    # 展示所有学生信息
    def show_student(self,page):
        result =self.__student_service.show_student(page)
        return result
    # 学生信息分页

    def count_student_page(self):
        result = self.__student_service.count_student_page()
        return result

    # 修改学生信息
    def update_student(self,s_name,chinese,math,english,s_id):
        self.__student_service.update_student(s_name,chinese,math,english,s_id)

    # 数学成绩排序
    def sort_math(self):
        result = self.__student_service.sort_math()
        return result

    # 语文成绩排序
    def sort_chinese(self):
        result = self.__student_service.sort_chinese()
        return result

    # 英语成绩排序
    def sort_english(self):
        result = self.__student_service.sort_english()
        return result

    # 获取所有学生
    def get_all(self,page):

        result=Student_service().show_student(page)
        for index in range(len(result)):
            one = result[index]
            return one



if __name__ == '__main__':
    a =Student_service().search_all_id()
    b = input("输入数字")


    if '('+b+',)' in str(a):
        print('在')
    else:
        print('不在')
    print(a)


