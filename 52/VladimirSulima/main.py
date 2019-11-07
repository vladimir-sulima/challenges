from pomodoro_timer import PomodoroTimer

def show_menu():
    print("Available options:")
    print("1 - Display list of tasks")
    print("2 - Add task")
    print("3 - Edit task")
    print("4 - Select and start task with set options")
    print("x - Exit program")

if __name__ == '__main__':
    terminate_program = False
    print("Welcome to 'Pomodoro Timer' console app")

    pomodoro = PomodoroTimer()

    while not terminate_program:
        show_menu()
        user_main_menu_choice = input("\n")

        if user_main_menu_choice.lower() == "x":
            terminate_program = True
        elif user_main_menu_choice == "1":
            pomodoro.get_all_available_tasks()
        elif user_main_menu_choice == "2":
            pomodoro.add_new_task()
        elif user_main_menu_choice == "3":
            print("Sorry, this functionality not implemented yet.")
            input("Press ENTER to continue...\n")
        elif user_main_menu_choice == "4":
            task_index = pomodoro.select_existing_task()
            pomodoro.run_task_session(task_index)




        # for task in pomodoro.tasks:
        #
        #     pomodoro.start_working_timer(task)
        #     pomodoro.add_work_duration(task)
        #     pomodoro.start_break_timer(task)
        #     pomodoro.add_break_duration(task)
        #
        #     print(pomodoro.tasks[0].total_task_duration)
        #     print(pomodoro.tasks[0].total_break_duration)
