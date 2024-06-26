from django.db import models

from users.models import Teacher, Schoolboy


class Laboratory(models.Model):
    class Meta:
        db_table = 'laboratories'
    
    title = models.CharField(verbose_name='Наименование', max_length=20, unique=True)
    img = models.CharField(verbose_name='Картинка', max_length=20)

    def __repr__(self):
        return self.title
        
    def __str__(self):
        return self.title    


class Task(models.Model):
    class Meta:
        db_table = 'tasks'
    
    number = models.CharField(max_length=20)
    description = models.TextField()
    solution = models.CharField(max_length=200)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    start_value = models.CharField(max_length=100, null = True)
    end_value = models.CharField(max_length=100, null = True) #default=None)
    
    def __repr__(self):
        return f'{self.number}: {self.description}'
        
    def __str__(self):
        return f'{self.number}: {self.description}'


class TaskSolution(models.Model):
    class Meta:
        db_table = 'tasks_solution'
    
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(null = True)
    solution = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=20) 
    grade = models.PositiveSmallIntegerField(null = True)
    scale = models.PositiveSmallIntegerField(default=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    user = models.ForeignKey(Schoolboy, on_delete=models.CASCADE)