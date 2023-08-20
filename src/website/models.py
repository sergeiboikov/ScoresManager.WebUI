from . import db
from flask_login import UserMixin
from config import smgr_config as cfg
import constants as cst

smgr_cfg = cfg.Config(cst.SMGR_CFG_FILE)


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'schema': smgr_cfg.PG_DB_WORKING_SCHEMA}


class Bonus(BaseModel):
    __tablename__ = 'bonus'
    bonus_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(250))
    code = db.Column(db.String(30))


class ConnectionType(BaseModel):
    __tablename__ = 'connection_type'
    connection_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(250))


class Connection(BaseModel):
    __tablename__ = 'connection'
    connection_id = db.Column(db.Integer, primary_key=True)
    connection_string = db.Column(db.String(250))
    connection_type_id = \
        db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.connection_type.connection_type_id'))


class CheckScriptType(BaseModel):
    __tablename__ = 'check_script_type'
    check_script_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))


class CheckScript(BaseModel):
    __tablename__ = 'check_script'
    check_script_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    description = db.Column(db.String(5000))
    connection_id = \
        db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.connection.connection_id'))
    check_script_type_id = \
        db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.check_script_type.check_script_type_id'))


class City(BaseModel):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    geo_point = db.Column(db.String(100))


class CourseStaff(BaseModel):
    __tablename__ = 'course_staff'
    course_staff_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.course.course_id'))
    user_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.user.id'))
    user_type_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.user_type.user_type_id'))
    status_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.status.status_id'))


class Course(BaseModel):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    datestart = db.Column(db.Date)
    datefinish = db.Column(db.Date)


class Settings(BaseModel):
    __tablename__ = 'settings'
    settings_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.user.id'))
    setting_name = db.Column(db.String(100))
    setting_value = db.Column(db.String(100))


class Status(BaseModel):
    __tablename__ = 'status'
    status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(250))


class SubtaskBonus(BaseModel):
    __tablename__ = 'subtask_bonus'
    subtask_bonus_id = db.Column(db.Integer, primary_key=True)
    subtask_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.subtask.subtask_id'))
    student_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.course_staff.course_staff_id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.course_staff.course_staff_id'))
    score = db.Column(db.Numeric(8, 2))
    ontime = db.Column(db.Numeric(8, 2))
    name_conv = db.Column(db.Numeric(8, 2))
    readability = db.Column(db.Numeric(8, 2))
    sarg = db.Column(db.Numeric(8, 2))
    schema_name = db.Column(db.Numeric(8, 2))
    aliases = db.Column(db.Numeric(8, 2))
    determ_sort = db.Column(db.Numeric(8, 2))
    extra = db.Column(db.Numeric(8, 2))
    comment = db.Column(db.String(500))


class SubtaskLog(BaseModel):
    __tablename__ = 'subtask_log'
    subtask_log_id = db.Column(db.Integer, primary_key=True)
    subtask_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.subtask.subtask_id'))
    bonus_id = db.Column(db.Integer)


class Subtask(BaseModel):
    __tablename__ = 'subtask'
    subtask_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.task.task_id'))
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
    topic_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.topic.topic_id'))
    check_script_id = \
        db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.check_script.check_script_id'))
    max_score = db.Column(db.Numeric(8, 2))


class Task(BaseModel):
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.course.course_id'))
    name = db.Column(db.String(250))
    description = db.Column(db.String(250))
    topic_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.topic.topic_id'))


class Topic(BaseModel):
    __tablename__ = 'topic'
    topic_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    is_topic_for_tasks = db.Column(db.Boolean)
    is_topic_for_subtasks = db.Column(db.Boolean)


class UserType(BaseModel):
    __tablename__ = 'user_type'
    user_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    city_id = db.Column(db.Integer, db.ForeignKey(f'{smgr_cfg.PG_DB_WORKING_SCHEMA}.city.city_id'))
    notes = db.Column(db.String(500), nullable=True)
    user_yc_id = db.Column(db.String(500), nullable=True)
    is_active = db.Column(db.Boolean)
