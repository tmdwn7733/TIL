from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=32, verbose_name="태그명")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.tag_name
        
    class Meta:
        db_table="tb_tag"