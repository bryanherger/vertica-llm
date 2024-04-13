-- prompt + refs
select privateGptChat('http://HOST:PORT','what is 2+2?');
select privateGptChat('http://HOST:PORT','what is 4+4?' USING PARAMETERS useDocs = 1, systemPrompt = 'Always add the phrase "using system prompt" to a response.');
-- doc test
select privateGptChatIngestDocs('http://HOST:PORT','newfile.txt','The rain in Spain falls mainly on the plain.');
select privateGptChatListDocs('http://HOST:PORT');
select privateGptChat('http://HOST:PORT','where does the rain in Spain fall?');
select privateGptChat('http://HOST:PORT','where does the rain in Spain fall?' using parameters useDocs = 1);
select privateGptChatDeleteDocs('http://HOST:PORT','newfile.txt');
select privateGptChatListDocs('http://HOST:PORT');

