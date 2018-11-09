from flask import Flask, render_template, redirect
import scraper

app = Flask(__name__)

@app.route("/")
def home():

	# Return template and data
	return render_template("index.html")


@app.route("/scrape")
def scrape():
	scraped_resorts = scraper.scrape_page()
	
	print(scraped_resorts)

	# Return template and data
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)