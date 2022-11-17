"""agregue tabla tareas

Revision ID: 5e214e5bf465
Revises: d18a595acfb9
Create Date: 2022-11-10 19:36:48.947554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e214e5bf465'
down_revision = 'd18a595acfb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tareas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('observacion', sa.Text(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tareas')
    # ### end Alembic commands ###
