import vertica_sdk
from urllib import request
import json, pprint, ssl

def privateGpt_api_call(endpoint,messages,use_context,incl_refs):
    req = request.Request(endpoint, method="POST")
    req.add_header('Content-Type', 'application/json')
    data = {
        "messages":messages,
        "stream":False,
        "use_context":use_context,
        "include_sources":incl_refs
    }
    data = json.dumps(data)
    data = data.encode()
    r = request.urlopen(req, data=data, context=ssl.SSLContext())
    content = json.loads(r.read())
    if 'choices' in content:
        if 'message' in content['choices'][0]:
            return content['choices'][0]['message']['content']
    return content

def privateGpt_api_custom_call(endpoint,method,data):
    req = request.Request(endpoint, method=method)
    req.add_header('Content-Type', 'application/json')
    data = json.dumps(data)
    data = data.encode()
    r = request.urlopen(req, data=data, context=ssl.SSLContext())
    content = json.loads(r.read())
    return content

class privateGptChat(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(privateGpt_api_call(x,msgs,False,False))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChat_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChat()

class privateGptChatWithPrompt(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            msgs = [{"content":y,"role":"system"},{"content":z,"role":"user"}]
            res_writer.setString(privateGpt_api_call(x,msgs,False,False))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatWithPrompt_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatWithPrompt()

class privateGptChatWithDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(privateGpt_api_call(x,msgs,True,True))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatWithDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatWithDocs()

class privateGptChatExtended(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        useDocs = False
        systemPrompt = "NONE"
        if server_interface.getParamReader().containsParameter("useDocs"):
            useDocs = server_interface.getParamReader().getBool("useDocs")
        if server_interface.getParamReader().containsParameter("systemPrompt"):
            systemPrompt = server_interface.getParamReader().getString("systemPrompt")
        server_interface.log("extended")
        server_interface.log(str(useDocs))
        server_interface.log(str(systemPrompt))
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            if systemPrompt != "NONE":
                msgs = [{"content":systemPrompt,"role":"system"},{"content":y,"role":"user"}]
            res_writer.setString(privateGpt_api_call(x,msgs,useDocs,useDocs))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatExtended_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getParameterType(self, server_interface, params):
        params.addVarchar(8192,"systemPrompt")
        params.addBool("useDocs")
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatExtended()

class privateGptChatIngestDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            data = [{"file_name":y,"text":z}]
            content = privateGpt_api_custom_call(x,"POST",data)
            res_writer.setString(content)
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatIngestDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addLongVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatIngestDocs()

class privateGptChatListDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(privateGpt_api_call(x,msgs,True,True))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatListDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatListDocs()

class privateGptChatDeleteDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(privateGpt_api_call(x,msgs,True,True))
            res_writer.next()
            if not arg_reader.next():
                break

class privateGptChatDeleteDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return privateGptChatDeleteDocs()


