from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema

class RetentionSchema(BaseModel):
    company_code: int
    division_code: int
    location_code: int
    quarter_app_cd: Optional[int] = None
    final_year: Optional[int] = None
    ecode: Optional[str] = None
    employee_code: Optional[int] = None
    
    retention_cd:  Optional[int] = None
    retention_vide: Optional[str] = None
    sanction_reference : Optional[str] = None
    retention_rec_date :Optional[date] = None  
    date_of_sos: Optional[date] = None  
    retention_reason : Optional[str] = None
    dependent :Optional[str] = None
    relation_with_allotte: Optional[str] = None
    retention_start_from: Optional[date] = None  
    effect_date_of_retention: Optional[date] = None  
    period_of_retention_granted : Optional[str] = None
    retention_completion_date: Optional[date] = None
    license_fee:Optional[str] = None
    allied_charged_recovered:  Optional[int] = None    
    
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

class RetentionCreateSchema(RetentionSchema):
    quarter_app_cd: int
    retention_cd:  int
    retention_vide: str
    sanction_reference : str
    retention_rec_date :date  
    date_of_sos: date  
    retention_reason : str
    dependent :str
    relation_with_allotte: str
    retention_start_from: date  
    effect_date_of_retention: date  
    period_of_retention_granted : str
    retention_completion_date: date
    license_fee:str
    allied_charged_recovered:  int  
    role_cd: str
    created_by: int
    created_date: datetime
    creator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

class RetentionResposneSchema(RetentionSchema, DateFormattingSchema):
    under_vacation_cd: int
    quarter_app_cd: int
    transaction_number: str
    transaction_date: Optional[str] = None
    transaction_doc_date: Optional[str] = None
    approved_date: Optional[str] = None
    created_date: Optional[str] = None
    updated_date: Optional[str] = None



class RetentionViewSchema(PaginationWrapperSchema):
    pass

class RetentionIdRequest(BaseModel):
    under_vacation_cd: int