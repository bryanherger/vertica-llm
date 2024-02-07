## Example using vanna.ai
Load the sample data into a Vertica table using the provided DDL and COPY to load the delimited file.

Then install vanna and JupyterPy in your Jupyter notebook environment.

Open the notebook and adjust vanna.json for credentials (see the vanna.ai documentation to get an API key) Edit any other settings such as database UI and table name or schema if you changed the above.

Connect to Vertica and define and build a training plan for vanna.ai by pulling metadata from V_CATALOG.COLUMNS as shown.  View and train the model.

Then you can ask vanna using natural language.  Depending on the result, you may also get a chart.  ask() runs several commands to generate and execute SQL and try to visualize.  You can just run generate_sql() to get the SQL.

The sample questions in the notebook all produce valid SQL and visuals.
