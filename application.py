from flask import Flask, request, redirect
import twilio.twiml
 
application = Flask(__name__)
 
@application.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
 
    with resp.gather(numDigits=5, action="/handle-key", method="POST") as g:
        g.say("Please enter passcode")
 
    return str(resp)
 
@application.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	resp = twilio.twiml.Response()
	digits_pressed = request.values.get('Digits', None)

	if (digits_pressed == "14789"):
		resp.say("Passcode OK")
		resp.play(digits=9)
	else:
		return redirect("/")

	return str(resp)

if __name__ == "__main__":
    application.run(debug=True)
