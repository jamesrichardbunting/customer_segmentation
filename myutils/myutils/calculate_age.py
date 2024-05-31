def calculate_age(birthdate, reference_date):
    """
    Calculate age in years from birthdate to a given reference date.

    Args:
    birthdate (pd.Series): Pandas Series of birth dates.
    reference_date (pd.Timestamp): The date from which to calculate the age.

    Returns:
    pd.Series: Age in years as of the reference date.
    """
    return (reference_date - birthdate).dt.days // 365