import urllib2
import twitter
import datetime

user = 3059201217 #user id

file = open("twittercredentials.txt") #opening the file
creds = file.readline().strip().split(',') #strip and splitting the lines of the data file
twitterSession = open("C:\Users\Jack\AppData\Local\Google\Chrome\User Data\Default\Current Session") #trying to open my current session
tweeting = twitterSession.read() #trying to read my twitter session path
lines = tweeting.splitlines() #trying to split the lines of the twitter session


api = twitter.Api(creds[0],creds[1],creds[2],creds[3]) #the twitter api which is the 4 keys that we get set when from twitter
statuses = api.GetUserTimeline(user) #pulling in the user timeline
print (statuses[0].text) #printing last status

timestamp = datetime.datetime.utcnow() #current date and time
response = api.PostUpdate("Tweeted at" + str(timestamp)) #posting the update to my twitter
print("Status updated to: " + response.text) #printing the status update in my IDLE shell
