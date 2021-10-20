import json, jwt
from django.http import response
from django.test import TestCase, Client
from unittest.mock import MagicMock, patch
from users.models import User
from .models  import Resume, Career, Skill
from my_settings import SECRET_KEY, ALGORITHM
class ResumeTest(TestCase):
  def setUp(self):
    global headers
    access_token = jwt.encode({'id' : 1}, SECRET_KEY, algorithm = ALGORITHM)
    headers      = {'HTTP_Authorization' : access_token}
    User.objects.create(
      id = 1,
      email = 'kimminho@gmail.com',
      name = '김민호',
      kakao_id = '123123123'
    )
    Resume.objects.create(
      id = 1,
      title = '제목1',
      status = '작성중',
      introduction = '소개글소개글소개글소개글소개글소개글',
      college = '위코드대학교',
      resume_file_url = 'asdfasdfasdfasdfsafasdfasdf',
      user = User.objects.get(id=1)
    )
    Career.objects.create(
      id = 1,
      company_name = 'wecode',
      duty = '신입개발자',
      date_of_joining = '2021-11-11',
      date_of_resigning = '2022-11-11',
      in_office = True,
      resume = Resume.objects.get(id=1)
    )
    Skill.objects.create(
      id = 1,
      name = '파이썬',
      resume = Resume.objects.get(id=1),
      user = User.objects.get(id=1)
    )
  def tearDown(self):
    User.objects.all().delete()
    Resume.objects.all().delete()
    Career.objects.all().delete()
  def test_resume_create_success(self):
    client = Client()
    data = {
      'id' : 1,
      'title' : '제목1',
      'status' : '작성중',
      'introduction' : '소개글소개글소개글소개글소개글소개글',
      'college' : '위코드대학교',
      'resume_file_url' : 'asdfasdfasdfasdfsafasdfasdf', #이게 뭘 따라해야하는건지....
      'careers' : [
        {
          'id' : 1,
          'company_name' : 'wecode',
          'duty' : '신입개발자',
          'date_of_joining' : '2021-11-11',
          'date_of_resigning' : '2022-11-11',
          'in_office' : True
        }
      ],
    'skills' : [{ 'name' : '파이썬' }]
    }
    response = client.post('/resume', json.dumps(data), content_type='application/json', **headers)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.json(), {'message' : 'CREATED'})
  def test_resume_get_success(self):
    client = Client()
    response = client.get('/resume/1', **headers)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {
      'MESSAGE' : 'SUCCESS',
      'resume_info' : {
        'id' : 1,
        'introduction' : '소개글소개글소개글소개글소개글소개글',
        'title' : '제목1',
        'status' : '작성중',
        'college' : '위코드대학교',
        'careers' : [{
          'id' : 1,
          'company_name' : 'wecode',
          'duty' : '신입개발자',
          'date_of_joining' : '2021-11-11',
          'date_of_resigning' : '2022-11-11',
          'in_office' : True
        }
      ],
        'skills' : [{ 'name' : '파이썬' }]
    },
    'user_info' : {
        'name' : '김민호',
        'email' : 'kimminho@gmail.com',
        'mobile_number' : None,
      }, },)
  def test_resume_delete_success(self):
    client = Client()
    response = client.delete('/resume/1', **headers)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(),{'MESSAGE':'SUCCESS'})
  def test_resume_put_success(self):
    client = Client()
    data = {
      'id' : 1,
      'introduction' : '수정된 소개글',
      'college' : '수정된 대학교',
      'status' : '수정중',
      'title' : '수정된 제목',
      'careers' : [
        {
        'company_name' : 'wecode',
        'duty' : '신입개발자',
        'date_of_joining' : '2021-11-11',
        'date_of_resigning' : '2022-11-11',
        'in_office' : True }
      ],
      'skills' : [{'name' : '파이썬'}]
    }
    access_token = jwt.encode({'id' : 1}, SECRET_KEY, algorithm = ALGORITHM)
    response = client.put('/resume/1', **{'HTTP_Authorization' : access_token, 'data' : data}, content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(),{'MESSAGE':'SUCCESS'})