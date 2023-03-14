from flask import Flask, request, render_template 
app = Flask(__name__)

@app.route('/')
def login_html():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login(): 
    username = request.form['username']
    password = request.form['password']
    checkpsswd = password.isalpha() or password.isnumeric()
    
    if username[0].isupper() and not(checkpsswd): 
        return render_template('login.html', info='Correct')
        # return render_template('home.html', name=username)
    else:
        return render_template('login.html', info='Invalid Credentials, Please Check Again')

    
if __name__ == "__main__": 
    app.run(debug=True)