from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://pg6lm1rrbl96ryj8h7j5:pscale_pw_RmvDZn1FR4o6U7E45Fi9UJU9BdS2Bp1Vxto4hMSyFPY@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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