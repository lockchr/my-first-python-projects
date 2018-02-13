from twilio.rest import Client

account_sid = 'ACb291717298fd7933d41f3520d72b5693'
auth_token = '94d76442f4b76a0db419936ea347908b'
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    body = "Type what you want here",
    to = "**your registerd number**",
    from_ = "**your twilio number from website**")
print (message.sid)
