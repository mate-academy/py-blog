# Py·Blog — Technical & User Guide

Single documentation entry point for the **py-blog** Django project.
Part I is for end users; Part II is for developers maintaining or
extending the codebase.

---

## 1. Overview

| | |
|---|---|
| **Purpose** | Simple blog: paginated post feed, post detail pages, commentaries |
| **Framework** | Django 6.1 (LTS-line), Python 3.10+ (CI) / 3.13 (local) |
| **UI** | Hand-written "ink & paper" CSS theme — no CSS framework |
| **Forms** | django-crispy-forms + crispy-bootstrap4 pack |
| **Database** | SQLite (`db.sqlite3`, gitignored) |
| **QA** | flake8 (79 chars, double quotes) + 9 Django tests (GitHub Actions) |

**Features**

- Post feed with 5 posts per page, newest first, commentary count per post
- Post detail page with comment thread and crispy-rendered comment form
- Only signed-in users can comment — the form itself rejects anonymous
  submissions (validation-level, not just hidden in the UI)
- Django admin with search, filters, and a commentary-count column
- Login / logout wired into an auth-aware navbar

---

## 2. User Guide

### 2.1 Quick Start (Windows)

```bat
cd C:\Users\AORUS\Documents\kodree\py-blog
venv\Scripts\activate
python manage.py runserver
```

The site is then served at **http://127.0.0.1:8000**.

First run on a fresh clone (no `db.sqlite3` yet):

```bat
python manage.py migrate
python manage.py loaddata blog_system_db_data.json
```

### 2.2 URLs & Credentials

| Page | URL |
|---|---|
| Blog home (paginated feed) | http://127.0.0.1:8000/ |
| Post detail (example pk=1) | http://127.0.0.1:8000/posts/1/ |
| Log in | http://127.0.0.1:8000/accounts/login/ |
| Admin panel | http://127.0.0.1:8000/admin/ |

> **Credentials note:** users shipped in the fixture (including
> `admin.user`) have **hashed, unknown passwords**. Create your own
> one-time superuser and use it for both the admin panel and commenting:
>
> ```bat
> python manage.py createsuperuser
> ```

### 2.3 Using the Blog

1. Open the home page — browse posts (5 per page, pager at the bottom).
2. Click a post title to open its detail page (content + comment thread).
3. Log in via the navbar **Log in** link.
4. Fill the **Leave a commentary** form and submit.
   Anonymous submissions are rejected with a validation error.
5. Log out via the navbar **Log out** button.

### 2.4 Command Reference (inside activated venv)

| Command | Purpose |
|---|---|
| `python manage.py runserver` | Start the dev server |
| `python manage.py test` | Run the 9-test suite |
| `flake8` | Lint (must be clean before pushing) |
| `python manage.py migrate` | Apply migrations |
| `python manage.py loaddata blog_system_db_data.json` | Load demo data |
| `python manage.py createsuperuser` | Create an admin account |

---

## 3. Developer Guide

### 3.1 Project Structure

```
py-blog/
├── blog/                        # Application
│   ├── models.py                # User, Post, Commentary
│   ├── admin.py                 # ModelAdmins + Group removal
│   ├── forms.py                 # CommentaryForm (anonymous rejection)
│   ├── views.py                 # PostListView, PostDetailView
│   ├── urls.py                  # app_name = "blog"
│   └── migrations/              # 0001_initial
├── blog_system/                 # Project config
│   ├── settings.py              # apps, crispy, dirs, auth overrides
│   └── urls.py                  # admin/ + accounts/ + blog include
├── static/css/styles.css        # Custom theme (no framework)
├── templates/
│   ├── base.html                # Auth-aware navbar + flash messages
│   ├── blog/post_list.html      # Card feed + pager include
│   ├── blog/post_detail.html    # Post + comment thread + form
│   ├── includes/pager.html      # Pagination controls
│   └── registration/login.html  # Crispy login form
├── tests/                       # Course-provided acceptance tests (do not edit)
├── manage.py
└── requirements.txt             # + crispy-bootstrap4
```

### 3.2 Data Model

