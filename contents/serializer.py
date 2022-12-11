from rest_framework import serializers

from contents.models import *


class serializers_issue(serializers.ModelSerializer):
    class Meta:
        model = RepoIssue


class serializers_pr(serializers.ModelSerializer):
    class Meta:
        model = RepoPr
