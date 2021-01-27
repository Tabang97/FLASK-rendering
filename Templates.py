from flask import Flask, render_template
app = Flask(__name__)

@app.route('/Index')
def index():
    return render_template('greet.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')
if __name__=='__main__':
    app.run(debug=True)
