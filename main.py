from colorama import Fore,Style
from service.student_service import Student_service
import os
import sys

__student_service = Student_service()


while True:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX,'\n\t================================================')
    print(Fore.LIGHTWHITE_EX,'\n\t欢迎来到学生信息管理系统')
    print(Fore.LIGHTBLUE_EX,'\n\t================================================')
    print(Fore.LIGHTMAGENTA_EX, '\n\t1.添加学生信息')
    print(Fore.LIGHTMAGENTA_EX, '\n\t2.查找学生信息')
    print(Fore.LIGHTMAGENTA_EX, '\n\t3.删除学生信息')
    print(Fore.LIGHTMAGENTA_EX, '\n\t4.修改学生信息')
    print(Fore.LIGHTMAGENTA_EX, '\n\t5.排序')
    print(Fore.LIGHTMAGENTA_EX, '\n\t6.显示所有学生信息')
    print(Fore.LIGHTMAGENTA_EX, '\n\t0.退出系统')
    print(Style.RESET_ALL)

    opt = input("\n\t请输入选择编号:")
    # 添加学生信息
    if opt == '1':
        while True:
            os.system('cls')

            s_name = input("\n\t输入学生姓名:")
            chinese = input("\n\t输入语文成绩:")
            math = input("\n\t输入数学成绩:")
            english = input("\n\t输入英语成绩:")

            opt = input("\n\t是否保存(y/n)")
            if opt == "Y" or opt == 'y':
                __student_service.insert_student(s_name,chinese,math,english)

            print(Fore.LIGHTCYAN_EX,'\n\t1.继续添加')
            print(Fore.LIGHTCYAN_EX,'\n\tback.返回上一级')
            print(Style.RESET_ALL)
            opt = input("\n\t请输入选择的编号")

            if opt == 'back':
                break






    # 查找学生信息
    elif opt == '2':
        while True:

            os.system('cls')
            print(Fore.LIGHTCYAN_EX,'\n\t1.按学号查找')
            print(Fore.LIGHTCYAN_EX, '\n\t2.按姓名查找')
            print(Fore.LIGHTCYAN_EX, '\n\tback.返回上一级')

            print(Style.RESET_ALL)


            opt = input("\n\t请输入选择的编号:")
            page=1
            if opt == '1':
                while True:
                    os.system('cls')
                    s_id = input('\n\t请输入要查找的学号:')
                    result = __student_service.search_all_id()
                    if '('+s_id+',)' in str(result):
                        result1 = __student_service.search_id(s_id)
                        for index1 in range(len(result1)):
                            one1 = result1[index1]
                            print(Fore.LIGHTBLUE_EX,'\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s'%(one1[0],one1[1],one1[2],one1[3],one1[4]))
                    else:
                        print('\n\t该学生不在信息库中!!!')
                    print(Fore.LIGHTCYAN_EX, '\n\t1.继续查找')
                    print(Fore.LIGHTCYAN_EX, '\n\tback.返回上一级')
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入选择的编号")

                    if opt == 'back':
                        break
            elif opt == '2':
                while True:
                    os.system('cls')
                    s_name = input('\n\t请输入要查找的姓名:')
                    result = __student_service.search_name(s_name)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX,
                              '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))

                    print(Fore.LIGHTCYAN_EX, '\n\t1.继续查找')
                    print(Fore.LIGHTCYAN_EX, '\n\t2.返回上一级')
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入选择的编号")

                    if opt == '2':
                        break
            elif opt == 'back':
                break


    # 删除学生信息

    elif opt == '3':
        page = 1
        while True:
            os.system('cls')
            count_page = __student_service.count_student_page()
            result = __student_service.show_student(page)
            for index in range(len(result)):
                one = result[index]

                print(Fore.LIGHTWHITE_EX,
                      '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
            print(Fore.LIGHTBLUE_EX,'\n\t-------------------------------------------------------------------------')
            print(Fore.LIGHTRED_EX,'\n\t%s/%s'%(page,count_page))
            print(Fore.LIGHTBLUE_EX, '\n\t------------------------------------------------------------------------')
            print(Fore.LIGHTCYAN_EX,'\n\tprev:上一页')
            print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
            print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')
            print(Fore.LIGHTCYAN_EX, '\n\t输入学号进行删除')
            print(Style.RESET_ALL)

            opt = input("输入要操作的编号:")
            if opt == 'prev':
                page-=1
            elif opt == 'next':
                page+=1
            elif opt == 'back':
                break

            elif 1<=int(opt)<=1000000000000000:

                __student_service.delete_student(opt)
                print("删除成功")

    # 修改学生信息
    elif opt == '4':
        page = 1
        while True:
            os.system('cls')
            count_page = __student_service.count_student_page()
            result = __student_service.show_student(page)
            for index in range(len(result)):
                one = result[index]

                print(Fore.LIGHTWHITE_EX,
                      '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------------------------------------------------------')
            print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))
            print(Fore.LIGHTBLUE_EX, '\n\t------------------------------------------------------------------------')
            print(Fore.LIGHTCYAN_EX, '\n\tprev:上一页')
            print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
            print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')
            print(Fore.LIGHTCYAN_EX, '\n\t选择学号进行修改')
            print(Style.RESET_ALL)

            opt = input("输入要操作的编号:")
            if opt == 'prev':
                page -= 1
            elif opt == 'next':
                page += 1
            elif opt == 'back':
                break

            elif 1 <= int(opt) <= 1000000000000000:
                s_name = input("\n\t输入学生姓名")
                chinese = input("\n\t输入语文成绩")
                math = input("\n\t输入数学成绩")
                english = input("\n\t输入英语成绩")
                __student_service.update_student(s_name,chinese,math,english,opt)
                print("\n\t更新学生信息成功")




    # 排序
    elif opt =='5':
        while True:
            os.system('cls')
            print(Fore.LIGHTCYAN_EX, '\n\t1:按语文成绩排序')
            print(Fore.LIGHTCYAN_EX, '\n\t2:按数学成绩排序')
            print(Fore.LIGHTCYAN_EX, '\n\t3:按英语成绩排序')
            print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')
            print(Style.RESET_ALL)

            opt = input("\n\t输入要操作的编号:")
            if opt == '1':
                page = 1
                while True:
                    os.system('cls')
                    count_page = __student_service.count_student_page()
                    result = __student_service.sort_chinese()
                    for index in range(len(result)):
                        one = result[index]

                        print(Fore.LIGHTWHITE_EX,
                              '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTCYAN_EX, '\n\tprev:上一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')

                    print(Style.RESET_ALL)

                    opt = input("输入要操作的编号:")
                    if opt == 'prev':
                        page -= 1
                    elif opt == 'next':
                        page += 1
                    elif opt == 'back':
                        break

            # 按数学成绩排序
            elif opt == '2':
                page = 1
                while True:
                    os.system('cls')
                    count_page = __student_service.count_student_page()
                    result = __student_service.sort_math()
                    for index in range(len(result)):
                        one = result[index]

                        print(Fore.LIGHTWHITE_EX,
                              '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTCYAN_EX, '\n\tprev:上一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')

                    print(Style.RESET_ALL)

                    opt = input("输入要操作的编号:")
                    if opt == 'prev':
                        page -= 1
                    elif opt == 'next':
                        page += 1
                    elif opt == 'back':
                        break

            # 按英语成绩排序
            elif opt == '3':
                page = 1
                while True:
                    os.system('cls')
                    count_page = __student_service.count_student_page()
                    result = __student_service.sort_english()
                    for index in range(len(result)):
                        one = result[index]

                        print(Fore.LIGHTWHITE_EX,
                              '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))
                    print(Fore.LIGHTBLUE_EX,
                          '\n\t-------------------------------------------------------------------------')
                    print(Fore.LIGHTCYAN_EX, '\n\tprev:上一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
                    print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')

                    print(Style.RESET_ALL)

                    opt = input("输入要操作的编号:")
                    if opt == 'prev':
                        page -= 1
                    elif opt == 'next':
                        page += 1
                    elif opt == 'back':
                        break
            elif opt == 'back':
                break



    elif opt == '6':
        page = 1
        while True:
            os.system('cls')
            count_page = __student_service.count_student_page()
            result = __student_service.show_student(page)
            for index in range(len(result)):
                one = result[index]

                print(Fore.LIGHTWHITE_EX,
                      '\n\t学号:%s\t姓名:%s\t语文成绩:%s\t数学成绩:%s\t英语成绩:%s' % (one[0], one[1], one[2], one[3], one[4]))
            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------------------------------------------------------')
            print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))
            print(Fore.LIGHTBLUE_EX, '\n\t------------------------------------------------------------------------')
            print(Fore.LIGHTCYAN_EX, '\n\tprev:上一页')
            print(Fore.LIGHTCYAN_EX, '\n\tnext:下一页')
            print(Fore.LIGHTCYAN_EX, '\n\tback:返回上一级')
            print(Style.RESET_ALL)

            opt = input("输入要操作的编号:")
            if opt == 'prev':
                page -= 1
            elif opt == 'next':
                page += 1
            elif opt == 'back':
                break

    elif opt == '0':
        print('\n\t您已退出系统')
        sys.exit(0)

