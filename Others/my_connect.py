from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:pw@localhost/db_name")