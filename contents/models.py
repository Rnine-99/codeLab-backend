from django.db import models


class RepoIssue(models.Model):
    repo_id = models.IntegerField(verbose_name="仓库id")
    issue_id = models.IntegerField(verbose_name="issue id")
    title = models.CharField(verbose_name="title", max_length=256)


class RepoPr(models.Model):
    repo_id = models.IntegerField(verbose_name="仓库id")
    pr_id = models.IntegerField(verbose_name="pr id")
    title = models.CharField(verbose_name="title", max_length=256)
