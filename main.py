from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
#	return("hello welkom  on my joke page")
        return render_template ('index.html')

@app.route('/joke')
def joke():
        return render_template ('joke.html')

@app.route('/answer')
def answer():
        return render_template ('answer.html')


if __name__ == '__main__':
    app.run(debug=True)
