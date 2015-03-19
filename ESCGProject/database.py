from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from ESCGProject.models import Base

engine = create_engine('mysql+pymysql://root:itcarlow@localhost/ESCGdb', convert_unicode=True, echo=True)
#metadata = MetaData()
#Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
def init_db():
    Base.metadata.create_all(bind=engine)