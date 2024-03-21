## vanna-udx: Train and run vanna.ai hosted text-to-SQL LLM within Vertica

This is a very lightweight set of UDX to access the hosted vanna.ai system.  The following commands are implemented:
* vannaGetTrainingDocs(apikey, model): wraps vn.generate_sql
* vannaGetSql(apikey, model, question): wraps vn.generate_sql and returns filtered output, which is usually only SELECT statements.  For DDL, ETL, etc. use vannaGetRawSql.
* vannaGetRawSql(apikey, model, question): wraps vn.generate_sql, but returns unfiltered result from LLM.  This function will return SQL other than SELECT statements.
* vannaTrain(apikey, model, traintype, traindata): wraps vn.train.  traintype is one of 'ddl, 'doc', 'sql', specifying what is in traindata string.
* vannaRemoveTraining(apikey, model, id): wraps vn.remove_training_data.  id is obtained from getTrainingDocs.

The sample SQL implements two stored procedures to get DDL using export_objects for use in training.

Please see the SQL file for install steps and samples of supported commands.

The Python file with the UDX implementation is also available for fixes and enhancements.
