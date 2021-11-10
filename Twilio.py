from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbf02fe253cef5d92aac22aa3bd5b1676"
# Your Auth Token from twilio.com/console
auth_token = "01dad8c9bf80cb7ae9a2489664c6bca6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12158079223",
    from_="+12156087254",
    body="Hello from Python!")

print(message.sid)