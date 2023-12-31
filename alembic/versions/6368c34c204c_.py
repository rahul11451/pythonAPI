"""empty message

Revision ID: 6368c34c204c
Revises: dbb3981310ae
Create Date: 2023-09-19 10:03:41.440962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6368c34c204c'
down_revision: Union[str, None] = 'dbb3981310ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('image', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'image')
    # ### end Alembic commands ###
