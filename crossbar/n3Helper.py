import objectpath
import json,requests,time
import pprint
import re


class N3Helper():
    
    def getEvent(self, params):

        url = "http://ewetasker.cluster.gsi.dit.upm.es/mobileConnectionHelper.php"
        payload = {"command" : "getChannels"}       
        
#        def find_between( s, first, last ):
#            try:
#                start = s.index( first ) + len( first )
#                end = s.index( last, start )
#                return s[start:end]
#            except ValueError:
#                return ""



        data_channels = requests.post(url, data=payload)

        data = data_channels.json()

        tree_obj = objectpath.Tree(data)
        

        
        
        try:
            #De todos los canales, cojemos el canal que coincida con el nombre
            channel = list(tree_obj.execute("$.*[@[title] is "+params['channel']+"]"))[0]
#            pprint.PrettyPrinter(indent=4).pprint(channel)
            #De ese canal, cojemos los eventos que tiene
            event = list(objectpath.Tree(channel).execute("$.events[str("+params['event']+") in @.title]]"))[0]
#            pprint.PrettyPrinter(indent=4).pprint(event)
            #De los eventos sacamos los prefijos de ese evento
            prefix = objectpath.Tree(event).execute("$.prefix")
#            pprint.PrettyPrinter(indent=4).pprint(prefix)
            #Cpgemos el ewe- correspondiente, lo vamos a utilizar en las reglas
            ewe = list(objectpath.Tree(prefix.split(" ")).execute("$*[str('ewe-') in @]]"))[0]
#            pprint.PrettyPrinter(indent=4).pprint(ewe)
            #Cogemos las reglas y las preparamos en el formato adecuado
            rule = objectpath.Tree(event).execute("$.rule")
            
            rule = rule.replace("?event ", ewe+params["channel"]+" ")
            rule = rule.replace("?event!", ewe+params["channel"]+" ")
#            pprint.PrettyPrinter(indent=4).pprint(rule)
            
            #Cogemos los parametros y los metermos en la regla.
            paramsName = re.findall('#[a-zA-Z]*#',rule)
            for param in paramsName:
#                test = find_between(rule, "?"+param.replace("#",""), param)
#                print(test)
                deleteString = rule[rule.find("?"+param.replace("#","")+" "):rule.find("#.")+2]
                deleteString1 = rule[rule.find("math:"):rule.find("#")]
                rule = rule.replace(deleteString, "")
                rule = rule.replace(deleteString1, "")
                rule = rule.replace("?"+param.replace("#",""), "'"+params["params"][param.replace("#","")]+"'")
                rule = rule.replace(param, "'"+params["params"][param.replace("#","")]+"'")
            #Puede que haya que quitar los \n
            
            return prefix+" "+rule
        except IndexError as e:
            print("Parameters not correctly defined, channel or event not found: " +str(e))
        except Exception as e:
            print("Something went wrong, parameters not correctly defined " + str(e))
            
        return None
 
        
        
    params = {}
    params["channel"] = "presence"
    params["event"] = "Less"
    params["params"] = {"sensorID" : "1023", "distance" : "0.23"}
#    getEvent(None, params)


    
#pprint.PrettyPrinter(indent=4).pprint(channel)

#events = list(objectpath.Tree(channel).execute("$.*[@[title] is 'Turn ON']"))[0]
#event = list(objectpath.Tree(channel).execute("$.events[str("+params['event']+") in @.title]]"))[0]
#pprint.PrettyPrinter(indent=4).pprint(event)

#prefix = objectpath.Tree(event).execute("$.prefix")
#print(prefix)
#string = prefix.split(" ")
#ewe = list(objectpath.Tree(string).execute("$*[str('ewe-') in @]]"))[0]
#print(ewe)

#rule = objectpath.Tree(event).execute("$.rule")
#smth = rule.replace("?event ", ewe+params["channel"]+" ")
#smth = smth.replace("?event!", ewe+params["channel"]+" ")

#print(smth)

#paramsName = re.findall('#[a-zA-Z]*#',rule)
#for param in paramsName:
#    print(param)
#    smth = smth.replace("?"+param.replace("#",""), "'"+params["params"][0][param.replace("#","")]+"'")
#    smth = smth.replace(param, "'"+params["params"][0][param.replace("#","")]+"'")
#    
#    
    
#print(smth)




