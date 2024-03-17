## Example using vanna.ai
Load the sample data into a Vertica table using the provided DDL and COPY to load the delimited file.

Then install vanna and JupyterPy in your Jupyter notebook environment.

Open the notebook and adjust vanna.json for credentials (see the vanna.ai documentation to get an API key) Edit any other settings such as database UI and table name or schema if you changed the above.

Connect to Vertica and define and build a training plan for vanna.ai by pulling metadata from V_CATALOG.COLUMNS as shown.  View and train the model.  You can also get the DDL using export_objects, which is shown in vertica_vanna.py and tester.py described below.

Then you can ask vanna using natural language.  Depending on the result, you may also get a chart.  ask() runs several commands to generate and execute SQL and try to visualize.  You can just run generate_sql() to get the SQL.  By default, vanna.ai only returns SELECT statements; the tester.py example below shows how to use a method to get the raw response if you ask for a more complex SQL like INSERT-SELECT, or a DDL like CREATE TABLE. 

The sample questions in the notebook all produce valid SQL and visuals if you create the table defined in nwsdata.sql and copy data from nwsdata.csv using FCSVPARSER().

There are two Python scripts here: vertica_vanna.py defines some helper methods to train and use Vertica tables a bit more easily, and tester.py shows simple examples how to use these methods, such as how to get DDL using export_objects for training, and how to get the raw response to look for more complex SQL like the INSERT-SELECT, CREATE TABLE, etc.  

You can read more about how to use vanna.ai with Vertica in the following LinkedIn articles:

[Ask Vertica from natural language to SQL query with LLM](https://www.linkedin.com/pulse/ask-vertica-from-natural-language-sql-query-llm-bryan-herger-lgsie)
