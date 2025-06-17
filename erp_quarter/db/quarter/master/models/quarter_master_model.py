from sqlalchemy import (
    Column, String, SmallInteger, Text, Integer, Date, BigInteger, DateTime,ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint
)
from erp_lib.db.connection.primary.db_connection import Base

class  QuarterMasterModel(Base):
    __tablename__ = "quarter_mst"

    company_code = Column('comp_cd', SmallInteger, nullable=False)
    divison_code = Column('div_cd', SmallInteger, nullable=False)
    location_code = Column('loc_cd', SmallInteger, nullable=False)
    quarter_cd = Column('quarter_cd', Integer, primary_key=True, nullable=False)
    quarter_no = Column('quarter_no', String, nullable=False)
    building_name = Column('building_name', String, nullable=False)
    floor = Column('floor', String, nullable=False)
    allocation_unit = Column('allocation_unit', String, nullable=False)
    configuration = Column('configuration', String, nullable=False)
    type_applicable = Column('type_applicable', String, nullable=False)
    rent = Column('rent', Integer, nullable=False)
    details = Column('details', String, nullable=False)
    file_detail = Column('file_detail', String, nullable=False)
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
        PrimaryKeyConstraint('quarter_cd'),  # Primary key constraint
        UniqueConstraint('comp_cd', 'div_cd', 'loc_cd', 'building_name','floor', 'allocation_unit', 'type_applicable'),  # Unique key constraint
        {"schema": "erp_quartering"},
    )


