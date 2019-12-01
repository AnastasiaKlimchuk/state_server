"""empty message

Revision ID: 92089b1a2787
Revises: 6b01daaf29cc
Create Date: 2019-11-10 15:20:29.200274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92089b1a2787'
down_revision = '6b01daaf29cc'
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
