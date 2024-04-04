## PrivateGPT UDX integration with Vertica
This UDX package implements API calls to [PrivateGPT](https://docs.privategpt.dev/overview/welcome/introduction) allowing users to interact with PrivateGPT LLM using Vertica SQL.  

Currently the only function is pgptChat(endpoint, question) that returns the chat response as a long varchar.

### Setup
Install and configure PrivateGPT as described.

Then install the UDX by running "vsql -f install.sql"

Test the install by editing PgptPyFunctions.sql with your PrivateGPT host and port, then run "vsql -f PgptPyFunctions.sql".  Your LLM should explain how to calculate 2+2.