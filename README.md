# password-buzzer
A Python Flask app powered by Twilio API for apartment/condo buzzer systems. 

Instead of having to answer the buzzer when a guest or delivery person arrives at your building, this app will pick up the call, ask them for a password, and then unlock the door when the correct password is entered. 

##Prerequisites for Use

Your buzzer system must be the type that connects to mobile phones. Your current workflow should be: when a guest enters your buzzer number, you receive a call, and then you must press a certain number on your key pad to "unlock" the door. 

##Instructions for Set Up

1. Download this repository
2. Create a Twilio account at https://www.twilio.com/try-twilio, and then create a Twilio phone number that can receive voice calls. This requires a small subscription fee (a few dollars per month). I recommend getting a number that corresponds with your geography as most buzzers cannot dial long distance phone numbers. 
3. Download virtulenv by typing the following command into your command prompt: 
`easy_install virtualenv`
4. Change your working directory to the directory where you've downloaded the project and type the following into your command prompt:
`pip install -r requirements.txt`
Optional: Do a quick test at this point. Type `python application.py` into your command prompt. Go to [localhost:5000](localhost:5000) in your browser, you should see "please enter passcode" in plain text. 
5. Modify the `passcode` variable in `application.py` to be any password you would like. Modify the `passcodeLen` variable to be the length of the passcode you've chosen. Modify the `unlockDigit` variable to be the number key that you currently need to press to let a guest in.
6. Twilio needs to find your server on the internet, so use any hosting service you'd like. The [Flask documentation](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart-deployment) has suggestions. I personally used [ngrok](https://ngrok.com/) for testing the app, and [AWS](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) for production.
7. Follow these [instructions](https://www.twilio.com/help/faq/voice/how-do-i-assign-my-twilio-number-to-my-voice-application) for connecting your Twilio phone number to the URL of your hosted application. 
8. Ask your building manager or superintendent to connect your buzzer number to to your Twilio number. 
