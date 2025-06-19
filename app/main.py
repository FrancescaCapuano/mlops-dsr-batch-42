import torch
import io
from pydantic import BaseModel

class Result(BaseModel):
    category: str
    confidence: float