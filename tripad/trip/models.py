from django.db import models
from django.db.models.fields import EmailField
from django.db.models.query import prefetch_related_objects

# Create your models here.

# 회원
class member(models.Model):
    member_id = models.CharField(max_length=100, verbose_name = '회원_id')
    password = models.CharField(max_length=10, verbose_name = '비밀번호')
    name = models.CharField(max_length = 10, verbose_name = '이름')
    nickname = models.CharField(max_length=100, verbose_name = '닉네임')
    email = models.EmailField(verbose_name = '이메일')
    phone = models.CharField(max_length = 20, verbose_name = '전화번호')

# 여행기획서
class plan(models.Model):
    plan_id = models.CharField(max_length=100, verbose_name = '기획서_id')
    period = models.CharField(max_length = 100, verbose_name = '여행기간')
    personnel = models.CharField(max_length = 20, verbose_name = '여행인원')
    classfication = models.CharField(max_length = 20, verbose_name = '여행종류')

# 장소
class spot(models.Model):
    spot_id = models.CharField(max_length=100, verbose_name = '장소_id')
    plan_id = models.CharField(max_length=100, verbose_name = '기획서_id')
    place = models.CharField(max_length=100, verbose_name = '위치')
    hour = models.DateTimeField(verbose_name = '시간')
    transportation = models.CharField(max_length = 100, verbose_name = '교통수단')
    cost = models.CharField(max_length = 100, verbose_name = '비용')
    memo = models.CharField(max_length = 500, verbose_name = '메모')
    # imageField추가?!

# 공유기획서
class share_people(models.Model):
    plan_id = models.CharField(max_length=100, verbose_name = '기획서_id')
    member_id = models.CharField(max_length=100, verbose_name = '멤버_id')

# 공유멤버
class spot_tag(models.Model):
    spot_id = models.CharField(max_length = 100, verbose_name = '장소_id')
    plan_id = models.CharField(max_length = 100, verbose_name = '기획서_id')
    tag = models.CharField(max_length = 50, verbose_name = '태그내용')

# 게시물
class post(models.Model):
    post_id = models.CharField(max_length = 100, verbose_name = '게시물_id')
    member_id = models.CharField(max_length = 100, verbose_name = '회원_id')
    plan_id = models.CharField(max_length = 100, verbose_name = '기획서_id')
    body = models.TextField(verbose_name = '게시물내용')
    like = models.IntegerField(default = 0, verbose_name = '좋아요개수')
    script = models.IntegerField(defualt = 0, verbose_name = '스크랩개수')
    date =models.DateField(verbose_name = '작성날짜')

# 추천여행지
class recommend(models.Model):
    recommend_spot = models.CharField(max_length = 100, verbose_name = '추천여행지장소')
    explanation = models.CharField(max_length = 500, verbose_name = '설명')