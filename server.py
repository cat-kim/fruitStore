from flask import Flask, render_template, request, session, redirect
import datetime

app = Flask(__name__)
app.secret_key = 'alksdfj;'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buyfruit', methods = ['POST'])
def buy():
    print(request.form)
    fruits = ['lemon', 'lime','orange','grapefruit']
    total = 0
    for fruit in fruits:
        total+=int(request.form[fruit])
        print(total)
    session['total'] = int(request.form['lemon']) + int(request.form['lime']) + int(request.form['grapefruit']) + int(request.form['orange'])
    session['cart'] = request.form
    session['date'] = datetime.datetime.now().strftime('%B %d %Y, %I:%M %p') 
    return redirect('/checkout')

@app.route('/checkout')
def check():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)

