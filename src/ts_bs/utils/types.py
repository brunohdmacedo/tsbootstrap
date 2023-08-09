from numbers import Integral
from typing import List, Literal, Optional, Tuple, Union

from arch.univariate.base import ARCHModelResult
from numpy.random import Generator
from statsmodels.tsa.ar_model import AutoRegResultsWrapper
from statsmodels.tsa.arima.model import ARIMAResultsWrapper
from statsmodels.tsa.statespace.sarimax import SARIMAXResultsWrapper
from statsmodels.tsa.vector_ar.var_model import VARResultsWrapper

ModelTypesWithoutArch = Literal["ar", "arima", "sarima", "var"]
ModelTypes = Literal["ar", "arima", "sarima", "var", "arch"]

FittedModelType = Union[
    AutoRegResultsWrapper,
    ARIMAResultsWrapper,
    SARIMAXResultsWrapper,
    VARResultsWrapper,
    ARCHModelResult,
]

OrderTypesWithoutNone = Union[
    Integral,
    List[Integral],
    Tuple[Integral, Integral, Integral],
    Tuple[Integral, Integral, Integral, Integral],
]
OrderTypes = Optional[OrderTypesWithoutNone]


RngTypes = Optional[Union[Generator, Integral]]
BlockCompressorTypes = Literal[
    "first",
    "middle",
    "last",
    "mean",
    "mode",
    "median",
    "kmeans",
    "kmedians",
    "kmedoids",
]
