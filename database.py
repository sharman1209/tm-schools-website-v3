from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
  }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tm_schools"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs

def fetch_school_data(school_query):
  with engine.connect() as conn:
      sql = text("""
          SELECT `KOD SEKOLAH`, `SENARAI SEKOLAH MALAYSIA`, `SEKOLAH INTERIM`, `SEKOLAH VSAT`, `SEKOLAH HIBRID`
          FROM tm_schools
          WHERE `KOD SEKOLAH` LIKE :school_query OR `SENARAI SEKOLAH MALAYSIA` LIKE :school_query
      """)
      result = conn.execute(sql, {"school_query": f"%{school_query}%"})
      rows = result.fetchall()

      if rows:
          # Manually construct the list of dictionaries
          column_names = ["KOD SEKOLAH", "SENARAI SEKOLAH MALAYSIA", "SEKOLAH INTERIM", "SEKOLAH VSAT", "SEKOLAH HIBRID"]
          school_data_list = [{column: row[i] for i, column in enumerate(column_names)} for row in rows]
          return school_data_list
      else:
          print(f"No result found for: {school_query}")
          return None


# Function to get suggestions from the database
def fetch_suggestions(school_query):
    with engine.connect() as conn:
        sql = text("SELECT `KOD SEKOLAH` FROM tm_schools WHERE `KOD SEKOLAH` LIKE :school_query")
        result = conn.execute(sql, {'school_query': f'%{school_query}%'})
        suggestions = [row['KOD SEKOLAH'] for row in result]
        print(suggestions)  # Add this line for debugging
    return suggestions


def load_job_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tm_schools"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    
    conn.execute(query, parameters=dict(job_id=job_id, full_name=data['full_name'], email=data['email'], linkedin_url=data['linkedin_url'], education=data['education'], work_experience=data['work_experience'], resume_url=data['resume_url']))

                            
  