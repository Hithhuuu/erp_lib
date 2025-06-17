from typing import Optional
from pydantic import BaseModel
from erp_lib.db.common_schema.pagination_wrapper_schema import PaginationWrapperSchema

from erp_lib.db.common_schema.sort_schema import SortSchema

class QuarterEmpRequestSchema( PaginationWrapperSchema):
    employee_id: Optional[str] = None
    employee_name: Optional[str] = None
    center_no: Optional[str] = None
    designation: Optional[str] = None

class QuarterEmpResponseSchema(BaseModel):
    employee_code: int
    employee_id: str
    employee_name: str
    center_no: str
    designation: str
    division_code: int

