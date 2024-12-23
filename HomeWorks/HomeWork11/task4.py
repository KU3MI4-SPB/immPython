class Stack:
    def __init__(self):
        self.__stack = list()

    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()

    def push(self, item):
        self.__stack.append(item)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def new_task(self, text, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
            self.tasks[priority].push(text)

    def remove_task(self, text):
        for stack in self.tasks.values():
            temp_stack = Stack()
            while not stack.is_empty():
                task = stack.pop()
                if task != text:
                    temp_stack.push(task)
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())

    def __str__(self):
        sorted_keys = sorted(self.tasks.keys())
        out = []
        for key in sorted_keys:
            task_line = [str(key)]
            temp_stack = Stack()
            while not self.tasks[key].is_empty():
                task = self.tasks[key].pop()
                temp_stack.push(task)
            while not temp_stack.is_empty():
                task_line.append(temp_stack.pop())
                out.append(' '.join(task_line))
            return '\n'.join(out)


def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)
    manager.remove_task("поесть")
    print("\nПосле удаления задачи:")
    print(manager)


main()
