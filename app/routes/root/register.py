from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.models.user import waec_registration
from app.models.admin import Event

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    admin_event = Event.query.first()
    if request.method == 'POST':
        form_data = request.form
        # Convert age to integer
        age = int(form_data['age'])
        new_registration = waec_registration(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            age=age,
            sex=form_data['sex'],
            email=form_data['email'],
            type_of_exam=form_data['exam_type'],
            num_of_subject=form_data['number_of_subject'],
            contact_no=form_data['contact_no'],
            country_of_residence=form_data['country_of_residence'],
            exam_name=admin_event.event_name,
            exam_venue=admin_event.exam_venue,
            eligibility=admin_event.eligibility,
            event_date=admin_event.event_date 
        )
        db.session.add(new_registration)
        db.session.commit()
        flash('You have successfully registered for the exam!', 'success')
        return redirect(url_for('user_inputs'))
    return render_template('root/register.html', admin_event=admin_event)

@app.route('/user_inputs')
def user_inputs():
    # Display all user input from database
    waec_registrations = waec_registration.query.all()
    return render_template('root/user_inputs.html', waec_registrations=waec_registrations)
