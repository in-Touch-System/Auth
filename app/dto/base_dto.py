from pydantic import BaseModel, model_validator

class BaseDTOModel(BaseModel):

    @model_validator(mode="after")
    def validate(cls, values):
        obj = cls(**values)

        if hasattr(obj, "validate"):
            obj.validate()

        return values
