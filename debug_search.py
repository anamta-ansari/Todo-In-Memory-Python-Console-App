import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from src.todo_app.services.task_service import TaskService
from src.todo_app.services.search_service import SearchService

def test_search():
    # Create services
    task_service = TaskService()
    search_service = SearchService(task_service)

    # Add test tasks
    task_service.add_task('High Priority Task', 'This is important', 'High', ['work', 'urgent'])
    task_service.add_task('Low Priority Task', 'This can wait', 'Low', ['personal'])
    task_service.add_task('Medium Priority Task', 'Regular task', 'Medium', ['work'])
    task_service.add_task('Another Work Task', 'More work stuff', 'High', ['work', 'meeting'])

    print(f"Total tasks: {len(task_service.get_all_tasks())}")
    
    # Test search
    results = search_service.search_tasks('High')
    print(f'Found {len(results)} tasks matching \"High\"')
    for task in results:
        print(f'  - {task.title}')
    
    # Also test with lowercase
    results2 = search_service.search_tasks('high')
    print(f'Found {len(results2)} tasks matching \"high\"')
    for task in results2:
        print(f'  - {task.title}')

if __name__ == "__main__":
    test_search()