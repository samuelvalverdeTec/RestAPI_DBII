import json

from db import Database


class AppService:

    def __init__(self, database: Database):
        self.database = database

    def get_tasks(self):
        data = self.database.get_tasks()
        return data

    def create_task(self, task):
        self.database.create_task(task)
        return task
    
    def get_task_by_id(self, request_task_id):
        data = self.database.get_task_by_id(request_task_id)
        return data

    def update_task(self, request_task, request_task_id):
        self.database.update_task(request_task, request_task_id)
        return request_task

    def delete_task(self, request_task_id):
        self.database.delete_task(request_task_id)
        return request_task_id
