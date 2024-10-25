"""field added to Comment

Revision ID: 766fe4fa8d96
Revises: 9f22f20f4d8b
Create Date: 2024-10-20 14:21:59.786238

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '766fe4fa8d96'
down_revision: Union[str, None] = '9f22f20f4d8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###
