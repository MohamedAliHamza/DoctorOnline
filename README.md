# Doctor Online Reservation System
 <img src="https://img.icons8.com/office/16/000000/booking.png"/> This is a reservation system API based on Django & Django REST Framework where the patient can reserve an appointment with a specific doctor.
 
 ## Setup & Launch
```
1. git clonehttps://github.com/MohamedAliHamza/DoctorOnline.git

2. cd DoctorOnline

3. pip install virtualenvwrapper-win

4. mkvirtualenv venv

5. workon venv

6. pip install -r requirements.txt

7. python manage.py migrate

8. python manage.py runserver
```
## API Swagger Docs 
```
 http://127.0.0.1:8000/api/v1/docs/
```
* The First Step To Access API :

    * ` Register ` As A Doctor :

        ```json
        URL: http://127.0.0.1:8000/api/v1/docs/#/user/user_register_create
        {
           "email": "doctor1@doctoronline.com",
           "password": "12345",
           "type": "DOCTOR"
       }
        ```   
    * ` Register ` As A Patient :

        ```json
        URL: http://127.0.0.1:8000/api/v1/docs/#/user/user_register_create
        {
           "email": "patient1@doctoronline.com",
           "password": "12345",
           "type": "PATIENT"
       }
        ```     

* The Second Step To Access API :

    * ` Log in ` As A Doctor :

        ```json
        URL: http://127.0.0.1:8000/api/v1/docs/#/user/user_login_doctor_create
        {
           "email": "doctor1@doctoronline.com",
           "password": "12345"
       }
        ```   
    * ` Log in ` As A Patient :

        ```json
        URL: http://127.0.0.1:8000/api/v1/docs/#/user/user_login_patient_create
        {
           "email": "patient1@doctoronline.com",
           "password": "12345"
       }
        ```     

* The Third Step To Access API :
    * Add ` "access":..... ` jwtAuth (http, Bearer)

___

## Doctor Domin : 
   * Register
   * Log in
   * Update Account Info
   * Add Clinic `CRUD`
   * Get His Reservation
   * Get All Clinics
 
 
## Patient Domin : 
   * Register
   * Log in
   * Update Account Info
   * Make Reservation `CRUD`
   * Get His Reservation
   * Get All Clinics
