#line
import Bujji_tasks
from config import key
import requests

def parse_function_response(message):
    function_call = message[0].get("functionCall")
    function_name = function_call["name"]
    print("Bujji: call function", function_name)
    try:
        arguments = function_call.get("args")
        print("Bujji: arguments are ", arguments)
        if arguments:
            d = getattr(Bujji_tasks,function_name)
            print("function is ", d)
            function_response = d(**arguments)
        else:
            function_response = "No Arguments are present"

    except Exception as e :
        print(e)
        function_response = "Invalid function"
    return function_response



def run_conversation(user_message):
    messages = []  
    print(user_message)
    system_message = """You are an AI bot that can do everything using function call. 
    When you are asked to do something, use the function call you have available 
    and then respond with message """

    message = {"role" : "user",
               "parts" : [{"text": system_message+" \n"+user_message }] }

    messages.append(message)

    data = { "contents": [messages],     
             "tools" :
             [ { "functionDeclarations" : Bujji_tasks.definitions
               }]
           }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyCSK0VcSDWjRlwzQKeVHL_DsTEwHRw3pwQ"
    response = requests.post(url, json=data )

    if response.status_code !=200: 
        print (response.text)

    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")
    
    message = t1.get("candidates")[0].get("content").get("parts")
    print("Message #######:",message)
    if 'functionCall' in message[0]:
        resp1=parse_function_response(message)
        print ("Actual response", resp1)
        return  resp1 
    else:
        print("No function call")
 

if __name__ == '__main__':
    user_message = "find the the ip address of google.com "
    print(run_conversation(user_message))  
        