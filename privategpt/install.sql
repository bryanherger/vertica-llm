-- Installation script: defined the shared library and the appropriate entry points
-- Note: run this file from the package directory so $PWD below gets the correct path!

select version();

-- Step 1: Create library
DROP LIBRARY IF EXISTS PrivateGptPyScalarFunctions CASCADE;
\set libfile '\''`pwd`'/PrivateGptPyFunctions.py\''
CREATE LIBRARY PrivateGptPyScalarFunctions AS :libfile LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION privateGptChat AS NAME 'privateGptChat_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatWithPrompt AS NAME 'privateGptChatWithPrompt_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatWithDocs AS NAME 'privateGptChatWithDocs_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatExtended AS NAME 'privateGptChatExtended_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatIngestDocs AS NAME 'privateGptChatIngestDocs_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatListDocs AS NAME 'privateGptChatListDocs_factory' LIBRARY PrivateGptPyScalarFunctions;
CREATE FUNCTION privateGptChatDeleteDocs AS NAME 'privateGptChatDeleteDocs_factory' LIBRARY PrivateGptPyScalarFunctions;
