# password-buzzer
A Python Flask app powered by Twilio API for apartment/condo buzzer systems. 

##Prerequisites for Use

Your buzzer system must be the type that connects to mobile phones. When a guest enters your buzzer number, you currently receive a call, and then you must press a certain number on your key pad to "unlock" the door. 

##Instructions for Set Up

1. Download this repository
2. Create a Twilio account at https://www.twilio.com/try-twilio, and then create a Twilio phone number that can receive voice calls. This requires a small subscription fee. 
3. Download virtulenv by typing the following command into your command prompt: 
`easy_install virtualenv`
4. Change your working directory to the directory where you've downloaded the repository and type the following into your command prompt:
`pip install -r requirements.txt`
5. Modify the `passcode` variable in `application.py` to be any 5 digit password you would like.
6. Twilio needs to find your server on the internet, so use any hosting service you'd like. The [Flask documentation](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart-deployment) has suggestions. I personally used [ngrok](https://ngrok.com/) for testing the app, and [AWS](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) for production.
7. Follow these [instructions](https://www.twilio.com/help/faq/voice/how-do-i-assign-my-twilio-number-to-my-voice-application) for connecting your Twilio phone number to the URL of your hosted application. 
8. Ask your building manager or superintendent to connect your buzzer number to to your Twilio number. 
