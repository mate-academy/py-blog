# Blog

In this task, you will create a simple `Blog` project from start to end.

Let's go through all the steps:

1. Create a virtual environment, activate it, and install django via pip.
2. Start project `blog_system` inside the current directory (add . at the end of the command).
3. Inside `py-blog` start application `blog`.
4. Inside `blog/models.py` create models according to this diagram:

   ![models-diagram](https://mate-academy-images.s3.eu-central-1.amazonaws.com/py-drf-forms-blog-task-2.png)

5. Edit `admin.py`:
    - Register all your models in the admin.
    - Unregister `Group` (you can make it with `admin.site.unregister(Group)` by importing `Group` from `django.contrib.auth.models`).
    - Do the filtering and searching in any way you think is logical.
6. Make migrations and migrate.
7. Use `python manage.py test` to run tests.
8. Use the following command to load prepared data from the fixture to test and debug your code:
   ```python manage.py loaddata blog_system_db_data.json```

   _Feel free to add more data using the admin panel if needed._
9. Inside `blog_system.urls` add a path to the `blog.urls`. Don't forget to specify the namespace.
10. Inside `blog.urls` create a path for the home page. Give this path the name `index`.
11. Inside `blog.views` create a view for the `index` url. This view returns a list of all posts, in descending order by `created_time`.
12. Before creating a template, you have to create styles. Create a directory `static` next to the directory `blog`. Inside this directory create a file with the following path `css/styles.css`. Don't forget to do all the necessary steps so that Django can serve these static files.
13. Create a directory `templates` next to the directory `blog`. There you will store templates for pages. Edit settings so that engine knows where to look for template source files.
14. Create a template for the main page. On this page, make it so that a list of all posts is displayed. The title and content were displayed, the author was visible when this post was created and the number of comments on the post. Make the post's title a link to the detailed page, which you would implement further.
15.  Add pagination for the main page. Set **5** posts on one page by default.
16. Create a `PostDetailView` view that returns detailed information about the post by the `id` field.
17. Add a template for this page and url with a path `posts/pk/` and name `post-detail`.
18. On the post detail page, display a list of post comments below this post.
19. Under the list of comments, add a form that allows you to create a new comment to the post. 

   **Please note**: only authorized users can post comments. If an anonymous user tries to create a new comment, the form must be invalid.

20. Use crispy forms in your forms to make the website more beautiful. 
21. Use `python manage.py test` to run tests.
22. Don't forget to add the `.gitignore` file before pushing. Don't push a lot of extra files(`venv`, `pycache`, `.idea`, etc.).


### Note: Attach screenshots of all created or modified pages to pull request.
1. Attach screenshots to the comment, NOT in the commit.
2. It's important to attach images not links to them. 

## Example of the post detailed page

**Notice**: that example is not a reference! You can make this page in another way. 

![post-detailed-page-reference-1](https://mate-academy-images.s3.eu-central-1.amazonaws.com/py-reference-of-the-post-detailed-page_3.png)
![post-detailed-page-reference-2](https://mate-academy-images.s3.eu-central-1.amazonaws.com/py-reference-of-the-post-detailed-page_2.png)
![post-detailed-page-reference-3](https://mate-academy-images.s3.eu-central-1.amazonaws.com/py-reference-of-the-post-detailed-page_1.png)

# Note
Follow these steps if you need to use `crispy_forms` v2.0 with Python 3.11:

1. Add `CRISPY_TEMPLATE_PACK` to `settings.py`.

```python
CRISPY_TEMPLATE_PACK="bootstrap4"
```

2. Add these apps to `INSTALLED_APPS` and install them corresponding to the `CRISPY_TEMPLATE_PACK` bootstrap version.

```python
INSTALLED APPS = [
   ...,
   "crispy_bootstrap4",
   "crispy_forms",
]
```
