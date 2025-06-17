from datetime import date
from typing import Optional
from pydantic import BaseModel
from erp_lib.db.common_schema.pagination_schema import PaginationSchema
from erp_lib.db.common_schema.sort_schema import SortSchema

class QuarterPriorityRoasterSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    employee_id: Optional[str] = None
    employee_code: Optional[int] = None
    name: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    caste: Optional[str] = None
    dob: Optional[str] = None
    doj: Optional[str] = None
    pay_level: Optional[str] = None
    address: Optional[str] = None
    type: Optional[str] = None
    role_cd: Optional[str] = None
    ecode: Optional[str] = None
    quarter_app_cd: Optional[int] = None
    quarter_app_chg_cd: Optional[int] = None
    tran_indicator: Optional[str] = None
    tran_indicator_type: Optional[str] = None
    transaction_mode: Optional[str] = "insert"
    transaction_number: Optional[str] = None  # Added field
    transaction_date: Optional[date] = None  # Added field
    transaction_doc_number: Optional[str] = None  # Added field
    transaction_doc_date: Optional[date] = None  # Added field
    transaction_stage: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True

class QuarterPriorityRoasterList(QuarterPriorityRoasterSchema):
    pagination: PaginationSchema
    sort: Optional[SortSchema]

class QuarterPriorityRoasterListParamsSchema(QuarterPriorityRoasterList):
    unit: Optional[str] = None
    type: Optional[str] = None