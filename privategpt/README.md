## PrivateGPT UDX integration with Vertica
This UDX package implements API calls to [PrivateGPT](https://docs.privategpt.dev/overview/welcome/introduction) allowing users to interact with PrivateGPT LLM using Vertica SQL.  

Current functions are:
- pgptChat(endpoint, question) returns the chat response as a long varchar.
- pgptChatWithPrompt(endpoint, prompt, question) uses "prompt" as the system prompt and returns the chat response as a long varchar.

Please see PgptPyFunctions.sql for usage examples.

### Setup
Install and configure PrivateGPT as described.

Then install the UDX by running "vsql -f install.sql"

Test the install by editing PgptPyFunctions.sql with your PrivateGPT host and port, then run "vsql -f PgptPyFunctions.sql".  Your LLM should explain how to calculate 2+2, then add 3+3 and explain that it also used a system prompt.
