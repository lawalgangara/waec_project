from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app.models.admin import Admin


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if any admin records exist
        existing_admin = Admin.query.first()

        if existing_admin:
            admin = Admin.query.filter_by(email=email, password=password).first()

            if admin:
                login_user(admin)
                return redirect(url_for('dashboard'))
            
            flash('Invalid email or password, please try again.', 'error')
            return render_template('admin/login.html')
        
        else:
            # If no admin records exist, create a new admin
            new_admin = Admin(email=email, password=password)
            db.session.add(new_admin)
            db.session.commit()

            # Log in admin
            login_user(new_admin)
            return redirect(url_for('dashboard'))

    return render_template('admin/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('login_page'))
