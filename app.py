from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio_client import make_call
import config

app = Flask(__name__)


@app.route("/voice-response", methods=["POST"])
def voice_response():
    print("Received a call request...")  # Debugging print

    response = VoiceResponse()
    response.say("Hello! Please enter your birthday in MMDDYYYY format followed by the pound sign.")
    response.gather(num_digits=8, finish_on_key="#", action="/process-birthday")

    print("Sent response to user to enter birthday.")  # Debugging print
    return str(response)

@app.route("/process-birthday", methods=["POST"])
def process_birthday():
    digits = request.form.get("Digits")
    print(f"User entered: {digits}")  # Debugging print

    response = VoiceResponse()
    response.say(f"Thank you! You entered {digits}. Goodbye!")

    print("Responded back to user and ended call.")  # Debugging print
    return str(response)

if __name__ == "__main__":
    print("Starting Flask app...")  # Debugging print
    app.run(debug=True, port=5000)
