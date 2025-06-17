from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema

class UnderVacationSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    final_year: Optional[int] = None
    ecode: Optional[str] = None
    employee_code: Optional[int] = None
    
    under_vacation_cd:  Optional[int] = None
    under_vacation_vide : Optional[str] = None
    under_vacation_date :Optional[date] = None  
    proposed_date_of_vacation: Optional[date] = None  
    reason_of_vacation :Optional[str] = None
    date_of_sos: Optional[date] = None
    retention_completion_date: Optional[date] = None
    allied_charged_recovered:  Optional[int] = None
    remarks:Optional[str] = None
    
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

class UnderVacationCreateSchema(UnderVacationSchema):
    under_vacation_cd:  int
    under_vacation_vide : str
    under_vacation_date : date  
    proposed_date_of_vacation: date  
    reason_of_vacation :str
    date_of_sos: date
    retention_completion_date: date
    allied_charged_recovered:  int
    remarks:str
    role_cd: str
    created_by: int
    created_date: datetime
    creator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

class UnderVacationResposneSchema(UnderVacationSchema, DateFormattingSchema):
    under_vacation_cd: int
    transaction_number: str
    transaction_date: Optional[str] = None
    transaction_doc_date: Optional[str] = None
    approved_date: Optional[str] = None
    created_date: Optional[str] = None
    updated_date: Optional[str] = None



class UnderVacationViewSchema(PaginationWrapperSchema):
    pass

class UnderVacationIdRequest(BaseModel):
    under_vacation_cd: int