| Model | Fields / relations |
|---|---|
| `User` | Extends `AbstractUser`; `Meta.ordering = ["username"]`; `__str__` shows `"Full Name (@username)"` |
| `Post` | `title` (CharField 255), `content` (Text), `created_time` (auto), `owner` → `AUTH_USER_MODEL` CASCADE `related_name="posts"`; `Meta.ordering = ["-created_time"]` |
| `Commentary` | `content`, `created_time` (auto), `user` → `AUTH_USER_MODEL`, `post` → `Post`, both CASCADE `related_name="commentaries"`; `Meta.ordering = ["created_time"]`, `verbose_name_plural = "commentaries"` |

`AUTH_USER_MODEL = "blog.User"` — the fixture (`blog.user`, `blog.Post`,
`blog.Commentary`) depends on these exact names and field labels.

### 3.3 URL Map & Views

| Route | Name | View |
|---|---|---|
| `/` | `blog:index` | `PostListView` |
| `/posts/<int:pk>/` | `blog:post-detail` | `PostDetailView` |
| `/admin/` | — | Django admin |
| `/accounts/…` | `login`, `logout`, … | `django.contrib.auth.urls` |

**`PostListView`** — feed in a single optimized query:

```python
Post.objects
    .select_related("owner")                       # no N+1 on author
    .annotate(commentaries_count=Count(...))       # no N+1 on count
    .order_by("-created_time")                     # explicit (see 3.7)
```

`paginate_by = 5`; context name `post_list` (test contract).

**`PostDetailView`** — one view, two verbs:
- **GET**: post + `commentary_list` (users prefetch) + bound `CommentaryForm`
- **POST**: validates the form; on success saves the commentary with
  `post`/`user` injected, flashes a success message and redirects back;
  on failure re-renders the page with form errors (HTTP 200).

### 3.4 Forms & Security

`CommentaryForm(forms.ModelForm)` accepts `request_user` in `__init__`
and rejects anonymous submitters **inside the form**:

```python
def clean(self):
    cleaned_data = super().clean()
    if self.request_user is None or not self.request_user.is_authenticated:
        raise forms.ValidationError(
            "Only signed-in users may leave commentaries. "
            "Please log in and try again."
        )
    return cleaned_data
```

Even a crafted POST from a logged-out client cannot create a commentary —
`form.is_valid()` is `False` regardless of UI state.

### 3.5 Admin Configuration

- `UserAdmin` extends Django's `DjangoUserAdmin` (correct password handling).
- `PostAdmin`: `list_display` includes an **annotated commentary-count
  column**; filters by owner/date; search on title/content; date hierarchy.
- `CommentaryAdmin`: excerpt + post-title accessor columns; filters;
  search on content and `post__title`.
- `admin.site.unregister(Group)` — per task requirement.

### 3.6 Settings Highlights

```python
INSTALLED_APPS += ["crispy_forms", "crispy_bootstrap4", "blog"]
AUTH_USER_MODEL = "blog.User"
CRISPY_TEMPLATE_PACK = "bootstrap4"
TEMPLATES["DIRS"] = [BASE_DIR / "templates"]
STATICFILES_DIRS = [BASE_DIR / "static"]
LOGIN_REDIRECT_URL = "blog:index"     # after login → feed
LOGOUT_REDIRECT_URL = "blog:index"    # after logout → feed
```

### 3.7 Known Gotcha: Ordering + GROUP BY (Django 6)

`QuerySet.ordered` ignores a model's default `Meta.ordering` when the
query has a `GROUP BY` (introduced by `.annotate(...)`). The paginated
feed would raise `UnorderedObjectListWarning`. Fix applied: the list
view orders **explicitly** with `.order_by("-created_time")`; the model
`Meta.ordering` remains as a defensive default elsewhere.

### 3.8 Verification Record

| Check | Result |
|---|---|
| `flake8` | Clean |
| `python manage.py test` | 9/9 OK |
| Pagination | 5 posts/page, 2 pages, `-created_time` order |
| Anonymous comment POST | Rejected by form; nothing created |
| Authenticated comment POST | Created, redirect + success message |
| Admin changelists | 200 (`blog_post`, `blog_commentary`) |
| Live server smoke | index/detail/login 200; CSS served `text/css` |

CI (`.github/workflows/test.yml`) repeats `flake8` + `manage.py test`
on Python 3.10 for every PR targeting `master`.
