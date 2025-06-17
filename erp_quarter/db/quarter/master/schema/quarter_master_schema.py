from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema

from erp_lib.db.common_schema.sort_schema import SortSchema
from erp_lib.db.common_schema.date_formatting_schema import DateFormattingSchema


class QuarterMasterSchema(BaseModel):
    company_code: int
    divison_code: int
    location_code: int
    quarter_cd: Optional[int] = None
    quarter_no:  Optional[str] = None
    building_name: Optional[str] = None
    floor: Optional[int] = None
    allocation_unit: Optional[str] = None
    configuration: Optional[str] = None
    type_applicable: Optional[str] = None
    rent: Optional[int] = None
    details: Optional[str] = None
    file_detail: Optional[str] = None
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


class QuarterMasterResponseSchema(QuarterMasterSchema, DateFormattingSchema):
    created_date: Optional[str] = None
    updated_date: Optional[str] = None

class QuarterMasterCreateSchema(QuarterMasterSchema):
    quarter_no:  Optional[str] = None
    building_name: Optional[str] = None
    floor: Optional[int] = None
    allocation_unit: Optional[str] = None
    configuration: Optional[str] = None
    type_applicable: Optional[str] = None
    rent: Optional[int] = None
    details: Optional[str] = None
    file_detail: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class QuarterMasterUpdateSchema(QuarterMasterSchema):
    quarter_cd: int
    updated_by: int
    updated_date: datetime
    updator_role_code: int

    class Config:
        orm_mode = True
        from_attributes = True

# Request schema with pagination and sort
class QuarterMasterRequestSchema(PaginationWrapperSchema):
    quarter_no:  Optional[str] = None
    building_name: Optional[str] = None
    floor: Optional[int] = None
    allocation_unit: Optional[str] = None
    configuration: Optional[str] = None
    type_applicable: Optional[str] = None
    rent: Optional[int] = None
    details: Optional[str] = None
    file_detail: Optional[str] = None
    

