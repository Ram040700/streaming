from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return  'Home Page'
@app.route('/second')
def second():
    return 'second page'
if __name__=='__main__':
    app.run(debug=True)
    