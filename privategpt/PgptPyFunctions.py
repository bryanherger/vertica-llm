import vertica_sdk
from urllib import request
import json, pprint, ssl

def pgpt_api_call(endpoint, messages,use_context,incl_refs):
    req = request.Request(endpoint, method="POST")
    req.add_header('Content-Type', 'application/json')
    data = {
        "messages":messages,
        "stream":False,
        "use_context":use_context,
        "use_context":incl_refs
    }
    data = json.dumps(data)
    data = data.encode()
    r = request.urlopen(req, data=data, context=ssl.SSLContext())
    content = json.loads(r.read())
    # print('api_call:',content)
    if 'choices' in content:
        if 'message' in content['choices'][0]:
            return content['choices'][0]['message']['content']
    return content

class pgptChat(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(pgpt_api_call(x,msgs,False,False))
            res_writer.next()
            if not arg_reader.next():
                break

class pgptChat_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return pgptChat()

class pgptChatWithPrompt(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            msgs = [{"content":y,"role":"system"},{"content":z,"role":"user"}]
            res_writer.setString(pgpt_api_call(x,msgs,False,False))
            res_writer.next()
            if not arg_reader.next():
                break

class pgptChatWithPrompt_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return pgptChatWithPrompt()

class pgptChatWithDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            msgs = [{"content":y}]
            res_writer.setString(pgpt_api_call(x,msgs,True,True))
            res_writer.next()
            if not arg_reader.next():
                break

class pgptChatWithDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return pgptChatWithDocs()

