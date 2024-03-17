import vertica_vanna as askvertica, vanna, pandas as pd, vertica_python as vp, json
from vanna.remote import VannaDefault

# get secrets from JSON in a local file
with open('vanna.json') as f:
    secrets = json.load(f)
    print(secrets['username'])
# connect to Vertica using vertica_python (vp)
conn_info = {'host': '127.0.0.1',
             'port': 5433,
             'user': secrets['username'],
             'password': secrets['password'],
             'database': secrets['database']}
conn = vp.connect(**conn_info)
# setup vanna.ai and get the VannaDefault object for later use
vn = askvertica.vanna_setup(conn, secrets['apikey'], 'vertica-demo-1')
# show the DDL
print(askvertica.get_training_ddl('weather.nwsdata_improved'))
# we can train using this DDL if not already donw, but model is already trained, so let's ask some questions
vn.ask("select the number of rows observaed at Newark in January 2024 from the new weather table")
# vanna.ai remote doesn't return anything other than SELECT, but the underlying LLM probably did, so let's get the raw response to our INSERT-SELECT question
print(askvertica.ask_rawanswer('insert data from the nwsflex table into the new improved weather table where station ID starts with K'))

