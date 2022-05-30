from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title="Home page", posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About us')


# @main.context_processor
# def base():
#     form = SearchForm()
#     return dict(form=form)


# @main.route('/search', methods=['GET', 'POST'])
# def search():
#     form = SearchForm()
#     if form.validate_on_submit():
#         # return redirect(url_for('search_results', query=form.search.data))
#         keyword = form.search.data
#         return render_template('search_results.html', title='Search', form=form, keyword=keyword)
    # return render_template('partials/offcanvas.html', title='Search', form=form, keyword=keyword)
