from django.test import TestCase
from .models import Comments,Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class CommentsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user1 = User(username='jiji')
        self.user1.save()
        self.profile1 = Profile(2,user=self.user1,bio='good')
        self.profile1.save_profile()
        self.me = Image(2,image='image',image_name='mine',image_caption='hhh',user=self.user1,profile=self.profile1)
        self.me.save()
        self.comm= Comments(comment='cool',comment_image=self.me,user=self.user1)
        self.comm.save_comment()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.comm, Comments))

    def test_save_method(self):
        self.comm.save_comment()
        comm = Comments.objects.all()
        self.assertTrue(len(comm)>0)
    
    def test_delete_comment(self):
        Comments.objects.all().delete()
        
    def tearDown(self):
        Comments.objects.all().delete()

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user1 = User(username='jiji')
        self.user1.save()
        self.profile1 = Profile(2,user=self.user1,bio='good')
        self.profile1.save_profile()
        # self.me = Image(2,image='image',image_name='mine',image_caption='hhh',user=self.user1,profile=self.profile1)
        # self.me.save()
        # self.comm= Comments(comment='cool',comment_image=self.me,user=self.user1)
        # self.comm.save_comment()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.profile1, Profile))

    def test_save_method(self):
        self.profile1.save_profile()
        comm = Profile.objects.all()
        self.assertTrue(len(comm)>0)
    
    def test_delete_comment(self):
        Profile.objects.all().delete()
        
    def tearDown(self):
        Profile.objects.all().delete()

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user1 = User(username='jiji')
        self.user1.save()
        self.profile1 = Profile(2,user=self.user1,bio='good')
        self.profile1.save_profile()
        self.me = Image(2,image='image',image_name='mine',image_caption='hhh',user=self.user1,profile=self.profile1)
        self.me.save()
        # self.comm= Comments(comment='cool',comment_image=self.me,user=self.user1)
        # self.comm.save_comment()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.me, Image))

    def test_save_method(self):
        self.me.save_image()
        comm = Image.objects.all()
        self.assertTrue(len(comm)>0)
    
    def test_delete_comment(self):
        Image.objects.all().delete()
        
    def tearDown(self):
        Image.objects.all().delete()