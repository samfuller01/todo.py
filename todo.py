import sys, os


class TodoApp:
    def __init__(self):
        self.todo_file = os.getenv('HOME') + '/.todo_file'
        self.cli_args = sys.argv
    
    def __add_todo(self):
        try:
            file = open(self.todo_file, 'a') 
            file.write(self.cli_args[2] + '\n')
            file.close()
            print('Successfully added todo')
        except:
            print('Error adding todo')

    def __delete_todo(self):
        try:
            with open(self.todo_file) as reader:
                lines = reader.readlines()
                todo_to_delete_index = lines.index(self.cli_args[2] + '\n')
                del lines[todo_to_delete_index]

                rewrite_todo = open(self.todo_file, 'w')

                for line in lines:
                    rewrite_todo.write(line)

                rewrite_todo.close()
                print('Deleted todo!')
        except (ValueError, IndexError):
            print('Error deleting todo. Are you sure you typed it in right?')

        
    def __list_todos(self):
        with open(self.todo_file) as reader:
            for line in reader.readlines():
                print(line, end='')

    def __print_help_message(self):
        print('Usage: python3 main.py [command] [arguments]\nExample: python3 main.py delete \'hi there\'')
        print('Avaliable commands:\nhelp\nlist\ndelete/finish\nadd/create')

    def run(self):
        try:
            if self.cli_args[1] == 'add' or self.cli_args[1] == 'create':
                self.__add_todo()
            elif self.cli_args[1] == 'delete' or self.cli_args[1] == 'finish':
                self.__delete_todo()
            elif self.cli_args[1] == 'list':
                self.__list_todos()
            elif self.cli_args[1] == 'help':
                self.__print_help_message()
            else:
                print('Error: Not a valid command')
        except IndexError:
            print('Error: Not a valid command')

if __name__ == '__main__':
    todo = TodoApp()
    todo.run()
