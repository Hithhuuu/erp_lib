from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from erp_lib.db.common_schema.pagination_schema import PaginationSchema
from erp_lib.db.common_schema.sort_schema import SortSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema

class ApplicationForChangeSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    quarter_app_chg_code: Optional[int] = None
    final_year: Optional[int] = None
    ecode: Optional[str] = None
    employee_code: Optional[int] = None
    quarter_app_chg_cd: Optional[int] = None
    quarter_preferred: Optional[str] = None
    reason: Optional[str] = None
    remarks: Optional[str] = None
    accomodation_preferred: Optional[str] = None
    tran_indicator: Optional[str] = None
    tran_indicator_type: Optional[str] = None
    transaction_mode: Optional[str] = "insert"
    transaction_number: Optional[str] = None  # Added field
    transaction_date: Optional[date] = None  # Added field
    transaction_doc_number: Optional[str] = None  # Added field
    transaction_doc_date: Optional[date] = None  # Added field
    transaction_stage: Optional[int] = None
    created_by: Optional[int] = None
    created_date: Optional[datetime] = None
    creator_role_code: Optional[int] = None
    updated_by: Optional[int] = None
    updated_date: Optional[datetime] = None
    updator_role_code: Optional[int] = None
    terminal_id: Optional[str] = None
    approved_by: Optional[int] = None
    approved_date: Optional[datetime] = None
    next_updator_role: Optional[int] = None
    version_number: Optional[int] = 0

    class Config:
        orm_mode = True
        from_attributes = True

class ApplicationForChangeCreateSchema(ApplicationForChangeSchema):
    quarter_preferred: str
    reason: str
    remarks: str
    accomodation_preferred: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class ApplicationForChangeEditSchema(ApplicationForChangeSchema, DateFormattingSchema):
    quarter_app_chg_cd: int
    transaction_number: str
    quarter_preferred: Optional[str] = None
    reason: Optional[str] = None
    remarks: Optional[str] = None
    accomodation_preferred: Optional[str] = None
    
    class Config:
        orm_mode = True
        from_attributes = True

class ApplicationForChangeViewScheme(ApplicationForChangeSchema):
    pagination: PaginationSchema
    sort: Optional[SortSchema]

class ApplicationForChangeGetIdSchema(BaseModel):
    quarter_app_chg_cd: int

class AppliactionForChangeRequestSchema(BaseModel):
    employee_id: int
    pagination: Optional[PaginationSchema] = None
    sort: Optional[SortSchema] = None