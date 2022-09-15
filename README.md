# Python-Tutorial Django for windows (Instruction guide)

These sessions are inspired and created using folowing refernce materials [^1]
These are for my students for refer them when they needed and I would like you to play around with these instrctions 
## Session 1 

### Initial Setup of Project and App

1. Place your working folder is in convenient location name it DjangoProject.
    - *C:\Users\dell\Desktop\Python_Tutorial\Django Tutorial*.

2. Install virtual environment with prefferd name I used chapter1.
    - *python -m venv chapter1*.


3. Go to windows powershell by typing *powershell* in **command prompt** then enter following command.
    - *set -ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser*.


4. Activate virtual Environment by entering below command on powershell
    - *.\chapter1\Scripts\Activate.ps*.


5. Do not go inside virtual environment and install Django using following Command
    - *python -m pip install django ~=4.1.1 (Latest version) *.


6. Create Django Project I use name django_project 
    - *django-admin startproject django_project . (Do not forget space and dot after command)*.


7. You are all set to run the project you can run that typing following command to cmd or powershell ignore any error message for now
    - *python manage.py runserver*
    - Inser Image Later


8. launch your browser and type 127.0.0.1:8000 or localhost:8000 and check below page is launch 
    - *Will insert Image Later*

9. To Exit press Ctrl+C
    - *.\chapter1\Scripts\Activate.ps*.

10. Enter below command to get rid of pesky error messages 
    - *python manage.py migrate*.

11. After that your folder must be like this  
    - Add image of old folder .
    - Add image of new folder .

12. You have created your web project it could contain multiple apps   

13. Lets create our first Django app I choose pages   
    - *python manage.py startapp pages*.

14. You need to go to project folder which is in our example **django_projects** go to settings.py file and add following new line   
    - Add Image Later.

15. Go to application folder our example **pages** go to view.py and add below new lines   
    - Add Image later.

16. Create new file name urls.py in **pages** folder  and add below lines 
    - Add Image Later.

17. Modify **django_project** project file urls.py file as below  
    - Add Image Later.

18. You are all set to run the app you can run that typing following command to cmd and you will not received error messages like before 
    - *python manage.py runserver*
    - Inser Image Later


19. launch your browser and type 127.0.0.1:8000 or localhost:8000 and check below page is launch 
    - *Will insert Image Later*



### Lets Play with GitHub
