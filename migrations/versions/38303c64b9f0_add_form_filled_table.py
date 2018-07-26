"""add form_filled table

Revision ID: 38303c64b9f0
Revises: 53fe466c047a
Create Date: 2018-06-13 12:42:40.530710

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '38303c64b9f0'
down_revision = '53fe466c047a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('form_filled',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_form_filled_campaign_id'), 'form_filled', ['campaign_id'], unique=False)
    op.create_index(op.f('ix_form_filled_recipient_id'), 'form_filled', ['recipient_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_form_filled_recipient_id'), table_name='form_filled')
    op.drop_index(op.f('ix_form_filled_campaign_id'), table_name='form_filled')
    op.drop_table('form_filled')
    # ### end Alembic commands ###
