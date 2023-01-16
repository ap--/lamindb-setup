from lnhub_rest import __version__ as lnhub_rest_v
from packaging import version

if version.parse(lnhub_rest_v) != version.parse("0.1.2"):
    raise RuntimeError("lndb_setup needs lnhub_rest==0.1.2")