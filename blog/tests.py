from django.test import TestCase
from .models import Post ,Category
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class BlogModelTest(TestCase):
    
    def post_create(self):
        author = User.objects.create(username='ahmed',password='12345678')
        category = Category.objects.create(name='test category')
        
        
        return Post.objects.create(
            auther=author ,
            title='django testing',
            tags='django',
            description='test description',
            category=category,
        )



    def test_model_str(self):
        post=self.post_create()
        self.assertEqual(post.__str__(),post.title)
        
        
class BlogViewTest(TestCase):
    
    #def test_blog_url(self):
     #   response = self.client.get('/blog/')
       # self.assertEqual(response.status_code,200) 
       
       
    
           
       
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:post_list')) 
        self.assertTemplateUsed(response,'blog/post_list.html')       