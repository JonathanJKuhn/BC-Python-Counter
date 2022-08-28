from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key= 'Super Secret Session Key'

def add_to_count(num=1,name='visits'):
    if name not in session:
        session[name] = num
    else:
        session[name] += num
    return session

@app.route('/')
def home():
    add_to_count()
    if 'isCountRedirect' not in session:
        session['isCountRedirect'] = False

    if session['isCountRedirect'] == False:
        add_to_count(1,'counter')

    session['isCountRedirect'] = False
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/count', methods=['POST'])
def count():
    incrementNumber = int(request.form['incrementNumber'])
    add_to_count(incrementNumber,'counter')
    session['isCountRedirect'] = True
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('counter')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)