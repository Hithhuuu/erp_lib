from sqlalchemy import (
    Column, SmallInteger, DateTime, Integer,
    UniqueConstraint, String, BigInteger, Text, Date,
    ForeignKeyConstraint
)
from erp_lib.db.connection.primary.db_connection import Base


class ErpRetentionModel(Base):
    __tablename__ = "retention_completed"
    __table_args__ = (
        UniqueConstraint(
            'emp_cd', 'div_cd', 'comp_cd', 'retention_cd',
            name='employee_retention_unique_constraint'
        ),
        ForeignKeyConstraint(
            ['comp_cd', 'div_cd', 'emp_cd'],
            ['erp_admin.emp_mst_enc.comp_cd', 'erp_admin.emp_mst_enc.div_cd', 'erp_admin.emp_mst_enc.emp_cd'],
            use_alter=True
        ),
        ForeignKeyConstraint(
            ['comp_cd','div_cd' ,'ecode'],
            ['erp_admin.ecode_mst.comp_cd', 'erp_admin.ecode_mst.div_cd','erp_admin.ecode_mst.ecode'],
            use_alter=True
        ),
        ForeignKeyConstraint(
            ['comp_cd', 'fin_yr'],

            ['erp_admin.finyr_mst.comp_cd', 'erp_admin.finyr_mst.fin_yr'],
            use_alter = True
        ),
        {'schema': 'erp_quartering'}
    )

    company_code = Column('comp_cd', SmallInteger, nullable=False)
    division_code = Column('div_cd', SmallInteger, nullable=False)
    location_code = Column('loc_cd', SmallInteger, nullable=False)
    final_year = Column('fin_yr', SmallInteger, nullable=True)
    ecode = Column('ecode', String(6), nullable=False)
    employee_code = Column('emp_cd', BigInteger, nullable=False)
   
    retention_cd = Column('retention_cd', Integer, primary_key=True, index=True)
    retention_vide = Column('retention_vide', Text)
    sanction_reference = Column('sanction_reference', Text)
    retention_rec_date = Column('retention_rec_date', Date)
    date_of_sos = Column('date_of_sos', Date)
    retention_reason = Column('retention_reason', Text)
    dependent = Column('dependent', Text)
    relation_with_allotte = Column('relation_with_allotte', Text)
    retention_start_from = Column('retention_start_from', Date)
    effect_date_of_retention = Column('effect_date_of_retention', Date)
    period_of_retention_granted = Column('period_of_retention_granted', Text)
    retention_completion_date = Column('retention_completion_date', Date)
    license_fee = Column('license_fee', Text)
    allied_charged_recovered =Column('allied_charged_recovered', Integer)

    transaction_number = Column('tran_no', Text, nullable=True)
    transaction_date = Column('tran_dt', Date, nullable=True)
    transaction_doc_number = Column('tran_doc_no', Text, nullable=True)
    transaction_doc_date = Column('tran_doc_dt', Date, nullable=True)
    transaction_stage = Column('transaction_stage', SmallInteger, nullable=True)
    created_by = Column('created_by', BigInteger, nullable=False)
    created_date = Column('created_dt', DateTime, nullable=True)
    creator_role_code = Column('creator_role_cd', SmallInteger, nullable=True)
    updated_by = Column('updated_by', BigInteger, nullable=True)
    updated_date = Column('updated_dt', DateTime, nullable=True)
    updater_role_code = Column('updator_role_cd', SmallInteger, nullable=True)
    terminal_id = Column('terminal_id', Text, nullable=True)
    approved_by = Column('app_by', BigInteger, nullable=True)
    approved_date = Column('app_dt', DateTime, nullable=True)
    next_updator_role = Column('next_updator_role', Integer, nullable=True)
    version_number = Column('ver_no', SmallInteger, nullable=False, default=0)