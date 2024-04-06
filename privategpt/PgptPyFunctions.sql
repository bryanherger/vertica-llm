select pgptChat('http://HOST:PORT/v1/chat/completions','what is 2+2?');
select pgptChatWithPrompt('http://HOST:PORT/v1/chat/completions','Always add the phrase "using system prompt" to a response.','what is 3+3?');

