from twilio.rest import Client

account_sid = '*********'
auth_token = '**********'
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    body = "Type what you want here",
    to = "**your registerd number**",
    from_ = "**your twilio number from website**")
print (message.sid)
