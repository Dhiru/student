# student

Installation: 

1. Installing required packages and its dependencies

    sudo apt-get install python git python-virtualenv python-pip mongodb

2. Get latest code

    git clone https://github.com/Dhiru/student.git

3. Set up virtual environment

    1. cd student_review
    2. virtualenv --system-site-packages
    3. source bin/activate
    4. ./bin/pip install -r requirements.txt (This takes time)

4. Run the following commands:
    
   1. python manage.py filldb 
   2. python manage.py runserver
