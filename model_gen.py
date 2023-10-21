import os

from pathlib import Path

from datamodel_code_generator import InputFileType, generate, DataModelType, LiteralType

IN_PATH = "api-docs/models"
OUT_PATH = "st_api/models"

_all = []

for f in Path(IN_PATH).iterdir():
    schema = f.read_text()
    _all.append(f.stem)
    out = (Path(OUT_PATH) / (str(f.stem) + ".py")).absolute()
    if out.exists():
        out.unlink()
    p = Path.cwd()
    os.chdir(IN_PATH)
    generate(
        schema,
        input_file_type=InputFileType.JsonSchema,
        input_filename=IN_PATH + "/" + f.name,
        output=out,
        output_model_type=DataModelType.PydanticV2BaseModel,
        class_name=f.stem,
        enum_field_as_literal=LiteralType.All,
    )
    os.chdir(p)

init = Path(OUT_PATH + "/__init__.py")
init.unlink(missing_ok=True)
init.write_text(f"""
from . import *
__all__ = {_all}
""")
