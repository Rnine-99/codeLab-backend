from django.db import models


class RepoIssue(models.Model):
    repo_id = models.IntegerField(verbose_name="仓库id")
    issue_id = models.IntegerField(verbose_name="issue id")
    title = models.CharField(verbose_name="title", max_length=256)
    status = models.BooleanField(verbose_name="status")


class RepoPr(models.Model):
    repo_id = models.IntegerField(verbose_name="仓库id")
    pr_id = models.IntegerField(verbose_name="pr id")
    title = models.CharField(verbose_name="title", max_length=256)
    status = models.BooleanField(verbose_name="status")

class RepoContributers(models.Model):
    repo_id = models.IntegerField(verbose_name="仓库id")
    contributer_id = models.IntegerField(verbose_name="contributer id")
    contributer_name = models.CharField(verbose_name="contributer name", max_length=256)
    contributer_html_url = models.CharField(verbose_name="contributer html url", max_length=256)
    contributer_type = models.CharField(verbose_name="contributer type", max_length=256)
    contributer_contributions = models.IntegerField(verbose_name="contributer contributions")

