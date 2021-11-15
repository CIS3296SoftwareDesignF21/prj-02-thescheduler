from twilio.rest import Client

TWILIO_SID = 'ACbf02fe253cef5d92aac22aa3bd5b1676'
TWILIO_TOKEN = '01dad8c9bf80cb7ae9a2489664c6bca6'
TWILIO_PHONE = '+12156087254'

client = Client(TWILIO_SID, TWILIO_TOKEN)


def sendOneMessage(sendTo):
    client.messages.create(body="Our first SMS message from twillio", from_=TWILIO_PHONE, to=sendTo)

sendOneMessage('+12158079223')

print('SMS sent succesfully')