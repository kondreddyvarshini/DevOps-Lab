from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')  # New phone field
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        # Basic validation
        if not full_name or not username or not email or not phone or not password or not confirm_password:
            return render_template('register.html', message="All fields are required.")
        if password != confirm_password:
            return render_template('register.html', message="Passwords do not match.")

        # If everything is valid, redirect to success page
        return redirect(url_for('success', username=username, phone=phone))  # Pass phone to success page

    # If the method is GET, render the registration form
    return render_template('register.html')

@app.route('/success')
def success():
    username = request.args.get('username')
    phone = request.args.get('phone')  # Retrieve phone number
    return render_template('success.html', username=username, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
