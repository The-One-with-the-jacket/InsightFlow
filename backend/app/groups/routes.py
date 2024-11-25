from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models import Group, Membership
from app.groups import groups
from app.groups.forms import CreateGroupForm

@groups.route('/create', methods=['GET', 'POST'])
@login_required
def create_group():
    form = CreateGroupForm()
    if form.validate_on_submit():
        group = Group(name=form.name.data, description=form.description.data)
        db.session.add(group)
        db.session.commit()
        membership = Membership(user_id=current_user.id, group_id=group.id, role='owner')
        db.session.add(membership)
        db.session.commit()
        flash('Group created successfully!')
        return redirect(url_for('groups.group', group_id=group.id))
    return render_template('groups/create_group.html', form=form)

@groups.route('/<int:group_id>', methods=['GET'])
@login_required
def group(group_id):
    group = Group.query.get_or_404(group_id)
    return render_template('groups/group.html', group=group)
