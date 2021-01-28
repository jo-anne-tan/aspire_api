# aspire_api

endpoints

| endpoints              | ...                                |
| ---------------------- | ---------------------------------- |
| GET /students          | return all students                |
| GET /students/id       | return specific student info       |
| GET /tutors            | return all tutors                  |
| GET /tutors/id         | return specific tutor info         |
| GET /subjects          | return all subjects                |
| GET /subjects/id       | return specific subject            |
| GET /tutor_sessions/me | return current_user tutor sessions |

| endpoints                | ...                               | requirements                                                                                                          |
| ------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| POST /login              | returns auth_token                | email, password                                                                                                       |
| POST /students           | request to sign up new student    | email, password                                                                                                       |
| POST /tutors             | request to sign up new tutor      | email,password                                                                                                        |
| POST /tutor_sessions/new | request to create a tutor session | Bearer token, tutor_id, subject_id, price, title, max_student_capacity, start_time, end_time, duration, host_zoom_url |
