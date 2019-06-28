from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACecc34eea21b508523924bedb3a0c5423"
# Your Auth Token from twilio.com/console
auth_token = "e3190ce49fcf9eee9cf265895f96ee4b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1 ",  # ! the number you want to send the message
    from_="+13035365929",  # ! twilio given number
    body="Hello from Python!")  # ! the message body

print(message.sid)
