from flask import Blueprint, render_template, jsonify
from flask_login import login_required

from services.reports.form_report import Report

reports_blueprint = Blueprint('reports', __name__,  url_prefix="/reports")


@reports_blueprint.route('/<string:campaign_id>')
@login_required
def all_report(campaign_id):
    return render_template('reports/index.html', campaign_id=campaign_id)


@reports_blueprint.route('/json/form-filled/<string:campaign_id>')
def json_form_filled(campaign_id):
    json_data = Report.generate_form_report(campaign_id)
    return jsonify(json_data)


@reports_blueprint.route('/json/form-filled-month/<string:campaign_id>')
def json_form_filled_month(campaign_id):
    json_data = Report.generate_form_report_by_month(campaign_id)
    return jsonify(json_data)