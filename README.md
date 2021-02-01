# aspire_api

endpoints

| endpoints              | ...                                       |
| ---------------------- | ----------------------------------        |
| GET /students          | return all students                       |
| GET /students/id       | return specific student info              |
| GET /students/me       | return current_user for user type student |
| GET /tutors            | return all tutors                         |
| GET /tutors/id         | return specific tutor info                |
| GET /tutors/me         | return current_user for user type tutor   |
| GET /subjects          | return all subjects                       |
| GET /subjects/category | return specific subject                   |
| GET /tutor_sessions/   | return all tutor sessions                 |
| GET /tutor_sessions/id | return specific tutor sessions            |
| GET /tutor_sessions/me | return current_user tutor sessions        |

| endpoints                | ...                               | requirements                                                                                                          |
| ------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| POST /login/student              | returns auth_token                | email, password                                                                                                       |
| POST /login/tutor              | returns auth_token                | email, password                                                                                                       |
| POST /students           | request to sign up new student    | email, password, first_name, last_name, gender, age                                                                   |
| POST /tutors             | request to sign up new tutor      | email,password, first_name, last_name, gender, age                                                                    |
| POST /tutor_sessions/new | request to create a tutor session | Bearer token, tutor_id, subject_id, price, title, max_student_capacity, start_time, end_time, duration, host_zoom_url |
| POST /tutor_sessions/delete/id | request to delete a tutor session | Bearer token, tutor_id |
