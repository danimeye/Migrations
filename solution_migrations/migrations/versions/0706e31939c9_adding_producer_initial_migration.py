"""adding-producer-initial-migration

Revision ID: 0706e31939c9
Revises: cc4e62ed21f0
Create Date: 2018-11-01 22:12:59.492240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0706e31939c9'
down_revision = 'cc4e62ed21f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('albums', sa.Column('producer', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('albums', 'producer')
    # ### end Alembic commands ###
