from myapp.models import Students, StudentClass
from django.db.models.signals import post_save

def display_signals(sender, instance, **kwrgs):
    print ("start signals")
    st_obj = Students.objects.get(id = instance.id)
    n_obj = StudentClass()
    n_obj.s_class = st_obj.name
    n_obj.save()
    print ("Done!")
post_save.connect(display_signals, sender = Students)