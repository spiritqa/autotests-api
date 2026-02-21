from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakes import get_randome_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_randome_email(),
    password="stringPass",
    last_name="stringLast",
    first_name="stringFirst",
    middle_name="stringMiddle"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestSchema(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'

)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_request)

course_client = get_courses_client(authentication_user)
create_courses_request = CreateCourseRequestSchema(
    title="Python3.13",
    max_score=200,
    min_score=30,
    description="Python course",
    estimated_time="23 year",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id

)
create_courses_response = course_client.create_course(create_courses_request)
print('Create course data', create_courses_response)

exercises_client = get_exercises_client(authentication_user)
create_exercises_request = CreateExercisesRequestSchema(
    title="Python start",
    course_id=create_courses_response.course.id,
    max_score=3,
    min_score=2,
    order_index=1,
    description="3,2,1...GO",
    estimated_time="1s"
)
create_exercises_response = exercises_client.create_exercise(create_exercises_request)
print("Create exercise data: ", create_exercises_response)


