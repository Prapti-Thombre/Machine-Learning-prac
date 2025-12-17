from flask import Flask, render_template

'''
it creates an insteance of the flask class,
which will be yuour WSGi application
'''


##WSGI applicoaton
App = flask(__name__)

@app.rorute("/")
def welcome():
   return "<html><H1>Weelcome to the flask course</H></html>"


@app.route("/index")
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')


if __name__ == "__main__": #this is the entry point of the py file or the application
   app.run(debug=True)