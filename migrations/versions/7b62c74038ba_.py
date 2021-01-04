"""empty message

Revision ID: 7b62c74038ba
Revises: 74ac99207718
Create Date: 2021-01-04 17:42:48.491378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b62c74038ba'
down_revision = '74ac99207718'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reader', sa.Column('image', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reader', 'image')
    # ### end Alembic commands ###
