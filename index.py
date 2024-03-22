from flask import Flask, request, jsonify
from gradio_client import Client
import os

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Get audio file path and language inputs from request
    audio_file = request.files['audio']
    src_lang = request.form['src_lang']
    tgt_lang = request.form['tgt_lang']
    
    # Save the uploaded audio file
    audio_file.save("uploaded_audio.wav")
    
    # Initialize Gradio client
    client = Client("[GRADIO_URL]")
    
    # Use Gradio client to process audio
    result = client.predict("uploaded_audio.wav", src_lang, tgt_lang, api_name="/s2tt")
    
    # Delete the uploaded audio file
    os.remove("uploaded_audio.wav")
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
