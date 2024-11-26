from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://cxn70yshjz6qmgsae1gw:pscale_pw_qDW198XQRomH4Rv16dv4XUgJZDJPt4X8X6AUponU5YI@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

