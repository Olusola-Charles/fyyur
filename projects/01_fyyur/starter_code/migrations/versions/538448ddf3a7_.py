"""empty message

Revision ID: 538448ddf3a7
Revises: 48ebfd216a1a
Create Date: 2022-08-18 21:26:21.285713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538448ddf3a7'
down_revision = '48ebfd216a1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_id')
    # ### end Alembic commands ###
