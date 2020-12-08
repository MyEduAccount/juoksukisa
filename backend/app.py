from flask import Flask

# Create a flask object
app = Flask(__name__)

@app.route('/api/results')
def results():
    results = [
        {
            'id' : 0, 
            'name' : 'Kalle Järvinen',
            'result' : '01:23:34',
            'distance' : '10km' 
        },
        {
            'id' : 1, 
            'name' : 'Pentti Mielonen',
            'result' : '02:11:04',
            'distance' : '10km' 
        },
        {
            'id' : 2, 
            'name' : 'Jukka Keimola',
            'result' : '01:09:31',
            'distance' : '10km' 
        },
        {
            'id' : 3, 
            'name' : 'Heikki Kinnunen',
            'result' : '02:09:51',
            'distance' : '10km' 
        },
        {
            'id' : 4, 
            'name' : 'Olli Ojala',
            'result' : '01:53:21',
            'distance' : '10km' 
        },
        {
            'id' : 5, 
            'name' : 'Veikko Huopalainen',
            'result' : '03:00:55',
            'distance' : '10km' 
        }
    ]

    # sort the dictionary according to result time
    results.sort(key = lambda x: x['result'])

    # Flask requires the return value to be a dictionary, list does not work
    return { "data": [results] }

'''
@app.route('/tulokset/{ID}:{nimi}')
def tulokset():
    # hae sanakirjasta/tietokannasta kilpailijan matkat ja tulokset (myös kuva ym tietoa?) ID:n ja/tai nimen mukaan
    # haku matkan mukaan?
    return tulokset
'''

if __name__ == '__main__':
    app.run(debug = True)