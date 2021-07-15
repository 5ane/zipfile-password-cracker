# Imports
import zipfile
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, init
from os import system
init()

root = tk.Tk()
root.withdraw()

file_txt_path = filedialog.askopenfilename(filetypes=[("Text files", '.txt')], title='Select Passwordlist')
file_path = filedialog.askopenfilename(filetypes=[("ZIP", '.zip .rar .7z .tar .gz')], title='Select Passwordlist')


count = 1

system("cls")
system("title Cracking...")

with open(file_txt_path, 'rb') as text1:
    for entry in text1.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(file_path, 'r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                system("cls")
                system("title Password found!")
                print(Fore.LIGHTGREEN_EX + "[+]" + Fore.WHITE + " Password found! ~ %s\n ~ %s\n ~ %s\n" % (password.decode('utf8'), data, data_size))
                input()
                break
        except:
            print(f"{Fore.LIGHTBLUE_EX}[%s]{Fore.RED} [-]{Fore.WHITE} Password failed! ~ %s" % (count,password.decode('utf8')))
            count += 1