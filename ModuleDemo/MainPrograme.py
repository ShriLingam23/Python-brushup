from MainPackage import MainScript
from MainPackage.SubPackage import SubScript


if __name__ == '__main__':
    print("Main Programe is Called/Executed Directly!")
    MainScript.main_report()
    SubScript.sub_report()
else:
    print("Main Programe is called as import\n")