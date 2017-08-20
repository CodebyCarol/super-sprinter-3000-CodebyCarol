from flask import Flask, render_template, redirect, request, session
import csv
import uuid


app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def route_list(*argv):
    with open('stories.csv', 'r') as csvfile:
        stories=[]
        for row in csvfile:
            stories.append(row.split(';'))
    return render_template('list.html', stories=stories)


@app.route('/story', methods=['GET', 'POST'])
#using form.html template
#add new story for the /story page, it is an empty form with a create button
def route_story():
    if request.method == 'GET':
        return render_template('form.html')

    with open('stories.csv', 'a') as csvfile:
        exportdata = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        exportdata.writerow([str(uuid.uuid4())[:6], request.form['title'], request.form['descr'], request.form['accr'], request. form['businessvalue'], request. form['estimation'], request. form['status']])
    
    return 'The new User Story Has been Created!'


# @app.route('/story/<story_id>', methods=['GET', 'POST'])
# using form.html
# the same form as /story page, but filled in with data of the given User Story
# Update button should update existing entry, not create a new
# def route_edit(story_id=None):
#     formdata = cgi.FieldStorage()
#     title = formdata.getvalue('title')
#     with open ("sprinter_datas.csv")
#     return render_template('form.html', story_id=story_id)


if __name__ == '__main__':
    # app.secret_key = '4Rkj4jo'
    app.run(debug = True, port=5000)

