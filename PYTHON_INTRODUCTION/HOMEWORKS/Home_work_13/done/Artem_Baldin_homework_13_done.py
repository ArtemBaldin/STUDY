import json
from datetime import datetime as dt


class Item:
    def __init__(self, done, info, last_updated):
        self.done = done
        self.info = info
        self.last_updated = last_updated

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }


class TodoList:
    def __init__(self, name, owner, dead_line):
        self.name = name
        self.owner = owner
        self.dead_line = dead_line
        self.file_name = '../tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'],
                                      item['info'], item['last_updated']))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\
            \t {item.last_updated}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        pos = 1
        for index, item in enumerate(self.tasks):
            if not item.done:
                tasks += f'\n {pos}\t {item.done}\t {item.info}\
                \t {item.last_updated} \t{index}|'
                pos += 1
        return tasks

    @property
    def ready_tasks(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            if item.done is True:
                tasks += f'\n {index}\t {item.done}\
                \t {item.info}\t {item.last_updated}'
        return tasks

    def done_task(self, index):
        self.tasks[index].done = True

    def undone_task(self, index):
        self.tasks[index].done = False

    def add_task(self, task):
        self.tasks.append(task)

    def get_task_index(self, task):
        return self.tasks.index(task)

    def to_json(self):
        with open(self.file_name, 'w') as file:
            tasks = []
            for task in self.tasks:
                tasks.append(task.as_dict())
            json.dump(tasks, file)


# main
list = ["Art"]


def init_todo_list():
    owner = "Art"  # input ("Enter owner: ")
    list_name = None
    if owner not in list:
        print("\nNo such OWNER")
        return
    return TodoList(list_name, owner, None)


def main():
    print("to exit press \"0\"")
    todo_list = init_todo_list()
    while True:
        print("SELECT:")
        print("1) CREATE NEW TASK. \n2) CHECK TODO LIST.")
        try:
            init_task = int(input("Select: "))
            if init_task == 0:
                break
            if init_task not in range(1, 3):
                print("\nWrong selection. \nInput correct digit (1 or 2)\n")
                continue
        except ValueError:
            print("\nWrong selection. \nInput correct digit (1 or 2)\n")
            continue

        if init_task == 1:
            while True:
                task_info = input("Describe TASK:")
                task_status = bool(int(input("0 - UNDONE / 1 - DONE: ")))
                task_update = str(dt.now().strftime("%d-%m-%y  %H:%M:%S"))

                task_new = Item(task_status, task_info, task_update)
                todo_list.add_task(task_new)
                todo_list.to_json()
                menu_choice = bool(input("Input 1 to one more TASK\
 or Press Enter to back.\nInput: "))
                if menu_choice is True:
                    continue
                else:
                    break

        if init_task == 2:
            while True:
                print("SELECT LIST:")
                print("1) All. \n2) DONE. \n3) UNDONE.\nPress ENTER to exit.")
                try:
                    list_name = input("\nSelect var:")
                    if list_name == "":
                        break
                    list_name = int(list_name)
                    list_name in range(1, 3) is True
                except ValueError:
                    list_name = -1

                if list_name == 1:  # all
                    print(todo_list.tasks_list)

                elif list_name == 2:  # done

                    while True:
                        print(todo_list.ready_tasks)
                        print("To change status enter\
 equal digit or press Enter to back")
                        change_status = input("Selection: ")
                        if change_status == "":
                            break
                        todo_list.undone_task(int(change_status))

                elif list_name == 3:  # undone
                    while True:

                        for i in todo_list.not_ready_tasks.split('|'):
                            i = str(i).split()[:-1]
                            print("\t".join(i))

                        var = (todo_list.not_ready_tasks)
                        print("To change status enter equal\
 digit or press Enter to back")
                        change_status = input("Selection: ")
                        if change_status == "":
                            break

                        if int(change_status) not in \
                                range(0, len(var.split("|"))):
                            print("\nValue not in range\n")
                            continue

                        for i in var.split("|"):
                            if int(str(i).split()[0]) == int(change_status):
                                change_status = int(str(i).split()[5])
                                print(change_status)
                                break
                        todo_list.done_task(int(change_status))
                        todo_list.to_json()


main()
