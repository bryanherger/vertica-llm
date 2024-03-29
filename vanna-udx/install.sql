-- Installation script: defined the shared library and the appropriate entry points
-- Note: run this file from the package directory so $PWD below gets the correct path!

select version();

-- Step 1: Create library
DROP LIBRARY IF EXISTS VannaPyScalarFunctions CASCADE;
\set libfile '\''`pwd`'/VannaPyFunctions.py\''
CREATE LIBRARY VannaPyScalarFunctions AS :libfile LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION vannaGetTrainingDocs AS NAME 'vannaGetTrainingDocs_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaGetSql AS NAME 'vannaGetSql_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaGetRawSql AS NAME 'vannaGetRawSql_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaTrain AS NAME 'vannaTrain_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaTrainQuestionSql AS NAME 'vannaTrainQuestionSql_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaRemoveTraining AS NAME 'vannaRemoveTraining_factory' LIBRARY VannaPyScalarFunctions;
CREATE FUNCTION vannaRemoveAllTraining AS NAME 'vannaRemoveAllTraining_factory' LIBRARY VannaPyScalarFunctions;

-- Step 3: Create stored procedures to support UDX
CREATE OR REPLACE PROCEDURE get_ddl(IN st varchar, OUT ddl varchar(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')';
    RAISE NOTICE 'DDL: %', ddl;
END;
$$;

CREATE OR REPLACE PROCEDURE vanna_train_ddl(IN apikey VARCHAR, IN model VARCHAR, IN st varchar, OUT ddl varchar(64000), OUT res VARCHAR(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')';
    RAISE NOTICE 'ddl: %', ddl;
    res := EXECUTE 'SELECT vannaTrain('''||apikey||''','''||model||''',''ddl'',$1)' USING ddl;
    RAISE NOTICE 'train: %', res;
END;
$$;

