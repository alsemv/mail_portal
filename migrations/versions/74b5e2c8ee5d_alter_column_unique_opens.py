"""alter column unique_opens

Revision ID: 74b5e2c8ee5d
Revises: fe75ac99dba2
Create Date: 2018-06-13 14:55:29.164024

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '74b5e2c8ee5d'
down_revision = 'fe75ac99dba2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('campaigns', 'unique_opens',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('campaigns', 'unique_opens',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
