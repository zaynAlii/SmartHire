"""new table addes and made relationship to other tables

Revision ID: 20fc254e190b
Revises: 03c69ce041e3
Create Date: 2024-06-03 01:35:43.342985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20fc254e190b'
down_revision: Union[str, None] = '03c69ce041e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quizquestion',
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questionbank.id'], ),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('quiz_id', 'question_id', 'topic_id', 'id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quizquestion')
    # ### end Alembic commands ###
