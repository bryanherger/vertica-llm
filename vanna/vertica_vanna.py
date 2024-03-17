

# vertica_vanna: convenience methods to interact with Vertica using vanna.ai
# install prerequisites: pip3 install --upgrade vanna vertica_python

import vanna, pandas as pd, vertica_python as vp, json
from vanna.remote import VannaDefault
from vanna.types import Question

def add_one(i):
    return i+1

vertica_connection = None
vn = None

def run_sql(sql: str) -> pd.DataFrame:
    df = pd.read_sql_query(sql, vertica_connection)
    return df

def vanna_setup(vertica_connection_arg, vanna_api_key, vanna_model_name):
    global vertica_connection, vn
    vn = VannaDefault(model=vanna_model_name, api_key=vanna_api_key)
    print(vn)
    vertica_connection = vertica_connection_arg
    vn.run_sql = run_sql
    vn.run_sql_is_set = True
    return vn

def vanna_train_from_vcatalog():
    global vertica_connection, vn
    df_information_schema = vn.run_sql("SELECT 'vertica' as DATABASE, * FROM V_CATALOG.COLUMNS;")
    plan = vn.get_training_plan_generic(df_information_schema)
    #print(plan)
    print([f"{item.item_value}" for item in plan._plan])

def ask_rawanswer(myquestion):
    global vertica_connection, vn
    params = [Question(question=myquestion)]
    d = vn._rpc_call(method="generate_sql_from_question", params=params)
    print(d['result']['raw_answer'])

def extract_substring_before_y(x, y):
    """
    Extracts the portion of string 'x' up until the first occurrence of string 'y'.

    Args:
        x (str): The input string.
        y (str): The substring to search for.

    Returns:
        str: The portion of 'x' before the first occurrence of 'y'.
    """
    index = x.find(y)
    if index != -1:
        return x[:index]
    else:
        raise ValueError(f"Substring '{y}' not found in the input string.")

def get_training_ddl(schema_table):
    global vertica_connection, vn
    cur = vertica_connection.cursor()
    cur.execute("SELECT EXPORT_OBJECTS('','"+schema_table+"')")
    datarow = cur.fetchone()
    table_ddl = extract_substring_before_y(datarow[0], "CREATE PROJECTION")
    print(table_ddl)
    return table_ddl

