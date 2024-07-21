from typing import Annotated
from imagekit import imagekit
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response, StreamingResponse
from dependencies import LoadImageDep


from pydantic import BaseModel, Field


class Img(BaseModel):
    content: str = Field(None, description="The content of the image.")


router = APIRouter(prefix="/image", tags=["Image"])


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/upload")
async def upload(img: LoadImageDep):
    return {"image_size": img.size}


@router.post("/text")
async def text(img: LoadImageDep):
    """Extracts and returns any text detected within an uploaded image PNG file."""
    text = imagekit.extract_text(img)
    return {"text": text}


@router.post("/smooth", response_model=Img)
async def smooth(
    img: LoadImageDep,
    sigma: float = Query(
        None,
        description="The Gaussian sigma to smooth by in pixels.",
    ),
):
    """Returns the smoothed version of an uploaded PNG file."""
    smoothed_img = imagekit.smooth(img, sigma=sigma)
    img_bytes = imagekit.to_bytes(smoothed_img)
    return StreamingResponse(
        content=img_bytes,
        media_type="image/png",
        # headers={"Content-Disposition": "attachment; filename=smoothed_image.png"},
    )


# @router.get("/create")
# async def create():
#     """Creates and returns a PNG image from a prompt."""
#     return {"text": "Foo bar"}


# @router.get("/resize")
# async def resize():
#     """Resizes and returns a PNG image from a prompt."""
#     return {"text": "Foo bar"}


# @router.get("/favicon")
# async def favicon():
#     """Resizes an image to 16x16 pixels suitable for a favicon."""
#     return {"text": "Foo bar"}


# @router.get("/colors")
# async def colors():
#     """Returns the N most frequent colors detected within an uploaded PNG file."""
#     return {"text": "Foo bar"}


# @router.get("/pad")
# async def pad():
#     """Returns the padded version of an uploaded PNG file."""
#     return {"text": "Foo bar"}


# @router.get("/noise")
# async def noise():
#     """Returns the noise version of an uploaded PNG file."""
#     return {"text": "Foo bar"}


# @router.get("/jackknife")
# async def jackknife():
#     """Returns the noise version of an uploaded PNG file."""
#     return {"text": "Foo bar"}
