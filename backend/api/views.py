from .models import CustomUser, Subject, AvailableTiming
from .serializers import UserSerializer, SubjectSerializer, AvailableTimingSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import json
from collections import defaultdict


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    # def perform_create(self, serializer):
    #     print(self.request.data)
        # serializer.save(user=self.request.user, status=Invoice.SENT)

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id) 


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return super().get_queryset().filter(teacher=user)
        elif user.is_student:
            return Subject.objects.all()


class AvailableTimingViewSet(viewsets.ModelViewSet):
    queryset = AvailableTiming.objects.all()
    serializer_class = AvailableTimingSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return AvailableTiming.objects.filter(teacher=user)


def get_subs(request):
    set = Subject.objects.order_by('name').values('name').distinct()
    return JsonResponse(list(set), safe=False)


def get_query_results(request):
    # print(request.GET['courses'])
    # print(request.GET['time'])
    subs = request.GET['courses'].split(',')
    time = request.GET['time']
    final_dict = {}
    for sub in subs:
        _ = {}
        teachers = Subject.objects.filter(name=sub).values('teacher__username')
        for i in teachers:
            timing = AvailableTiming.objects.filter(teacher__username=i['teacher__username']).values('data')
            time_dict = []
            try:
                for j in timing[0]['data'].items():
                    if time in j[1]:
                        time_dict.append(j[0])
                if len(time_dict) > 0:
                    _[i['teacher__username']] = time_dict
            except:
                pass
        final_dict[sub] = {**_}
    obj_ = json.dumps(final_dict, default=set_default)
    # print(obj_)
    return JsonResponse(obj_, safe=False)
    

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError