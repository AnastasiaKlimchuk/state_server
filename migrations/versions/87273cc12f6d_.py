"""empty message

Revision ID: 87273cc12f6d
Revises: 
Create Date: 2019-11-10 14:44:59.759320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87273cc12f6d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('states',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('timestamp', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('states')
    # ### end Alembic commands ###
