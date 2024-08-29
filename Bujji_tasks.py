import requests
import socket
from config import key


def get_ip(host):
    try:
        result = socket.getaddrinfo("google.com",None)
    except Exception as e :
        print(e)
        result = f"Error in finding the IP, {e}"
    return result

def temp_room(room):
    result = "Temp = 20, Humidity 70 "
    return result

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city,"format":"json","u":"f"}

    headers = {
        "x-rapidapi-key": "c141acc747msh739fef9eb81af3ap140c35jsn5e58b57545dd",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1 = response.json()
    #print (d1)
    d1 = d1.get("current_observation")
    hum=d1.get('atmosphere').get("humidity")
    temp = d1.get('condition').get("temperature")
    temp = round((temp-32)*5/9,2)
    return (f"Humidity: {hum}, Temp in C: {temp}")


def chat1(chat):
    messages = []   #list of messages
    
    system_message = f"You are an AI bot, your name is Bujji find the content related to the query:"
    message = {"role" : "user", "parts" : [{"text": system_message+" "+chat }] }
    messages.append(message)   
    data = { "contents": messages }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyCSK0VcSDWjRlwzQKeVHL_DsTEwHRw3pwQ"
    response = requests.post(url, json=data )

    t1 = response.json()
    #print (t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)
    return t2
#chat = mic1()
#chat = input("Enter the Query: ")    
#chat = "who is Narendra Modi"
#chat1(chat)      

definitions = [
            {
            "name": "chat1", 
            "description": "hi hello general message",
            "parameters" :
                {
                "type": "object",
                "properties": {
                "chat" : {
                    "type" : "string",
                    "description" : "full query asked by user"
                         }
                               }
                }
            },

            {
            "name": "temp_city", 
            "description": "find weather, temperature of a city",
            "parameters" :
                {
                "type": "object",
                "properties": {
                "city" : {
                    "type" : "string",
                    "description" : "City to find weather"
                         }
                               }
                }
            },


            {
            "name": "temp_room", 
            "description": "find temperature of my room or home",
            "parameters" :
                {
                "type": "object",
                "properties": {
                "room" : {
                    "type" : "string",
                    "description" : "room or home"
                         }
                               }
                }
            },

            {
            "name": "get_ip", 
            "description": "find the address of given url or domain name",
            "parameters" :
                {
                "type": "object",
                "properties": {
                "host" : {
                    "type" : "string",
                    "description" : "get url or Domain name"
                         }
                               }
                }
            },


              ]

if __name__=="__main__":
    print (temp_city("Delhi"))
 