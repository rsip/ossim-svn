# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyossimtest', [dirname(__file__)])
        except ImportError:
            import _pyossimtest
            return _pyossimtest
        if fp is not None:
            try:
                _mod = imp.load_module('_pyossimtest', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyossimtest = swig_import_helper()
    del swig_import_helper
else:
    import _pyossimtest
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyossimtest.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _pyossimtest.SwigPyIterator_value(self)
    def incr(self, n = 1): return _pyossimtest.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _pyossimtest.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _pyossimtest.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _pyossimtest.SwigPyIterator_equal(self, *args)
    def copy(self): return _pyossimtest.SwigPyIterator_copy(self)
    def next(self): return _pyossimtest.SwigPyIterator_next(self)
    def __next__(self): return _pyossimtest.SwigPyIterator___next__(self)
    def previous(self): return _pyossimtest.SwigPyIterator_previous(self)
    def advance(self, *args): return _pyossimtest.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _pyossimtest.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _pyossimtest.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _pyossimtest.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _pyossimtest.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _pyossimtest.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _pyossimtest.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _pyossimtest.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class UintVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UintVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UintVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _pyossimtest.UintVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _pyossimtest.UintVector___nonzero__(self)
    def __bool__(self): return _pyossimtest.UintVector___bool__(self)
    def __len__(self): return _pyossimtest.UintVector___len__(self)
    def pop(self): return _pyossimtest.UintVector_pop(self)
    def __getslice__(self, *args): return _pyossimtest.UintVector___getslice__(self, *args)
    def __setslice__(self, *args): return _pyossimtest.UintVector___setslice__(self, *args)
    def __delslice__(self, *args): return _pyossimtest.UintVector___delslice__(self, *args)
    def __delitem__(self, *args): return _pyossimtest.UintVector___delitem__(self, *args)
    def __getitem__(self, *args): return _pyossimtest.UintVector___getitem__(self, *args)
    def __setitem__(self, *args): return _pyossimtest.UintVector___setitem__(self, *args)
    def append(self, *args): return _pyossimtest.UintVector_append(self, *args)
    def empty(self): return _pyossimtest.UintVector_empty(self)
    def size(self): return _pyossimtest.UintVector_size(self)
    def clear(self): return _pyossimtest.UintVector_clear(self)
    def swap(self, *args): return _pyossimtest.UintVector_swap(self, *args)
    def get_allocator(self): return _pyossimtest.UintVector_get_allocator(self)
    def begin(self): return _pyossimtest.UintVector_begin(self)
    def end(self): return _pyossimtest.UintVector_end(self)
    def rbegin(self): return _pyossimtest.UintVector_rbegin(self)
    def rend(self): return _pyossimtest.UintVector_rend(self)
    def pop_back(self): return _pyossimtest.UintVector_pop_back(self)
    def erase(self, *args): return _pyossimtest.UintVector_erase(self, *args)
    def __init__(self, *args): 
        this = _pyossimtest.new_UintVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _pyossimtest.UintVector_push_back(self, *args)
    def front(self): return _pyossimtest.UintVector_front(self)
    def back(self): return _pyossimtest.UintVector_back(self)
    def assign(self, *args): return _pyossimtest.UintVector_assign(self, *args)
    def resize(self, *args): return _pyossimtest.UintVector_resize(self, *args)
    def insert(self, *args): return _pyossimtest.UintVector_insert(self, *args)
    def reserve(self, *args): return _pyossimtest.UintVector_reserve(self, *args)
    def capacity(self): return _pyossimtest.UintVector_capacity(self)
    __swig_destroy__ = _pyossimtest.delete_UintVector
    __del__ = lambda self : None;
UintVector_swigregister = _pyossimtest.UintVector_swigregister
UintVector_swigregister(UintVector)

class Mapss(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mapss, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mapss, name)
    __repr__ = _swig_repr
    def iterator(self): return _pyossimtest.Mapss_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _pyossimtest.Mapss___nonzero__(self)
    def __bool__(self): return _pyossimtest.Mapss___bool__(self)
    def __len__(self): return _pyossimtest.Mapss___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _pyossimtest.Mapss___getitem__(self, *args)
    def __delitem__(self, *args): return _pyossimtest.Mapss___delitem__(self, *args)
    def has_key(self, *args): return _pyossimtest.Mapss_has_key(self, *args)
    def keys(self): return _pyossimtest.Mapss_keys(self)
    def values(self): return _pyossimtest.Mapss_values(self)
    def items(self): return _pyossimtest.Mapss_items(self)
    def __contains__(self, *args): return _pyossimtest.Mapss___contains__(self, *args)
    def key_iterator(self): return _pyossimtest.Mapss_key_iterator(self)
    def value_iterator(self): return _pyossimtest.Mapss_value_iterator(self)
    def __setitem__(self, *args): return _pyossimtest.Mapss___setitem__(self, *args)
    def asdict(self): return _pyossimtest.Mapss_asdict(self)
    def __init__(self, *args): 
        this = _pyossimtest.new_Mapss(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _pyossimtest.Mapss_empty(self)
    def size(self): return _pyossimtest.Mapss_size(self)
    def clear(self): return _pyossimtest.Mapss_clear(self)
    def swap(self, *args): return _pyossimtest.Mapss_swap(self, *args)
    def get_allocator(self): return _pyossimtest.Mapss_get_allocator(self)
    def begin(self): return _pyossimtest.Mapss_begin(self)
    def end(self): return _pyossimtest.Mapss_end(self)
    def rbegin(self): return _pyossimtest.Mapss_rbegin(self)
    def rend(self): return _pyossimtest.Mapss_rend(self)
    def count(self, *args): return _pyossimtest.Mapss_count(self, *args)
    def erase(self, *args): return _pyossimtest.Mapss_erase(self, *args)
    def find(self, *args): return _pyossimtest.Mapss_find(self, *args)
    def lower_bound(self, *args): return _pyossimtest.Mapss_lower_bound(self, *args)
    def upper_bound(self, *args): return _pyossimtest.Mapss_upper_bound(self, *args)
    __swig_destroy__ = _pyossimtest.delete_Mapss
    __del__ = lambda self : None;
Mapss_swigregister = _pyossimtest.Mapss_swigregister
Mapss_swigregister(Mapss)

pyossimtestConstants_HEADER = _pyossimtest.pyossimtestConstants_HEADER
pyossimtestInfo_HEADER = _pyossimtest.pyossimtestInfo_HEADER
class Info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Info, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pyossimtest.new_Info()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyossimtest.delete_Info
    __del__ = lambda self : None;
    def initialize(self, *args): return _pyossimtest.Info_initialize(self, *args)
    def execute(self): return _pyossimtest.Info_execute(self)
    def getImageInfo(self, *args): return _pyossimtest.Info_getImageInfo(self, *args)
Info_swigregister = _pyossimtest.Info_swigregister
Info_swigregister(Info)

pyossimtestInit_HEADER = _pyossimtest.pyossimtestInit_HEADER
class Init(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Init, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Init, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyossimtest.delete_Init
    __del__ = lambda self : None;
    __swig_getmethods__["instance"] = lambda x: _pyossimtest.Init_instance
    if _newclass:instance = staticmethod(_pyossimtest.Init_instance)
    def initialize(self, *args): return _pyossimtest.Init_initialize(self, *args)
Init_swigregister = _pyossimtest.Init_swigregister
Init_swigregister(Init)

def Init_instance():
  return _pyossimtest.Init_instance()
Init_instance = _pyossimtest.Init_instance

pyossimtestSingleImageChain_HEADER = _pyossimtest.pyossimtestSingleImageChain_HEADER
class SingleImageChain(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SingleImageChain, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SingleImageChain, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pyossimtest.new_SingleImageChain()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyossimtest.delete_SingleImageChain
    __del__ = lambda self : None;
    def open(self, *args): return _pyossimtest.SingleImageChain_open(self, *args)
    def isOpen(self): return _pyossimtest.SingleImageChain_isOpen(self)
    def close(self): return _pyossimtest.SingleImageChain_close(self)
    def getEntryList(self): return _pyossimtest.SingleImageChain_getEntryList(self)
    def getFilename(self): return _pyossimtest.SingleImageChain_getFilename(self)
    def createRenderedChain(self): return _pyossimtest.SingleImageChain_createRenderedChain(self)
    def selectBands(self, *args): return _pyossimtest.SingleImageChain_selectBands(self, *args)
    def getBandSelection(self): return _pyossimtest.SingleImageChain_getBandSelection(self)
    def getNumberOfBands(self): return _pyossimtest.SingleImageChain_getNumberOfBands(self)
    def setHistogram(self, *args): return _pyossimtest.SingleImageChain_setHistogram(self, *args)
    def getHistogramFile(self): return _pyossimtest.SingleImageChain_getHistogramFile(self)
    def setOverview(self, *args): return _pyossimtest.SingleImageChain_setOverview(self, *args)
    def getOverviewFile(self): return _pyossimtest.SingleImageChain_getOverviewFile(self)
SingleImageChain_swigregister = _pyossimtest.SingleImageChain_swigregister
SingleImageChain_swigregister(SingleImageChain)

# This file is compatible with both classic and new-style classes.


