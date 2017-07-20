from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcbe521b26804dac1b58a6f22ea328bc6"
# Your Auth Token from twilio.com/console
auth_token  = "319a0779f0f57af111162cbef68f96ea"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13476925249", 
    from_="+12014290079",
    body="Hello Dramane! This Guy just Enter in your Room: ",
	media_url="robot-friend-popular-science.jpg")
print(message.sid)