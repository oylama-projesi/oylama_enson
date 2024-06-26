"""Change choice field to String in Vote model

Revision ID: 4b6ea7a20b87
Revises: 5ee30cbea213
Create Date: 2024-05-25 16:39:16.023350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6ea7a20b87'
down_revision = '5ee30cbea213'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.alter_column('choice',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.alter_column('choice',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=False)

    # ### end Alembic commands ###
