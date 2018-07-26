from faker import Faker
from src import db
from src.models.recipients.recipient import Recipient

fake = Faker()

for item in range(2000):
    recipient = Recipient(user_id=1, email="test_recipients@ukr.net", name=fake.name(), state='active')
    db.session.add(recipient)
    db.session.commit()