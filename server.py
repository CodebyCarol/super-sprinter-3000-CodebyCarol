from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def route_index():
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('index.html', note=note_text)

@app.route('/edit-note')
def route_edit():
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('edit.html', note=note_text)

@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    session['note'] = request.form['note']
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = '4Rkj4jo'
    app.run(debug = True)
