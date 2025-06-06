"""Create freebies table

Revision ID: 5241293fc7a0
Revises: c8b598c23fce
Create Date: 2025-05-25 23:46:05.647399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5241293fc7a0'
down_revision = 'c8b598c23fce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.alter_column('item_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('value',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('dev_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('company_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.alter_column('company_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('dev_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('value',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('item_name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
