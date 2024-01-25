from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, fetch_school_data, fetch_suggestions

app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs)

@app.route("/get_suggestions", methods=["POST"])
def get_suggestions():
    query = request.form.get('query', '')
    suggestions = fetch_suggestions(query)
    return jsonify(suggestions)

@app.route("/", methods=["GET", "POST"])
def search_school():
    result = None
    if request.method == "POST":
        school_query = request.form.get("school_query")
        result = fetch_school_data(school_query)
    return render_template("home.html", result=result)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id,data)
  return render_template('application_submitted.html', application=data, job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)