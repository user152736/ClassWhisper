from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from config.config import HOST, DATABASE, PORT, USER_NAME, PASSWORD
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class GroupTable(Base):
    __tablename__ = 'group_name'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)

    def save(self, session):
        session.add(self)
        session.commit()

class StudentsTable(Base):
    __tablename__ = 'student_info'
    id = Column(Integer, autoincrement=True, primary_key=True)
    group_name_id = Column(ForeignKey('group_name.id'))
    student_name = Column(String(50), nullable=False)
    parents_name = Column(String(50), nullable=False)
    parents_user_id = Column(String(50), nullable=False)
    student_score = Column(Integer, nullable=True)





