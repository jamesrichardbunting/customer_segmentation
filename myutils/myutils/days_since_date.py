def days_since_date(first_purchase_date, reference_date):
    """
    Calculate time in days since the first purchase date to a given reference date.

    Args:
    first_purchase_date (pd.Series): Pandas Series of first purchase dates.
    reference_date (pd.Timestamp): The date from which to calculate the years since first purchase.

    Returns:
    pd.Series: Years since first purchase as of the reference date.
    """
    return (reference_date - first_purchase_date).dt.days 