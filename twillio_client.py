from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

def make_call(to_number, from_number):
   
    call = client.calls.create(
        url="http:221/voice-response",  
        to=to_number,
        from_=from_number
    )
    return call
