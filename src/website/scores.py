from flask import Blueprint, render_template, request, flash
import json
import config.smgr_config as cfg
import dbcontext.dbcontext as db
from flask_login import login_required, current_user
import constants as cst

scores_blueprint = Blueprint('scores', __name__)
smgr_cfg = cfg.Config(cst.SMGR_CFG_FILE)
dbcontext = db.DBcontext(smgr_cfg)
api_schema = smgr_cfg.PG_DB_API_SCHEMA


@scores_blueprint.route('/scores', methods=['GET', 'POST'])
@login_required
def scores_info():
    courses = dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_courses_by_user_id({current_user.id});')[0]
    if request.method == 'POST':
        course = request.form.get('course')
        subtask = request.form.get('subtask')
        reviewer = request.form.get('reviewer')
        student = request.form.get('student')
        max_score = request.form.get('max_score')
        score = request.form.get('score')
        name_conv = request.form.get('name_conv')
        readability = request.form.get('readability')
        sarg = request.form.get('sarg')
        schema_name = request.form.get('schema_name')
        aliases = request.form.get('aliases')
        determ_sorting = request.form.get('determ_sorting')
        ontime = request.form.get('ontime')
        extra = request.form.get('extra')
        comment = request.form.get('comment')
        if course is None:
            flash('Course is not selected', category='error')
        if max_score is None or float(score) > float(max_score):
            flash('Entered Score should be less or equal to Max Score', category='error')
        else:
            data = {
                'course_id': course,
                'reviewer_id': reviewer,
                'student_id': student,
                'subtask_id': subtask,
                'score': score,
                'name_conv': name_conv,
                'readability': readability,
                'sarg': sarg,
                'schema_name': schema_name,
                'aliases': aliases,
                'determ_sorting': determ_sorting,
                'ontime': ontime,
                'extra': extra,
                'comment': comment
            }
            json_data = json.dumps(data)
            sql_sttm = f"CALL mentor.usp_score_insert('{json_data}');"
            print(f'sql_sttm={sql_sttm}')
            dbcontext.run_procedure(sql_sttm)
            flash('Scores were saved successfully!', category='success')
    return render_template('scores.html', user=current_user, courses=courses)


@scores_blueprint.route('/get_tasks', methods=['GET', 'POST'])
@login_required
def get_tasks():
    course_id = request.args.get('courseId')
    tasks = dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_tasks_by_course_id({course_id});')[0]
    return json.dumps(tasks)


@scores_blueprint.route('/get_subtasks', methods=['GET', 'POST'])
@login_required
def get_subtasks():
    task_id = request.args.get('taskId')
    subtasks = dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_subtasks_by_task_id({task_id});')[0]
    return json.dumps(subtasks)


@scores_blueprint.route('/get_reviewer', methods=['GET', 'POST'])
@login_required
def get_reviewer():
    course_id = request.args.get('courseId')
    reviewer = \
        dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_reviewer_by_course_user_id({course_id}, {current_user.id});')[0][0]
    return json.dumps(reviewer)


@scores_blueprint.route('/get_students', methods=['GET', 'POST'])
@login_required
def get_students():
    course_id = request.args.get('courseId')
    students = dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_students_by_course_id({course_id});')[0]
    return json.dumps(students)


@scores_blueprint.route('/get_max_score', methods=['GET', 'POST'])
@login_required
def get_max_score():
    subtask_id = request.args.get('subtaskId')
    max_score = dbcontext.run_query(f'SELECT * FROM {api_schema}.udf_get_max_score_by_subtask_id({subtask_id});')[0][0]
    return json.dumps(max_score)
