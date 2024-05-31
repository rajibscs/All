from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory user database for demonstration purposes
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run(debug=True)

