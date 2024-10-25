from typing import Annotated

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response, StreamingResponse
import imagekit
from loguru import logger

from dependencies import GetDBDep, LoadImageDep, GetCurrentUserDep


router = APIRouter(prefix="/image", tags=["Image"])


@router.post("/size")
async def size(db: GetDBDep, user: GetCurrentUserDep, img: LoadImageDep):
    return {"image_size": img.size}


@router.post("/extract_text")
async def extract_text(db: GetDBDep, user: GetCurrentUserDep, img: LoadImageDep):
    """Extracts and returns any text detected within an image."""
    text = imagekit.extract_text(img)
    logger.debug(f"{text = }")
    return {"text": text}


@router.post("/smooth")
async def smooth(
    db: GetDBDep,
    user: GetCurrentUserDep,
    img: LoadImageDep,
    sigma: float = Query(
        None,
        description="The Gaussian sigma to smooth by in pixels.",
    ),
):
    """Returns the smoothed version of an image."""
    smoothed_img = imagekit.smooth(img, sigma=sigma)
    img_bytes = imagekit.to_bytes(smoothed_img)
    return StreamingResponse(content=img_bytes, media_type="image/png")


# @router.get("/noise")
# async def noise():
#     """Returns the noise version of an uploaded PNG file."""
#     # window_size = 4
#     return {"text": "Foo bar"}
