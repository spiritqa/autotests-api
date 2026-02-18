from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from tools.fakes import get_randome_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_randome_email(),
    password="stringPass",
    lastName="stringLast",
    firstName="stringFirst",
    middleName="stringMiddle"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'

)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_request)

course_client = get_courses_client(authentication_user)
create_courses_request = CreateCourseRequestDict(
    title="Python3.13",
    maxScore=200,
    minScore=30,
    description="Python course",
    estimatedTime="23 year",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']

)
create_courses_response = course_client.create_course(create_courses_request)
print('Create course data', create_courses_response)

exercises_client = get_exercises_client(authentication_user)
create_exercises_request = CreateExercisesRequestDict(
    title="Python start",
    courseId=create_courses_response['course']['id'],
    maxScore=3,
    minScore=2,
    orderIndex=1,
    description="3,2,1...GO",
    estimatedTime="1s"
)
create_exercises_response = exercises_client.create_exercise(create_exercises_request)
print("Create exercise data: ", create_exercises_response)


