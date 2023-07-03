"""
Реализовать консольное приложение заметки,
с сохранением,
чтением,
добавлением,
редактированием и
удалением заметок.
Заметка должна содержать:
идентификатор,
заголовок,
тело заметки и
дату/время создания или
последнего изменения заметки.
Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
"""
import json
from datetime import datetime

def launcher():
    with open("notes.json", "r") as file:
        try:
            notes = json.load(file)
            print("Done")
        except:
            notes = {}
            print("error")
    Controller(notes)
    save_n_exit(notes)
def Controller(notes):
    while True:
        action = input("Notes actions:\n"
                       "add\n"
                       "read\n"
                       "edit\n"
                       "delete\n"
                       "exit\n")
        print(action)
        match action:
            case "add":
                try:
                    lastid = max([int(i) for i in notes.keys()])
                except:
                    lastid = 0
                Title = input("Enter the title of a note:\n")
                Body = input("\nEnter the body of a note:\n")
                time = str(datetime.now())
                notes[str(lastid+1)] = {"Title":Title,"Body":Body,"Time":time}
                print("New Note ID:", str(lastid+1))
            case "read":
                note = str(input("Enter note ID\n"))
                if note in notes.keys():
                    print("Note ID:",note)
                    print("Timestamp:", notes[note]["Time"])
                    print("Title:", notes[note]["Title"])
                    print("Body:", notes[note]["Body"])
                else:
                    print("No note with that ID exists\n")
            case "edit":
                note = str(input("Enter note ID\n"))
                if note in notes.keys():
                    Title = input("Enter new title of a note:\n")
                    Body = input("Enter new body of a note:\n")
                    time = str(datetime.now())
                    notes[note] = {"Title":Title,"Body":Body,"Time":time}
                else:
                    print("No note with that ID exists\n")
            case "delete":
                note = str(input("Enter note ID\n"))
                if note in notes.keys():
                    del notes[note]
                    print("Note deleted!")
                else:
                    print("No note with that ID exists\n")
            case "exit":
                break
def save_n_exit(notes):
    with open("notes.json", "w") as file:
        file.write(json.dumps(notes))

launcher()
