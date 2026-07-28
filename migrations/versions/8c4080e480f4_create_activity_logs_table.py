"""create activity logs table

Revision ID: 8c4080e480f4
Revises: 3c67aab2cc7a
Create Date: 2026-07-29 00:11:31.261618

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8c4080e480f4"
down_revision: Union[str, None] = "3c67aab2cc7a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    with op.batch_alter_table(
        "activity_logs"
    ) as batch_op:

        batch_op.alter_column(
            "description",
            existing_type=sa.TEXT(),
            type_=sa.String(length=500),
            existing_nullable=True,
            nullable=False
        )

        batch_op.create_index(
            "ix_activity_logs_user_id",
            ["user_id"],
            unique=False
        )


def downgrade() -> None:

    with op.batch_alter_table(
        "activity_logs"
    ) as batch_op:

        batch_op.drop_index(
            "ix_activity_logs_user_id"
        )

        batch_op.alter_column(
            "description",
            existing_type=sa.String(length=500),
            type_=sa.TEXT(),
            existing_nullable=False,
            nullable=True
        )