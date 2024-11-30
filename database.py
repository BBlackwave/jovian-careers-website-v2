from sqlalchemy import create_engine, text
import os

from sqlalchemy.engine.interfaces import ReflectedForeignKeyConstraint


db_connection_string = os.environ["DB_CONNECTION_STRING"]


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM jobs'))
    jobs = []
    for row in result.mappings().all():
      jobs.append(dict(row))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result =conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    row = result.fetchone()
    if row:
      return row._asdict()
    else:
      return None
      
    
                         
    