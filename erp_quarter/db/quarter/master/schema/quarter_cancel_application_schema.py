from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema

from erp_lib.db.common_schema.sort_schema import SortSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema

class QuarterCancelApplicationSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    quarter_app_cd: int
    quarter_cancel_cd : Optional[int] = None
    final_year: Optional[int] = None
    ecode: Optional[str] = None
    employee_code: Optional[int] = None
    cancel_reason: Optional[str] = None
    cancel_remark: Optional[str] = None
    role_cd: Optional[str] = None
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

class QuarterCancelApplicationCreateSchema(QuarterCancelApplicationSchema):
    cancel_reason: str
    cancel_remark: str
    quarter_app_cd : int
    created_by: int
    created_date: datetime
    creator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

class QuarterCancelApplicationResposneSchema(QuarterCancelApplicationSchema, DateFormattingSchema):
    quarter_app_cd: int
    cancel_reason: str
    cancel_remark: str  
    transaction_number: str
    transaction_date: Optional[str] = None
    transaction_doc_date: Optional[str] = None
    application_date: Optional[str] = None
    approved_date: Optional[str] = None
    created_date: Optional[str] = None
    updated_date: Optional[str] = None



class QuarterCancelApplicationViewSchema(PaginationWrapperSchema):
    pass

class QuarterCancelApplicationIdRequest(BaseModel):
    quarter_app_cd: int