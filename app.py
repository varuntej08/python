from flask import Flask

app = Flask(__name__)  # Correct use of __name_

@app.route('/test', methods=['POST'])
def run():
    return '{"message":"hello python"}'  # Correct JSON format

if __name__ == "__main__":  # Correct use of __main_
    app.run(host="0.0.0.0", port=5000, debug=True)  # Simplified port conversion
