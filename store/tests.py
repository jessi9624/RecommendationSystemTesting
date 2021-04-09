from django.test import TestCase
from store.models.Customer_form import Contact1
from store.models.category import Category

# Create your tests here.
class Basictest(TestCase):
    def setUp(self):
        self.blog=Contact1.objects.create(Relation='father',name='chandan',dob='2021-04-01',category='Earphones')
        self.blog1=Category.objects.create(name='Earphones')
    
    def test_model(self):
        d=self.blog
        self.assertTrue(isinstance(d,Contact1))
        self.assertEqual(str(d),'chandan')
    
    def test_model1(self):
        e=self.blog1
        self.assertTrue(isinstance(e,Category))
        self.assertEqual(str(e),'Earphones') 
     
        