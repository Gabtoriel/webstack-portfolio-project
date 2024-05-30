from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,
                                                                  per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
<<<<<<< HEAD
=======


@main.route("/mission")
def mission():
    return render_template('mission.html', title='Mission')


@main.route("/news")
def news():
    return render_template('news.html', title='News')


@main.route("/announcement")
def announcement():
    return render_template('announcement.html', title='Announcement')
>>>>>>> d19ecca34df0329b77329ba355d3e389e14a25d6
