#!/usr/bin/env python
import sys
import os

def main():
    print('''
        ----------------
        | 1.新增学生信息 |
        | 2.删除学生信息 |
        | 3.修改学生信息 |
        | 4.查询学生信息 |
        | 4.退出管理系统 |
        ---------------
    ''')

    while True:
        line = sys.stdin.readline()
        if line == "1\n":
            insertStuInfo()
        elif line == "2\n":
            delStuInfo()
        elif line == "3\n":
            delStuInfo()
        elif line == "4\n":
            delStuInfo()
        elif line == "exit\n":
            print("已退出系统")
            sys.exit(0)
        else:
            print("请输入有效的选项")

        if not line:
            break


def insertStuInfo():
    os.system("clear")
    print("这是新增")


def delStuInfo():
    os.system("clear")
    print("这是删除方法")


if __name__ == '__main__':
    main()



