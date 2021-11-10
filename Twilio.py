from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbf02fe253cef5d92aac22aa3bd5b1676"
# Your Auth Token from twilio.com/console
auth_token = ""  # Get from discord, Twilio blocks functionality if this token is in a rebo

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12158079223",
    from_="+12156087254",
    body="Cool, this works and we can now notify our clientele via SMS")

print(message.sid)
