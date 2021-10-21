from django.test   import TestCase, Client
from unittest.mock import MagicMock, patch

from users.models  import User

class KakaoSignInTest(TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    User.objects.all().delete()

  @patch("users.views.requests")
  def test_kakao_signin_success(self, mocked_requests):
    client = Client()

    class MockedResponse:
      def json(self):
        return {
            "id" : "123123123",
            "kakao_account" : 
            {
                "profile" : {"nickname" : "김민호"},
                "email"   : "kimminho@gmail.com"
            }
        }
    
    mocked_requests.get = MagicMock(return_value = MockedResponse())
    headers             = {"HTTP_Authorization" : "가짜 access_token"}
    response            = client.get("/users/kakao", **headers)

    self.assertEqual(response.status_code, 200)