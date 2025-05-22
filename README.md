# room_rent_django
This is a website for rent purpose using django as a backend


djant/first--> python manage.py runserver
model--> migrantion--> migrate
model provide admin mai opt data added acc to user choice
tables created through model


while creating the migration automatic id key bna dega

for creating 1 step: python manage.py startapp service(models banaan ka liya)

in service there is admin and models.py(class create)


python manage.py makemigrations(model ban jayega)

when fiels are created

python manage.py migrate(table ban jayegi)

then after creating service 
settign .py installed app-->'service'(model.py)


python manage.py createsuperuser(jb django admin ka pwd nhul jao
palayushi293@gmail.com
PALfamily@123
)


thik hai ssb  ho gya ppr utna dikhana jitnaa hai bus uska liya model import in view


template filte supose ki admin ma likth hua tag bna diya toh fir usko execute karna safe template filter
in html file 1\upper  |loewr |capfirst

tinymce
pip install django-tinymce  add setting --> installed-->'tinymce'
# suppose if you want to provide editor html for description so that tage are ther and full editor mode is there then 
# from tinymce.models import HTMLField

# service+Desc=HTMLField()
in models.py in app (Service)


Marquee Tag--> it is like jaise news mai neecha new chlti rhi hai uss type ka


pip install django-autoslug
use of autoslug isthat url mai  automatically about us jaye but  in room rental suppose user click on the certain room detail then slug automatic generate

Pagination means eek tie prr kitni entries dehani hai like in rent particular 3 hi dekhana hia
import library 
from django.core.paginator import Paginator in view