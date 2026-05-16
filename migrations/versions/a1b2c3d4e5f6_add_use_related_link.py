"""add use_related_link to rss feeds

Revision ID: a1b2c3d4e5f6
Revises: f411849d887d
Create Date: 2026-05-16 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, None] = "f411849d887d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("feeds", sa.Column("use_related_link", sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column("feeds", "use_related_link")
