"""Added many to many relationship

Revision ID: 0bbc3a2d4b6c
Revises: 36f6470b0a54
Create Date: 2023-12-29 11:19:37.289241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bbc3a2d4b6c'
down_revision: Union[str, None] = '36f6470b0a54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
