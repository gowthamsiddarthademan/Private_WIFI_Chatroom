from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Route for the login page
@app.route('/')
def home():
    return render_template('index.html')  # Login page

# Route for the chatroom
@app.route('/chat')
def chat():
    username = request.args.get('username')
    if not username:
        return redirect(url_for('home'))  # Redirect to login if username not provided
    return render_template('chat.html', username=username)

# WebSocket event for handling messages
@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)  # Broadcast message to all connected clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
