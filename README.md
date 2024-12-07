# Private_WIFI_Chatroom


This project is a simple offline chat application designed to facilitate real-time communication among devices connected to the same Wi-Fi network. Built with Python (Flask and Flask-SocketIO), it provides a seamless chatting experience without requiring an internet connection.

---

## **Features**
- **Real-time messaging:** Devices can instantly exchange messages in a shared group chat.
- **User-friendly:** Login requires only a display name; no additional setup is needed.
- **Cross-device support:** Compatible with laptops, desktops, and mobile devices connected to the same Wi-Fi network.
- **Customizable design:** The app includes CSS styling for a clean and modern interface.

---

## **Technology Stack**
- **Backend:** Flask and Flask-SocketIO.
- **Frontend:** HTML, CSS, and JavaScript.
- **Real-time communication:** Powered by the Socket.IO library.

---

## **Setup Instructions**

### ** Install Dependencies**
Ensure Python is installed on your system, then run:
```bash
pip install flask flask-socketio
```


### ** Run the Application**
Start the server by executing:
```bash
python app.py
```

### ** Connect Devices**
1. Open the app in a browser by visiting:
   ```
   http://<your-local-IP>:5000
   ```
   Replace `<your-local-IP>` with the IP address of the server.
2. Share this link with others on the same Wi-Fi network to join the chat.

---

## **Usage**
1. Enter your name on the login screen.
2. Join the group chat and start messaging!
3. All connected devices will see messages in real-time.

---

## **Customization**
- Update the frontend (HTML/CSS) to reflect your preferred design.
- Extend the backend to include additional features like private messaging, emojis, or message history.

