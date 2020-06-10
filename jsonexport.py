import os
import django
import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_webproject.settings')
django.setup()

from blog.models import Post

with open('posts.json') as f:
    posts_json = json.load(f)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()