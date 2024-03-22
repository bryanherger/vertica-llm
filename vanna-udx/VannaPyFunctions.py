import vertica_sdk
from urllib import request
import json, pprint, ssl

def vanna_api_call(endpoint, apikey, model, method, params, whichfield):
    req = request.Request(endpoint, method="POST")
    req.add_header('Content-Type', 'application/json')
    req.add_header('Vanna-Key', apikey)
    req.add_header('Vanna-Org', model)
    data = {
        "method":method,
        "params":params
    }
    data = json.dumps(data)
    data = data.encode()
    r = request.urlopen(req, data=data, context=ssl.SSLContext())
    content = json.loads(r.read())
    # print('api_call:',content)
    if 'result' in content:
        if whichfield in content['result']:
            return content['result'][whichfield]
        return content['result']
    return content

class vannaGetTrainingDocs(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'get_training_data', {}, 'data'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaGetTrainingDocs_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaGetTrainingDocs()

class vannaGetSql(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'generate_sql_from_question', [{"question":z}], 'sql'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaGetSql_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaGetSql()

class vannaGetRawSql(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'generate_sql_from_question', [{"question":z}], 'raw_answer'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaGetRawSql_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaGetRawSql()

class vannaTrainQuestionSql(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            w = arg_reader.getString(3)
            res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'add_sql', [{"question":z,"sql":w,"tag":"manual"}], 'result'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaTrainQuestionSql_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addLongVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaTrainQuestionSql()

class vannaTrain(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            w = arg_reader.getString(3)
            if z == 'sql':
                res_writer.setString('Training with sql is not yet implemented.')
                q = vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'generate_question', [{"raw_answer":"","prefix":"","postfix":"","sql":w}], 'result')
                r = vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'add_sql', [{"question":q['question'],"sql":w,"tag":"Manually Trained"}], 'result')
                res_writer.setString(json.dumps(q) + ' ' + json.dumps(r))
            elif z == 'ddl':
                res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'add_ddl', [{"data":w}], 'result'))
            else:
                res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'add_documentation', [{"data":w}], 'result'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaTrain_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addLongVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaTrain()

class vannaRemoveTraining(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            z = arg_reader.getString(2)
            res_writer.setString(vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'remove_training_data', [{"data":z}], 'result'))
            res_writer.next()
            if not arg_reader.next():
                break

class vannaRemoveTraining_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addLongVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addLongVarchar(131072)
    def createScalarFunction(self, srv):
        return vannaRemoveTraining()

class vannaRemoveAllTraining(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            x = arg_reader.getString(0)
            y = arg_reader.getString(1)
            t = vanna_api_call("https://ask.vanna.ai/rpc", x, y, 'get_training_data', {}, 'data')
            tj = json.loads(t)
            for tji in tj:
                server_interface.log("Will remove {}".format(tji['id']))
            res_writer.setString("Not yet implemented")
            res_writer.next()
            if not arg_reader.next():
                break

class vannaRemoveAllTraining_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(64)
    def createScalarFunction(self, srv):
        return vannaRemoveAllTraining()
