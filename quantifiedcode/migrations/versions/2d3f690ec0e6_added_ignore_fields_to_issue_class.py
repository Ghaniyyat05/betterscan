"""
This file is part of Betterscan CE (Community Edition).

Betterscan is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Betterscan is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Betterscan. If not, see <https://www.gnu.org/licenses/>.

Originally licensed under the BSD-3-Clause license with parts changed under
LGPL v2.1 with Commons Clause.
See the original LICENSE file for details.

"""
"""Added ignore fields to issue class.

Revision ID: 2d3f690ec0e6
Revises: a2e0f8f4b344
Create Date: 2017-01-11 11:47:55.728409

"""

# revision identifiers, used by Alembic.
revision = '2d3f690ec0e6'
down_revision = 'a2e0f8f4b344'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import expression

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issue', sa.Column('ignore', sa.Boolean(), server_default=expression.literal(False), nullable=False))
    op.add_column('issue', sa.Column('ignore_comment', sa.String(length=255), nullable=True))
    op.add_column('issue', sa.Column('ignore_reason', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_issue_ignore'), 'issue', ['ignore'], unique=False)
    op.create_index(op.f('ix_issue_ignore_reason'), 'issue', ['ignore_reason'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_issue_ignore_reason'), table_name='issue')
    op.drop_index(op.f('ix_issue_ignore'), table_name='issue')
    op.drop_column('issue', 'ignore_reason')
    op.drop_column('issue', 'ignore_comment')
    op.drop_column('issue', 'ignore')
    # ### end Alembic commands ###
