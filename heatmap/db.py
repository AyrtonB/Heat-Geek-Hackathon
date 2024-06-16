import datetime

from sqlmodel import Session, select

from heatmap.definitions.timeseries import PointInTimeRecord


def get_records_within_dates(
    session: Session,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    schema: PointInTimeRecord,
) -> list[PointInTimeRecord]:
    """
    Retrieves records from the time-series tables where the 'start_time'
    falls within the specified start and end datetime.

    Args:
    session (Session): The SQLAlchemy session object used to execute queries.
    start_date (datetime): The start datetime for the query range.
    end_date (datetime): The end datetime for the query range.
    schema (PointInTimeRecord): The schema object for the table to query.

    Returns:
    List[PointInTimeRecord]: A list of PointInTimeRecord records within the given datetime range.
    """
    statement = select(schema).where(schema.start_time >= start_date, schema.start_time <= end_date)
    results = session.scalars(statement).all()
    return results
