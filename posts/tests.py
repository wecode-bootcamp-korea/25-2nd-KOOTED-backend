import json, jwt

from time             import strftime
from django.test      import TestCase, Client

from my_settings      import SECRET_KEY, ALGORITHM
from users.models     import User
from .models          import Bookmark, Post, PostImage, UserWorkingYear, WorkingYear
from companies.models import CompanyImage, CompanyTag, JobGroup, Job, Company, Tag

class PostsTest(TestCase):
    def setUp(self):
        JobGroup.objects.create(
            id = 1,
            name = '개발',
            image_url = '#FF0000'
        )

        Job.objects.create(
            id = 1,
            name = '프론트 개발자',
            image_url = '#FAECC5',
            job_group_id = 1
        )

        Job.objects.create(
            id = 2,
            name = '백 개발자',
            image_url = '#E4F7BA',
            job_group_id = 1
        )

        Company.objects.create(
            id = 1,
            name = '커코1',
            location = '서울 은평구',
            salary = 31610000.0,
            employee_number = 26,
            description = '빠르게 성장',
        )

        Company.objects.create(
            id = 2,
            name = '커코2',
            location = '서울 은평구',
            salary = 41610000.0,
            employee_number = 36,
            description = '빠르게 성장',
        )

        Tag.objects.create(
            id = 1,
            name = '업계연봉수준',
            color = 'rgb(246, 246, 246)'
        )

        Tag.objects.create(
            id = 2,
            name = '투자',
            color = 'rgb(240, 248, 248)'
        )

        Tag.objects.create(
            id = 3,
            name = '인원성장률',
            color = 'rgb(238, 237, 244)'
        )

        Tag.objects.create(
            id = 4,
            name = '퇴사율',
            color = 'rgb(246, 246, 246)'
        )

        CompanyTag.objects.create(
            tag_id = 1,
            company_id = 1,
        )

        CompanyTag.objects.create(
            tag_id = 2,
            company_id = 1,
        )

        CompanyTag.objects.create(
            tag_id = 3,
            company_id = 2,
        )

        CompanyTag.objects.create(
            tag_id = 4,
            company_id = 2,
        )

        Post.objects.create(
            id = 1,
            title = 'PHP 백엔드 개발자',
            working_year = 3,
            recommender_reward = 5000.000,
            applicant_reward = 5000.000,
            content = 'PHP 백엔드 개발 등등',
            job_id = 2,
            company_id = 1
        )

        Post.objects.create(
            id = 2,
            title = '프론트엔드 개발자1',
            working_year = 0,
            recommender_reward = 10000.0,
            applicant_reward = 10000.0,
            content = '프론트엔드 개발 등등',
            job_id = 1,
            company_id = 1
        )

        Post.objects.create(
            id = 3,
            title = '프론트엔드 개발자2',
            working_year = 0,
            recommender_reward = 15000.0,
            applicant_reward = 15000.0,
            content = '프론트엔드 개발 등등',
            job_id = 1,
            company_id = 2
        )

        Post.objects.create(
            id = 4,
            title = '백엔드 개발자',
            working_year = 0,
            recommender_reward = 5000.000,
            applicant_reward = 5000.000,
            content = '벡엔드 개발 등등',
            job_id = 2,
            company_id = 2
        )

        Post.objects.get(id=1).postimage_set.create(
            id = 1,
            image_url = 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg'
        )

        Post.objects.get(id=1).postimage_set.create(
            id = 2,
            image_url = 'https://cdn.pixabay.com/photo/2013/05/12/18/55/balance-110850_960_720.jpg'
        )

        Post.objects.get(id=2).postimage_set.create(
            id = 3,
            image_url = 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg'
        )

        Post.objects.get(id=2).postimage_set.create(
            id = 4,
            image_url = 'https://cdn.pixabay.com/photo/2013/05/12/18/55/balance-110850_960_720.jpg'
        )

        for year in range(11):
            WorkingYear.objects.create(
                id = year + 1,
                years = year
            )

        User.objects.create(
            id = 1,
            name = '구본욱',
            password = 'asdf',
            email = 'qhsdnr@naver.com',
            mobile_number = '01092280154',
            kakao_id = 1,
            salary = 30000000.0
        )

        User.objects.create(
            id = 2,
            name = '김민호',
            password = 'sdf',
            email = 'alsgh@naver.com',
            mobile_number = '01022222222',
            kakao_id = 2,
            salary = 35000000.0
        )

        User.objects.create(
            id = 3,
            name = '홍승균',
            password = 'asdf1',
            email = 'tmdrbs@naver.com',
            mobile_number = '01033333333',
            kakao_id = 3,
            salary = 40000000.0
        )

        User.objects.create(
            id = 4,
            name = '정민지',
            password = 'asdf12',
            email = 'alswl@naver.com',
            mobile_number = '01044444444',
            kakao_id = 4,
            salary = 45000000.0
        )

        User.objects.create(
            id = 5,
            name = '서동혁',
            password = 'asdf3',
            email = 'ehdgur@naver.com',
            mobile_number = '01055555555',
            kakao_id = 5,
            salary = 50000000.0
        )

        User.objects.create(
            id = 6,
            name = '박미연',
            password = 'asdf23',
            email = 'aldus@naver.com',
            mobile_number = '01066666666',
            kakao_id = 6,
            salary = 55000000.0
        )

        Bookmark.objects.create(
            post_id = 4,
            user_id =1 
        )

        Bookmark.objects.create(
            post_id = 1,
            user_id = 2
        )

        Bookmark.objects.create(
            post_id = 4,
            user_id = 2
        )

        Bookmark.objects.create(
            post_id = 2,
            user_id = 3
        )

        Bookmark.objects.create(
            post_id = 2,
            user_id = 4
        )

        Bookmark.objects.create(
            post_id = 3,
            user_id = 5
        )

        Bookmark.objects.create(
            post_id = 2,
            user_id = 6
        )

        Bookmark.objects.create(
            post_id = 3,
            user_id = 6
        )

        UserWorkingYear.objects.create(
            working_year_id = 1,
            user_id = 1,
            job_id = 2
        )

        UserWorkingYear.objects.create(
            working_year_id = 4,
            user_id = 2,
            job_id = 2
        )

        UserWorkingYear.objects.create(
            working_year_id = 4,
            user_id = 3,
            job_id = 1
        )

        UserWorkingYear.objects.create(
            working_year_id = 5,
            user_id = 4,
            job_id = 1
        )

        UserWorkingYear.objects.create(
            working_year_id = 8,
            user_id = 5,
            job_id = 1
        )

        UserWorkingYear.objects.create(
            working_year_id = 11,
            user_id = 6,
            job_id = 1
        )

    def tearDown(self):
        JobGroup.objects.all().delete()
        Job.objects.all().delete()
        Company.objects.all().delete()
        Post.objects.all().delete()
        Tag.objects.all().delete()
        UserWorkingYear.objects.all().delete()
        CompanyTag.objects.all().delete()
        CompanyImage.objects.all().delete()
        PostImage.objects.all().delete()
        User.objects.all().delete()
        WorkingYear.objects.all().delete()
        Bookmark.objects.all().delete()

    def test_postsview_job_posts_get_success(self):
        created_at1 = Post.objects.get(id=1).created_at
        created_at4 = Post.objects.get(id=4).created_at
        client = Client()
        response = client.get('/posts?job=2')
        self.assertEqual(response.json(),
            {
                'category_list' : [{
                    'id' : 1,
                    'name' : '프론트 개발자',
                    'image_url' : '#FAECC5',
                    'job_group_id' : 1
                    
                }],
                'salary_list' : [{
                    'working_year' : 0,
                    'total_salary' : '30000000.0000000'
                },
                {
                    'working_year' : 3,
                    'total_salary' : '35000000.0000000'
                },],
                'result' : [{
                    'id' : 4,
                    'title' : '백엔드 개발자',
                    'reward' : '10000.000',
                    'company_name' : '커코2',
                    'created_at' : created_at4.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3],
                    'tag' : [{'id' : 3, 'name' : '인원성장률', 'color' : 'rgb(238, 237, 244)'},
                             {'id' : 4, 'name' : '퇴사율', 'color' : 'rgb(246, 246, 246)'}],
                    'working_year' : 0,
                    'count' : 2, 
                    'image_url' : None
                },
                {
                    'id' : 1,
                    'title' : 'PHP 백엔드 개발자',
                    'reward' : '10000.000',
                    'company_name' : '커코1',
                    'created_at' :  created_at1.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3],
                    'tag' : [{'id' : 1, 'name' : '업계연봉수준', 'color' : 'rgb(246, 246, 246)'},
                             {'id' : 2, 'name' : '투자', 'color' : 'rgb(240, 248, 248)'}],
                    'working_year' : 3,
                    'count' : 1, 
                    'image_url' : 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg'
                },]
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_postdetailview_get_success(self):
        client = Client()
        response = client.get('/posts/1')
        self.assertEqual(response.json(),
            {
                'result' : {
                    'id' : 1,
                    'title' : 'PHP 백엔드 개발자',
                    'recommender_reward' : '5000.000',
                    'applicant_reward' : '5000.000',
                    'company_name' : '커코1',
                    'content' : 'PHP 백엔드 개발 등등',
                    'deadline' : None,
                    'tag' : [{'id' : 1, 'name' : '업계연봉수준', 'color' : 'rgb(246, 246, 246)'},
                             {'id' : 2, 'name' : '투자', 'color' : 'rgb(240, 248, 248)'},],
                    'location' : '서울 은평구',
                    'count' : 1,
                    'image_url' : [{'id' : 1, 'image_url' : 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg'},
                                   {'id' : 2, 'image_url' : 'https://cdn.pixabay.com/photo/2013/05/12/18/55/balance-110850_960_720.jpg'}]
                }
            }
        )

    def test_postsview_posts_get_post_does_not_exist(self):
        client = Client()
        response = client.get('/posts/5')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'POST_DOES_NOT_EXIST'
            }
        )
    
    def test_bookmark_post_success(self):
        client = Client()
            
        headers = {'HTTP_Authorization' : jwt.encode({'id' : 1}, SECRET_KEY, algorithm=ALGORITHM)}
        
        bookmark = {
            'post_id' : 1,
        }
        response = client.post('/posts/bookmarks', json.dumps(bookmark), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),
            {
                'message' : 'CREATED'
            }
        )

    def test_bookmark_delete_success(self):
        client = Client()
        headers = {'HTTP_Authorization' : jwt.encode({'id' : 1}, SECRET_KEY, algorithm=ALGORITHM)}
        bookmark = {
            'post_id' : 4,
        }
        response = client.delete('/posts/bookmarks', json.dumps(bookmark), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )