"""empty message

Revision ID: 985cd6968185
Revises: 
Create Date: 2018-12-02 23:56:37.220723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985cd6968185'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('grade', sa.String(length=255), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###
