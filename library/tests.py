from django.test import TestCase

# Create your tests here.
from datetime import datetime,timedelta
days = datetime.now() - (datetime.now()+timedelta(days=30) )
print(days.days)