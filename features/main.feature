Feature: To-Do List Management
  To ensure the To-Do List application works as expected, we will define scenarios for adding tasks, listing tasks, marking tasks as completed, updating tasks, and clearing all tasks.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task          |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Mark a task as in progress
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as in progress
    Then the to-do list should show task "Buy groceries" as in progress

  Scenario: Update a task's description
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
    When the user updates the task "Buy groceries" to "Buy fresh groceries"
    Then the to-do list should contain "Buy fresh groceries"