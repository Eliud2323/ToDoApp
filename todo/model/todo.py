class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id:int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] =[]

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
            return f"{self.code_id} - {self.title}"

    class TodoBook:
        def __init__(self):
            self.todos: dict[int, Todo] = {}

        def add_todo(self, title: str, description: str) -> int:
            todo_id = len(self.todos) + 1
            new_todo = Todo(todo_id, title, description)
            self.todos[todo_id] = new_todo
            return todo_id

        def pending_todos (self) -> list:
            return [todo for todo in self.todos.values() if todo.completed]

        def compled_todos (self) ->list:
