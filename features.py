from flask import Flask
FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'hello this is the first project in flask'

@FAI.route('/secondstringresponse')
def secondstringresponse():
    return 'hello this is the second string response in flask project'

if__name__='__main__'
FAI.run(debug=True)