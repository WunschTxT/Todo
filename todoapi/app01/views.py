from rest_framework.views import APIView

from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import TodoSerializer
from app01 import models

import json


class TodoAPIView(APIView):

    def get(self, request, *args, **kwargs):
        todo_list = models.Todo.objects.filter(is_finish=0)
        print(todo_list)
        res = TodoSerializer(instance=todo_list, many=True).data
        return Response( res)

    def post(self, request, *args, **kwargs):
        todo_obj = TodoSerializer(data=request.data)
        if todo_obj.is_valid():
            todo_obj.save()
            return Response({
                'status': 1,
                'msg': 'ok',
            })
        return Response({
            'status': 1,
            'msg': 'ok',
        })

    def patch(self, request, *args, **kwargs):
        print(isinstance(request.data, dict))
        data = request.data
        pk = kwargs.get('pk')
        if pk and isinstance(data, dict):
            print('jinnfa')
            pks = [pk, ]
            data = [data, ]
        elif not pk and isinstance(data, list):
            pks = []
            for dic in data:
                pk = dic.pop('id', None)
                if pk:
                    pks.append(pk)
                else:
                    return Response({
                        'status': 2,
                        'msg': '参数错误!'
                    })
        else:
            return Response({
                'status': 2,
                'msg': '参数错误!'
            })
        objs = []
        new_data = []
        for index, pk in enumerate(pks):
            try:
                todo_obj = models.Todo.objects.get(id=pk)
                objs.append(todo_obj)
                new_data.append(data[index])
            except:
                continue
        todo_ser = TodoSerializer(instance=objs, data=new_data, partial=True, many=True)
        todo_ser.is_valid(raise_exception=True)
        todo_objs = todo_ser.save()

        return Response({
            'status': 1,
            'msg': 'ok',
            'results': TodoSerializer(todo_objs, many=True).data
        })

    def edit(requset):
        pass
