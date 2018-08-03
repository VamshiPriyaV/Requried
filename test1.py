import json
import pymongo
from py2neo import Graph, authenticate
from py2neo.packages.httpstream import http
http.socket_timeout = 9999

def myListip(doc):
        myVar = doc['Network']['transprotProtocol']
        myList = []
        for var in myVar:
		pass
                #print var
       
        for var in myVar:
                if (var['destinationIp']!=None and '127.0.0.1' not in var['destinationIp']) and (var['sourceIp']!=var['destinationIp']):
                        #print var
                        inner_dict = {}
                        inner_dict['sourceIp'] = var['sourceIp']
                        inner_dict['sourcePort'] = str(var['sourcePort'])
			inner_dict['destinationIp'] = var['destinationIp']
                        inner_dict['destinationPort'] = str(var['destinationPort'])
                        myList.append(inner_dict)
        return myList


def network_Data(doc):
        sample = {}
        sample['ipaddress'] = myListip(doc)
	sample['ip'] = doc['Network']['ip']
	sample['Os'] = doc['Os']['osName']
        return sample

def final_output(doc):
        output = {}
        output['Network'] = network_Data(doc)
        return json.dumps(output)


def file_writing(doc):
	output = final_output(doc)
        ff = open('data1.json', 'w')
        ff.write(output)
        ff.flush()
        ff.close()


	
authenticate("localhost:7474", "neo4j", "neo123")
graph = Graph()


	
connection = pymongo.MongoClient("mongodb://localhost")
db = connection['db_sample1']
record1 = db['collection_name']
cursor = record1.find()
#count = 0
for index, doc in enumerate(cursor):
	print index
	file_writing(doc)
        with open('data1.json') as data_file:
		json1 = json.load(data_file)
	
	'''
	myVar = json1['Network']['ipaddress']
	
	
	for var in myVar:
		print type(var['destinationPort'])
		count+=1
       		#print var['sourceIp']+"               "+ var['destinationIp']+"                        "+str(var['sourcePort'])+"                   "+str(var['destinationPort'])
	
	'''	
	print("--------------------------------------------------------------------------------------------------------------------------------------")


	
	query = """
        WITH {json} AS document
        UNWIND document.Network.ip as ip
        UNWIND document.Network.Os as os
        UNWIND document.Network.ipaddress AS network
        MERGE (sIp:Ip {name:ip})
        MERGE (dIp:Ip {name:network.destinationIp})
        MERGE (sIp)-[r:tcp]->(dIp)
        """



	print graph.cypher.execute(query, json=json1)



#{name:' S - '+network.sourcePort+' TCP '+' D - '+network.destinationPort}
