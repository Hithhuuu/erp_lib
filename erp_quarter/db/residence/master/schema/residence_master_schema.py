from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema

from erp_lib.db.common_schema.sort_schema import SortSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema





class ResidenceMasterSchema(BaseModel):
    company_code: int
    divison_code: int
    location_code: int
    
    from_pay_level : str
    to_pay_level : str
    type : str
    from_dt : date
    to_dt : date
    res_cd: int

    created_by: Optional[int] = None 
    created_date: Optional[datetime] = None
    creator_role_code: Optional[int] = None
    updated_by: Optional[int] = None
    updated_date: Optional[datetime] = None
    updator_role_code: Optional[int] = None
    terminal_id: Optional[str] = None
    active_yn: Optional[int] = 1
    version_number: Optional[int] = 0 
    role_cd: Optional[str] = None

    class Config:
        orm_mod = True
        from_attributes = True


class ResidenceMasterResponseSchema(ResidenceMasterSchema, DateFormattingSchema):
    created_date: Optional[str] = None
    updated_date: Optional[str] = None

class ResidenceMasterCreateSchema(ResidenceMasterSchema):
    from_pay_level : str
    to_pay_level : str
    type : str
    from_dt : date
    to_dt : date
    res_cd: int

    class Config:
        orm_mode = True
        from_attributes = True

class ResidenceMasterUpdateSchema(ResidenceMasterSchema):
    res_cd: int
    updated_by: int
    updated_date: datetime
    updator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

# Request schema with pagination and sort
class ResidenceMasterRequestSchema(PaginationWrapperSchema):
    from_pay_level : str
    to_pay_level : str
    type : str
    from_dt : date
    to_dt : date
    res_cd: int

