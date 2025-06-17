from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema

class MaintenanceSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    final_year: Optional[int] = None
    ecode: Optional[str] = None
    employee_code: Optional[int] = None
   
    maintenance_cd: Optional[int] = None
    under_maintenance_cd: Optional[int] = None

    quarter: Optional[str] = None
    building : Optional[str] = None
    to_date :Optional[date] = None  
    from_date: Optional[date] = None  
    maintenance_reason : Optional[str] = None
    remark :Optional[str] = None
   
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

class MaintenanceCreateSchema(MaintenanceSchema):
    maintenance_cd: Optional[int] = None
    quarter: Optional[str] = None
    building : Optional[str] = None
    to_date :Optional[date] = None  
    from_date: Optional[date] = None  
    maintenance_reason : Optional[str] = None
    remark :Optional[str] = None
    role_cd: str
    created_by: int
    created_date: datetime
    creator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

class MaintenanceResposneSchema(MaintenanceSchema, DateFormattingSchema):
    maintenance_cd: int
    transaction_number: str
    transaction_date: Optional[str] = None
    transaction_doc_date: Optional[str] = None
    approved_date: Optional[str] = None
    created_date: Optional[str] = None
    updated_date: Optional[str] = None



class MaintenanceViewSchema(PaginationWrapperSchema):
    pass

class MaintenanceIdRequest(BaseModel):
    maintenance_cd: int