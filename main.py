import tkinter as tk
from tkinter import filedialog
import requests
def show_message():
    message = "ВНИМАНИЕ! Для работы данной программы необходимо указать путь к файлу, " \
            "где прописаны все парольные фразы. Каждая фраза должна находиться на отдельной строке." \
            "После выполнения должен появиться файл \"resutl.txt\" в котором будут парольные фразы не пройденых учеников"
    tk.messagebox.showinfo("Предупреждение", message)
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        test(file_path)      
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.split("\n")
        return lines  
def test(file_path:str):
    values = read_file(file_path)
    validData = []
    for value in values:    
        url = "https://spt.edu.orb.ru/testing/bypass"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "PHPSESSID=63eec91bfd6e16cd0bd7cdfd73b83b92",
            "Host": "spt.edu.orb.ru",
            "Origin": "https://spt.edu.orb.ru",
            "Referer": "https://spt.edu.orb.ru/testing/bypass",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "X-Requested-With": "XMLHttpRequest"
        }
        data = {"passphrase": value}
        response = requests.post(url, headers=headers, data=data)
        if(response.status_code == 200):
            validData.append(value)
        elif(response.status_code == 400):
            continue
        else:
            tk.messagebox.showinfo("ОШИБКА", "ОШИБКА САЙТ НЕ ДОСТУПЕН")         
    with open("result.txt", "a") as file:
                if file.tell() != 0:
                    file.write("\n------------------------\n")
                file.write("\n".join(validData))
    tk.messagebox.showinfo("Успешно", "Программа успешно выполнила работу, можете искать файл с результатами)")
root = tk.Tk()
root.title("Поиск не пройденных тестов")
root.geometry("300x200")
button_message = tk.Button(root, text="Как работает программа?", command=show_message)
button_message.pack(pady=10)
button_open_file = tk.Button(root, text="Выбрать файл", command=open_file)
button_open_file.pack(pady=10)
root.mainloop()
