from twilio.rest import Client

TWILIO_SID = ''
TWILIO_TOKEN = ''
TWILIO_PHONE = ''

client = Client(TWILIO_SID, TWILIO_TOKEN)


def sendOneMessage(sendTo):
    client.messages.create(body="Our first SMS message from twillio", from_=TWILIO_PHONE, to=sendTo)

sendOneMessage('')

print('SMS sent succesfully')

# def Messagerecieved():
#     incoming_msg = request.values.get('Body', '').lower()
#     resp = MessagingResponse()
#     msg = resp.message()
#     responded = False
#
#     if incoming_msg == "CST":
#         msg.body("You chose CST")
#         responded = True
#
#     if "book class" in str.lower(incoming_msg) or "CST" in str.lower(incoming_msg):
#         msg.body("You chose this department")
#         responded = True
#
#     if incoming_msg == "3207" or "Introduction to Systems Programming and Operating Systems" in incoming_msg":
#         msg.body("You chose 3207")
#         responded = True

#Another altnerative to receiving/sending messages
# def MessageAlternative():
#     """Respond to incoming messages with a simple text message."""
#     question = request.values.get('Body')
#     print(question)
#     # Start our TwiML response
#     resp = MessagingResponse()
#     if (question == 'Class'):
#         resp.message('What class would you like to choose')
#
#     elif (question == '3207'):
#         resp.message('You chose 3207 - 3207" or "Introduction to Systems Programming and Operating Systems" in incoming_msg ')
#
#     return str(resp)