# from flask import Flask, render_template, request, redirect, url_for, flash

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# # Simulated user database (replace this with a real database later)
# users = {}

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
#         confirm_password = request.form['confirm-password']

#         # Check if the username already exists
#         if username in users:
#             flash('Username already exists! Please choose a different one.', 'danger')
#             return redirect(url_for('signup'))

#         # Check if the passwords match
#         if password != confirm_password:
#             flash('Passwords do not match! Please try again.', 'danger')
#             return redirect(url_for('signup'))

#         # Save the new user
#         users[username] = {
#             'fullname': fullname,
#             'email': email,
#             'password': password
#         }
#         flash('Signup successful! You can now log in.', 'success')
#         return redirect(url_for('login'))  # Redirect to login page

#     return render_template('signup.html')  # Render signup page for GET request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if user exists and password matches
#         if username in users and users[username]['password'] == password:
#             flash('Login successful!', 'success')
#             return redirect(url_for('dashboard'))  # Redirect to a dashboard or home page
#         else:
#             flash('Invalid username or password!', 'danger')

#     return render_template('login.html')  # Render login page for GET request

# @app.route('/dashboard')
# def dashboard():
#     return 'Welcome to your dashboard!'  # Placeholder for your dashboard

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Simulated user database (replace this with a real database later)
users = {}

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Check if the username already exists
        if username in users:
            flash('Username already exists! Please choose a different one.', 'danger')
            return redirect(url_for('signup'))

        # Check if the passwords match
        if password != confirm_password:
            flash('Passwords do not match! Please try again.', 'danger')
            return redirect(url_for('signup'))

        # Save the new user with password hashing
        users[username] = {
            'fullname': fullname,
            'email': email,
            'password': password  # Ideally, use password hashing here
        }
        flash('Signup successful! You can now log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login page

    return render_template('signup.html')  # Render signup page for GET request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists
        if username in users:
            stored_password = users[username]['password']
            # Check if the provided password matches the stored password
            if stored_password == password:
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))  # Redirect to a dashboard or home page
            else:
                flash('Invalid password! Please try again.', 'danger')
        else:
            flash('Invalid username! Please try again.', 'danger')

    return render_template('login.html')  # Render login page for GET request

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'  # Placeholder for your dashboard

if __name__ == '__main__':
    app.run(debug=True)

