"""create freebies table

Revision ID: 12e945c366c2
Revises: 5f72c58bf48c
Create Date: 2024-09-20 19:57:19.175977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12e945c366c2'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False),
    )

def downgrade():
    op.drop_table('freebies')
