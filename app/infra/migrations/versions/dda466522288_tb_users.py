"""tb_users

Revision ID: dda466522288
Revises:
Create Date: 2025-06-25 10:29:55.781742

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dda466522288"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tb_users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(50), nullable=False, unique=True),
        sa.Column("email", sa.String(100), nullable=False, unique=True),
        sa.Column("password", sa.String(128), nullable=False),
        sa.Column("full_name", sa.String(150), nullable=False),
        sa.Column("user_status", sa.Enum("ACTIVE", "BLOCKED", name="user_status"), nullable=False),
        sa.Column("user_type", sa.Enum("ADMIN", "STUDENT", "INSTRUCTOR", name="user_type"), nullable=False),
        sa.Column("phone_number", sa.String(20), nullable=True),
        sa.Column("cpf", sa.String(14), nullable=True),
        sa.Column("image_url", sa.String(255), nullable=True),
        sa.Column("creation_date", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column(
            "last_update_date",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            onupdate=sa.func.current_timestamp(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("tb_users")
