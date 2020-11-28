import pandas as pd
from typing import Iterable
from sklearn.impute import SimpleImputer


def dealWithMissingValues(X: pd.DataFrame, categorical_labels: Iterable[str], strategy: str = "median", fill_value=None, show_fill: bool = True, add_back_categorical: bool = False) -> pd.DataFrame:
    """
    A function to remove or replace missing data in a DataFrame.  Note that this returns a numerical DataFrame, i.e. all categorical labels are removed.  If you would like to add them back in, specify that option.

    Args:
        X (pd.DataFrame): The DataFrame missing values
        categorical_labels (Iterable[str]): Labels of non-numerical columns/features
        strategy (str, optional): This is a string representing the manner in which missing values should be dealt with.  Potential options include:

        * "mean"
        * "median"
        * "most_frequent"
        * "constant"

        Defaults to "median".

        fill_value (float): If specified and the strategy is constant, this will fill in the missing values with the constant.  Defaults to None.

        show_fill (bool):  If specified to True, will print the fill values of each attribute

        add_back_categorical:  If specified to True, will return the DataFrame containing the original categorical labels.  Otherwise, only a numerical DataFrame will be returned

    Returns:
        pd.DataFrame: Transformed DataFrame, missing values remedied.  Not modified inplace, so save to a variable.
    """
    X_new = X.copy()
    # Step 1 - Construct a SimpleImputer instance, with the strategy

    imputer = SimpleImputer(strategy=strategy)
    if (fill_value):
        imputer = SimpleImputer(strategy=strategy, fill_value=fill_value)

    # Step 2 - Remove text features
    # For each label in the labels specified, drop that label from the  DataFrame.
    for label in categorical_labels:
        X_new.drop(label, axis=1, inplace = True)

    # Step 3 - Fit the Imputer

    X_tr = imputer.fit_transform(X_new)

    # Step 4 - Transform back to a DataFrame
    X_tr = pd.DataFrame(X_tr, columns=X_new.columns, index=X_new.index)

    # Step 5 - Add back in categorical labels if they want
    if (add_back_categorical):
        for label in categorical_labels:
            X_tr[label] = X[label]
    # If they want the fill values printed, print them
    if (show_fill):
        print("Fill Values by Attribute: \n")
        showImputerFill(X_new, imputer)

    return X_tr


def showImputerFill(X: pd.DataFrame, imputer: SimpleImputer):
    """Shows the values an imputer is filling missing data with

    Args:
        X (pd.DataFrame): The transformed/remedied DataFrame
        imputer (SimpleImputer): The imputer doing the fitting/transforming on X
    """
    for column, fill_value in zip(X.columns, imputer.statistics_):
        print(f"{column}: {fill_value}")
