from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

# Configuração base
from config import Config 
from app import db  # Certifique-se de que o 'db' é configurado corretamente no seu projeto Flask

Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name_project = Column(String(200), nullable=False)
    description_project = Column(String(200), nullable=False)
    deadline_project = Column(String(200), nullable=False)
    status_project = Column(String(200), nullable=False)

    def __repr__(self):
        return f"<Project {self.name_project}>"
    
class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True)
    name_member = Column(String(200), nullable=False)
    email_member = Column(String(200), nullable=False)
    role_member = Column(String(200), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)

    def __repr__(self):
        return f"<Member {self.name_member}>"
    
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(bind=engine)