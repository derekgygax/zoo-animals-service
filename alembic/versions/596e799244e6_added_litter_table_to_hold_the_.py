"""added litter table to hold the offspring from breeding

Revision ID: 596e799244e6
Revises: e8a7e1e9d79e
Create Date: 2024-12-08 14:10:13.222204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '596e799244e6'
down_revision: Union[str, None] = 'e8a7e1e9d79e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('litter',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('breeding_id', sa.UUID(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('birth_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['breeding_id'], ['breeding.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('breeding_id')
    )
    op.add_column('animal', sa.Column('litter_id', sa.UUID(), nullable=True))
    op.alter_column('animal', 'acquisition_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.create_foreign_key(None, 'animal', 'litter', ['litter_id'], ['id'])
    op.add_column('breeding', sa.Column('description', sa.String(length=1000), nullable=True))
    op.drop_constraint('unique_breeding_combination', 'breeding', type_='unique')
    op.create_unique_constraint('unique_breeding_combination', 'breeding', ['parent_1_id', 'parent_2_id'])
    op.drop_constraint('breeding_offspring_id_fkey', 'breeding', type_='foreignkey')
    op.drop_column('breeding', 'offspring_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('breeding', sa.Column('offspring_id', sa.UUID(), autoincrement=False, nullable=False))
    op.create_foreign_key('breeding_offspring_id_fkey', 'breeding', 'animal', ['offspring_id'], ['id'], ondelete='RESTRICT')
    op.drop_constraint('unique_breeding_combination', 'breeding', type_='unique')
    op.create_unique_constraint('unique_breeding_combination', 'breeding', ['parent_1_id', 'parent_2_id', 'offspring_id'])
    op.drop_column('breeding', 'description')
    op.drop_constraint(None, 'animal', type_='foreignkey')
    op.alter_column('animal', 'acquisition_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_column('animal', 'litter_id')
    op.drop_table('litter')
    # ### end Alembic commands ###