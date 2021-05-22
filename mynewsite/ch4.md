# Ch4
查看 migrations 轉換成 SQL 指令
```
python manage.py sqlmigrate $APP_NAME $Migrate_file
```
```
python manage.py sqlmigrate mysite 0001
```


ORM
---
檢查庫存中是否有 SONY 的二手機
```
Product.objects.filter(name__contains='SONY').exists()
```
