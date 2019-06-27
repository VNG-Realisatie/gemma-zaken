"""
Defines the scopes used in the ZRC component.

The Exxellence authorisation model is taken into consideration as well, see
https://wiki.exxellence.nl/display/KPORT/2.+Zaaktype+autorisaties
"""

from vng_api_common.scopes import Scope

EXAMPLE_SCOPE = Scope(
    "zds.scopes.domain.example",
    description="""
**Laat toe om**:

* ...
""",
)
