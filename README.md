# aspire_api

endpoints

| endpoints              | ...                                       |
| ---------------------- | ----------------------------------        |
| GET /students          | return all students                       |
| GET /students/id       | return specific student info              |
| GET /students/me       | return current_user for user type student, requires bearer token |
| GET /tutors            | return all tutors                         |
| GET /tutors/id         | return specific tutor info                |
| GET /tutors/me         | return current_user for user type tutor, requires bearer token   |
| GET /subjects          | return all subjects                       |
| GET /subjects/category | return specific subject                   |
| GET /tutor_sessions/   | return all tutor sessions                 |
| GET /tutor_sessions/id | return specific tutor sessions            |
| GET /tutor_sessions/me | return tutor's tutor sessions, requires bearer token             |
| GET /tutor_sessions/tutor/id | return tutor's tutor sessions, requires tutor id             |
| GET /student_tutor_sessions/me | return student's tutor sessions, requires bearer token             |
| GET /student_tutor_sessions/student/id | return student's tutor sessions, requires student id            |

| endpoints                | ...                               | requirements                                                                                                          |
| ------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| POST /login/student              | returns auth_token                | email, password                                                                                                       |
| POST /login/tutor              | returns auth_token                | email, password                                                                                                       |
| POST /students           | request to sign up new student    | email, password, first_name, last_name, gender, age                                                                   |
| POST /students/update-profile-image           | request to update profile picture    | Bearer token, file image                                                                   |
| POST /tutors             | request to sign up new tutor      | email,password, first_name, last_name, gender, age                                                                    |
| POST /tutors/update-profile-image           | request to update profile picture    | Bearer token, file image                                                                   |
| POST /tutor_sessions/new | request to create a tutor session | Bearer token, tutor_id, subject_id, price, title, max_student_capacity, start_time, end_time, duration, host_zoom_url |
| POST /tutor_sessions/delete/id | request to delete a tutor session | Bearer token, tutor_id |
| POST /student_tutor_sessions/enroll | request to enroll a tutor session | Bearer token, tutor_session_id |
| POST /student_tutor_sessions/unenroll | request to unenroll a tutor session | Bearer token, tutor_session_id |
| POST /student_tutor_sessions/update | request to update payment status | Bearer token, student_tutor_session_id |
| POST /payments/new | request to save payment transaction | Bearer token, student_tutor_session_id |
| POST /payments/update | request to update payment transaction | Bearer token, payment_id |


