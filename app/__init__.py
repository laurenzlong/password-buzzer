from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
passcode = "1" # passcode that your guest must enter when prompted
passcodeLen = 1 # length of the passcode
unlockDigit = 9 #the key that the receiver currently needs to press to unlock the door
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
 
    with resp.gather(numDigits=passcodeLen, action="/handle-key", method="POST") as g:
        g.say("Please enter passcode")
 
    return str(resp)
 
@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	resp = twilio.twiml.Response()
	digits_pressed = request.values.get('Digits', None)

	if (digits_pressed == passcode):
		resp.say("Passcode OK")
		resp.play(digits=unlockDigit)
	else:
		return redirect("/") #plays prompt again

	return str(resp)
