import tkinter as tk
from tkinter import messagebox
from questions import questions

class PythonAdventuresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кодовые Приключения: Python")
        self.levels = [
            "Привет, Python!",
            "Переменные и волшебные числа",
            "Лабиринт условий",
            "Циклическая спираль",
            "Функциональная башня",
            "Сокровища списков",
            "Словарный остров",
            "Исключительный вулкан",
            "Файловый портал",
            "Классный мир",
            "Модульная крепость",
            "Финальная миссия: Автоматизация",
            "Тайны строк",
            "Многомерные загадки",
            "Генераторный шторм",
            "Тайное время",
            "Магия итераций",
            "Сетевые квесты",
            "Пандас в дикой природе",
            "Потоковый лабиринт"
        ]
        self.questions = questions
        self.start_index = 0  # Индекс первого отображаемого уровня
        self.visible_levels = 20  # Количество уровней, отображаемых на экране одновременно
        self.create_login_screen()

    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("600x500")
        tk.Label(self.root, text='Добро пожаловать на мини викторину    Кодовые Приключения в Python!', font=("Times New Roman", 14), wraplength=350).pack(pady=20)
        tk.Label(self.root, text="Введите ваше имя:", font=("Times New Roman", 14)).pack(pady=10)

        self.username_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.username_entry.pack(pady=10)

        tk.Button(self.root, text="Вход", font=("Times New Roman", 14), command=self.enter_game).pack(pady=10)

    def enter_game(self):
        username = self.username_entry.get().strip()
        if username:
            self.username = username
            self.create_levels_screen()
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите ваше имя.")

    def create_levels_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("600x1000")
        tk.Label(self.root, text=f"Привет, {self.username}! Выберите уровень сложности который вы хотите:", font=("Times New Roman", 14)).pack(pady=20)

        levels_frame = tk.Frame(self.root)
        levels_frame.pack(pady=10)

        # Отображение видимых уровней
        for i in range(self.start_index, min(self.start_index + self.visible_levels, len(self.levels))):
            level_number = i + 1
            tk.Button(
                levels_frame,
                text=f"{level_number}. {self.levels[i]}",
                font=("Times New Roman", 12),
                width=40,
                command=lambda lvl=level_number: self.select_level(lvl)
            ).pack(pady=5)

        # Кнопки навигации
        navigation_frame = tk.Frame(self.root)
        navigation_frame.pack(pady=10)

        if self.start_index > 0:
            tk.Button(navigation_frame, text="Наверх", font=("Times New Roman", 12), command=self.scroll_up).pack(side=tk.LEFT, padx=5)

        if self.start_index + self.visible_levels < len(self.levels):
            tk.Button(navigation_frame, text="Вниз", font=("Times New Roman", 12), command=self.scroll_down).pack(side=tk.LEFT, padx=5)

    def scroll_up(self):
        if self.start_index > 0:
            self.start_index -= 1
            self.create_levels_screen()

    def scroll_down(self):
        if self.start_index + self.visible_levels < len(self.levels):
            self.start_index += 1
            self.create_levels_screen()

    def select_level(self, level_number):
        level_name = self.levels[level_number - 1]
        self.current_level = level_name
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        questions = self.questions.get(self.current_level, [])
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            tk.Label(self.root, text=question_data["question"], font=("Times New Roman", 14), wraplength=500).pack(pady=20)

            for option in question_data["options"]:
                tk.Button(
                    self.root,
                    text=option,
                    font=("Times New Roman", 12),
                    width=40,
                    command=lambda opt=option: self.check_answer(opt)
                ).pack(pady=5)
        else:
            self.show_result()

    def check_answer(self, selected_option):
        questions = self.questions.get(self.current_level, [])
        question_data = questions[self.current_question]
        if selected_option == question_data["answer"]:
            self.score += 1

        self.current_question += 1
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Результат", f"Ваш счет: {self.score} из {len(self.questions.get(self.current_level, []))}")
        self.create_levels_screen()