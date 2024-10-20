"""3a987f91d6fc0e55977e22feccd2a3b7d04a6dac

Revision ID: d12158d30cd9
Revises: 2c48b36beafd
Create Date: 2024-07-22 15:03:28.228867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd12158d30cd9'
down_revision: Union[str, None] = '2c48b36beafd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('api_credit_balance', sa.Integer(), nullable=True))
    op.drop_column('user', 'credits')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('credits', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user', 'api_credit_balance')
    op.drop_column('user', 'is_admin')
    # ### end Alembic commands ###
