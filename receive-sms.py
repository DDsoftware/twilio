import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def sms_reply():
	resp = MessageResponse()

	resp.message("Ok, Goo. I got it!")

	return str(resp)

if __name__ == "__main__":
		app.run(debug=True)