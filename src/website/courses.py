from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_required, current_user
from .models import Course


courses_blueprint = Blueprint('courses', __name__)


@courses_blueprint.route('/courses', methods=['GET', 'POST'])
@login_required
def courses_info():
    courses = Course.query.all()
    if request.method == 'POST':
        name = request.form.get('name')
        datestart = request.form.get('datestart')
        datefinish = request.form.get('datefinish')

        new_course = Course(name=name, datestart=datestart, datefinish=datefinish)
        db.session.add(new_course)
        db.session.commit()
        flash('Course was saved successfully!', category='success')
        return redirect(url_for('courses.courses_info'))
    return render_template('courses.html', user=current_user, courses=courses)
