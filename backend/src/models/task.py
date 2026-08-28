from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime
from sql.alchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class meta_goal():
    __tablename__ = "Meta_goal"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    session_id = Column(String, index=True)
    start_date = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deadline = Column(DateTime)
    status = Column(String)

    nodes = relationship(argument:"Task", back_populates="meta_goal")

class Task():
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    session_id = Column(String, index=True)
    start_date = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deadline = Column(DateTime)
    status = Column(String)

    meta_goal = relationship(argument:"SubGoal", back_populates="nodes")
