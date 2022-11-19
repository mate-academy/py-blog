# Blog

In this task, you will create a simple `Blog` project from start to end.

Let's go through all the steps:

1. Create a virtual environment, activate it, and install django via pip.
2. Start project `blog_system` inside the current directory (add . at the end of the command).
3. Inside `py-blog` start application `blog`.
4. Inside `blog/models.py` create models according to this diagram:

![models-diagram](../../../../../var/folders/1v/lc6bhtr544s1nxpg4l2jh6y80000gp/T/TemporaryItems/NSIRD_screencaptureui_FnPxQj/Снимок экрана 2022-11-19 в 23.41.05.png)

5. Edit `admin.py`:
    - Register all your models in the admin.
    - Unregister `Group`.
    - Do the filtering and searching in any way you think is logical.
6. Make migrations and migrate.
7. Use `python manage.py test` to run tests.
8. Use the following command to load prepared data from fixture to test and debug your code:
   ```python manage.py loaddata blog_system_db_data.json```

   _Feel free to add more data using admin panel, if needed._
9. Inside `blog_system.urls` add path to the `blog.urls`. Don't forget to specify namespace.
10. Inside `blog.urls` create a path for the home page. Give this path the name `index`.
11. Inside `blog.views` create view for the `index` url. This view returns a list of all posts, in descending order by `created_time`.
12. Before you create a template you have to create styles for the template. Create directory `static` next to the directory `blog`. 
Inside this directory create a file with the following path `css/styles.css`. Don't forget to do all necessary steps so that 
Django can serve these static files.
13. Create directory `templates` next to the directory `blog`. There you will store templates for pages. Edit settings so
that engine knows where to look for template source files.
14. Create template for the main page. On this page, make it so that a list of all posts is displayed. 
The title and content were displayed, the author was visible, when this post was created and the number of comments on
the post. Make the title of the post a link to the detailed page, that you would implement further.
15. Add pagination for the main page. Set a `5` posts in ine page by default.
16. Create a `PostDetailViewset` view that returns detailed information about the post by `id` field.
17. Add a template for this page and url with a path `posts/pk/`.
18. On the post detail page, display a list of post comments below this post.
19. Under the list of comments, add a form that allows you to create a new comment to the post. 

**Please note**: only authorized users can post comments. If an anonymous user tries to 
create new comment, the form must be invalid.
20. Use crispy forms in your forms to make website more beautiful. 
21. Use `python manage.py test` to run tests.
22. Don't forget add `.gitignore` file before pushing. Don't push a lot of extra files(`venv`, `pycache`, `.idea`, etc.).


### Note: Attach screenshots of all created or modified pages to pull request.
1. Attach screenshots to the comment, NOT in commit.
2. It's important to attach images not links to them. 