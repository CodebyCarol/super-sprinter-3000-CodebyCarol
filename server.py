from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
#not specified in the assignment correctly... what is the requirement in the main page???
#should be a welcoming page, links to /list and /story(add new) can also show /list

@app.route('/list', method=['POST', 'GET'])
#using list.html
#lists the data in a HTML table
#the pen at the end of the row redirect to editor, the bin icon removes the actual row from the table
#has an add new user story button -redirects to the (creating)/story page
def route_list():


@app.route('/story')
#using form.html
#add new story for the /story page, it is an empty form with a create button

@app.route('/story/<story_id>')
#using editor.html
#the same form as /story page, but filled in with data of the given User Story
#Update button should update existing entry, not create a new

if __name__ == '__main__':
    app.secret_key = '4Rkj4jo'
    app.run(debug = True)
