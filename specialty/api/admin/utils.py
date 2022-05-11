from .exceptions import SpecialtyExist, SpecialtyNotExist
from ...models import Specialty

from common.utils import _object_exist


def clean_specialty_title(title: str):
    ...


def clean_specialty_id(id: int):
    if not object_exist(Specialty, id=id):
        raise SpecialtyNotExist()
    ...
    