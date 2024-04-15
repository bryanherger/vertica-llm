## PrivateGPT UDX integration with Vertica
This UDX package implements API calls to [PrivateGPT](https://docs.privategpt.dev/overview/welcome/introduction) allowing users to interact with PrivateGPT LLM using Vertica SQL.  

Current functions are:
- privateGptChat(endpoint, question [ USING PARAMETERS useDocs {0|1}, systemPrompt = 'VARCHAR' ] )
   - required arguments are PrivateGPT API endpoint in the form 'http[s]://HOST:PORT' (no trailing slash) and question.
   - optional parameters are useDocs (boolean, whether to use document store to augment results), and systemPrompt (varchar, system prompt to pass to LLM)
   - returns the chat response as a long varchar.
- privateGptChatIngestDocs(endpoint, filename, filecontent)
   - required arguments are PrivateGPT API endpoint in the form 'http[s]://HOST:PORT' (no trailing slash), filename to identify this content, and actual content.
   - returns success/failure message as a varchar.
- privateGptChatListDocs(endpoint)
   - required argument is PrivateGPT API endpoint in the form 'http[s]://HOST:PORT' (no trailing slash).
   - returns list of stored filenames as varchar.
- privateGptChatDeleteDocs(endpoint, filename)
   - required arguments are PrivateGPT API endpoint in the form 'http[s]://HOST:PORT' (no trailing slash) and filename to delete as shown in list (or from ingest).
   - returns success/failure message as a varchar.

Please see PrivateGptPyFunctions.sql for usage examples.

### Setup
Install and configure PrivateGPT as described. I test with qdrant and ollama running dolphin-mixtral.

Then install the UDX by running "vsql -f install.sql" on a Vertica node as database superuser.

Test the install by editing PrivateGptPyFunctions.sql with your PrivateGPT host and port, then run "vsql -f PrivateGptPyFunctions.sql".  Your LLM should explain how to calculate 2+2, then add 3+3 and explain that it also used a system prompt, then show some tests with or without document store to discuss the rain in Spain.
