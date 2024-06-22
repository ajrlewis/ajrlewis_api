from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import user
from ..dependencies import get_db


router = APIRouter(
    prefix="/image",
    tags=["Image"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/text")
async def text():
    """Extracts and returns any text detected within an uploaded image PNG file."""
    return {"text": "Foo bar"}


@router.get("/create")
async def create():
    """Creates and returns a PNG image from a prompt."""
    return {"text": "Foo bar"}


@router.get("/resize")
async def resize():
    """Resizes and returns a PNG image from a prompt."""
    return {"text": "Foo bar"}


@router.get("/favicon")
async def favicon():
    """Resizes an image to 16x16 pixels suitable for a favicon."""
    return {"text": "Foo bar"}


@router.get("/colors")
async def colors():
    """Returns the N most frequent colors detected within an uploaded PNG file."""
    return {"text": "Foo bar"}


@router.get("/pad")
async def pad():
    """Returns the padded version of an uploaded PNG file."""
    return {"text": "Foo bar"}


@router.get("/smooth")
async def smooth():
    """Returns the smoothed version of an uploaded PNG file."""
    psf = ""
    return {"text": "Foo bar"}


@router.get("/noise")
async def noise():
    """Returns the noise version of an uploaded PNG file."""
    return {"text": "Foo bar"}


@router.get("/jackknife")
async def jackknife():
    """Returns the noise version of an uploaded PNG file."""
    return {"text": "Foo bar"}
