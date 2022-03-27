import os
def rewrite_file():
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        outout_file = "result.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open('result.txt', 'w', encoding='utf-8') as result:
            if len(file1) < len(file2) and len(file1) < len(file3):
                result.write(path1 + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
                result.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                result.write(path2 + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
                result.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                result.write(path3 + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)
                result.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                result.write(path1 + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
                result.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                result.write(path2 + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
                result.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                result.write(path3 + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)
                result.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                result.write(path1 + '\n')
                result.write(str(len(file1)) + '\n')
                result.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                result.write(path2 + '\n')
                result.write(str(len(file2)) + '\n')
                result.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                result.write(path3 + '\n')
                result.write(str(len(file3)) + '\n')
                result.writelines(file3)
            else:
                print('Нет данных')
            return
rewrite_file()
