"""fix models

Revision ID: 3dc9be76d6cd
Revises: f98fccd93452
Create Date: 2025-02-11 23:00:48.907613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3dc9be76d6cd'
down_revision: Union[str, None] = 'f98fccd93452'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('announcements', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('announcements', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('announcements', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'announcements', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('announcements', 'create_at')
    op.add_column('requirement_categories', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('requirement_categories', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('requirement_categories', 'create_at')
    op.add_column('requirements', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('requirements', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_constraint('requirements_category_id_fkey', 'requirements', type_='foreignkey')
    op.create_foreign_key(None, 'requirements', 'requirement_categories', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_column('requirements', 'create_at')
    op.drop_constraint('service_requirement_association_requirement_id_fkey', 'service_requirement_association', type_='foreignkey')
    op.drop_constraint('service_requirement_association_service_id_fkey', 'service_requirement_association', type_='foreignkey')
    op.create_foreign_key(None, 'service_requirement_association', 'requirements', ['requirement_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'service_requirement_association', 'services', ['service_id'], ['id'], ondelete='CASCADE')
    op.add_column('services', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('services', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('services', 'create_at')
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.add_column('services', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('services', 'updated_at')
    op.drop_column('services', 'created_at')
    op.drop_constraint(None, 'service_requirement_association', type_='foreignkey')
    op.drop_constraint(None, 'service_requirement_association', type_='foreignkey')
    op.create_foreign_key('service_requirement_association_service_id_fkey', 'service_requirement_association', 'services', ['service_id'], ['id'])
    op.create_foreign_key('service_requirement_association_requirement_id_fkey', 'service_requirement_association', 'requirements', ['requirement_id'], ['id'])
    op.add_column('requirements', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'requirements', type_='foreignkey')
    op.create_foreign_key('requirements_category_id_fkey', 'requirements', 'requirement_categories', ['category_id'], ['id'])
    op.drop_column('requirements', 'updated_at')
    op.drop_column('requirements', 'created_at')
    op.add_column('requirement_categories', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('requirement_categories', 'updated_at')
    op.drop_column('requirement_categories', 'created_at')
    op.add_column('announcements', sa.Column('create_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'announcements', type_='foreignkey')
    op.drop_column('announcements', 'updated_at')
    op.drop_column('announcements', 'created_at')
    op.drop_column('announcements', 'user_id')
    # ### end Alembic commands ###
