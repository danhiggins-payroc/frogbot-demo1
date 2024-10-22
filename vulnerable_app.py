from flask import Flask, request

app = Flask(__name__)

# Example of a vulnerability: This allows command injection via the URL parameter
@app.route('/exec', methods=['GET'])
def exec_command():
    command = request.args.get('command')
    # Vulnerability: Unsafe execution of user-provided input
    return os.system(command)

if __name__ == "__main__":
    app.run(debug=True)