from behave import given, when, then
from todo_list import ToDoList

# Inicialización de la lista de tareas
@given('the to-do list is empty')
def step_given_list_empty(context):
    context.todo_list = ToDoList()
    context.todo_list.clear_tasks()

@given('the to-do list contains tasks')
def step_given_list_contains_tasks(context):
    context.todo_list = ToDoList()
    context.todo_list.clear_tasks()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.todo_list.add_task(task)

@when('the user lists all tasks')
def step_when_user_lists_tasks(context):
    context.task_output = context.todo_list.list_tasks()

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    context.todo_list.mark_task_completed(task)

@when('the user marks task "{task}" as in progress')
def step_when_user_marks_task_in_progress(context, task):
    context.todo_list.mark_task_in_progress(task)

@when('the user updates the task "{task}" to "{new_task}"')
def step_when_user_updates_task(context, task, new_task):
    context.todo_list.update_task(task, new_task)

@when('the user clears the to-do list')
def step_when_user_clears_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should contain "{task}"')
def step_then_list_should_contain_task(context, task):
    assert task in [t.description for t in context.todo_list.list_tasks()], f'Task "{task}" not found in the list'

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = [task.description for task in context.task_output]
    assert expected_tasks == actual_tasks, f'Expected tasks {expected_tasks} but got {actual_tasks}'

@then('the to-do list should show task "{task}" as completed')
def step_then_list_should_show_completed(context, task):
    task_found = next((t for t in context.todo_list.list_tasks() if t.description == task), None)
    assert task_found is not None, f'Task "{task}" not found in the list'
    assert task_found.status == "Completed", f'Task "{task}" is not marked as completed'

@then('the to-do list should show task "{task}" as in progress')
def step_then_list_should_show_in_progress(context, task):
    task_found = next((t for t in context.todo_list.list_tasks() if t.description == task), None)
    assert task_found is not None, f'Task "{task}" not found in the list'
    assert task_found.status == "In Progress", f'Task "{task}" is not marked as in progress'

@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    assert len(context.todo_list.list_tasks()) == 0, 'The to-do list is not empty'