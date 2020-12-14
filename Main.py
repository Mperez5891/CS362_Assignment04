from flask import Flask, redirect, url_for, render_template, request
from Search import getResults, printResults
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        # pull the data
        term = request.form['inputKeyword']
        city = request.form['inputCity']
        radius = request.form['inputState']
        radius = int(radius) # convert into int
        
        # get the results from our search functions
        results = getResults(term, radius, city)
        printResults(results)
#        return redirect(url_for('display', data = results))
        return render_template('base.html')
    else:
        return render_template('base.html')

@app.route('/results')
def display():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug = True)