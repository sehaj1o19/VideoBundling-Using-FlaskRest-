import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld/Ekam")

#data = [
 #   {"likes":10, "name": "Ekamjot", "views": 10000},
  #  {"likes":78000, "name": "How to make a Rest API", "views": 80000},
   # {"likes":35, "name": "Tim", "views": 200}    
#]


#response = requests.post(BASE + "video/1", {"likes":10, "name": "Ekamjot", "views": 10000})
#for i in range(len(data)):
 #   response = requests.post(BASE + "video/" + str(i), data[i])
 #   print(response.json())

#input()
#response= requests.delete(BASE+ "video/0")
#print(response)
#input()

#response = requests.get(BASE + "video/6")
#print(response.json())

response = requests.patch(BASE + "video/0", {"views":99, "likes": 101})
print(response.json())