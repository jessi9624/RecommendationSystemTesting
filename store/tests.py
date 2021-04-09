from django.test import TestCase
from store.models.Customer_form import Contact1
from store.models.category import Category
from store.models.customer  import Customer

# Create your tests here.
class Basictest(TestCase):
    def setUp(self):
        self.blog=Contact1.objects.create(Relation='father',name='chandan',dob='2021-04-01',category='Earphones')
        self.blog1=Category.objects.create(name='Earphones')
        self.sign=Customer.objects.create(first_name='chandan',last_name='kamal',phone='1234567891',dob='2021-03-01',email='test1@gmail.com',password='123456')
    
    def test_model(self):
        d=self.blog
        self.assertTrue(isinstance(d,Contact1))
        self.assertEqual(str(d),'chandan')
    
    def test_model1(self):
        e=self.blog1
        self.assertTrue(isinstance(e,Category))
        self.assertEqual(str(e),'Earphones') 
    def test_model2(self):
        f=self.sign
        self.assertTrue(isinstance(f,Customer))
        self.assertEqual(str(f),'Customer object (1)')
     
    
        
