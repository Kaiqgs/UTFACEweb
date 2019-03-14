"""empty message

Revision ID: c95773d4cc7c
Revises: 985cd6968185
Create Date: 2018-12-27 11:59:42.591552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95773d4cc7c'
down_revision = '985cd6968185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('source', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'source')
    # ### end Alembic commands ###
