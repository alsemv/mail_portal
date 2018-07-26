import datetime
from sqlalchemy import extract
from src import db
from src.models.forms.form_filled import FormFilled
from src.models.campaigns.campaign import Campaign


class Report(object):
    @staticmethod
    def generate_form_report(campaign_id):
        number_of_filled_forms = len(FormFilled.query.filter_by(campaign_id=campaign_id).all())
        campaign = Campaign.query.get(campaign_id)
        total_forms = len(campaign.recipients.all())
        number_of_not_filled_forms = total_forms - number_of_filled_forms

        return [
            {
                "label": "Form submitted",
                "items": number_of_filled_forms
            },
            {
                "label": "Form not submitted",
                "items": number_of_not_filled_forms
            }
        ]

    @staticmethod
    def generate_form_report_by_month(campaign_id):
        number_of_filled_forms_by_month = len(db.session.query(FormFilled).filter(extract('month', FormFilled.date) == datetime.datetime.now().month).filter(
            FormFilled.campaign_id == campaign_id).all())

        campaign = Campaign.query.get(campaign_id)
        number_of_filled_forms = len(FormFilled.query.filter_by(campaign_id=campaign_id).all())
        total_forms = len(campaign.recipients.all())
        number_of_not_filled_forms = total_forms - number_of_filled_forms

        return [
            {
                "label": "Form submitted by month",
                "items": number_of_filled_forms_by_month
            },
            {
                "label": "Form not submitted",
                "items": number_of_not_filled_forms
            }
        ]