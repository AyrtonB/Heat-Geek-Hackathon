import datetime

from sqlmodel import Session, select

from heatmap.definitions.timeseries import PowerCarbonIntensity


def get_records_within_dates(
    session: Session, start_date: datetime.datetime, end_date: datetime.datetime
) -> list[PowerCarbonIntensity]:
    """
    Retrieves records from the 'power_carbon_intensity' table where the 'start_time'
    falls within the specified start and end datetime.

    Args:
    session (Session): The SQLAlchemy session object used to execute queries.
    start_date (datetime): The start datetime for the query range.
    end_date (datetime): The end datetime for the query range.

    Returns:
    List[PowerCarbonIntensity]: A list of PowerCarbonIntensity records within the given datetime range.
    """
    statement = select(PowerCarbonIntensity).where(
        PowerCarbonIntensity.start_time >= start_date, PowerCarbonIntensity.start_time <= end_date
    )
    results = session.scalars(statement).all()
    return results
