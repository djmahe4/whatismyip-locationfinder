import requests

z=str(input(f"Enter choice:\n"
 "1:location \n"
 "2:whois "))

api_key=""  #get api key from https://www.whatismyip.com

if z=="1":
   x="ip-address-lookup.php"
elif z=="2":
   x="whois.php"
y=str(input("Enter ip address:"))
link="https://api.whatismyip.com/"+x+"?"+api_key+"&input="+y
print(link)
response = requests.get(link)
print(response.text)
