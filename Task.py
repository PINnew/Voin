from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Ошибка: Неверный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")

# Пример использования

manager = TaskManager()

# Добавление задач
manager.add_task("Купить продукты", "2024-08-20")
manager.add_task("Закончить проект", "2024-08-25")
manager.add_task("Накормить кота", "2024-08-19")

# Вывод всех задач
print("Все задачи:")
manager.display_tasks()

# Отметка задачи как выполненной
manager.mark_task_completed(0)

# Вывод текущих (не выполненных) задач
print("\nТекущие задачи:")
for task in manager.get_current_tasks():
    print(task)
