from src import app, User
from flask_login import LoginManager
from src.models.alerts.views import alert_blueprint
from src.models.auth.views import auth_blueprint
from src.models.campaigns.views import campaign_blueprint
from src.models.forms.views import form_blueprint
from src.models.recipients.views import recipient_blueprint
from src.models.reports.views import reports_blueprint


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(recipient_blueprint)
app.register_blueprint(reports_blueprint)
app.register_blueprint(form_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(campaign_blueprint)
app.register_blueprint(alert_blueprint)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=4995)
