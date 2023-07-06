from flask import Blueprint, render_template, request, flash
import json
import config.smgr_config as cfg
import dbcontext.dbcontext as db
from flask_login import login_required, current_user
from .models import Course

scores = Blueprint('scores', __name__)
smgr_config = cfg.Config(r"src\config\smgr_config.yaml")
dbcontext = db.DBcontext(smgr_config)
api_schema = smgr_config.PG_DB_API_SCHEMA


@scores.route("/scores", methods=["GET", "POST"])
@login_required
def scores_info():
    courses = dbcontext.run_query(f"SELECT course_id, course_name FROM {api_schema}.udf_get_courses_by_user_id({current_user.id});").
    course_id = courses
    print(f"courses={courses}")
    if request.method == "POST":
        course = request.form.get("course")
        task = request.form.get("task")
        subtask = request.form.get("subtask")
        reviewer = request.form.get("reviewer")
        student = request.form.get("student")
        max_score = str(request.form.get("max_score"))
        score = str(request.form.get("score"))
        name_conv = request.form.get("name_conv")
        readability = request.form.get("readability")
        sarg = request.form.get("sarg")
        schema_name = request.form.get("schema_name")
        aliases = request.form.get("aliases")
        determ_sorting = request.form.get("determ_sorting")
        ontime = request.form.get("ontime")
        extra = request.form.get("extra")
        comment = request.form.get("comment")
        # Score that were entered by mentor should be less or equal to Max score
        if float(score) > float(max_score):
            flash("Entered Score should be less or equal to Max Score", category="error")
        else:
            data = {
                "course_name": course,
                "reviewer_name": reviewer,
                "student_name": student,
                "task_name": task,
                "subtask_name": subtask,
                "score": score,
                "name_conv": name_conv,
                "readability": readability,
                "sarg": sarg,
                "schema_name": schema_name,
                "aliases": aliases,
                "determ_sorting": determ_sorting,
                "ontime": ontime,
                "extra": extra,
                "comment": comment
            }
            json_data = json.dumps(data)
            dbcontext.run_procedure(f"CALL mentor.usp_score_insert('[{json_data}]');")
            flash("Scores were saved successfully!", category="success")
    return render_template("scores.html", user=current_user, courses=courses)
