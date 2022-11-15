from django.db import models


# Create your models here.
class Repo(models.Model):
    owner = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stargazers_count = models.IntegerField()
    forks_count = models.IntegerField()
    open_issues_count = models.IntegerField()
    subscribers_count = models.IntegerField()
    git_url = models.CharField(max_length=100)
    clone_url = models.CharField(max_length=100)
    ssh_url = models.CharField(max_length=100)
    root_dir = models.TextField(verbose_name="根目录")

    def __str__(self):
        return self.full_name
