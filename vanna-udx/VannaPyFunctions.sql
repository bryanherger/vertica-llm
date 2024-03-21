\set apimodel '\''`echo $MODEL`'\''
\set apikey '\''`echo $APIKEY`'\''
-- Step 1: Create library
CREATE LIBRARY VannaPyScalarFunctions AS '/home/azureuser/python/vanna-udx/VannaPyFunctions.py' LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION vannaGetTrainingDocs AS NAME 'vannaGetTrainingDocs_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaGetSql AS NAME 'vannaGetSql_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaGetRawSql AS NAME 'vannaGetRawSql_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaTrain AS NAME 'vannaTrain_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaRemoveTraining AS NAME 'vannaRemoveTraining_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaRemoveAllTraining AS NAME 'vannaRemoveAllTraining_factory' LIBRARY VannaPyScalarFunctions;

-- Step 3: Create stored procedures to support UDX
CREATE OR REPLACE PROCEDURE get_ddl(IN st varchar, OUT ddl varchar(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')'; 
    RAISE NOTICE 'DDL: %', ddl;
END;
$$;

CREATE OR REPLACE PROCEDURE vanna_train_ddl(IN apikey VARCHAR, IN model VARCHAR, IN st varchar, OUT ddl varchar(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')'; 
    res <- EXECUTE SELECT vannaTrain('''||apikey||''','''||model||''',''ddl'','''||ddl||''')';
    RAISE NOTICE 'train: %', res;
END;
$$;

-- Step 4: Use functions
SELECT vannaGetTrainingDocs(:apikey,:apimodel);
SELECT vannaGetSql(:apikey,:apimodel,'what was the average daily temperature at Newark in January in order by date?');
SELECT vannaGetRawSql(:apikey,:apimodel,'create a copy of the new weather table');
SELECT vannaTrain(:apikey,:apimodel,'sql','create a copy of the new weather table');
-- this needs to be set every time since it's API assigned and not predictable  154711-sql
SELECT vannaRemoveTraining(:apikey,:apimodel,'154711-sql');
SELECT vannaRemoveAllTraining(:apikey,:apimodel);

-- Step X: clean up
DROP LIBRARY VannaPyScalarFunctions CASCADE;
