from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbf02fe253cef5d92aac22aa3bd5b1676"
# Your Auth Token from twilio.com/console
auth_token = "c58258f739588c8c6da79949d6ce1a63"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12158079223",
    from_="+12156087254",
    body="Hello from Python!")

print(message.sid)