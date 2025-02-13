from flask import render_template, redirect, url_for,flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access,action
import os
from . import appbuilder, db
from .models import Member, Project
from flask import request
from config import Config


API_URL = "http://localhost:8080/api-extrator/process"


class MemberView(ModelView):

    datamodel = SQLAInterface(Member)

    list_columns = ['id','name_member','email_member','role_member','project_id']

    search_columns = ['name_member','email_member','role_member','project_id']


class ProjectView(ModelView):

    datamodel = SQLAInterface(Project)

    list_columns = ['id','name_project','description_project','deadline_project','status_project']

    search_columns = ['name_project','description_project','deadline_project','status_project']


@appbuilder.app.route('/updateParticipants', methods=['GET','POST'])
def showParticipants() :
    if request.method == 'POST':
        project_id = request.form.get('name_project')
        member_id = request.form.get('name_member')
        member = db.session.query(Member).filter_by(id=member_id).first()
        member.project_id = project_id
        db.session.commit()
        flash('Participante adicionado com sucesso')

    projects = db.session.query(Project).all()
    members = db.session.query(Member).all()
    return render_template(
        'updateParticipants.html',
        projects=projects,
        members=members,
        appbuilder=appbuilder,
        base_template=appbuilder.base_template
    )


appbuilder.add_view(
    MemberView,
    "Members",
    icon="fa-folder-open-o",
    category="Members",
    category_icon='fa-envelope'
)


appbuilder.add_view(
    ProjectView,
    "Projects",
    icon="fa-folder-open-o",
    category="Projects",
    category_icon='fa-envelope'
)

appbuilder.add_link(
    "Projects",
    href='/updateParticipants',
    category='Projects',
    category_icon='fa-envelope'

)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


