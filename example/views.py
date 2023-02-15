from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET'])
def HelloAPI(request):
    return  Response("hello world")

# 함수를 꾸며주는 데코레이터
# 해당 함수에 대한 성격을 표시해주는 표기법

# HelloAPI라는 함수가 GET 요청을 받을  수 있는 API 라는 것을 @api_view 표기법으로 나타냄
# Django안에서 RESTful API서버를 쉽게 구축할 수 있도록 도와주는 오픈소스
#
# request 객체의 경우, 요청을 효과적으로 처리 해주고 인증 기능 구현 시 편리함 제공
# 요청이 어떤 타입인지 ?  -> request.method
# 요청이 어떤 데이터를 가졌는지 ? -> request.data
# 요청 결과 반환  request.status
# HTTP_200_OK -> 응답 정상



