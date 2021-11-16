from twilio.rest import Client

TWILIO_SID = 'ACaca34ef76a878d566a4e15abc5740e2a'
TWILIO_TOKEN = '4aa2a7e873de6b0a7c628244c2d32260'
TWILIO_PHONE = '+12524604073'

client = Client(TWILIO_SID, TWILIO_TOKEN)



def sendOneMessage(sendTo):
    client.messages.create(body="Our first SMS message from twillio", from_=TWILIO_PHONE, to=sendTo)

sendOneMessage('+12673486451')

print('SMS sent succesfully')