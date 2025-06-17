from sqlalchemy import (
    Column, String, SmallInteger, Text, Integer, Date, BigInteger, DateTime,ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, Date
)
from erp_lib.db.connection.primary.db_connection import Base

# creates "erp_leave_ccl_records" model for "leave_ccl_records" table
class  ResidenceMasterModel(Base):
    __tablename__ = "residence_typ_mst"

    company_code = Column('comp_cd', SmallInteger, nullable=False)
    divison_code = Column('div_cd', SmallInteger, nullable=False)
    location_code = Column('loc_cd', SmallInteger, nullable=False)
    res_cd = Column('res_cd', Integer, primary_key=True, nullable=False)
    from_pay_level = Column('from_pay_level', String, nullable=False)
    to_pay_level = Column('to_pay_level', String, nullable=False)
    type = Column('type', String, nullable=False)
    from_dt = Column('from_dt', Date, nullable=False)
    to_dt = Column('to_dt', Date, nullable=False)
    created_by = Column('created_by', BigInteger, nullable=False)
    created_date = Column('created_dt', DateTime(timezone=False), nullable=False)
    creator_role_code = Column('creator_role_cd', SmallInteger, nullable=False)
    updated_by = Column('updated_by', BigInteger, nullable=True)
    updated_date = Column('updated_dt', DateTime(timezone=False), nullable=True)
    updator_role_code = Column('updator_role_cd', SmallInteger, nullable=True)
    terminal_id = Column('terminal_id', Text, nullable=True)
    active_yn = Column('active_yn', SmallInteger, nullable=False, default=1)
    version_number = Column('ver_no', SmallInteger, nullable=False, default=0)

    # Table constraints
    __table_args__ = (
        PrimaryKeyConstraint('res_cd'),  # Primary key constraint
        UniqueConstraint('comp_cd', 'div_cd', 'loc_cd', 'from_pay_level', 'to_pay_level'),  # Unique key constraint
        {"schema": "erp_quartering"},
    )


