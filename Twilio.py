from twilio.rest import Client

TWILIO_SID = 'ACbf02fe253cef5d92aac22aa3bd5b1676'
TWILIO_TOKEN = ''
TWILIO_PHONE = '+12156087254'

client = Client(TWILIO_SID, TWILIO_TOKEN)


def sendOneMessage(sendTo):
    client.messages.create(body="Hey There ! Your schedule is complete, you can take a look at it on our site !", from_=TWILIO_PHONE, to=sendTo)

sendOneMessage('+12158079223')

print('SMS sent succesfully')