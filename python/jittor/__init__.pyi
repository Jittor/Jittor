from typing import List, Tuple, Optional, Union, Any, ContextManager, Callable, overload
import builtins
import math
import pickle
def unary(x,op):...
def cast(x,op):...
def bool(x):...
def int8(x):...
def int16(x):...
def int32(x):...
def int64(x):...
def uint8(x):...
def uint16(x):...
def uint32(x):...
def uint64(x):...
def float32(x):...
def float64(x):...
def abs(x):...
def negative(x):...
def logical_not(x):...
def bitwise_not(x):...
def log(x):...
def exp(x):...
def sqrt(x):...
def round(x):...
def floor(x):...
def ceil(x):...
def sin(x):...
def asin(x):...
def arcsin(x):...
def sinh(x):...
def asinh(x):...
def arcsinh(x):...
def tan(x):...
def atan(x):...
def arctan(x):...
def tanh(x):...
def atanh(x):...
def arctanh(x):...
def cos(x):...
def acos(x):...
def arccos(x):...
def cosh(x):...
def acosh(x):...
def arccosh(x):...
def sigmoid(x):...
def erf(x):...
def broadcast(x,shape,dims):...
def broadcast(x,y,dims):...
def broadcast_var(x,y,dims):...
def tape(x):...
def fetch(inputs,func):...
def transpose(x,axes):...
def code(shape,dtype,inputs,cpu_src,cpu_grad_src,cpu_header,cuda_src,cuda_grad_src,cuda_header):...
def code(shapes,dtypes,inputs,cpu_src,cpu_grad_src,cpu_header,cuda_src,cuda_grad_src,cuda_header):...
def code(inputs,outputs,cpu_src,cpu_grad_src,cpu_header,cuda_src,cuda_grad_src,cuda_header):...
def setitem(x,slices,y,op):...
def candidate(x,fail_cond,dtype):...
def getitem(x,slices):...
def random(shape,dtype,type):...
def reindex_reduce(y,op,shape,indexes,overflow_conditions,extras):...
def clone(x):...
def reshape(x,shape):...
def reduce(x,op,dim,keepdims):...
def reduce(x,op,dims,keepdims):...
def max(x,dim,keepdims):...
def max(x,dims,keepdims):...
def max(x,dims_mask,keepdims_mask):...
def reduce_maximum(x,dim,keepdims):...
def reduce_maximum(x,dims,keepdims):...
def reduce_maximum(x,dims_mask,keepdims_mask):...
def min(x,dim,keepdims):...
def min(x,dims,keepdims):...
def min(x,dims_mask,keepdims_mask):...
def reduce_minimum(x,dim,keepdims):...
def reduce_minimum(x,dims,keepdims):...
def reduce_minimum(x,dims_mask,keepdims_mask):...
def sum(x,dim,keepdims):...
def sum(x,dims,keepdims):...
def sum(x,dims_mask,keepdims_mask):...
def reduce_add(x,dim,keepdims):...
def reduce_add(x,dims,keepdims):...
def reduce_add(x,dims_mask,keepdims_mask):...
def prod(x,dim,keepdims):...
def prod(x,dims,keepdims):...
def prod(x,dims_mask,keepdims_mask):...
def product(x,dim,keepdims):...
def product(x,dims,keepdims):...
def product(x,dims_mask,keepdims_mask):...
def reduce_multiply(x,dim,keepdims):...
def reduce_multiply(x,dims,keepdims):...
def reduce_multiply(x,dims_mask,keepdims_mask):...
def reduce_logical_and(x,dim,keepdims):...
def reduce_logical_and(x,dims,keepdims):...
def reduce_logical_and(x,dims_mask,keepdims_mask):...
def all_(x,dim,keepdims):...
def all_(x,dims,keepdims):...
def all_(x,dims_mask,keepdims_mask):...
def reduce_logical_or(x,dim,keepdims):...
def reduce_logical_or(x,dims,keepdims):...
def reduce_logical_or(x,dims_mask,keepdims_mask):...
def any_(x,dim,keepdims):...
def any_(x,dims,keepdims):...
def any_(x,dims_mask,keepdims_mask):...
def reduce_logical_xor(x,dim,keepdims):...
def reduce_logical_xor(x,dims,keepdims):...
def reduce_logical_xor(x,dims_mask,keepdims_mask):...
def reduce_bitwise_and(x,dim,keepdims):...
def reduce_bitwise_and(x,dims,keepdims):...
def reduce_bitwise_and(x,dims_mask,keepdims_mask):...
def reduce_bitwise_or(x,dim,keepdims):...
def reduce_bitwise_or(x,dims,keepdims):...
def reduce_bitwise_or(x,dims_mask,keepdims_mask):...
def reduce_bitwise_xor(x,dim,keepdims):...
def reduce_bitwise_xor(x,dims,keepdims):...
def reduce_bitwise_xor(x,dims_mask,keepdims_mask):...
def mean(x,dim,keepdims):...
def mean(x,dims,keepdims):...
def mean(x,dims_mask,keepdims_mask):...
def copy(x):...
def arg_reduce(x,op,dim,keepdims):...
def argsort(x,dim,descending,dtype):...
def ternary(cond,x,y):...
def binary(x,y,p):...
def pow(x,y):...
def maximum(x,y):...
def minimum(x,y):...
def add(x,y):...
def subtract(x,y):...
def multiply(x,y):...
def divide(x,y):...
def floor_divide(x,y):...
def mod(x,y):...
def less(x,y):...
def less_equal(x,y):...
def greater(x,y):...
def greater_equal(x,y):...
def equal(x,y):...
def not_equal(x,y):...
def left_shift(x,y):...
def right_shift(x,y):...
def logical_and(x,y):...
def logical_or(x,y):...
def logical_xor(x,y):...
def bitwise_and(x,y):...
def bitwise_or(x,y):...
def bitwise_xor(x,y):...
def numpy_code(shape,dtype,inputs,forward,backward):...
def numpy_code(shapes,dtypes,inputs,forward,backward):...
def numpy_code(shape,dtype,inputs,forward):...
def numpy_code(shapes,dtypes,inputs,forward):...
def where(cond,dtype):...
def index(shape,dim,dtype):...
def index(shape,dtype):...
def index(a,dim,dtype):...
def index(a,dtype):...
def index_var(a,dim,dtype):...
def index_var(a,dtype):...
def array_(args):...
def array(obj):...
def reindex(x,shape,indexes,overflow_value,overflow_conditions,extras):...
def reindex(x,indexes,overflow_value,overflow_conditions):...
def reindex_var(x,indexes,overflow_value,overflow_conditions):...
def empty(shape,dtype):...
