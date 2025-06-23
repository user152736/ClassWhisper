from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]')