from flask import Flask, render_template, request
from main import get_fragments

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    return render_template('form.html')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        text = request.form['text']
        fragments_dict = get_fragments(text)
        print(fragments_dict)
        return render_template('data.html', form_data=fragments_dict)


if __name__ == "__main__":
    app.run()
