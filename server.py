from flask import Flask, render_template, redirect, request, session
import csv
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
#using list.html
#lists the data in a HTML table
#the pen at the end of the row redirect to editor, the bin icon removes the actual row from the table
#has an add new user story button -redirects to the (creating)/story page
def route_list(*argv):
    return render_template('list.html')


# @app.route('/story')
# #using form.html
# #add new story for the /story page, it is an empty form with a create button
# def route_story():
#     return render_template('form.html')

@app.route('/story/<story_id>', methods=['GET', 'POST'])
#using editor.html
#the same form as /story page, but filled in with data of the given User Story
#Update button should update existing entry, not create a new
def route_edit(story_id=None):
    return render_template('form.html', story_id=story_id)

if __name__ == '__main__':
    # app.secret_key = '4Rkj4jo'
    app.run(debug = True, port=5000)
