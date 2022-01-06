"""empty message

Revision ID: df13d0a6df5e
Revises: 
Create Date: 2022-01-06 13:49:55.926115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df13d0a6df5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('automobile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('automobile')
    # ### end Alembic commands ###