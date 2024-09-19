-- Create stored procedures to support UDX
-- get_ddl: get the export_objects DDL for the [schema.]table specified in "st" and return in "ddl"
CREATE OR REPLACE PROCEDURE get_ddl(IN st varchar, OUT ddl varchar(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')';
    RAISE NOTICE 'DDL: %', ddl;
END;
$$;

-- privategpt_train_ddl: get the export_objects DDL for the [schema.]table specified in "st" and submit to PrivateGPT instance specified by "endpoint" using filename = "[[schema.]table].ddl.txt"
-- return DDL in "ddl" and server API response in "res"
CREATE OR REPLACE PROCEDURE privategpt_train_ddl(IN endpoint VARCHAR, IN st varchar, OUT ddl varchar(64000), OUT res VARCHAR(64000)) LANGUAGE PLvSQL AS $$
BEGIN
    ddl := EXECUTE 'SELECT EXPORT_OBJECTS('''','''||st||''')';
    RAISE NOTICE 'ddl: %', ddl;
    res := EXECUTE 'SELECT privateGptChatIngestDocs('''||endpoint||''','''||model||'.ddl.txt'',$1)' USING ddl;
    RAISE NOTICE 'train: %', res;
END;
$$;
