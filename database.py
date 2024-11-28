from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://pix0hf8pu9e3tofa36dm:pscale_pw_8Bjkr7x79QD9ic4VJvZjqHGDciHONWLEzljJHxembsi@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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
