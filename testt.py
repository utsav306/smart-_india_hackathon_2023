from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('personal_details.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['inputUsername']
        first_name = request.form['inputFirstName']
        last_name = request.form['inputLastName']
        university_name = request.form['inputOrgName']
        gender = request.form['selectedGender']
        location = request.form['inputLocation']
        email = request.form['inputEmailAddress']
        phone_number = request.form['inputPhone']
        birthday = request.form['inputBirthday']
        course_enrolled = request.form['inputPhone']
        topics_interested = request.form['inputBirthday']
        level = request.form['selectedLevel']

        # Do something with the data (e.g., save to a database)
        # For now, just print the data
        print(f"Username: {username}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"University Name: {university_name}")
        print(f"Gender: {gender}")
        print(f"Location: {location}")
        print(f"Email: {email}")
        print(f"Phone Number: {phone_number}")
        print(f"Birthday: {birthday}")
        print(f"Course Enrolled: {course_enrolled}")
        print(f"Topics Interested: {topics_interested}")
        print(f"Level: {level}")

        # Return a response (you can customize this based on your needs)
        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
