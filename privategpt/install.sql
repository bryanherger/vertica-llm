-- Installation script: defined the shared library and the appropriate entry points
-- Note: run this file from the package directory so $PWD below gets the correct path!

select version();

-- Step 1: Create library
DROP LIBRARY IF EXISTS PgptPyScalarFunctions CASCADE;
\set libfile '\''`pwd`'/PgptPyFunctions.py\''
CREATE LIBRARY PgptPyScalarFunctions AS :libfile LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION pgptChat AS NAME 'pgptChat_factory' LIBRARY PgptPyScalarFunctions;
CREATE FUNCTION pgptChatWithPrompt AS NAME 'pgptChatWithPrompt_factory' LIBRARY PgptPyScalarFunctions;
CREATE FUNCTION pgptChatWithDocs AS NAME 'pgptChatWithDocs_factory' LIBRARY PgptPyScalarFunctions;
