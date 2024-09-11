"""Remove unique constraint from question text

Revision ID: 9279d520557c
Revises: e4f3eabb9b28
Create Date: 2024-09-03 03:41:14.457016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9279d520557c'
down_revision = 'e4f3eabb9b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('text',
               existing_type=sa.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('answer',
               existing_type=sa.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('clint',
               existing_type=sa.TEXT(),
               type_=sa.String(length=25),
               existing_nullable=False)
        batch_op.alter_column('session_id',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('session_id',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('clint',
               existing_type=sa.String(length=25),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('answer',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('text',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    # ### end Alembic commands ###
