from flask import Flask,render_template,url_for
import dbconnect, datetime

db = dbconnect.tryConnect()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	headerItems = [
		{'item': 'Home',},
		{'item': 'About',},
		{'item': 'Projects',},
		{'item': 'nom'}
		]
	user = {'nickname': 'butts'} 
	title = user['nickname']
	people = [
		{'person': 'Chris',},
		{'person': 'Rose',},
		{'person': 'Brian'}
		]
	posts = [
		{'title': 'First Post', 'content': 'oauishdeofhwo aoiwuerbfobaso owiebfoabsdfbo webfraoiwebf aosidbofwef bowiebfr oiabofbwe boaiwebnorjpaomweprn nfosnfwone nwoebraowepnr nsapdnfpwen', 'date': 'December 20th, 2016',},
		{'title': 'Second Post', 'content': 'oauishdeofhwo aoiwuerbfobaso owiebfoabsdfbo webfraoiwebf aosidbofwef bowiebfr oiabofbwe boaiwebnorjpaomweprn nfosnfwone nwoebraowepnr nsapdnfpwen', 'date': 'December 21st, 2016',},
		{'title': 'Third Post', 'content': 'oauishdeofhwo aoiwuerbfobaso owiebfoabsdfbo webfraoiwebf aosidbofwef bowiebfr oiabofbwe boaiwebnorjpaomweprn nfosnfwone nwoebraowepnr nsapdnfpwen', 'date': 'December 22nd, 2016',}
	]
	return render_template('blog.html', 
		headerItems=headerItems,
		title=title, 
		user=user, 
		people=people,
		posts=posts)



if __name__ == '__main__':
    app.run(debug=True)