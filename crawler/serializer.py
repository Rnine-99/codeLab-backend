from rest_framework import serializers

from crawler.models import Repo


class serializers_repo(serializers.ModelSerializer):
    class Meta:
        model = Repo
        exclude = ['root_dir']
