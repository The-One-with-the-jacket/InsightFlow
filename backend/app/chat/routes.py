from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from . import chat
from .forms import ChatForm
from app.models import Message, Group, Membership
from app import db

@chat.route('/chat/<group_id>', methods=['GET', 'POST'])
@login_required
def chat_room(group_id):
    group = Group.query.get_or_404(group_id)
    if not Membership.query.filter_by(user_id=current_user.id, group_id=group_id).first():
        flash('You are not a member of this group.')
        return redirect(url_for('main.index'))
    
    form = ChatForm()
    if form.validate_on_submit():
        msg = Message(body=form.message.data, author=current_user, group=group)
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('chat.chat_room', group_id=group.id))
    
    messages = Message.query.filter_by(group_id=group.id).order_by(Message.timestamp.asc()).all()
    return render_template('chat/chat_room.html', group=group, messages=messages, form=form)
