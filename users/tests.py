import jwt

from django.test   import TestCase, Client
from unittest.mock import MagicMock, patch

from users.models  import User
from my_settings   import SECRET_KEY, ALGORITHM

class KakaoSignInTest(TestCase):
  def setUp(self):
    User.objects.create(
      id       = 1,
      email    = 'kimminho2@gmail.com',
      name     = '김민호',
      kakao_id = '123123123'
    )

  def tearDown(self):
    User.objects.all().delete()

  @patch('users.views.requests')
  def test_kakao_signin_success(self, mocked_requests):
    client = Client()

    class MockedResponse:
      def json(self):
        return {
            'id'            : '123123123',
            'kakao_account' : {
              "email" : 'kimminho2@gmail.com',
              "profile"       : {'nickname' : '김민호'}
              }
        }
    
    mocked_requests.get = MagicMock(return_value = MockedResponse())
    headers             = {'HTTP_Authorization' : '가짜 access_token'}
    response            = client.get('/users/kakao', **headers)
    access_token        = jwt.encode({'user' : 1}, SECRET_KEY, algorithm = ALGORITHM)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {'access_token' : access_token})