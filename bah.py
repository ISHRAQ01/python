from flask import Flask, request, jsonify
from google.cloud import translate_v2 as translate

app = Flask(__name__)
client = translate.Client()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language', 'en')  # Default to English if target_language is not provided

    result = client.translate(text, target_language=target_language)

    return jsonify({
        'input_text': text,
        'translated_text': result['translatedText']
    })

if __name__ == '__main__':
    app.run(debug=True)
