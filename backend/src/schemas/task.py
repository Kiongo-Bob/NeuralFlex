from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in progress"
    blocked = "blocked"
    completed = "completed"

class TaskBaseSchema(BaseModel):
    name: str
    description: str
    start_date: datetime
    deadline: datetime
    status: TaskStatus = TaskStatus.todo

class MetaGoalSchema(TaskBaseSchema):
    pass

class CreateTaskRequest(TaskBaseSchema):
    pass

class ReadTaskResponse(TaskBaseSchema):
    id: int
    session_id: str
    created_at: datetime
    
class UpdateTaskRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    deadline: Optional[datetime] = None
    status: Optional[TaskStatus] = None