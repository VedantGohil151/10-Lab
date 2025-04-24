import shutil,os

if os.path.exists("D:\\Vedant\\Python\\practice"):
    print("Path already exists")
else:
    os.mkdir('D:\\Vedant\\Python\\practice')
    print("Made new directory")

shutil.copyfile('D:\\Vedant\\Python\\File.txt','D:\\Vedant\\Python\\practice\\Copyfile.txt')
