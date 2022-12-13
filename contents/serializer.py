from rest_framework import serializers

from contents.models import *


class serializers_issue(serializers.ModelSerializer):
    class Meta:
        model = RepoIssue
        fields = ['id', 'title']


class serializers_pr(serializers.ModelSerializer):
    class Meta:
        model = RepoPr
        fields = ['id', 'title']
