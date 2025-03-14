import random
import requests
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import BlogModel, CommentModel
from faker import Faker
from django.core.files.base import ContentFile

fake = Faker()

class Command(BaseCommand):
    help = 'Create fake blog posts and comments'

    def handle(self, *args, **kwargs):
        self.create_users()
        self.create_blogs()
        self.create_comments()

    def create_users(self):
        for _ in range(5):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )

    def create_blogs(self):
        users = User.objects.all()
        for _ in range(20):
            blog = BlogModel.objects.create(
                title=fake.sentence(),
                content=fake.paragraph(nb_sentences=10),
                author=random.choice(users),
                views=random.randint(0, 100)
            )
            # Add random image from picsum.photos
            image_url = 'https://picsum.photos/800/600'
            response = requests.get(image_url)
            if response.status_code == 200:
                blog.media.save(f'{blog.id}.jpg', ContentFile(response.content), save=True)

    def create_comments(self):
        blogs = BlogModel.objects.all()
        users = User.objects.all()
        for _ in range(50):
            CommentModel.objects.create(
                blog=random.choice(blogs),
                user=random.choice(users),
                text=fake.sentence()
            )