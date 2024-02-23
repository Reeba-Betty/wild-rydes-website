from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Wild Rydes\nDeveloper: [Reeba Mary Betty]\nCompany ID: [100890704]'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')