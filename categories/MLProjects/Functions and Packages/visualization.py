import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from typing import Iterable
import numpy as np
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go  # importing graphical objects
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from pandas.plotting import register_matplotlib_converters


class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


def plot_confusion_matrix(y_actual: Iterable, y_pred: Iterable) -> pd.DataFrame:
    """Returns a DataFrame of the confusion matrix when passed the actual labels and the predicted labels, and displays a heatmap representation of the confusion matrix

    Args:
        y_actual (Iterable): The actual labels      
        y_pred (Iterable):  The predicted labels

    Returns:
        pd.DataFrame: A DataFrame of the confusion matrix
    """
    data = {'y_Actual': y_actual,
            'y_Predicted': y_pred
            }
    df = pd.DataFrame(data, columns=['y_Actual', 'y_Predicted'])
    confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=[
                                   'Actual'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True)
    plt.show()
    return df


def plot_lin_reg(fitted_estimator, X: pd.DataFrame, y_initial: pd.DataFrame):
    """Plots a linear regression given a fitted estimator, and the initial dataset in the form of a DataFrame as well as the initial target, also in DataFrame form.

    Args:
        fitted_estimator (Object): estimator (ex. Ridge object)
        X (pd.DataFrame): The features of the dataset
        y_initial (pd.DataFrame): The dataset target
    """
    # Scatter initial data
    xarr = X.values.ravel()
    fig = px.scatter(data_frame=None, x=X.values.ravel(),
                     y=y_initial.values.ravel())

    # Create ranges for regression
    X_range = np.linspace(X.min(), X.max(), 100)
    y_range = fitted_estimator.predict(X_range.reshape(-1, 1))

    # Add traces
    fig.add_traces(go.Scatter(x=X_range.ravel(),
                              y=y_range.ravel(), name='Regression'))

    fig.show()
