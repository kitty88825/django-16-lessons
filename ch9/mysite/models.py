from django.db import models
from django.contrib.auth.models import User

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

# 貼心提醒要先刪掉class User喔！不然會報錯！！！

class Profile(models.Model):
    # models.OneToOneField(User, on_delete=models.CASCADE)和ForeignKey類似，
    # 但是使用這個指定的類別只能是一對一的關係，
    # 也就是每一個Profile「只能」對應到「一個User」
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()

    def __str__(self):
        return f'{self.ddate}({self.user})'
