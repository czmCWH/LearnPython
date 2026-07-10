# 案例 - 教务管理后台
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下:
# 1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中。
# 2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩。
# 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩。
# 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出。
# 5. 展示全部学生成绩：展示出系统中所有学生的成绩。

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def __str__(self):
        """返回学生成绩的字符串表示形式"""
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"
    
    def update_score(self, chinese=None, math=None, english=None):
        """修改学生成绩"""
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduMnagement:
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        # 存储学生成绩的列表，初始为空
        self.students = []

    def add_student(self):
        """添加学生成绩"""
        name = input("请输入学生姓名：")
        for s in self.students:
            if s.name == name:
                print("该学生已存在，添加失败！")
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        if 0<= chinese <= 100 and 0<= math <= 100 and 0<= english <= 100:
            new_student = Student(name, chinese, math, english)
            self.students.append(new_student)
            print("学生成绩已成功添加！")
        else:
            print("成绩输入有误，成绩输入必须在 0～100，请重新输入！")
    
    def modify_student(self):
        """修改学生成绩"""
        name = input("请输入要修改的学生姓名：")
        for student in self.students:
            if student.name == name:
                print(f"当前成绩：{student}")
                chinese = int(input("请输入新的语文成绩："))
                math = int(input("请输入新的数学成绩："))
                english = int(input("请输入新的英语成绩："))
                if 0<= chinese <= 100 and 0<= math <= 100 and 0<= english <= 100:
                    student.update_score(chinese, math, english)
                    print("\n学生成绩已成功修改！")
                    print(f"修改后的成绩：{student}")
                    return
                else:
                    print("\n成绩输入有误，成绩输入必须在 0～100!")
                    return
        print("未找到该学生的信息，修改失败！")
    
    def delete_student(self):
        """删除学生成绩"""
        name = input("请输入要删除的学生姓名：")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("学生成绩已成功删除！")
                return
        print("未找到该学生的信息，请重新输入。")
    
    def query_student(self):
        """查询指定学生成绩"""
        name = input("请输入要查询的学生姓名：")
        for student in self.students:
            if student.name == name:
                print(f"查询结果：{student}")
                return
        print("未找到该学生的信息，请重新输入。")
    
    def show_all_students(self):
        """展示全部学生成绩"""
        if len(self.students) == 0:
            print("当前系统中没有学生成绩数据。")
        else:
            for student in self.students:
                print(student)

    def run(self):
        """运行教务管理系统"""
        print(f"欢迎使用{self.system_name}，版本：{self.system_version}")
        while True:
            print()
            print("#" * 113)
            print("# 1. 添加学生成绩   2. 修改学生成绩   3. 删除学生成绩   4. 查询指定学生成绩   5. 展示全部学生成绩   0. 退出系统 #")
            print("#" * 113)
            print()
            choice = input("请输入你的选择：")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.modify_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.show_all_students()
                case "0":
                    print("感谢使用教务管理系统，再见！")
                    return
                case _:
                    print("输入有误，请输入0～5之间的菜单功能！")


edu = EduMnagement()
edu.run()