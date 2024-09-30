from contextlib import contextmanager
from datetime import date
from typing import Generator, Optional
import connexion.lifecycle  # type: ignore
from flask import g
import pydantic
from sqlalchemy.orm import Session
from sqlalchemy import text
import connexion  # type: ignore

from backend_engineer_interview.models import Employee


class PydanticBaseModel(pydantic.BaseModel):
    model_config = {"from_attributes": True}


@contextmanager
def db_session() -> Generator[Session, None, None]:
    """Get a plain SQLAlchemy Session."""
    session: Optional[Session] = g.get("db")
    if session is None:
        raise Exception("No database session available in application context")

    yield session


def get_request() -> connexion.lifecycle.ConnexionRequest:
    return connexion.request


def status() -> tuple[dict, int, dict]:
    with db_session() as session:
        session.execute(text("SELECT 1;")).one()
        return ({"status": "up"}, 200, {})


class EmployeeResponse(PydanticBaseModel):
    model_config = {"from_attributes": True}

    id: int
    first_name: str
    last_name: str
    date_of_birth: date


def get_employee(id: int) -> None:
    # ANSWER
    pass


def patch_employee(id: int, body: dict) -> None:
    # Answer
    pass


def post_application() -> None:
    """
    Accepts a leave_start_date, leave_end_date, employee_id and creates an Application
    with those properties.  It should then return the new application with a status code of 200.

    If any of the properties are missing in the request body, it should return the new application
    with a status code of 400.

    Verify the handler using the test cases in TestPostApplication.  Add any more tests you think
    are necessary.
    """
    # Answer
    pass


def search_application() -> None:
    """
    Returns a list of applications.  Can provide an employee id, first name or last name to filter the results
    """
    # Answer
    pass
