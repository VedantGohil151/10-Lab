import shutil,os

if os.path.exists("D:\\Krish\\Python\\practice"):
    print("Path already exists")
else:
    os.mkdir('D:\\Krish\\Python\\practice')
    print("Made new directory")

shutil.copyfile('D:\\Krish\\Python\\File.txt','D:\\Krish\\Python\\practice\\Copyfile.txt')