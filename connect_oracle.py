import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_8")

# TODO change credentials
#
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "", "", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()
cursor.execute("""
    SELECT cFName, cLName
    FROM CLIENTS
    """)
cursor = connection.cursor()
cursor.execute("""
    SELECT cAddress
    FROM CLIENTS
    """)
cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM CLEANINGSERVICE
    """)
cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM EQUIPMENT
    WHERE COST < 30
    """)

cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM EMPLOYEE
    WHERE SALARY > 30000
    """)

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column
############################################################################

