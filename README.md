# 🎆 KOOTED

## ✍🏼 Introduction

- [Wanted 사이트](https://www.wanted.co.kr/newintro) 사이트 클론 프로젝트
- 카테고리별 채용 공고를 확인하고, 이력서를 작성하여 원하는 회사에 지원할 수 있는 사이트

## 👩‍👩‍👧‍👦 팀 소개

- 팀명 : Kooted 

- 개발 기간 : 2021.10.18 ~ 2021.10.29

- 개발 인원

  - FrontEnd : 정민지, 박미연, 서동혁, 홍승균
  - BackEnd  : 구본욱, 김민호

  

## 🎬 [프로젝트 시연 영상](https://www.youtube.com/watch?v=IAU3L0hZchE&t=2s)

## ⚙️ 적용기술

- **Frontend**: `JSX` `React(CRA)`, `React Hook`, `Sass` (Library: `React-router-DOM`)
- **Backend**: `Python`, `Django Web Framework`, `AWS`, `MySQL`, `JWT`
- **Common**: 버전관리 - `Git & GitHub` , 소통 - `Slack` , 일정관리 - `Trello` ([Kooted Trello 페이지](https://trello.com/b/7H4voa32/kooted))

## 💾 데이터베이스 

![모델링 최신](https://user-images.githubusercontent.com/79758688/139999392-70b40c87-f9f7-4f5e-9fde-ab7b0e5d7629.png)



## 📒 구현기능

### Front-end 

#### 정민지

- 메인(헤더, 바디, 푸터) 페이지
- 마이페이지 리스트업
- 이력서 레이아웃 / CRUD 관리

#### 박미연

- 채용 공고 목록 페이지
- 목록 데이터 필터링 정렬
- 연봉 데이터 수치화

#### 서동혁

- 채용공고 상세 페이지
- 카카오 지도 API
- 이력서 선택하여 지원하기 후 저장

#### 홍승균

- 로그인 modal, 회원가입 페이지
- 카카오 소셜로그인 API


### Back-end

#### 공통

- ERD modeling
- CSV 파일 샘플 데이터 작성
- AWS 배포

#### 구본욱

- 채용 관련, 마이페이지 백엔드 데이터 리스트업
- 채용공고 조회, 상세페이지 View 작성
- 북마크 생성, 삭제 View 작성

#### 김민호

- 카카오 로그인 API를 이용한 소셜로그인 기능 구현
- 이력서 작성, 조회, 수정, 삭제 View 작성


## ⌨️ EndPoint

- KakaoSignInView : `GET` /users/kakao
- PostsView : `GET` /posts
- PostsDetailView : `GET` /posts/<int:post_id>
- BookMarkView : `POST`, `DELETE` /posts/bookmarks

- ResumeView : `POST`, `GET`, `DELETE`, `PUT`
- AllResumeView : `GET` 
- ApplicationView : `POST` 




## ❗️ Reference

- 이 프로젝트는 [Wanted 사이트](https://www.wanted.co.kr/newintro) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
