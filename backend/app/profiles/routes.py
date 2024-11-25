from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models import User, Profile  # Ensure User is imported here
from app.profiles import profiles
from app.profiles.forms import EditProfileForm

@profiles.route('/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profiles/profile.html', user=user)

@profiles.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.profile.bio = form.bio.data
        current_user.profile.avatar_url = form.avatar_url.data
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('profiles.profile', username=current_user.username))
    elif request.method == 'GET':
        form.bio.data = current_user.profile.bio
        form.avatar_url.data = current_user.profile.avatar_url
    return render_template('profiles/edit_profile.html', form=form)
