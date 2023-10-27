from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    # Intégrez votre code Python pour traiter la question ici
    # Pour l'instant, nous allons simplement renvoyer la question
    response = "Votre question était : " + question
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
