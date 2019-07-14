from django.db import models

# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透露身份的人', verbose_name='暱稱')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10, verbose_name='刪除密碼')
    pub_time = models.DateTimeField(auto_now=True, verbose_name='修改時間')
    enabled = models.BooleanField(default=False, verbose_name='顯示狀態')

    def __str__(self):
        return self.message


class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name