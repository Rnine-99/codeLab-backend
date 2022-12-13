from rest_framework import serializers

from contents.models import *


class serializers_issue(serializers.ModelSerializer):
    class Meta:
        model = RepoIssue
        fields = ['pr_id', 'title']


class serializers_pr(serializers.ModelSerializer):
    class Meta:
        model = RepoPr
        fields = ['pr_id', 'title']


class serializers_contributers(serializers.ModelSerializer):
    class Meta:
        model = RepoContributers
        fields = ['id', 'contributer_name', 'contributer_html_url', 'contributer_type', 'contributer_contributions']
