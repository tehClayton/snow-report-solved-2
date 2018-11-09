from flask import Flask, render_template, redirect
import scraper
from ski_resort import Base, SkiResort
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():

	# Return template and data
	return render_template("index.html")


@app.route("/scrape")
def scrape():
	scraped_resorts = scraper.scrape_page()
	resort_list = []
	scrape_ts = datetime.now()
	for k, v in scraped_resorts.items():
		resort_list.append(SkiResort(
			resort_name=k,
			open_status=v['open_status'],
			inches_24_hr=v['new_snow_24_hr'],
			inches_72_hr=v['new_snow_72_hr'],
			open_lift_pct=v['open_lift_pct'],
			open_trail_pct=v['open_trail_pct'],
			scrape_ts=scrape_ts
			))

	for resort in resort_list:
		print(type(resort))


	# Return template and data
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)