import snowflake.connector
from _creds import account1, user1, password1

con = snowflake.connector.connect(
    user=user1,
    password=password1,
    account=account1,
    warehouse='TEST_WH',
    database='OUR_FIRST_DB',
    schema='PUBLIC'
)

# con.cursor().execute("SELECT * FROM PY_TABLE; ")

con.cursor().execute("PUT file://D:\\PyCharm_Projects\\mysnowflake\\python-connector\\1-2*.csv @%PY_TABLE")