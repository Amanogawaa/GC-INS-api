"""add attr and column in announcement table

Revision ID: 5fdccd62a0e7
Revises: 972e7de075e4
Create Date: 2025-03-22 00:15:22.754364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fdccd62a0e7'
down_revision: Union[str, None] = '972e7de075e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('announcements', sa.Column('labels', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('announcements', 'labels')
    # ### end Alembic commands ###
