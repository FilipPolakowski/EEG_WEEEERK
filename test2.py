# Put this at the very top of your script (or in a file that runs first)
import collections
from collections.abc import Iterable, Mapping, Sequence, MutableMapping

# Re-inject the old names so old packages still work
collections.Iterable = Iterable
collections.Mapping = Mapping
collections.Sequence = Sequence
collections.MutableMapping = MutableMapping

# Now dn3 imports fine
import dn3
print("DN3 imported successfully!")